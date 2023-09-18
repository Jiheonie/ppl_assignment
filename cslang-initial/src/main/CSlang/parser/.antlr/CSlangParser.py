# Generated from d:\hoc_ki_231\ppl\ass1\assignment1\cslang-initial\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
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
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\37\n\3\3\4\3\4\3\5\3\5\5\5%\n\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6+\n\6\3\6\3\6\5\6/\n\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\2\2\t")
        buf.write("\2\4\6\b\n\f\16\2\4\4\2\37\37!!\3\2\4\5\2?\2\23\3\2\2")
        buf.write("\2\4\36\3\2\2\2\6 \3\2\2\2\b$\3\2\2\2\n&\3\2\2\2\f\62")
        buf.write("\3\2\2\2\16:\3\2\2\2\20\24\5\4\3\2\21\24\5\16\b\2\22\24")
        buf.write("\5\b\5\2\23\20\3\2\2\2\23\21\3\2\2\2\23\22\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2")
        buf.write("\27\30\7\2\2\3\30\3\3\2\2\2\31\32\5\6\4\2\32\33\t\2\2")
        buf.write("\2\33\34\5\6\4\2\34\37\3\2\2\2\35\37\5\6\4\2\36\31\3\2")
        buf.write("\2\2\36\35\3\2\2\2\37\5\3\2\2\2 !\t\3\2\2!\7\3\2\2\2\"")
        buf.write("%\5\n\6\2#%\5\f\7\2$\"\3\2\2\2$#\3\2\2\2%\t\3\2\2\2&\'")
        buf.write("\7\27\2\2\'*\7\b\2\2()\7\3\2\2)+\7\b\2\2*(\3\2\2\2*+\3")
        buf.write("\2\2\2+,\3\2\2\2,.\79\2\2-/\5\16\b\2.-\3\2\2\2./\3\2\2")
        buf.write("\2/\60\3\2\2\2\60\61\7:\2\2\61\13\3\2\2\2\62\63\7\31\2")
        buf.write("\2\63\64\7\b\2\2\64\65\7\67\2\2\65\66\7\21\2\2\66\67\7")
        buf.write(")\2\2\678\7\5\2\289\78\2\29\r\3\2\2\2:;\7\b\2\2;<\7(\2")
        buf.write("\2<=\5\4\3\2=>\78\2\2>\17\3\2\2\2\b\23\25\36$*.")
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
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", 
                     "'%'", "'('", "')'", "'['", "']'", "'.'", "','", "':'", 
                     "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "FLOAT_LIT", "INT_LIT", 
                      "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                      "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                      "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                      "CONST", "FUNC", "PLUS_OP", "MINUS_OP", "MUL_OP", 
                      "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", 
                      "EQUAL_OP", "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", 
                      "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                      "CONCAT_OP", "DIV_OP", "LP", "RP", "LSB", "RSB", "DOT", 
                      "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "SIN_Q", 
                      "DOU_Q", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_exp1 = 2
    RULE_decl = 3
    RULE_class_decl = 4
    RULE_attr_decl = 5
    RULE_assign_stmt = 6

    ruleNames =  [ "program", "exp", "exp1", "decl", "class_decl", "attr_decl", 
                   "assign_stmt" ]

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
    DECL_OP=39
    DIFF_OP=40
    LESS_OP=41
    LESS_EQUAL_OP=42
    GREATER_OP=43
    GREATER_EQUAL_OP=44
    CONCAT_OP=45
    DIV_OP=46
    LP=47
    RP=48
    LSB=49
    RSB=50
    DOT=51
    COMMA=52
    COLON=53
    SEMICOLON=54
    LCB=55
    RCB=56
    SIN_Q=57
    DOU_Q=58
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




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT]:
                    self.state = 14
                    self.exp()
                    pass
                elif token in [CSlangParser.ID]:
                    self.state = 15
                    self.assign_stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR]:
                    self.state = 16
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR))) != 0)):
                    break

            self.state = 21
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




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.exp1()
                self.state = 24
                _la = self._input.LA(1)
                if not(_la==CSlangParser.PLUS_OP or _la==CSlangParser.MUL_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 25
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
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




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
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

        def assign_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_decl




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(CSlangParser.CLASS)
            self.state = 37
            self.match(CSlangParser.ID)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__0:
                self.state = 38
                self.match(CSlangParser.T__0)
                self.state = 39
                self.match(CSlangParser.ID)


            self.state = 42
            self.match(CSlangParser.LCB)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 43
                self.assign_stmt()


            self.state = 46
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

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def DECL_OP(self):
            return self.getToken(CSlangParser.DECL_OP, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl




    def attr_decl(self):

        localctx = CSlangParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(CSlangParser.VAR)
            self.state = 49
            self.match(CSlangParser.ID)
            self.state = 50
            self.match(CSlangParser.COLON)
            self.state = 51
            self.match(CSlangParser.INT)
            self.state = 52
            self.match(CSlangParser.DECL_OP)
            self.state = 53
            self.match(CSlangParser.INT_LIT)
            self.state = 54
            self.match(CSlangParser.SEMICOLON)
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




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(CSlangParser.ID)
            self.state = 57
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 58
            self.exp()
            self.state = 59
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





