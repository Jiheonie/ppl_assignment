from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    # def visitProgram(self,ctx:CSlangParser.ProgramContext):
    #     return Program([self.visit(x) for x in ctx.classdecl()])

    # def visitClassdecl(self,ctx:CSlangParser.ClassdeclContext):
    #     return ClassDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.memdecl()])

    # def visitMemdecl(self,ctx:CSlangParser.MemdeclContext):
    #     return AttributeDecl(VarDecl(Id(ctx.ID().getText()),self.visit(ctx.cslangtype())))

    # def visitCslangtype(self,ctx:CSlangParser.CslangtypeContext):
    #     return IntType() if ctx.INTTYPE() else VoidType()
        


    
  def visitProgram(self, ctx:CSlangParser.ProgramContext):
    return Program(self.visit(ctx.prog_decl_list()))


  # Visit a parse tree produced by CSlangParser#prog_decl_list.
  def visitProg_decl_list(self, ctx:CSlangParser.Prog_decl_listContext):
    return [self.visit(ctx.prog_decl())] + (self.visit(ctx.prog_decl_list()) if ctx.prog_decl_list() else [])


  # Visit a parse tree produced by CSlangParser#exp.
  def visitExp(self, ctx:CSlangParser.ExpContext):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp1(0))
    return BinaryOp(ctx.CONCAT_OP().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))


  # Visit a parse tree produced by CSlangParser#exp1.
  def visitExp1(self, ctx:CSlangParser.Exp1Context):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp2(0))
    return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))


  # Visit a parse tree produced by CSlangParser#exp2.
  def visitExp2(self, ctx:CSlangParser.Exp2Context):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp3())
    return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))


  # Visit a parse tree produced by CSlangParser#exp3.
  def visitExp3(self, ctx:CSlangParser.Exp3Context):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp4())
    return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))


  # Visit a parse tree produced by CSlangParser#exp4.
  def visitExp4(self, ctx:CSlangParser.Exp4Context):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp5())
    return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))


  # Visit a parse tree produced by CSlangParser#exp5.
  def visitExp5(self, ctx:CSlangParser.Exp5Context):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp6())
    return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp5()))


  # Visit a parse tree produced by CSlangParser#exp6.
  def visitExp6(self, ctx:CSlangParser.Exp6Context):
    if ctx.getChildCount() == 1:
      return self.visit(ctx.exp7())
    return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))


  # Visit a parse tree produced by CSlangParser#exp7.
  def visitExp7(self, ctx:CSlangParser.Exp7Context):
    return self.visit(ctx.exp8()) if ctx.exp8() else self.visit(ctx.arr_ele())


  # Visit a parse tree produced by CSlangParser#exp8.
  def visitExp8(self, ctx:CSlangParser.Exp8Context):
    if ctx.exp8():
      if ctx.getChildCount() == 3:
        return FieldAccess(self.visit(ctx.exp8()), Id(ctx.ID().getText()))
      return CallExpr(self.visit(ctx.exp8()), Id(ctx.ID().getText()), self.visit(ctx.exp_list()))
    return self.visit(ctx.exp9())


  # Visit a parse tree produced by CSlangParser#exp9.
  def visitExp9(self, ctx:CSlangParser.Exp9Context):
    if ctx.exp10():
      return self.visit(ctx.exp10())
    return self.visit(ctx.static_access())


  # Visit a parse tree produced by CSlangParser#exp10.
  def visitExp10(self, ctx:CSlangParser.Exp10Context):
    if ctx.literal():
      return self.visit(ctx.literal())
    if ctx.obj_cre():
      return self.visit(ctx.obj_cre())
    if ctx.exp():
      return self.visit(ctx.exp())
    if ctx.ID():
      return Id(ctx.ID().getText())
    if ctx.self_access():
      return self.visit(ctx.self_access())
    return NullLiteral()


  # Visit a parse tree produced by CSlangParser#literal.
  def visitLiteral(self, ctx:CSlangParser.LiteralContext):
    if ctx.array_lit():
      return self.visit(ctx.array_lit())
    return self.visit(ctx.ele_literal())


  # Visit a parse tree produced by CSlangParser#ele_literal.
  def visitEle_literal(self, ctx:CSlangParser.Ele_literalContext):
    if ctx.INT_LIT():
      return IntLiteral(int(ctx.INT_LIT().getText()))
    if ctx.FLOAT_LIT():
      return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
    if ctx.STR_LIT():
      return StringLiteral(ctx.STR_LIT().getText())    
    return BooleanLiteral(True if ctx.BOOL_LIT().getText() == "true" else False)


  # Visit a parse tree produced by CSlangParser#ele_literal_list.
  def visitEle_literal_list(self, ctx:CSlangParser.Ele_literal_listContext):
    return [self.visit(ctx.ele_literal())] + (self.visit(ctx.ele_literal_list()) if ctx.ele_literal_list() else [])


  # Visit a parse tree produced by CSlangParser#exp_list.
  def visitExp_list(self, ctx:CSlangParser.Exp_listContext):
    return self.visit(ctx.exp_prime()) if ctx.getChildCount() == 1 else []


  # Visit a parse tree produced by CSlangParser#exp_prime.
  def visitExp_prime(self, ctx:CSlangParser.Exp_primeContext):
    return [self.visit(ctx.exp())] + (self.visit(ctx.exp_prime()) if ctx.exp_prime() else [])


  # Visit a parse tree produced by CSlangParser#func_type.
  def visitFunc_type(self, ctx:CSlangParser.Func_typeContext):
    return self.visit(ctx.ref_type()) if ctx.ref_type() else VoidType()


  # Visit a parse tree produced by CSlangParser#ref_type.
  def visitRef_type(self, ctx:CSlangParser.Ref_typeContext):
    return self.visit(ctx.ele_type() if ctx.ele_type() else ctx.array_type())


  # Visit a parse tree produced by CSlangParser#array_type.
  def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
    return ArrayType(ctx.INT_LIT().getText(), self.visit(ctx.ele_type()))


  # Visit a parse tree produced by CSlangParser#ele_type.
  def visitEle_type(self, ctx:CSlangParser.Ele_typeContext):
    return self.visit(ctx.value_type()) if ctx.value_type() else ClassType(Id(ctx.ID().getText()))


  # Visit a parse tree produced by CSlangParser#value_type.
  def visitValue_type(self, ctx:CSlangParser.Value_typeContext):
    if ctx.INT():
      return IntType()
    if ctx.FLOAT():
      return FloatType()
    if ctx.STRING():
      return StringType()
    return BoolType()


  # Visit a parse tree produced by CSlangParser#prog_decl.
  def visitProg_decl(self, ctx:CSlangParser.Prog_declContext):
    return self.visit(ctx.class_decl()) 


  # Visit a parse tree produced by CSlangParser#class_decl.
  def visitClass_decl(self, ctx:CSlangParser.Class_declContext):
    if ctx.INHERIT():
      return ClassDecl(
        Id(ctx.ID(1).getText()), 
        self.visit(ctx.class_mem_list()),
        Id(ctx.ID(0).getText()), 
      )
    return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.class_mem_list()))


  # Visit a parse tree produced by CSlangParser#class_mem_list.
  def visitClass_mem_list(self, ctx:CSlangParser.Class_mem_listContext):
    return self.visit(ctx.class_mem()) + self.visit(ctx.class_mem_list()) if ctx.class_mem() else []


  # Visit a parse tree produced by CSlangParser#class_mem.
  def visitClass_mem(self, ctx:CSlangParser.Class_memContext):
    return self.visit(ctx.attr_decl()) if ctx.attr_decl() else [self.visit(ctx.method_decl())]


  # Visit a parse tree produced by CSlangParser#obj_cre.
  def visitObj_cre(self, ctx:CSlangParser.Obj_creContext):
    return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exp_list()))


  # Visit a parse tree produced by CSlangParser#inst_method_access.
  def visitInst_method_access(self, ctx:CSlangParser.Inst_method_accessContext):
    return (self.visit(ctx.exp8()), Id(ctx.ID().getText()), self.visit(ctx.exp_list()))


  # Visit a parse tree produced by CSlangParser#static_access.
  def visitStatic_access(self, ctx:CSlangParser.Static_accessContext):
    if ctx.static_mem_access():
      return self.visit(ctx.static_mem_access()) 
    params = self.visit(ctx.static_method_access())
    return CallExpr(params[0], params[1], params[2])
    # return CallExpr(None, params[0], params[1])


  # Visit a parse tree produced by CSlangParser#static_mem_access.
  def visitStatic_mem_access(self, ctx:CSlangParser.Static_mem_accessContext):
    return FieldAccess(Id(ctx.ID().getText()) if ctx.ID() else None, Id(ctx.AT_ID().getText()))
    # return FieldAccess(None, Id(ctx.AT_ID().getText()))


  # Visit a parse tree produced by CSlangParser#static_method_access.
  def visitStatic_method_access(self, ctx:CSlangParser.Static_method_accessContext):
    if ctx.ID():
      return (Id(ctx.ID().getText()), Id(ctx.AT_ID().getText()), self.visit(ctx.exp_list()))
    return (None, Id(ctx.AT_ID().getText()), self.visit(ctx.exp_list()))
    # return (Id(ctx.AT_ID().getText()), self.visit(ctx.exp_list()))


  # Visit a parse tree produced by CSlangParser#self_access.
  def visitSelf_access(self, ctx:CSlangParser.Self_accessContext):
    if ctx.self_mem_access():
      return self.visit(ctx.self_mem_access()) 
    params = self.visit(ctx.self_method_access())
    return CallExpr(params[0], params[1], params[2])


  # Visit a parse tree produced by CSlangParser#self_mem_access.
  def visitSelf_mem_access(self, ctx:CSlangParser.Self_mem_accessContext):
    return FieldAccess(SelfLiteral(), Id(ctx.getChild(2).getText()))


  # Visit a parse tree produced by CSlangParser#self_method_access.
  def visitSelf_method_access(self, ctx:CSlangParser.Self_method_accessContext):
    return (SelfLiteral(), Id(ctx.getChild(2).getText()), self.visit(ctx.exp_list()))


  # Visit a parse tree produced by CSlangParser#method_decl.
  def visitMethod_decl(self, ctx:CSlangParser.Method_declContext):
    if ctx.func_decl():
      return self.visit(ctx.func_decl())
    if ctx.constructor_decl():
      return self.visit(ctx.constructor_decl())
    return self.visit(ctx.static_func_decl())


  # Visit a parse tree produced by CSlangParser#func_decl.
  def visitFunc_decl(self, ctx:CSlangParser.Func_declContext):
    decl_params = self.visit(ctx.expo_func())
    return MethodDecl(
      Id(ctx.ID().getText()),
      decl_params[0],
      decl_params[1],
      decl_params[2]
    )


  # Visit a parse tree produced by CSlangParser#static_func_decl.
  def visitStatic_func_decl(self, ctx:CSlangParser.Static_func_declContext):
    expo_func = self.visit(ctx.expo_func())
    return MethodDecl(Id(ctx.AT_ID().getText()), expo_func[0], expo_func[1], expo_func[2])


  # Visit a parse tree produced by CSlangParser#expo_func.
  def visitExpo_func(self, ctx:CSlangParser.Expo_funcContext):
    return (self.visit(ctx.params_list()), self.visit(ctx.func_type()), self.visit(ctx.block_stmt()))


  # Visit a parse tree produced by CSlangParser#constructor_decl.
  def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
    return MethodDecl(
      Id("constructor"),
      self.visit(ctx.params_list()),
      VoidType(),
      self.visit(ctx.block_stmt())
    )


  # Visit a parse tree produced by CSlangParser#attr_decl.
  def visitAttr_decl(self, ctx:CSlangParser.Attr_declContext):
    lst = ctx.const_decl() if ctx.const_decl() else ctx.var_decl()
    return [AttributeDecl(x) for x in self.visit(lst)]


    # Visit a parse tree produced by CSlangParser#const_decl.
  def visitConst_decl(self, ctx:CSlangParser.Const_declContext):
    # attr_decl_list = []
    # mid_idx = int((len(self.visit(ctx.attr_decl_body_full())) - 1) / 2)
    # ref_type = self.visit(ctx.attr_decl_body_full())[mid_idx]
    # for idx in range(0, mid_idx):
    #   identifier = self.visit(ctx.attr_decl_body_full())[idx]
    #   exp = self.visit(ctx.attr_decl_body_full())[mid_idx + 1 + idx]
    #   attr_decl_list.append((identifier, ref_type, exp))
    # return [ConstDecl(x[0], x[1], x[2]) for x in attr_decl_list]
    return [ConstDecl(x[0], x[1], x[2]) for x in self.visit(ctx.attr_decl_body())]



  # Visit a parse tree produced by CSlangParser#var_decl.
  def visitVar_decl(self, ctx:CSlangParser.Var_declContext):
    return [VarDecl(x[0], x[1], x[2]) for x in self.visit(ctx.attr_decl_body())]


  # Visit a parse tree produced by CSlangParser#attr_decl_body.
  def visitAttr_decl_body(self, ctx:CSlangParser.Attr_decl_bodyContext):
    if ctx.attr_decl_body_full():
      attr_decl_list = []
      mid_idx = int((len(self.visit(ctx.attr_decl_body_full())) - 1) / 2)
      ref_type = self.visit(ctx.attr_decl_body_full())[mid_idx]
      for idx in range(0, mid_idx):
        identifier = self.visit(ctx.attr_decl_body_full())[idx]
        exp = self.visit(ctx.attr_decl_body_full())[mid_idx + 1 + idx]
        attr_decl_list.append((identifier, ref_type, exp))
      return attr_decl_list
    return self.visit(ctx.attr_decl_body_short())


  # Visit a parse tree produced by CSlangParser#attr_decl_body_short.
  def visitAttr_decl_body_short(self, ctx:CSlangParser.Attr_decl_body_shortContext):
    return list(map(lambda x: (x, self.visit(ctx.ref_type()), None), self.visit(ctx.identifier_list())))


  # Visit a parse tree produced by CSlangParser#attr_decl_body_full.
  def visitAttr_decl_body_full(self, ctx:CSlangParser.Attr_decl_body_fullContext):
    identifier = Id(ctx.ID().getText() if ctx.ID() else ctx.AT_ID().getText())
    if ctx.attr_decl_body_full():
      return [identifier] +  self.visit(ctx.attr_decl_body_full()) + [self.visit(ctx.exp())]
    return [identifier, self.visit(ctx.ref_type()), self.visit(ctx.exp())]


  # Visit a parse tree produced by CSlangParser#identifier_list.
  def visitIdentifier_list(self, ctx:CSlangParser.Identifier_listContext):
    identifier = Id(ctx.ID().getText() if ctx.ID() else ctx.AT_ID().getText())
    return [identifier] + (self.visit(ctx.identifier_list()) if ctx.getChildCount() == 3 else [])


  # Visit a parse tree produced by CSlangParser#stmt.
  def visitStmt(self, ctx:CSlangParser.StmtContext):
    if ctx.assign_stmt():
      return [self.visit(ctx.assign_stmt())]
    if ctx.if_stmt():
      return [self.visit(ctx.if_stmt())]
    if ctx.for_stmt():
      return [self.visit(ctx.for_stmt())]
    if ctx.break_stmt():
      return [self.visit(ctx.break_stmt())]
    if ctx.continue_stmt():
      return [self.visit(ctx.continue_stmt())]
    if ctx.return_stmt():
      return [self.visit(ctx.return_stmt())]
    if ctx.method_invocation_stmt():
      return [self.visit(ctx.method_invocation_stmt())]
    return self.visit(ctx.decl_stmt())
  

  # Visit a parse tree produced by CSlangParser#decl_stmt.
  def visitDecl_stmt(self, ctx:CSlangParser.Decl_stmtContext):
    return self.visit(ctx.const_decl_stmt()) if ctx.const_decl_stmt() else self.visit(ctx.var_decl_stmt())


    # Visit a parse tree produced by CSlangParser#const_decl_stmt.
  def visitConst_decl_stmt(self, ctx:CSlangParser.Const_decl_stmtContext):
    return [ConstDecl(x[0], x[1], x[2]) for x in self.visit(ctx.decl_stmt_body())]


    # Visit a parse tree produced by CSlangParser#var_decl_stmt.
  def visitVar_decl_stmt(self, ctx:CSlangParser.Var_decl_stmtContext):
    return [VarDecl(x[0], x[1], x[2]) for x in self.visit(ctx.decl_stmt_body())]


    # Visit a parse tree produced by CSlangParser#decl_stmt_body.
  def visitDecl_stmt_body(self, ctx:CSlangParser.Decl_stmt_bodyContext):
    if ctx.decl_stmt_body_full():
      attr_decl_list = []
      mid_idx = int((len(self.visit(ctx.decl_stmt_body_full())) - 1) / 2)
      ref_type = self.visit(ctx.decl_stmt_body_full())[mid_idx]
      for idx in range(0, mid_idx):
        identifier = self.visit(ctx.decl_stmt_body_full())[idx]
        exp = self.visit(ctx.decl_stmt_body_full())[mid_idx + 1 + idx]
        attr_decl_list.append((identifier, ref_type, exp))
      return attr_decl_list
    return self.visit(ctx.decl_stmt_body_short())


    # Visit a parse tree produced by CSlangParser#decl_stmt_body_short.
  def visitDecl_stmt_body_short(self, ctx:CSlangParser.Decl_stmt_body_shortContext):
      return list(map(lambda x: (x, self.visit(ctx.ref_type()), None), self.visit(ctx.id_list_not_null())))


    # Visit a parse tree produced by CSlangParser#decl_stmt_body_full.
  def visitDecl_stmt_body_full(self, ctx:CSlangParser.Decl_stmt_body_fullContext):
      iden = Id(ctx.ID().getText())
      if ctx.decl_stmt_body_full():
        return [iden] + self.visit(ctx.decl_stmt_body_full()) + [self.visit(ctx.exp())]
      return [iden, self.visit(ctx.ref_type()), self.visit(ctx.exp())]


  # Visit a parse tree produced by CSlangParser#assign_stmt.
  def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
    return Assign(self.visit(ctx.exp7()), self.visit(ctx.exp()))


  # Visit a parse tree produced by CSlangParser#if_stmt.
  def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
    if ctx.getChildCount() == 3:
      return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(0)))
    if ctx.getChildCount() == 4:
      return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(1)), self.visit(ctx.block_stmt(0)))
    if ctx.getChildCount() == 5:
      return If(self.visit(ctx.exp()), self.visit(ctx.block_stmt(0)), None, self.visit(ctx.block_stmt(1)))
    return If(
      self.visit(ctx.exp()), 
      self.visit(ctx.block_stmt(1)), 
      self.visit(ctx.block_stmt(1)), 
      self.visit(ctx.block_stmt(2))
    )


  # Visit a parse tree produced by CSlangParser#for_stmt.
  def visitFor_stmt(self, ctx:CSlangParser.For_stmtContext):
    return For(
      self.visit(ctx.assign_stmt(0)),
      self.visit(ctx.exp()),
      self.visit(ctx.assign_stmt(1)),
      self.visit(ctx.block_stmt())
    )


  # Visit a parse tree produced by CSlangParser#break_stmt.
  def visitBreak_stmt(self, ctx:CSlangParser.Break_stmtContext):
    return Break()


  # Visit a parse tree produced by CSlangParser#continue_stmt.
  def visitContinue_stmt(self, ctx:CSlangParser.Continue_stmtContext):
    return Continue()


  # Visit a parse tree produced by CSlangParser#return_stmt.
  def visitReturn_stmt(self, ctx:CSlangParser.Return_stmtContext):
    return Return(self.visit(ctx.exp())) if ctx.exp() else Return(None)


  # Visit a parse tree produced by CSlangParser#method_invocation_stmt.
  def visitMethod_invocation_stmt(self, ctx:CSlangParser.Method_invocation_stmtContext):
    params = self.visit(ctx.getChild(0))
    # if ctx.inst_method_access():
    #   return CallStmt(params[0], params[1], params[2])
    # if ctx.static_method_access():
    #   return CallStmt(None, params[0], params[1])
    return CallStmt(params[0], params[1], params[2])


  # Visit a parse tree produced by CSlangParser#block_stmt.
  def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
    return Block(self.visit(ctx.body()))


  # Visit a parse tree produced by CSlangParser#body.
  def visitBody(self, ctx:CSlangParser.BodyContext):
    return self.visit(ctx.stmt()) + self.visit(ctx.body()) if ctx.getChildCount() == 2 else []


  # Visit a parse tree produced by CSlangParser#params_list.
  def visitParams_list(self, ctx:CSlangParser.Params_listContext):
    return self.visit(ctx.params_prime()) if ctx.params_prime() else []


  # Visit a parse tree produced by CSlangParser#params_prime.
  def visitParams_prime(self, ctx:CSlangParser.Params_primeContext):
    return self.visit(ctx.params_1_type()) + (self.visit(ctx.params_prime()) if ctx.params_prime() else [])


  # Visit a parse tree produced by CSlangParser#params_1_type.
  def visitParams_1_type(self, ctx:CSlangParser.Params_1_typeContext):
    return [VarDecl(x, self.visit(ctx.ref_type())) for x in self.visit(ctx.id_list_not_null())]


  # Visit a parse tree produced by CSlangParser#id_list_not_null.
  def visitId_list_not_null(self, ctx:CSlangParser.Id_list_not_nullContext):
    return [Id(ctx.ID().getText())] + (self.visit(ctx.id_list_not_null()) if ctx.getChildCount() == 3 else [])


  # Visit a parse tree produced by CSlangParser#array_lit.
  def visitArray_lit(self, ctx:CSlangParser.Array_litContext):
    return ArrayLiteral(self.visit(ctx.ele_literal_list()))


  # Visit a parse tree produced by CSlangParser#arr_ele.
  def visitArr_ele(self, ctx:CSlangParser.Arr_eleContext):
    return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp()))
      

  
