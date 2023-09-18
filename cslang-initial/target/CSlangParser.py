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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\6\2\36\n\2\r\2\16\2\37\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\5\3\5\3\6\3\6\5")
        buf.write("\6\65\n\6\3\7\3\7\3\7\3\7\5\7;\n\7\3\7\3\7\3\7\7\7@\n")
        buf.write("\7\f\7\16\7C\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("M\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13^\n\13\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4")
        buf.write("\3\2\679\4\2\23\23\27\27\2e\2\35\3\2\2\2\4,\3\2\2\2\6")
        buf.write(".\3\2\2\2\b\60\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\16F\3")
        buf.write("\2\2\2\20L\3\2\2\2\22N\3\2\2\2\24]\3\2\2\2\26_\3\2\2\2")
        buf.write("\30a\3\2\2\2\32\36\5\4\3\2\33\36\5\30\r\2\34\36\5\n\6")
        buf.write("\2\35\32\3\2\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\2\2\3\"")
        buf.write("\3\3\2\2\2#$\5\6\4\2$%\7\33\2\2%&\5\6\4\2&-\3\2\2\2\'")
        buf.write("(\5\6\4\2()\7\31\2\2)*\5\6\4\2*-\3\2\2\2+-\5\6\4\2,#\3")
        buf.write("\2\2\2,\'\3\2\2\2,+\3\2\2\2-\5\3\2\2\2./\5\b\5\2/\7\3")
        buf.write("\2\2\2\60\61\t\2\2\2\61\t\3\2\2\2\62\65\5\f\7\2\63\65")
        buf.write("\5\16\b\2\64\62\3\2\2\2\64\63\3\2\2\2\65\13\3\2\2\2\66")
        buf.write("\67\7\21\2\2\67:\7;\2\289\7\3\2\29;\7;\2\2:8\3\2\2\2:")
        buf.write(";\3\2\2\2;<\3\2\2\2<A\7\63\2\2=@\5\26\f\2>@\5\16\b\2?")
        buf.write("=\3\2\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3")
        buf.write("\2\2\2CA\3\2\2\2DE\7\64\2\2E\r\3\2\2\2FG\t\3\2\2GH\5\20")
        buf.write("\t\2HI\7\62\2\2I\17\3\2\2\2JM\5\24\13\2KM\5\22\n\2LJ\3")
        buf.write("\2\2\2LK\3\2\2\2M\21\3\2\2\2NO\7;\2\2OP\7\61\2\2PQ\7\13")
        buf.write("\2\2Q\23\3\2\2\2RS\7;\2\2ST\7\60\2\2TU\5\24\13\2UV\7\60")
        buf.write("\2\2VW\78\2\2W^\3\2\2\2XY\7;\2\2YZ\7\61\2\2Z[\7\13\2\2")
        buf.write("[\\\7#\2\2\\^\78\2\2]R\3\2\2\2]X\3\2\2\2^\25\3\2\2\2_")
        buf.write("`\5\30\r\2`\27\3\2\2\2ab\7;\2\2bc\7\"\2\2cd\5\4\3\2de")
        buf.write("\7\62\2\2e\31\3\2\2\2\13\35\37,\64:?AL]")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'break'", "'continue'", "'if'", 
                     "'else'", "'for'", "'true'", "'false'", "'int'", "'float'", 
                     "'bool'", "'string'", "'return'", "'null'", "'class'", 
                     "'constructor'", "'var'", "'self'", "'new'", "'void'", 
                     "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'!'", "'&&'", "'||'", "'=='", "':='", "'='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'^'", "'%'", "'('", 
                     "')'", "'['", "']'", "'.'", "','", "':'", "';'", "'{'", 
                     "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", 
                      "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                      "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS_OP", 
                      "MINUS_OP", "MUL_OP", "SLASH", "BACKSLASH", "NOT_OP", 
                      "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", 
                      "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
                      "GREATER_EQUAL_OP", "CONCAT_OP", "DIV_OP", "LP", "RP", 
                      "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "LCB", "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "INT_LIT", 
                      "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_exp1 = 2
    RULE_literal = 3
    RULE_decl = 4
    RULE_class_decl = 5
    RULE_attr_decl = 6
    RULE_attr_decl_exp = 7
    RULE_attr_decl_exp_no_value = 8
    RULE_attr_decl_exp_value = 9
    RULE_stmt = 10
    RULE_assign_stmt = 11

    ruleNames =  [ "program", "exp", "exp1", "literal", "decl", "class_decl", 
                   "attr_decl", "attr_decl_exp", "attr_decl_exp_no_value", 
                   "attr_decl_exp_value", "stmt", "assign_stmt" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSE=5
    FOR=6
    TRUE=7
    FALSE=8
    INT=9
    FLOAT=10
    BOOL=11
    STRING=12
    RETURN=13
    NULL=14
    CLASS=15
    CONSTRUCTOR=16
    VAR=17
    SELF=18
    NEW=19
    VOID=20
    CONST=21
    FUNC=22
    PLUS_OP=23
    MINUS_OP=24
    MUL_OP=25
    SLASH=26
    BACKSLASH=27
    NOT_OP=28
    AND_OP=29
    OR_OP=30
    EQUAL_OP=31
    ASSIGN_OP=32
    DECL_OP=33
    DIFF_OP=34
    LESS_OP=35
    LESS_EQUAL_OP=36
    GREATER_OP=37
    GREATER_EQUAL_OP=38
    CONCAT_OP=39
    DIV_OP=40
    LP=41
    RP=42
    LSB=43
    RSB=44
    DOT=45
    COMMA=46
    COLON=47
    SEMICOLON=48
    LCB=49
    RCB=50
    SIN_Q=51
    DOU_Q=52
    FLOAT_LIT=53
    INT_LIT=54
    STR_LIT=55
    BOOL_LIT=56
    ID=57
    CMT_LINE=58
    WS=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.DeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.DeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT]:
                    self.state = 24
                    self.exp()
                    pass
                elif token in [CSlangParser.ID]:
                    self.state = 25
                    self.assign_stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST]:
                    self.state = 26
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.ID))) != 0)):
                    break

            self.state = 31
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
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.exp1()
                self.state = 34
                self.match(CSlangParser.MUL_OP)
                self.state = 35
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.exp1()
                self.state = 38
                self.match(CSlangParser.PLUS_OP)
                self.state = 39
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
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

        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(CSlangParser.STR_LIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT))) != 0)):
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtContext,i)


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
            self.state = 52
            self.match(CSlangParser.CLASS)
            self.state = 53
            self.match(CSlangParser.ID)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__0:
                self.state = 54
                self.match(CSlangParser.T__0)
                self.state = 55
                self.match(CSlangParser.ID)


            self.state = 58
            self.match(CSlangParser.LCB)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.ID))) != 0):
                self.state = 61
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 59
                    self.stmt()
                    pass
                elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                    self.state = 60
                    self.attr_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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

        def attr_decl_exp(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_expContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

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
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.attr_decl_exp()
            self.state = 70
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl_exp_value(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_exp_valueContext,0)


        def attr_decl_exp_no_value(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_exp_no_valueContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_exp" ):
                return visitor.visitAttr_decl_exp(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_exp(self):

        localctx = CSlangParser.Attr_decl_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_decl_exp)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.attr_decl_exp_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.attr_decl_exp_no_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_exp_no_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_exp_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_exp_no_value" ):
                return visitor.visitAttr_decl_exp_no_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_exp_no_value(self):

        localctx = CSlangParser.Attr_decl_exp_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_decl_exp_no_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CSlangParser.ID)
            self.state = 77
            self.match(CSlangParser.COLON)
            self.state = 78
            self.match(CSlangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_exp_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def attr_decl_exp_value(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_exp_valueContext,0)


        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def DECL_OP(self):
            return self.getToken(CSlangParser.DECL_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_exp_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_exp_value" ):
                return visitor.visitAttr_decl_exp_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_exp_value(self):

        localctx = CSlangParser.Attr_decl_exp_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_decl_exp_value)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(CSlangParser.ID)
                self.state = 81
                self.match(CSlangParser.COMMA)
                self.state = 82
                self.attr_decl_exp_value()
                self.state = 83
                self.match(CSlangParser.COMMA)
                self.state = 84
                self.match(CSlangParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(CSlangParser.ID)
                self.state = 87
                self.match(CSlangParser.COLON)
                self.state = 88
                self.match(CSlangParser.INT)
                self.state = 89
                self.match(CSlangParser.DECL_OP)
                self.state = 90
                self.match(CSlangParser.INT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.assign_stmt()
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

        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

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
        self.enterRule(localctx, 22, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(CSlangParser.ID)
            self.state = 96
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 97
            self.exp()
            self.state = 98
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





