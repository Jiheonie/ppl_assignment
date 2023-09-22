# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp.
    def visitExp(self, ctx:CSlangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp1.
    def visitExp1(self, ctx:CSlangParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp2.
    def visitExp2(self, ctx:CSlangParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp3.
    def visitExp3(self, ctx:CSlangParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp4.
    def visitExp4(self, ctx:CSlangParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp5.
    def visitExp5(self, ctx:CSlangParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp6.
    def visitExp6(self, ctx:CSlangParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp7.
    def visitExp7(self, ctx:CSlangParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp8.
    def visitExp8(self, ctx:CSlangParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp9.
    def visitExp9(self, ctx:CSlangParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_list.
    def visitExp_list(self, ctx:CSlangParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#func_type.
    def visitFunc_type(self, ctx:CSlangParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ref_type.
    def visitRef_type(self, ctx:CSlangParser.Ref_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#value_type.
    def visitValue_type(self, ctx:CSlangParser.Value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decl.
    def visitDecl(self, ctx:CSlangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_decl.
    def visitClass_decl(self, ctx:CSlangParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_access.
    def visitStatic_access(self, ctx:CSlangParser.Static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#inst_access.
    def visitInst_access(self, ctx:CSlangParser.Inst_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#obj_cre.
    def visitObj_cre(self, ctx:CSlangParser.Obj_creContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#mem_access.
    def visitMem_access(self, ctx:CSlangParser.Mem_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_mem_access.
    def visitStatic_mem_access(self, ctx:CSlangParser.Static_mem_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_access.
    def visitMethod_access(self, ctx:CSlangParser.Method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_method_access.
    def visitStatic_method_access(self, ctx:CSlangParser.Static_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_decl.
    def visitMethod_decl(self, ctx:CSlangParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#func_decl.
    def visitFunc_decl(self, ctx:CSlangParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_func_decl.
    def visitStatic_func_decl(self, ctx:CSlangParser.Static_func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expo_func.
    def visitExpo_func(self, ctx:CSlangParser.Expo_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_decl.
    def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_constructor_decl.
    def visitStatic_constructor_decl(self, ctx:CSlangParser.Static_constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expo_constructor.
    def visitExpo_constructor(self, ctx:CSlangParser.Expo_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#func_call.
    def visitFunc_call(self, ctx:CSlangParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl.
    def visitAttr_decl(self, ctx:CSlangParser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_body.
    def visitAttr_decl_body(self, ctx:CSlangParser.Attr_decl_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_body_short.
    def visitAttr_decl_body_short(self, ctx:CSlangParser.Attr_decl_body_shortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_body_full.
    def visitAttr_decl_body_full(self, ctx:CSlangParser.Attr_decl_body_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_stmt.
    def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_stmt.
    def visitFor_stmt(self, ctx:CSlangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSlangParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSlangParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSlangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:CSlangParser.Method_invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#body.
    def visitBody(self, ctx:CSlangParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params_list.
    def visitParams_list(self, ctx:CSlangParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params_1_type.
    def visitParams_1_type(self, ctx:CSlangParser.Params_1_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_lit.
    def visitArray_lit(self, ctx:CSlangParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arr_ele.
    def visitArr_ele(self, ctx:CSlangParser.Arr_eleContext):
        return self.visitChildren(ctx)



del CSlangParser