
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


class BKClass:
  def __init__(self, n, p, m):
    self.name = n
    self.parent = p
    self.member = m

  def __str__(self):
    return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) + "])"


class GetEnv(BaseVisitor, Utils):
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
      if "@main" not in method_names:
        continue
      
      main_func_list = list(filter(lambda mem: isinstance(mem, MethodDecl) and mem.name.name == "@main" , pc.memlist))
      valid_main_func = list(filter(lambda func: len(func.param) == 0 and isinstance(func.returnType, VoidType), main_func_list))
      if len(valid_main_func) == 0:
        continue
      has_entry_point = True
      break

    if not has_entry_point:
      raise NoEntryPoint()
    
    c = self.global_env
    self.global_env = reduce(lambda c_pre, decl: self.visit(decl, c_pre), ast.decl, c)
    return self.global_env

  def visitClassDecl(self, ast:ClassDecl, globalScope):
    if ast.classname.name in map(lambda x: x.name, globalScope): 
      raise Redeclared(Class(), ast.classname.name)
    env = [[], ast.classname.name]
    env = reduce(lambda env_pre, mem_cur: self.visit(mem_cur, env_pre), ast.memlist, env)
    return globalScope + [BKClass(ast.classname.name, ast.parentname.name if ast.parentname else None, env[0])]

  def visitMethodDecl(self, ast:MethodDecl, classScope):
    if ast.name.name != "constructor":
      if "@" not in ast.name.name:
        if ast.name.name in map(lambda x: x.name, classScope[0]): 
          raise Redeclared(Method(), ast.name.name) 
        classScope[0] += [Member(ast.name.name, MType([param.varType for param in ast.param], ast.returnType), False)]
        return classScope
      # static
      if ast.name.name in [mem.name for mem in self.global_env if isinstance(mem, StaticMember)]:
        raise Redeclared(Method(), ast.name.name)
      self.global_env += [StaticMember(classScope[1], ast.name.name, MType([param.varType for param in ast.param], ast.returnType))]
      return classScope
    # constructor
    classScope[0] += [Member("constructor", MType([param.varType for param in ast.param], ast.returnType), False)]
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
  
  def visitVarDecl(self, ast:VarDecl, c):
    return {"name": ast.variable.name, "typ": self.visit(ast.varType, c), "isMu": True}

  def visitConstDecl(self, ast:ConstDecl, c):
    return {"name": ast.constant.name, "typ": self.visit(ast.constType, c), "isMu": False}

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

  def visitArrayType(self, ast, param):
    return ast

  def visitClassType(self, ast, c):
    return ClassType(ast.classname)
  

class StaticChecker(BaseVisitor, Utils):
  def __init__(self, ast):
    self.ast = ast
    self.global_env = []

  def check(self):
    self.visit(self.ast, self.global_env)
    return ""

  def searchClassByName(self, classname:str):
    for mem in self.global_env:
      if classname == mem.name and isinstance(mem, BKClass):
        return mem
    return None
  
  def searchStaticMemByName(self, name):
    for mem in self.global_env:
      if name == mem.name and isinstance(mem, StaticMember):
        return mem
    return None
  
  def checkIsChildOf(self, subName:str, ancestorName:str):
    pass

  def checkTypeMatch(self, lType:Type, rType:Type):
    pass

  def searchMethodCalledByClass(self, classname:str, method:str):
    targetClass = self.searchClassByName(classname) # => BKClass
    for mem in targetClass.member: # => Member
      if method == mem.name and isinstance(mem.typ, MType):
        return mem
    if targetClass.parent == None: return None
    return self.searchMethodCalledByClass(targetClass.parent, method)

  def visitProgram(self, ast, c):
    self.global_env = GetEnv().visit(ast, c)
    reduce(lambda c_pre, decl: self.visit(decl, c_pre), ast.decl, self.global_env)

  def visitClassDecl(self, ast, globalScope):
    func_mem = list(filter(lambda mem: isinstance(mem, MethodDecl), ast.memlist))
    reduce(lambda c_pre, mem_cur: self.visit(mem_cur, c_pre), func_mem, globalScope)
  
  def visitMethodDecl(self, ast, globalScope):
    env = [] # => List[{name, typ, isMu}]
    env = reduce(lambda env_pre, decl: self.visit(decl, ("param", env_pre)), ast.param, env)
    self.visit(ast.body, [env, globalScope])

  def visitAttributeDecl(self,ast,c): pass

  def visitVarDecl(self, ast, localScope):
    if ast.variable.name in map(lambda decl: decl["name"], localScope[1]):
      if localScope[0] == "var":
        raise Redeclared(Variable(), ast.variable.name)
      # param
      raise Redeclared(Parameter(), ast.variable.name)
    return localScope[1] + [{"name": ast.variable.name, "typ": self.visit(ast.varType, localScope), "isMu": True}]

  def visitConstDecl(self, ast, localScope):
    if ast.constant.name in map(lambda decl: decl["name"], localScope[1]):
      raise Redeclared(Constant(), ast.constant.name)
    return localScope[1] + [{"name": ast.constant.name, "typ": self.visit(ast.constType, localScope), "isMu": False}]
    
  def visitBlock(self, ast, visibleScope): # => [[param], [global]]
    decl_block = [stmt for stmt in ast.stmt if isinstance(stmt, StoreDecl)]
    stmt_block = [stmt for stmt in ast.stmt if not isinstance(stmt, StoreDecl)]
    env = []
    env = reduce(lambda env_pre, decl: self.visit(decl, ("var", env_pre)) if isinstance(decl, VarDecl) else self.visit("const", env_pre), decl_block, env)
    for stmt in stmt_block:
      self.visit(stmt, [env] + visibleScope)

  # visibleScope => [[local],...,[global]]
  def visitId(self, ast, visibleScope):
    for scope in visibleScope:
      for decl in scope: # => local env of Block, Method => [StoreDecl]
        if decl["name"] == ast.name:
          return decl["typ"]
    raise Undeclared(Identifier(), ast.name)

  def visitFieldAccess(self, ast, visibleScope): 
    #Note: No parent
    typ = self.visit(ast.obj, visibleScope) # typ must be ClassType
    if isinstance(typ, ClassType):
      type_info = None
      found = False
      for classdecl in visibleScope[-1]: # => global
        if typ.classname == classdecl.name:
          type_info = classdecl
          found = True
          break
      if not found: raise Undeclared(Class(), typ.classname)
      # Note: must check in parent class, still not check in parent class
      for mem in type_info.member: # => Member
        if ast.fieldname.name == mem.name and not isinstance(mem.typ, MType):
          return mem.typ
      raise Undeclared(Attribute(), ast.fieldname.name)
    raise TypeMismatchInExpression(ast)
  
  def visitCallExpr(self, ast, visibleScope):
    pass
  
  def visitCallStmt(self, ast, visibleScope):
    #Note: No static yet
    typ = self.visit(ast.obj, visibleScope) # typ must be ClassType
    if isinstance(typ, ClassType):
      type_info = None
      found = False
      for classdecl in visibleScope[-1]: # => global
        if typ.classname.name == classdecl.name:
          type_info = classdecl
          found = True
          break
      if not found: raise Undeclared(Class(), typ.classname.name)
      target_method = self.searchMethodCalledByClass(type_info.name, ast.method.name)
      if target_method:
        if not isinstance(target_method.typ.rettype, VoidType):
          raise TypeMismatchInStatement(ast)
        return target_method.typ
      raise Undeclared(Method(), ast.method.name)
    raise TypeMismatchInStatement(ast)
  
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

  def visitArrayType(self, ast, param):
    return ast

  def visitClassType(self, ast, c):
    return ClassType(ast.classname)