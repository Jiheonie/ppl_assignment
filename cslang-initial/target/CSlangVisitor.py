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


    # Visit a parse tree produced by CSlangParser#decl.
    def visitDecl(self, ctx:CSlangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_decl.
    def visitClass_decl(self, ctx:CSlangParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl.
    def visitAttr_decl(self, ctx:CSlangParser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_exp.
    def visitAttr_decl_exp(self, ctx:CSlangParser.Attr_decl_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_exp_no_value.
    def visitAttr_decl_exp_no_value(self, ctx:CSlangParser.Attr_decl_exp_no_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr_decl_exp_value.
    def visitAttr_decl_exp_value(self, ctx:CSlangParser.Attr_decl_exp_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
        return self.visitChildren(ctx)



del CSlangParser