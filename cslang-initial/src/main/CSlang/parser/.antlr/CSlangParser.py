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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u00d3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\6\2\66\n\2\r\2\16\2\67\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3E\n\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\7\6N\n\6\f\6\16\6Q\13\6\3\7\3\7\3\7\5\7")
        buf.write("V\n\7\3\b\3\b\3\b\3\b\5\b\\\n\b\3\b\3\b\3\b\7\ba\n\b\f")
        buf.write("\b\16\bd\13\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tl\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\5\fx\n\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u0089\n\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\5\21\u0094\n\21\3\22\3\22\3\22\7\22\u0099")
        buf.write("\n\22\f\22\16\22\u009c\13\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ac")
        buf.write("\n\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\7\27\u00bc\n\27\f\27\16\27\u00bf")
        buf.write("\13\27\3\27\5\27\u00c2\n\27\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\7\31\u00cb\n\31\f\31\16\31\u00ce\13\31\3\31\3")
        buf.write("\31\3\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\2\4\3\2\679\4\2\23\23\27\27\2\u00d0")
        buf.write("\2\65\3\2\2\2\4D\3\2\2\2\6F\3\2\2\2\bH\3\2\2\2\nJ\3\2")
        buf.write("\2\2\fU\3\2\2\2\16W\3\2\2\2\20k\3\2\2\2\22m\3\2\2\2\24")
        buf.write("q\3\2\2\2\26u\3\2\2\2\30~\3\2\2\2\32\u0082\3\2\2\2\34")
        buf.write("\u0086\3\2\2\2\36\u008d\3\2\2\2 \u0093\3\2\2\2\"\u0095")
        buf.write("\3\2\2\2$\u00ab\3\2\2\2&\u00ad\3\2\2\2(\u00af\3\2\2\2")
        buf.write("*\u00b4\3\2\2\2,\u00c1\3\2\2\2.\u00c3\3\2\2\2\60\u00c7")
        buf.write("\3\2\2\2\62\66\5\4\3\2\63\66\5(\25\2\64\66\5\f\7\2\65")
        buf.write("\62\3\2\2\2\65\63\3\2\2\2\65\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\67\65\3\2\2\2\678\3\2\2\289\3\2\2\29:\7\2\2\3:\3\3\2")
        buf.write("\2\2;<\5\6\4\2<=\7\33\2\2=>\5\6\4\2>E\3\2\2\2?@\5\6\4")
        buf.write("\2@A\7\31\2\2AB\5\6\4\2BE\3\2\2\2CE\5\6\4\2D;\3\2\2\2")
        buf.write("D?\3\2\2\2DC\3\2\2\2E\5\3\2\2\2FG\5\b\5\2G\7\3\2\2\2H")
        buf.write("I\t\2\2\2I\t\3\2\2\2JO\5\4\3\2KL\7\60\2\2LN\5\4\3\2MK")
        buf.write("\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\13\3\2\2\2QO\3")
        buf.write("\2\2\2RV\5\16\b\2SV\5\36\20\2TV\5\20\t\2UR\3\2\2\2US\3")
        buf.write("\2\2\2UT\3\2\2\2V\r\3\2\2\2WX\7\21\2\2X[\7;\2\2YZ\7\3")
        buf.write("\2\2Z\\\7;\2\2[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]b\7\63")
        buf.write("\2\2^a\5&\24\2_a\5\f\7\2`^\3\2\2\2`_\3\2\2\2ad\3\2\2\2")
        buf.write("b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef\7\64\2\2f\17")
        buf.write("\3\2\2\2gl\5\22\n\2hl\5\30\r\2il\5\24\13\2jl\5\32\16\2")
        buf.write("kg\3\2\2\2kh\3\2\2\2ki\3\2\2\2kj\3\2\2\2l\21\3\2\2\2m")
        buf.write("n\7\30\2\2no\7;\2\2op\5\26\f\2p\23\3\2\2\2qr\7\30\2\2")
        buf.write("rs\7<\2\2st\5\26\f\2t\25\3\2\2\2uw\7+\2\2vx\5,\27\2wv")
        buf.write("\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7,\2\2z{\7\61\2\2{|\7\13")
        buf.write("\2\2|}\5*\26\2}\27\3\2\2\2~\177\7\30\2\2\177\u0080\7;")
        buf.write("\2\2\u0080\u0081\5\34\17\2\u0081\31\3\2\2\2\u0082\u0083")
        buf.write("\7\30\2\2\u0083\u0084\7<\2\2\u0084\u0085\5\34\17\2\u0085")
        buf.write("\33\3\2\2\2\u0086\u0088\7+\2\2\u0087\u0089\5,\27\2\u0088")
        buf.write("\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008b\7,\2\2\u008b\u008c\5*\26\2\u008c\35\3\2\2")
        buf.write("\2\u008d\u008e\t\3\2\2\u008e\u008f\5 \21\2\u008f\u0090")
        buf.write("\7\62\2\2\u0090\37\3\2\2\2\u0091\u0094\5$\23\2\u0092\u0094")
        buf.write("\5\"\22\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("!\3\2\2\2\u0095\u009a\7;\2\2\u0096\u0097\7\60\2\2\u0097")
        buf.write("\u0099\7;\2\2\u0098\u0096\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\7\61\2\2\u009e")
        buf.write("\u009f\7\13\2\2\u009f#\3\2\2\2\u00a0\u00a1\7;\2\2\u00a1")
        buf.write("\u00a2\7\60\2\2\u00a2\u00a3\5$\23\2\u00a3\u00a4\7\60\2")
        buf.write("\2\u00a4\u00a5\78\2\2\u00a5\u00ac\3\2\2\2\u00a6\u00a7")
        buf.write("\7;\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9\7\13\2\2\u00a9")
        buf.write("\u00aa\7#\2\2\u00aa\u00ac\78\2\2\u00ab\u00a0\3\2\2\2\u00ab")
        buf.write("\u00a6\3\2\2\2\u00ac%\3\2\2\2\u00ad\u00ae\5(\25\2\u00ae")
        buf.write("\'\3\2\2\2\u00af\u00b0\7;\2\2\u00b0\u00b1\7\"\2\2\u00b1")
        buf.write("\u00b2\5\4\3\2\u00b2\u00b3\7\62\2\2\u00b3)\3\2\2\2\u00b4")
        buf.write("\u00b5\7\63\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\7\64\2")
        buf.write("\2\u00b7+\3\2\2\2\u00b8\u00bd\5.\30\2\u00b9\u00ba\7\60")
        buf.write("\2\2\u00ba\u00bc\5.\30\2\u00bb\u00b9\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c2\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c2\5\60\31")
        buf.write("\2\u00c1\u00b8\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2-\3\2")
        buf.write("\2\2\u00c3\u00c4\7;\2\2\u00c4\u00c5\7\61\2\2\u00c5\u00c6")
        buf.write("\7\13\2\2\u00c6/\3\2\2\2\u00c7\u00cc\7;\2\2\u00c8\u00c9")
        buf.write("\7\60\2\2\u00c9\u00cb\7;\2\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7")
        buf.write("\61\2\2\u00d0\u00d1\7\13\2\2\u00d1\61\3\2\2\2\23\65\67")
        buf.write("DOU[`bkw\u0088\u0093\u009a\u00ab\u00bd\u00c1\u00cc")
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
                      "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_exp1 = 2
    RULE_literal = 3
    RULE_exp_list = 4
    RULE_decl = 5
    RULE_class_decl = 6
    RULE_method_decl = 7
    RULE_func_decl = 8
    RULE_static_func_decl = 9
    RULE_expo_func = 10
    RULE_constructor_decl = 11
    RULE_static_constructor_decl = 12
    RULE_expo_constructor = 13
    RULE_attr_decl = 14
    RULE_attr_decl_exp = 15
    RULE_attr_decl_exp_short = 16
    RULE_attr_decl_exp_full = 17
    RULE_stmt = 18
    RULE_assign_stmt = 19
    RULE_block_stmt = 20
    RULE_params_list = 21
    RULE_param = 22
    RULE_params_same_type = 23

    ruleNames =  [ "program", "exp", "exp1", "literal", "exp_list", "decl", 
                   "class_decl", "method_decl", "func_decl", "static_func_decl", 
                   "expo_func", "constructor_decl", "static_constructor_decl", 
                   "expo_constructor", "attr_decl", "attr_decl_exp", "attr_decl_exp_short", 
                   "attr_decl_exp_full", "stmt", "assign_stmt", "block_stmt", 
                   "params_list", "param", "params_same_type" ]

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
    AT_ID=58
    CMT_LINE=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

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
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT]:
                    self.state = 48
                    self.exp()
                    pass
                elif token in [CSlangParser.ID]:
                    self.state = 49
                    self.assign_stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                    self.state = 50
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.ID))) != 0)):
                    break

            self.state = 55
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
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.exp1()
                self.state = 58
                self.match(CSlangParser.MUL_OP)
                self.state = 59
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.exp1()
                self.state = 62
                self.match(CSlangParser.PLUS_OP)
                self.state = 63
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
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




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
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




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
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


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp_list




    def exp_list(self):

        localctx = CSlangParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.exp()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 73
                self.match(CSlangParser.COMMA)
                self.state = 74
                self.exp()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def method_decl(self):
            return self.getTypedRuleContext(CSlangParser.Method_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decl




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.method_decl()
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


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.DeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.DeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_decl




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(CSlangParser.CLASS)
            self.state = 86
            self.match(CSlangParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__0:
                self.state = 87
                self.match(CSlangParser.T__0)
                self.state = 88
                self.match(CSlangParser.ID)


            self.state = 91
            self.match(CSlangParser.LCB)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.ID))) != 0):
                self.state = 94
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 92
                    self.stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                    self.state = 93
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(CSlangParser.Func_declContext,0)


        def constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_declContext,0)


        def static_func_decl(self):
            return self.getTypedRuleContext(CSlangParser.Static_func_declContext,0)


        def static_constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Static_constructor_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_decl




    def method_decl(self):

        localctx = CSlangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_decl)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.static_func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.static_constructor_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expo_func(self):
            return self.getTypedRuleContext(CSlangParser.Expo_funcContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_func_decl




    def func_decl(self):

        localctx = CSlangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CSlangParser.FUNC)
            self.state = 108
            self.match(CSlangParser.ID)
            self.state = 109
            self.expo_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def expo_func(self):
            return self.getTypedRuleContext(CSlangParser.Expo_funcContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_func_decl




    def static_func_decl(self):

        localctx = CSlangParser.Static_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_static_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(CSlangParser.FUNC)
            self.state = 112
            self.match(CSlangParser.AT_ID)
            self.state = 113
            self.expo_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expo_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(CSlangParser.Params_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expo_func




    def expo_func(self):

        localctx = CSlangParser.Expo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expo_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(CSlangParser.LP)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 116
                self.params_list()


            self.state = 119
            self.match(CSlangParser.RP)
            self.state = 120
            self.match(CSlangParser.COLON)
            self.state = 121
            self.match(CSlangParser.INT)
            self.state = 122
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expo_constructor(self):
            return self.getTypedRuleContext(CSlangParser.Expo_constructorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(CSlangParser.FUNC)
            self.state = 125
            self.match(CSlangParser.ID)
            self.state = 126
            self.expo_constructor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def expo_constructor(self):
            return self.getTypedRuleContext(CSlangParser.Expo_constructorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_constructor_decl




    def static_constructor_decl(self):

        localctx = CSlangParser.Static_constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_static_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CSlangParser.FUNC)
            self.state = 129
            self.match(CSlangParser.AT_ID)
            self.state = 130
            self.expo_constructor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expo_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(CSlangParser.Params_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expo_constructor




    def expo_constructor(self):

        localctx = CSlangParser.Expo_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expo_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CSlangParser.LP)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 133
                self.params_list()


            self.state = 136
            self.match(CSlangParser.RP)
            self.state = 137
            self.block_stmt()
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




    def attr_decl(self):

        localctx = CSlangParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 140
            self.attr_decl_exp()
            self.state = 141
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

        def attr_decl_exp_full(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_exp_fullContext,0)


        def attr_decl_exp_short(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_exp_shortContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_exp




    def attr_decl_exp(self):

        localctx = CSlangParser.Attr_decl_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attr_decl_exp)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.attr_decl_exp_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.attr_decl_exp_short()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_exp_shortContext(ParserRuleContext):
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_exp_short




    def attr_decl_exp_short(self):

        localctx = CSlangParser.Attr_decl_exp_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attr_decl_exp_short)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(CSlangParser.ID)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 148
                self.match(CSlangParser.COMMA)
                self.state = 149
                self.match(CSlangParser.ID)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(CSlangParser.COLON)
            self.state = 156
            self.match(CSlangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_exp_fullContext(ParserRuleContext):
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

        def attr_decl_exp_full(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_exp_fullContext,0)


        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def DECL_OP(self):
            return self.getToken(CSlangParser.DECL_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_exp_full




    def attr_decl_exp_full(self):

        localctx = CSlangParser.Attr_decl_exp_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_attr_decl_exp_full)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(CSlangParser.ID)
                self.state = 159
                self.match(CSlangParser.COMMA)
                self.state = 160
                self.attr_decl_exp_full()
                self.state = 161
                self.match(CSlangParser.COMMA)
                self.state = 162
                self.match(CSlangParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(CSlangParser.ID)
                self.state = 165
                self.match(CSlangParser.COLON)
                self.state = 166
                self.match(CSlangParser.INT)
                self.state = 167
                self.match(CSlangParser.DECL_OP)
                self.state = 168
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




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
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




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(CSlangParser.ID)
            self.state = 174
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 175
            self.exp()
            self.state = 176
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_block_stmt




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(CSlangParser.LCB)


            self.state = 180
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParamContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def params_same_type(self):
            return self.getTypedRuleContext(CSlangParser.Params_same_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params_list




    def params_list(self):

        localctx = CSlangParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.param()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 183
                    self.match(CSlangParser.COMMA)
                    self.state = 184
                    self.param()
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.params_same_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
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
            return CSlangParser.RULE_param




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(CSlangParser.ID)
            self.state = 194
            self.match(CSlangParser.COLON)
            self.state = 195
            self.match(CSlangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_same_typeContext(ParserRuleContext):
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_params_same_type




    def params_same_type(self):

        localctx = CSlangParser.Params_same_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_params_same_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(CSlangParser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 198
                self.match(CSlangParser.COMMA)
                self.state = 199
                self.match(CSlangParser.ID)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(CSlangParser.COLON)
            self.state = 206
            self.match(CSlangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





