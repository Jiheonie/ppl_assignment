# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\34")
        buf.write("\n\3\3\4\3\4\3\5\3\5\3\5\3\5\5\5$\n\5\3\6\3\6\5\6(\n\6")
        buf.write("\3\7\3\7\3\7\3\7\5\7.\n\7\3\7\3\7\7\7\62\n\7\f\7\16\7")
        buf.write("\65\13\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b=\n\b\f\b\16\b@\13")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bF\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\5\4\2")
        buf.write("\37\37!!\3\2\4\5\4\2\31\31\35\35\2O\2\24\3\2\2\2\4\33")
        buf.write("\3\2\2\2\6\35\3\2\2\2\b#\3\2\2\2\n\'\3\2\2\2\f)\3\2\2")
        buf.write("\2\168\3\2\2\2\20I\3\2\2\2\22M\3\2\2\2\24\25\7\2\2\3\25")
        buf.write("\3\3\2\2\2\26\27\5\6\4\2\27\30\t\2\2\2\30\31\5\6\4\2\31")
        buf.write("\34\3\2\2\2\32\34\5\6\4\2\33\26\3\2\2\2\33\32\3\2\2\2")
        buf.write("\34\5\3\2\2\2\35\36\t\3\2\2\36\7\3\2\2\2\37 \5\n\6\2 ")
        buf.write("!\5\b\5\2!$\3\2\2\2\"$\5\n\6\2#\37\3\2\2\2#\"\3\2\2\2")
        buf.write("$\t\3\2\2\2%(\5\f\7\2&(\5\16\b\2\'%\3\2\2\2\'&\3\2\2\2")
        buf.write("(\13\3\2\2\2)*\7\27\2\2*-\7\b\2\2+,\7\3\2\2,.\7\b\2\2")
        buf.write("-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/\63\78\2\2\60\62\5\16\b")
        buf.write("\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2")
        buf.write("\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\79\2\2\67\r\3\2")
        buf.write("\2\289\t\4\2\29>\7\b\2\2:;\7\65\2\2;=\7\b\2\2<:\3\2\2")
        buf.write("\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2A")
        buf.write("B\7\66\2\2BE\7\21\2\2CD\7(\2\2DF\5\4\3\2EC\3\2\2\2EF\3")
        buf.write("\2\2\2FG\3\2\2\2GH\7\67\2\2H\17\3\2\2\2IJ\7\b\2\2JK\7")
        buf.write("\'\2\2KL\7\5\2\2L\21\3\2\2\2MN\7\b\2\2NO\5\4\3\2OP\7\67")
        buf.write("\2\2P\23\3\2\2\2\t\33#\'-\63>E")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
                     "'float'", "'bool'", "'string'", "'return'", "'null'", 
                     "'class'", "'constructor'", "'var'", "'self'", "'new'", 
                     "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "':='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", "'%'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "':'", "';'", 
                     "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "FLOAT_LIT", "INT_LIT", 
                      "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                      "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                      "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                      "CONST", "FUNC", "PLUS_OP", "MINUS_OP", "MUL_OP", 
                      "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", 
                      "EQUAL_OP", "ASSIGN_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
                      "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "DIV_OP", 
                      "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", 
                      "SEMICOLON", "LCB", "RCB", "SIN_Q", "DOU_Q", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_exp1 = 2
    RULE_decllist = 3
    RULE_decl = 4
    RULE_class_decl = 5
    RULE_attr_decl = 6
    RULE_attr_decl1 = 7
    RULE_assign_stmt = 8

    ruleNames =  [ "program", "exp", "exp1", "decllist", "decl", "class_decl", 
                   "attr_decl", "attr_decl1", "assign_stmt" ]

    EOF = Token.EOF
    T__0=1
    FLOAT_LIT=2
    INT_LIT=3
    STR_LIT=4
    BOOL_LIT=5
    ID=6
    CMT_LINE=7
    BREAK=8
    CONTINUE=9
    IF=10
    ELSE=11
    FOR=12
    TRUE=13
    FALSE=14
    INT=15
    FLOAT=16
    BOOL=17
    STRING=18
    RETURN=19
    NULL=20
    CLASS=21
    CONSTRUCTOR=22
    VAR=23
    SELF=24
    NEW=25
    VOID=26
    CONST=27
    FUNC=28
    PLUS_OP=29
    MINUS_OP=30
    MUL_OP=31
    SLASH=32
    BACKSLASH=33
    NOT_OP=34
    AND_OP=35
    OR_OP=36
    EQUAL_OP=37
    ASSIGN_OP=38
    DIFF_OP=39
    LESS_OP=40
    LESS_EQUAL_OP=41
    GREATER_OP=42
    GREATER_EQUAL_OP=43
    CONCAT_OP=44
    DIV_OP=45
    LP=46
    RP=47
    LSB=48
    RSB=49
    DOT=50
    COMMA=51
    COLON=52
    SEMICOLON=53
    LCB=54
    RCB=55
    SIN_Q=56
    DOU_Q=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp1Context,i)


        def MUL_OP(self):
            return self.getToken(CSlangParser.MUL_OP, 0)

        def PLUS_OP(self):
            return self.getToken(CSlangParser.PLUS_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.exp1()
                self.state = 21
                _la = self._input.LA(1)
                if not(_la==CSlangParser.PLUS_OP or _la==CSlangParser.MUL_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 22
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==CSlangParser.FLOAT_LIT or _la==CSlangParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(CSlangParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(CSlangParser.DecllistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = CSlangParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decllist)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.decl()
                self.state = 30
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(CSlangParser.Class_declContext,0)


        def attr_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attr_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.attr_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def attr_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Attr_declContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Attr_declContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CSlangParser.CLASS)
            self.state = 40
            self.match(CSlangParser.ID)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__0:
                self.state = 41
                self.match(CSlangParser.T__0)
                self.state = 42
                self.match(CSlangParser.ID)


            self.state = 45
            self.match(CSlangParser.LCB)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.VAR or _la==CSlangParser.CONST:
                self.state = 46
                self.attr_decl()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = CSlangParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(CSlangParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 56
                self.match(CSlangParser.COMMA)
                self.state = 57
                self.match(CSlangParser.ID)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(CSlangParser.COLON)
            self.state = 64
            self.match(CSlangParser.INT)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ASSIGN_OP:
                self.state = 65
                self.match(CSlangParser.ASSIGN_OP)
                self.state = 66
                self.exp()


            self.state = 69
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def EQUAL_OP(self):
            return self.getToken(CSlangParser.EQUAL_OP, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl1" ):
                return visitor.visitAttr_decl1(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl1(self):

        localctx = CSlangParser.Attr_decl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_decl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(CSlangParser.ID)
            self.state = 72
            self.match(CSlangParser.EQUAL_OP)
            self.state = 73
            self.match(CSlangParser.INT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(CSlangParser.ID)
            self.state = 76
            self.exp()
            self.state = 77
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





