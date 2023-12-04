
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy


class Member:
  def __init__(self, n, t, isMu=False):
    self.name = n
    self.typ = t
    self.isMu = isMu

  def __str__(self):
    return "Member("+self.name+","+str(self.typ)+","+str(self.kind)+","+str(self.isMu)+")"


class StaticMember:
  def __init__(self, c, n, t, isMu=False):
    self.classname = c
    self.name = n
    self.typ = t
    self.isMu = isMu

  def setClassname(self, n):
    self.name = n


class Instance:
  def __init__(self, c):
    self.classtype = c


class BKClass:
  def __init__(self, n, p, m):
    self.name = n
    self.parent = p
    self.member = m

  def __str__(self):
    return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) + "])"


class SupportUtils:
  def checkIsChildOf(self, subName:str, ancestorName:str, globalScope):
    sub_class = self.searchClassByName(subName, globalScope) # => BKClass
    if sub_class.parent == None: return False
    if sub_class.parent == ancestorName: return True
    return self.checkIsChildOf(sub_class.parent, ancestorName, globalScope)

  def checkTypeMatch(self, lType:Type, rType:Type, globalScope) -> bool:
    if type(lType) != type(rType):
      if isinstance(lType, FloatType) and isinstance(rType, IntType):
        return True
      return False
    if isinstance(lType, ClassType) and isinstance(rType, ClassType):
      lClassname = lType.classname.name
      rClassname = rType.classname.name
      if lClassname == rClassname: 
        return True
      return self.checkIsChildOf(rClassname, lClassname, globalScope)
    if isinstance(lType, ArrayType) and isinstance(rType, ArrayType):
      if not self.checkTypeMatch(lType.eleType, rType.eleType, globalScope):
        return False # tested 669
      if lType.size != rType.size: 
        return False # tested 668
    return True

  def checkIsConst(self, lhs, visibleScope) -> bool:
    if isinstance(lhs, Id): #name:str
      decl = self.searchLocalIdByName(lhs.name, visibleScope)
      return decl["isMu"] == False
    if isinstance(lhs, FieldAccess): #obj:Expr, fieldname:Id
      mem = self.searchMemberCalledByClass(lhs.obj)
      return mem.isMu == False

  def searchLocalIdByName(self, name:str, visibleScope):
    for scope in visibleScope[:-1]:
      for decl in scope:
        if name == decl["name"]:
          return decl
    return None

  def searchClassByName(self, classname:str, globalScope):
    for mem in globalScope:
      if isinstance(mem, BKClass) and classname == mem.name:
        return mem
    return None
  
  def searchStaticMemByName(self, name:str, globalScope):
    for mem in globalScope:
      if name == mem.name and isinstance(mem, StaticMember):
        return mem
    return None
  
  def searchMemberCalledByClass(self, classname:str, memName:str, globalScope):
    target_class = self.searchClassByName(classname, globalScope) # => BKClass
    for mem in target_class.member: # => Member
      if memName == mem.name: return mem
    if target_class.parent == None: return None
    return self.searchMemberCalledByClass(target_class.parent, memName, globalScope)

  def getConstructorList(self, classname:str, globalScope):
    target_class = self.searchClassByName(classname, globalScope)
    if target_class:
      constructor_list = []
      for mem in target_class.member:
        # mem: Member(name, typ, False)
        if mem.name == "constructor": constructor_list.append(mem)
      return constructor_list


class GetEnv(BaseVisitor, Utils, SupportUtils):
  def __init__(self):
    self.io = BKClass("io", None, [
      Member("@readInt", MType([], IntType()), False),
      Member("@writeIntLn", MType([IntType()], VoidType()), False),
    ])
    self.global_env = [self.io] # => List[BKClass]

  def visitProgram(self, ast:Program, c):
    class_name = [classdecl.classname.name for classdecl in ast.decl]
    if "Program" not in class_name:
      raise NoEntryPoint()
    
    program_classes = list(filter(lambda decl: decl.classname.name == "Program", ast.decl))
    has_entry_point = False
    for pc in program_classes:
      method_names = [mem.name.name for mem in pc.memlist if type(mem) is MethodDecl]
      if "@main" not in method_names: continue
      
      main_func_list = list(filter(lambda mem: isinstance(mem, MethodDecl) and mem.name.name == "@main" , pc.memlist))
      valid_main_func = list(filter(lambda func: len(func.param) == 0 and isinstance(func.returnType, VoidType), main_func_list))
      if len(valid_main_func) == 0: continue
      has_entry_point = True
      break

    if not has_entry_point: raise NoEntryPoint()

    for decl in ast.decl:
      self.visit(decl, self.global_env)
    return self.global_env

  def visitClassDecl(self, ast:ClassDecl, globalScope):
    if ast.classname.name in map(lambda x: x.name, globalScope): 
      raise Redeclared(Class(), ast.classname.name)
    env = [[], ast.classname.name]
    env = reduce(lambda env_pre, mem_cur: self.visit(mem_cur, env_pre), ast.memlist, env)
    self.global_env += [BKClass(ast.classname.name, ast.parentname.name if ast.parentname else None, env[0])]

  def visitMethodDecl(self, ast:MethodDecl, classScope):
    param_types = [self.visit(param.varType, self.global_env) for param in ast.param]
    ret_type = self.visit(ast.returnType, self.global_env)
    if ast.name.name != "constructor":
      if "@" not in ast.name.name:
        if ast.name.name in map(lambda x: x.name, classScope[0]): 
          raise Redeclared(Method(), ast.name.name) 
        classScope[0] += [Member(ast.name.name, MType(param_types, ret_type), False)]
        return classScope
      # static
      if ast.name.name in [mem.name for mem in self.global_env if isinstance(mem, StaticMember)]:
        raise Redeclared(Method(), ast.name.name)
      self.global_env += [StaticMember(classScope[1], ast.name.name, MType(param_types, ret_type))]
      return classScope
    # constructor
    classScope[0] += [Member("constructor", MType(param_types, ret_type), False)]
    return classScope

  def visitAttributeDecl(self, ast:AttributeDecl, classScope):
    decl = self.visit(ast.decl, classScope[0])
    if "@" not in decl["name"]:
      if decl["name"] in [decl.name for decl in classScope[0]]:
        raise Redeclared(Attribute(), decl["name"])
      classScope[0] += [Member(decl["name"], decl["typ"], decl["isMu"])]
      return classScope
    if decl["name"] in [mem.name for mem in self.global_env if isinstance(mem, StaticMember)]:
      raise Redeclared(Attribute(), decl["name"])
    self.global_env += [StaticMember(classScope[1], decl["name"], decl["typ"], decl["isMu"])]
    return classScope
  
  def visitVarDecl(self, ast:VarDecl, classScope):
    vartype = self.visit(ast.varType, classScope)
    if isinstance(vartype, ClassType):
      vartype = Instance(vartype)    
    return {"name": ast.variable.name, "typ": vartype, "isMu": True}

  def visitConstDecl(self, ast:ConstDecl, c):
    consttype = self.visit(ast.constType, c)
    if isinstance(consttype, ClassType):
      consttype = Instance(consttype)
    return {"name": ast.constant.name, "typ": consttype, "isMu": False}

  def visitIntType(self, ast, param):
    return IntType()

  def visitFloatType(self, ast, param):
    return FloatType()

  def visitBoolType(self, ast, param):
    return BoolType()

  def visitStringType(self, ast, param):
    return StringType()

  def visitVoidType(self, ast, param):
    return VoidType()

  def visitArrayType(self, ast, c):
    return ArrayType(int(ast.size), self.visit(ast.eleType, c))

  def visitClassType(self, ast, c):
    target_class = self.searchClassByName(ast.classname.name, self.global_env)
    if target_class: return ClassType(ast.classname)
    raise Undeclared(Class(), ast.classname.name)
  

class StaticChecker(BaseVisitor, Utils, SupportUtils):
  def __init__(self, ast):
    self.ast = ast
    self.global_env = []
    self.stackscope = []

  def check(self):
    self.visit(self.ast, self.global_env)
    return ""

  def visitProgram(self, ast, c):
    self.global_env = GetEnv().visit(ast, c)
    reduce(lambda c_pre, decl: self.visit(decl, c_pre), ast.decl, self.global_env)

  def visitClassDecl(self, ast, globalScope):
    reduce(lambda c_pre, mem_cur: self.visit(mem_cur, c_pre), ast.memlist, globalScope)
  
  def visitMethodDecl(self, ast, globalScope):
    env = [[]] # => [List[{name, typ, isMu}]]
    if len(ast.param) > 0:
      env = reduce(lambda env_pre, decl: self.visit(decl, ("param", env_pre)), ast.param, env)
    self.stackscope.append(MethodDecl)
    self.visit(ast.body, env + [globalScope])
    self.stackscope.pop()

  def visitAttributeDecl(self, ast, globalScope): 
    self.visit(ast.decl, ("var" if isinstance(ast.decl, VarDecl) else "const", [[], globalScope]))

  # (decltype, [[local]...[global]])
  def visitVarDecl(self, ast, visibleScope):
    # chua test type la Instance
    if ast.variable.name in map(lambda decl: decl["name"], visibleScope[1][0]):
      if visibleScope[0] == "var":
        raise Redeclared(Variable(), ast.variable.name)
      # param
      raise Redeclared(Parameter(), ast.variable.name) 
    vartype = self.visit(ast.varType, visibleScope)
    if isinstance(vartype, ClassType):
      vartype = Instance(vartype)
    if ast.varInit:
      init_type = self.visit(ast.varInit, visibleScope[1])
      if isinstance(init_type, VoidType):
        raise TypeMismatchInDeclaration(ast) #
      if isinstance(vartype, Instance) and isinstance(init_type, Instance):
        if not self.checkTypeMatch(vartype.classtype, init_type.classtype, visibleScope[1][-1]):
          raise TypeMismatchInDeclaration(ast) #
      if not self.checkTypeMatch(vartype, init_type, visibleScope[1][-1]):
        raise TypeMismatchInDeclaration(ast) # tested 666
    visibleScope[1][0] += [{"name": ast.variable.name, "typ": vartype, "isMu": True}]
    return visibleScope[1]

  # (decltype, [[local]...[global]])
  # (decltype, [[], [global]]) => attribute
  def visitConstDecl(self, ast, visibleScope):
    if ast.constant.name in map(lambda decl: decl["name"], visibleScope[1][0]):
      raise Redeclared(Constant(), ast.constant.name)
    consttype = self.visit(ast.constType, visibleScope)
    if isinstance(consttype, ClassType):
      consttype = Instance(consttype)
    if not ast.value:
      raise TypeMismatchInDeclaration(ast) # tested 667
    init_type = self.visit(ast.value, visibleScope[1])
    if isinstance(init_type, VoidType):
      raise TypeMismatchInDeclaration(ast) #
    if isinstance(consttype, Instance) and isinstance(init_type, Instance):
      if not self.checkTypeMatch(consttype.classtype, init_type.classtype, visibleScope[1][-1]):
        raise TypeMismatchInDeclaration(ast) #
    if not self.checkTypeMatch(consttype, init_type, visibleScope[1][-1]):
      raise TypeMismatchInDeclaration(ast) # tested 667

    visibleScope[1][0] += [{"name": ast.constant.name, "typ": consttype, "isMu": False}]
    return visibleScope[1]

  def visitBinaryOp(self, ast, visibleScope):
    lType = self.visit(ast.left, visibleScope)
    rType = self.visit(ast.right, visibleScope)
    if ast.op in ["+", "-", "*"]:
      if not isinstance(lType, IntType) and not isinstance(lType, FloatType):
        raise TypeMismatchInExpression(ast) #
      if not isinstance(rType, IntType) and not isinstance(rType, FloatType):
        raise TypeMismatchInExpression(ast) #
      if isinstance(lType, FloatType) or isinstance(rType, FloatType):
        return FloatType()
      return IntType()

    if ast.op == "/":
      if not isinstance(lType, IntType) and not isinstance(lType, FloatType):
        raise TypeMismatchInExpression(ast) #
      if not isinstance(rType, IntType) and not isinstance(rType, FloatType):
        raise TypeMismatchInExpression(ast) #
      return FloatType()
    
    if ast.op in ["\\", "%"]:
      if not isinstance(lType, IntType) or not isinstance(rType, IntType):
        raise TypeMismatchInExpression(ast) #
      return IntType()
    
    if ast.op in ["&&", "||"]:
      if not isinstance(lType, BoolType) or not isinstance(rType, BoolType):
        raise TypeMismatchInExpression(ast) #
      return BoolType()

    if ast.op == "^":
      if not isinstance(lType, StringType) or not isinstance(rType, StringType):
        raise TypeMismatchInExpression(ast) #
      return StringType()
    
    if ast.op in ["==", "!="]:
      if isinstance(lType, IntType) and not isinstance(rType, IntType):
        raise TypeMismatchInExpression(ast) #
      if isinstance(rType, IntType) and not isinstance(lType, IntType):
        raise TypeMismatchInExpression(ast) #
      if isinstance(lType, BoolType) and not isinstance(rType, BoolType):
        raise TypeMismatchInExpression(ast) #
      if isinstance(rType, BoolType) and not isinstance(rType, BoolType):
        raise TypeMismatchInExpression(ast) #
      return BoolType()

  def visitUnaryOp(self,ast,param):
    bodyType = self.visit(ast.body, visibleScope)
    if ast.op == "-":
      if isinstance(bodyType, IntType):
        return IntType()
      if isinstance(bodyType, FloatType):
        return FloatType()
      raise TypeMismatchInExpression(ast) #
    
    if ast.op == "!":
      if not isinstance(bodyType, BoolType):
        raise TypeMismatchInExpression(ast)
      return BoolType()

  def visitNewExpr(self,ast,visibleScope):
    classtype = self.visit(ast.classname, visibleScope)
    if len(ast.param) == 0:
      return Instance(classtype)
    constructor_list = self.getConstructorList(classtype.classname.name, self.global_env)
    has_found = False
    for constructor in constructor_list:
      param_list = constructor.typ.partype
      wrong_method = False
      if len(param_list) != len(ast.param):
        continue
      for idx in range(len(param_list)):
        exp_typ = self.visit(ast.param[idx], visibleScope)
        if self.checkTypeMatch(exp_typ, param_list[idx], self.global_env):
          continue
        wrong_method = True
      if wrong_method:
        continue
      has_found = True
    if not has_found:
      raise TypeMismatchInExpression(ast) # tested 670
    return Instance(classtype)

  def visitArrayCell(self,ast,visibleScope):
    idxtype = self.visit(ast.idx, visibleScope)
    arrtype = self.visit(ast.arr, visibleScope)
    if not isinstance(arrtype, ArrayType):
      raise TypeMismatchInExpression(ast) # tested 674
    if not isinstance(idxtype, IntType):
      raise TypeMismatchInExpression(ast) # tested 675
    return arrtype.eleType
    
  def visitBlock(self, ast, visibleScope): # [[param],...,[global]]
    decl_block = [stmt for stmt in ast.stmt if isinstance(stmt, StoreDecl)]
    stmt_block = [stmt for stmt in ast.stmt if not isinstance(stmt, StoreDecl)]
    env = [[]] + visibleScope
    env = reduce(lambda env_pre, decl: self.visit(decl, ("var" if isinstance(decl, VarDecl) else "const", env_pre)), decl_block, env)
    for stmt in stmt_block:
      self.visit(stmt, env)

  # visibleScope => [[local],...,[global]]
  def visitId(self, ast, visibleScope):
    searchedDecl = self.searchLocalIdByName(ast.name, visibleScope)
    if searchedDecl: 
      return searchedDecl["typ"]
    for decl in visibleScope[-1]: # => [BKClass, StaticMember]
      if isinstance(decl, BKClass):
        if decl.name == ast.name: return ClassType(Id(decl.name))
        for memdecl in decl.member:
          if memdecl.name == ast.name: return memdecl.typ
      if decl.name == ast.name: return decl.typ
    raise Undeclared(Identifier(), ast.name)
  
  # visibleScope => [[local],...,[param],[global]]
  # lhs:Expr, exp:Expr
  def visitAssign(self, ast, visibleScope):
    lt = self.visit(ast.lhs, visibleScope) 
    rt = self.visit(ast.exp, visibleScope) 
    if isinstance(ast.lhs, Id):
      decl = self.searchLocalIdByName(ast.lhs.name, visibleScope) 
      if not decl["isMu"]: 
        raise CannotAssignToConstant(ast) # tested 639
    if isinstance(ast.lhs, FieldAccess):
      classtype = self.visit(ast.lhs.obj, visibleScope).classtype
      classname = classtype.classname.name
      fieldname = ast.lhs.fieldname.name
      mem = self.searchMemberCalledByClass(classname, fieldname, visibleScope[-1])
      if "@" in fieldname:
        mem = self.searchStaticMemByName(fieldname, visibleScope) 
      if not mem.isMu:
        raise CannotAssignToConstant(ast) # tested 640
    if isinstance(lt, ArrayType) and isinstance(rt, ArrayType): 
      if not self.checkTypeMatch(lt.eleType, rt.eleType, self.global_env):
        raise TypeMismatchInStatement(ast) # tested 671
      if lt.size != rt.size:
        raise TypeMismatchInStatement(ast) # 
    if not self.checkTypeMatch(lt, rt, visibleScope[-1]):
      raise TypeMismatchInStatement(ast) # tested 641

  def visitFieldAccess(self, ast, visibleScope): 
    if "@" in ast.fieldname.name:
      target_mem = self.searchStaticMemByName(ast.fieldname.name, self.global_env)
      if not target_mem:
        raise Undeclared(Attribute(), ast.fieldname.name) # tested 644
      if ast.obj:
        typ = self.visit(ast.obj, visibleScope)
        if not isinstance(typ, ClassType):
          raise TypeMismatchInExpression(ast) # tested 643
        if typ.classname.name != target_mem.classname:
          raise TypeMismatchInExpression(ast) # tested 645
      if isinstance(target_mem.typ, MType):
        raise TypeMismatchInExpression(ast) # tested 646
      return target_mem.typ.rettype
    
    if isinstance(ast.obj, Id):
      obj_decl = self.searchLocalIdByName(ast.obj.name, visibleScope)
      if not obj_decl:
        raise Undeclared(Identifier(), ast.obj.name) # tested 647
    typ = self.visit(ast.obj, visibleScope)
    if not isinstance(typ, Instance):
      raise TypeMismatchInExpression(ast) # tested 648
    target_class = self.searchClassByName(typ.classtype.classname.name, self.global_env)
    target_mem = self.searchMemberCalledByClass(target_class.name, ast.fieldname.name, self.global_env)
    if not target_mem:
      raise Undeclared(Attribute(), ast.fieldname.name) # tested 649
    if isinstance(target_mem.typ, MType):
      raise TypeMismatchInExpression(ast) # tested 650
    return target_mem.typ
  
  # [[blockdecl], [param], [global]]
  def visitCallExpr(self, ast, visibleScope):
    if "@" in ast.method.name:
      target_method = self.searchStaticMemByName(ast.method.name, self.global_env)
      if not target_method:
        raise Undeclared(Method(), ast.method.name) # tested 652
      if ast.obj:
        typ = self.visit(ast.obj, visibleScope)
        if isinstance(typ, Instance):
          raise TypeMismatchInExpression(ast) # tested 653
        if not isinstance(typ, ClassType): 
          raise TypeMismatchInExpression(ast) # tested 654
        if typ.classname.name != target_method.classname: 
          raise TypeMismatchInExpression(ast) # tested 655
      if not isinstance(target_method.typ, MType): 
        raise TypeMismatchInExpression(ast) # tested 656
      if isinstance(target_method.typ.rettype, VoidType):
        raise TypeMismatchInExpression(ast) # tested 657
      params = [self.visit(param, visibleScope) for param in ast.param]
      args = target_method.typ.partype
      if len(params) != len(args):
        raise TypeMismatchInExpression(ast) # tested 658
      for idx in range(len(params)):
        if not self.checkTypeMatch(params[idx], args[idx], visibleScope[-1]):
          raise TypeMismatchInExpression(ast) # tested 659
      return target_method.typ.rettype 
      
    if isinstance(ast.obj, Id):
      obj_decl = self.searchLocalIdByName(ast.obj.name, visibleScope)
      if not obj_decl:
        raise Undeclared(Identifier(), ast.obj.name) # tested 660
    typ = self.visit(ast.obj, visibleScope) 
    if not isinstance(typ, Instance):
      raise TypeMismatchInExpression(ast) # tested 661
    target_class = self.searchClassByName(typ.classtype.classname.name, self.global_env)
    target_mem = self.searchMemberCalledByClass(target_class.name, ast.method.name, self.global_env)
    if not target_mem:
      raise Undeclared(Method(), ast.method.name) # tested 651
    if not isinstance(target_mem.typ, MType):
      raise TypeMismatchInExpression(ast) # tested 662
    if isinstance(target_mem.typ.rettype, VoidType): 
      raise TypeMismatchInExpression(ast) # tested 663
    params = [self.visit(param, visibleScope) for param in ast.param]
    args = target_mem.typ.partype
    if len(params) != len(args):
      raise TypeMismatchInExpression(ast) # tested 664
    for idx in range(len(params)):
      if not self.checkTypeMatch(params[idx], args[idx], visibleScope[-1]):
        raise TypeMismatchInExpression(ast) # tested 665
    return target_mem.typ.rettype
  
  def visitCallStmt(self, ast, visibleScope):
    if "@" in ast.method.name:
      target_method = self.searchStaticMemByName(ast.method.name, self.global_env)
      if not target_method:
        raise Undeclared(Method(), ast.method.name) #tested 630
      if ast.obj:
        typ = self.visit(ast.obj, visibleScope)
        if isinstance(typ, Instance):
          raise TypeMismatchInStatement(ast) #tested 629
        if not isinstance(typ, ClassType): 
          raise TypeMismatchInStatement(ast) #tested 642
        if typ.classname.name != target_method.classname: 
          raise TypeMismatchInStatement(ast) #tested 631
      if not isinstance(target_method.typ, MType): 
        raise TypeMismatchInStatement(ast) #tested 632
      if not isinstance(target_method.typ.rettype, VoidType):
        raise TypeMismatchInStatement(ast) #tested 624, 633
      params = [self.visit(param, visibleScope) for param in ast.param]
      args = target_method.typ.partype
      if len(params) != len(args):
        raise TypeMismatchInStatement(ast) #tested 635
      for idx in range(len(params)):
        if not self.checkTypeMatch(params[idx], args[idx], visibleScope[-1]):
          raise TypeMismatchInStatement(ast) #tested 637
      return target_method.typ.rettype 
      
    if isinstance(ast.obj, Id):
      obj_decl = self.searchLocalIdByName(ast.obj.name, visibleScope)
      if not obj_decl:
        raise Undeclared(Identifier(), ast.obj.name) # tested 626
    typ = self.visit(ast.obj, visibleScope) 
    if not isinstance(typ, Instance):
      raise TypeMismatchInStatement(ast) # tested 627
    target_class = self.searchClassByName(typ.classtype.classname.name, self.global_env)
    target_mem = self.searchMemberCalledByClass(target_class.name, ast.method.name, self.global_env)
    if not target_mem:
      raise Undeclared(Method(), ast.method.name)
    if not isinstance(target_mem.typ, MType):
      raise TypeMismatchInStatement(ast) # tested 623, 625
    if not isinstance(target_mem.typ.rettype, VoidType): 
      raise TypeMismatchInStatement(ast) # tested 625
    params = [self.visit(param, visibleScope) for param in ast.param]
    args = target_mem.typ.partype
    if len(params) != len(args):
      raise TypeMismatchInStatement(ast) 
    for idx in range(len(params)):
      if not self.checkTypeMatch(params[idx], args[idx], visibleScope[-1]):
        raise TypeMismatchInStatement(ast)
    return target_mem.typ.rettype
  
  # [[local]...[global]]
  def visitIf(self, ast, visibleScope):
    env = [[]] + visibleScope
    # if ast.preStmt:
      
    self.stackscope.append(If)

    self.stackscope.pop()
  
  def visitFor(self,ast,param):
    pass

  def visitContinue(self,ast,param):
    if For not in self.stackscope: 
      raise MustInLoop(ast)

  def visitBreak(self,ast,param):
    if For not in self.stackscope: 
      raise MustInLoop(ast)

  def visitReturn(self,ast,param):
    pass

  
  def visitIntType(self, ast, param):
    return IntType()

  def visitFloatType(self, ast, param):
    return FloatType()

  def visitBoolType(self, ast, param):
    return BoolType()

  def visitStringType(self, ast, param):
    return StringType()

  def visitVoidType(self, ast, param):
    return VoidType()

  def visitArrayType(self, ast, c):
    return ArrayType(int(ast.size), self.visit(ast.eleType, c))

  def visitClassType(self, ast, c):
    target_class = self.searchClassByName(ast.classname.name, self.global_env)
    if target_class: return ClassType(ast.classname)
    raise Undeclared(Class(), ast.classname.name) # tested 622
  
  def visitIntLiteral(self, ast, c):
    return IntType()
  
  def visitFloatLiteral(self,ast,param):
    return FloatType()
    
  def visitBooleanLiteral(self,ast,param):
    return BoolType()
  
  def visitStringLiteral(self,ast,param):
    return StringType()
  
  def visitNullLiteral(self,ast,param):
    return None
  
  def visitSelfLiteral(self,ast,param):
    return None 
      
  def visitArrayLiteral(self,ast,visibleScope):
    if len(ast.value) == 0:
      return ArrayType(0, None)
    root_type = self.visit(ast.value[0], visibleScope)
    if len(ast.value) == 1:
      return ArrayType(1, root_type)
    for value in ast.value[1:]:
      valuetype = self.visit(value, visibleScope)
      if not self.checkTypeMatch(valuetype, root_type, self.global_env):
        raise IllegalArrayLiteral(ast)
    return ArrayType(len(ast.value), root_type)