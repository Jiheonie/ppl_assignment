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


    # Visit a parse tree produced by CSlangParser#prog_decl_list.
    def visitProg_decl_list(self, ctx:CSlangParser.Prog_decl_listContext):
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


    # Visit a parse tree produced by CSlangParser#exp10.
    def visitExp10(self, ctx:CSlangParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_list.
    def visitExp_list(self, ctx:CSlangParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_prime.
    def visitExp_prime(self, ctx:CSlangParser.Exp_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#func_type.
    def visitFunc_type(self, ctx:CSlangParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ref_type.
    def visitRef_type(self, ctx:CSlangParser.Ref_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ele_type.
    def visitEle_type(self, ctx:CSlangParser.Ele_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#prog_decl.
    def visitProg_decl(self, ctx:CSlangParser.Prog_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_decl.
    def visitClass_decl(self, ctx:CSlangParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#program_class_decl.
    def visitProgram_class_decl(self, ctx:CSlangParser.Program_class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_mem_list.
    def visitClass_mem_list(self, ctx:CSlangParser.Class_mem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_mem.
    def visitClass_mem(self, ctx:CSlangParser.Class_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#prog_class_mem_list.
    def visitProg_class_mem_list(self, ctx:CSlangParser.Prog_class_mem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#prog_class_mem.
    def visitProg_class_mem(self, ctx:CSlangParser.Prog_class_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#obj_cre.
    def visitObj_cre(self, ctx:CSlangParser.Obj_creContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#mem_access.
    def visitMem_access(self, ctx:CSlangParser.Mem_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_access.
    def visitMethod_access(self, ctx:CSlangParser.Method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#inst_mem_access.
    def visitInst_mem_access(self, ctx:CSlangParser.Inst_mem_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#inst_method_access.
    def visitInst_method_access(self, ctx:CSlangParser.Inst_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_access.
    def visitStatic_access(self, ctx:CSlangParser.Static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_mem_access.
    def visitStatic_mem_access(self, ctx:CSlangParser.Static_mem_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_method_access.
    def visitStatic_method_access(self, ctx:CSlangParser.Static_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#self_access.
    def visitSelf_access(self, ctx:CSlangParser.Self_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#self_mem_access.
    def visitSelf_mem_access(self, ctx:CSlangParser.Self_mem_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#self_method_access.
    def visitSelf_method_access(self, ctx:CSlangParser.Self_method_accessContext):
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


    # Visit a parse tree produced by CSlangParser#main_func_decl.
    def visitMain_func_decl(self, ctx:CSlangParser.Main_func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_decl.
    def visitConstructor_decl(self, ctx:CSlangParser.Constructor_declContext):
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


    # Visit a parse tree produced by CSlangParser#identifier_list.
    def visitIdentifier_list(self, ctx:CSlangParser.Identifier_listContext):
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


    # Visit a parse tree produced by CSlangParser#params_prime.
    def visitParams_prime(self, ctx:CSlangParser.Params_primeContext):
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