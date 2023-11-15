
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

  def searchClassByName(self, classname):
    for mem in self.global_env:
      if classname == mem.name and isinstance(mem, BKClass):
        return mem
    return None
  
  def searchStaticMemByName(self, name):
    for mem in self.global_env:
      if name == mem.name and isinstance(mem, StaticMember):
        return mem
    return None

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

  # def visitIntType(self, ast, param):
  #   return IntType()

  # def visitFloatType(self, ast, param):
  #   return FloatType()

  # def visitBoolType(self, ast, param):
  #   return BoolType()

  # def visitStringType(self, ast, param):
  #   return StringType()

  # def visitVoidType(self, ast, param):
  #   return VoidType()

  # def visitArrayType(self, ast, param):
  #   return ast

  # def visitClassType(self, ast, param):
  #   env = self.globalEnv
  #   return ClassType(ast.classname)

  

class StaticChecker(BaseVisitor, Utils):
  inttype = IntType()
  floattype = FloatType()
  voidtype = VoidType()
  booltype = BoolType()
  stringtype = StringType()

  def __init__(self, ast):
    self.ast = ast
    self.global_env = []

  def check(self):
    self.visit(self.ast, self.global_env)
    return ""

  def visitProgram(self, ast, c):
    c = GetEnv().visit(ast, c)
    self.global_env = reduce(lambda c_pre, decl: self.visit(decl, c_pre), ast.decl, c)
    return self.global_env

  def visitClassDecl(self, ast, c):
    func_mem = list(filter(lambda mem: type(mem) is MethodDecl, ast.memlist))
    reduce(lambda c_pre, mem_cur: self.visit(mem_cur, c_pre), func_mem, c)
  
  def visitMethodDecl(self, ast, c):
    decl_block = [decl for decl in ast.body.stmt if type(decl) in [VarDecl, ConstDecl]]
    stmt_block = [decl for decl in ast.body.stmt if decl not in decl_block]
    local_decl = ast.param + decl_block


    env = [] # => List[{name, typ, isMu}]
    env = reduce(lambda env_pre, decl: self.visit(decl, (Parameter(), env_pre)), ast.param, env)
    env = reduce(lambda env_pre, decl: self.visit(decl, (Variable(), env_pre)) if type(decl) is VarDecl else self.visit(Constant(), env_pre), local_decl, env)

    for stmt in stmt_block:
      self.visit(stmt, (env, c))

  def visitAttributeDecl(self,ast,c): pass

  def visitVarDecl(self, ast, c):
    if ast.variable.name in map(lambda decl: decl["name"], c[1]):
      if c[0] == Variable():
        raise Redeclared(Variable(), ast.variable.name)
      raise Redeclared(Parameter(), ast.variable.name)
    return c + [{"name": ast.variable.name, "typ": self.visit(ast.varType, c), "isMu": True}]

  def visitConstDecl(self, ast, c):
    if ast.constant.name in map(lambda decl: decl["name"], c[1]):
      raise Redeclared(Constant(), ast.constant.name)
    return c + [{"name": ast.constant.name, "typ": self.visit(ast.constType, c), "isMu": False}]
    

  def visitBlock(self, ast, c):
    pass