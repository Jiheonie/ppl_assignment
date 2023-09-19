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


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_list.
    def visitExp_list(self, ctx:CSlangParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#decl.
    def visitDecl(self, ctx:CSlangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_decl.
    def visitClass_decl(self, ctx:CSlangParser.Class_declContext):
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


    # Visit a parse tree produced by CSlangParser#attr_decl.
    def visitAttr_decl(self, ctx:CSlangParser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_exp.
    def visitAttr_decl_exp(self, ctx:CSlangParser.Attr_decl_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_exp_short.
    def visitAttr_decl_exp_short(self, ctx:CSlangParser.Attr_decl_exp_shortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_exp_full.
    def visitAttr_decl_exp_full(self, ctx:CSlangParser.Attr_decl_exp_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params_list.
    def visitParams_list(self, ctx:CSlangParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params_same_type.
    def visitParams_same_type(self, ctx:CSlangParser.Params_same_typeContext):
        return self.visitChildren(ctx)



del CSlangParser