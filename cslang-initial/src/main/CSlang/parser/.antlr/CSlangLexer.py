# Generated from d:\hoc_ki_231\ppl\ass1\assignment1\cslang-initial\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0191\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\3\3\3\5\3\u0090\n")
        buf.write("\3\3\4\3\4\7\4\u0094\n\4\f\4\16\4\u0097\13\4\3\5\3\5\5")
        buf.write("\5\u009b\n\5\3\5\3\5\3\6\6\6\u00a0\n\6\r\6\16\6\u00a1")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7\u00ab\n\7\f\7\16\7\u00ae")
        buf.write("\13\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00b6\n\b\3\t\3\t\7")
        buf.write("\t\u00ba\n\t\f\t\16\t\u00bd\13\t\3\n\3\n\3\n\3\n\7\n\u00c3")
        buf.write("\n\n\f\n\16\n\u00c6\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\6>\u0185")
        buf.write("\n>\r>\16>\u0186\3>\3>\3?\3?\3?\3@\3@\3A\3A\2\2B\3\3\5")
        buf.write("\4\7\2\t\2\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33")
        buf.write("\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30")
        buf.write("\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q")
        buf.write("(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s9u:")
        buf.write("w;y<{=}>\177?\u0081@\3\2\n\3\2\62;\4\2GGgg\4\2--//\3\2")
        buf.write("$$\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16")
        buf.write("\17\"\"\2\u0199\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2")
        buf.write("\2\2\5\u008f\3\2\2\2\7\u0091\3\2\2\2\t\u0098\3\2\2\2\13")
        buf.write("\u009f\3\2\2\2\r\u00a5\3\2\2\2\17\u00b5\3\2\2\2\21\u00b7")
        buf.write("\3\2\2\2\23\u00be\3\2\2\2\25\u00c9\3\2\2\2\27\u00cf\3")
        buf.write("\2\2\2\31\u00d8\3\2\2\2\33\u00db\3\2\2\2\35\u00e0\3\2")
        buf.write("\2\2\37\u00e4\3\2\2\2!\u00e9\3\2\2\2#\u00ef\3\2\2\2%\u00f3")
        buf.write("\3\2\2\2\'\u00f9\3\2\2\2)\u00fe\3\2\2\2+\u0105\3\2\2\2")
        buf.write("-\u010c\3\2\2\2/\u0111\3\2\2\2\61\u0117\3\2\2\2\63\u0123")
        buf.write("\3\2\2\2\65\u0127\3\2\2\2\67\u012c\3\2\2\29\u0130\3\2")
        buf.write("\2\2;\u0135\3\2\2\2=\u013b\3\2\2\2?\u0140\3\2\2\2A\u0142")
        buf.write("\3\2\2\2C\u0144\3\2\2\2E\u0146\3\2\2\2G\u0148\3\2\2\2")
        buf.write("I\u014a\3\2\2\2K\u014c\3\2\2\2M\u014f\3\2\2\2O\u0152\3")
        buf.write("\2\2\2Q\u0155\3\2\2\2S\u0158\3\2\2\2U\u015a\3\2\2\2W\u015d")
        buf.write("\3\2\2\2Y\u015f\3\2\2\2[\u0162\3\2\2\2]\u0164\3\2\2\2")
        buf.write("_\u0167\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2e\u016d\3")
        buf.write("\2\2\2g\u016f\3\2\2\2i\u0171\3\2\2\2k\u0173\3\2\2\2m\u0175")
        buf.write("\3\2\2\2o\u0177\3\2\2\2q\u0179\3\2\2\2s\u017b\3\2\2\2")
        buf.write("u\u017d\3\2\2\2w\u017f\3\2\2\2y\u0181\3\2\2\2{\u0184\3")
        buf.write("\2\2\2}\u018a\3\2\2\2\177\u018d\3\2\2\2\u0081\u018f\3")
        buf.write("\2\2\2\u0083\u0084\7>\2\2\u0084\u0085\7/\2\2\u0085\4\3")
        buf.write("\2\2\2\u0086\u0087\5\13\6\2\u0087\u0088\5\7\4\2\u0088")
        buf.write("\u0090\3\2\2\2\u0089\u008b\5\13\6\2\u008a\u008c\5\7\4")
        buf.write("\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d")
        buf.write("\3\2\2\2\u008d\u008e\5\t\5\2\u008e\u0090\3\2\2\2\u008f")
        buf.write("\u0086\3\2\2\2\u008f\u0089\3\2\2\2\u0090\6\3\2\2\2\u0091")
        buf.write("\u0095\5k\66\2\u0092\u0094\t\2\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\b\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a")
        buf.write("\t\3\2\2\u0099\u009b\t\4\2\2\u009a\u0099\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\5\13\6")
        buf.write("\2\u009d\n\3\2\2\2\u009e\u00a0\t\2\2\2\u009f\u009e\3\2")
        buf.write("\2\2\u00a0\u00a1\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b\6\2\2\u00a4")
        buf.write("\f\3\2\2\2\u00a5\u00ac\5y=\2\u00a6\u00ab\n\5\2\2\u00a7")
        buf.write("\u00a8\5G$\2\u00a8\u00a9\5y=\2\u00a9\u00ab\3\2\2\2\u00aa")
        buf.write("\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3")
        buf.write("\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\5y=\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b2\b\7\3\2\u00b2\16\3\2\2\2\u00b3\u00b6")
        buf.write("\5\37\20\2\u00b4\u00b6\5!\21\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6\20\3\2\2\2\u00b7\u00bb\t\6\2\2\u00b8")
        buf.write("\u00ba\t\7\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\22\3\2")
        buf.write("\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\7\61\2\2\u00bf\u00c0")
        buf.write("\7\61\2\2\u00c0\u00c4\3\2\2\2\u00c1\u00c3\n\b\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3")
        buf.write("\2\2\2\u00c7\u00c8\b\n\4\2\u00c8\24\3\2\2\2\u00c9\u00ca")
        buf.write("\7d\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7m\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\7e\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7w\2\2\u00d6\u00d7\7g\2\2\u00d7\30\3\2\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7h\2\2\u00da\32\3\2\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7u\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\34\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7t\2\2\u00e3\36\3\2\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8 \3\2\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb")
        buf.write("\7c\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\"\3\2\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2$\3\2\2\2\u00f3\u00f4")
        buf.write("\7h\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7v\2\2\u00f8&\3\2\2\2\u00f9\u00fa")
        buf.write("\7d\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7n\2\2\u00fd(\3\2\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7i\2\2\u0104*\3\2\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7g\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7w\2\2\u0109\u010a\7t\2\2\u010a\u010b\7p\2\2\u010b,\3")
        buf.write("\2\2\2\u010c\u010d\7p\2\2\u010d\u010e\7w\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7n\2\2\u0110.\3\2\2\2\u0111\u0112")
        buf.write("\7e\2\2\u0112\u0113\7n\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115\u0116\7u\2\2\u0116\60\3\2\2\2\u0117\u0118")
        buf.write("\7e\2\2\u0118\u0119\7q\2\2\u0119\u011a\7p\2\2\u011a\u011b")
        buf.write("\7u\2\2\u011b\u011c\7v\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7w\2\2\u011e\u011f\7e\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\u0122\7t\2\2\u0122\62\3\2\2\2\u0123\u0124")
        buf.write("\7x\2\2\u0124\u0125\7c\2\2\u0125\u0126\7t\2\2\u0126\64")
        buf.write("\3\2\2\2\u0127\u0128\7u\2\2\u0128\u0129\7g\2\2\u0129\u012a")
        buf.write("\7n\2\2\u012a\u012b\7h\2\2\u012b\66\3\2\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\u012e\7g\2\2\u012e\u012f\7y\2\2\u012f8\3")
        buf.write("\2\2\2\u0130\u0131\7x\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7f\2\2\u0134:\3\2\2\2\u0135\u0136")
        buf.write("\7e\2\2\u0136\u0137\7q\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7u\2\2\u0139\u013a\7v\2\2\u013a<\3\2\2\2\u013b\u013c")
        buf.write("\7h\2\2\u013c\u013d\7w\2\2\u013d\u013e\7p\2\2\u013e\u013f")
        buf.write("\7e\2\2\u013f>\3\2\2\2\u0140\u0141\7-\2\2\u0141@\3\2\2")
        buf.write("\2\u0142\u0143\7/\2\2\u0143B\3\2\2\2\u0144\u0145\7,\2")
        buf.write("\2\u0145D\3\2\2\2\u0146\u0147\7\61\2\2\u0147F\3\2\2\2")
        buf.write("\u0148\u0149\7^\2\2\u0149H\3\2\2\2\u014a\u014b\7#\2\2")
        buf.write("\u014bJ\3\2\2\2\u014c\u014d\7(\2\2\u014d\u014e\7(\2\2")
        buf.write("\u014eL\3\2\2\2\u014f\u0150\7~\2\2\u0150\u0151\7~\2\2")
        buf.write("\u0151N\3\2\2\2\u0152\u0153\7?\2\2\u0153\u0154\7?\2\2")
        buf.write("\u0154P\3\2\2\2\u0155\u0156\7<\2\2\u0156\u0157\7?\2\2")
        buf.write("\u0157R\3\2\2\2\u0158\u0159\7?\2\2\u0159T\3\2\2\2\u015a")
        buf.write("\u015b\7#\2\2\u015b\u015c\7?\2\2\u015cV\3\2\2\2\u015d")
        buf.write("\u015e\7>\2\2\u015eX\3\2\2\2\u015f\u0160\7>\2\2\u0160")
        buf.write("\u0161\7?\2\2\u0161Z\3\2\2\2\u0162\u0163\7@\2\2\u0163")
        buf.write("\\\3\2\2\2\u0164\u0165\7@\2\2\u0165\u0166\7?\2\2\u0166")
        buf.write("^\3\2\2\2\u0167\u0168\7`\2\2\u0168`\3\2\2\2\u0169\u016a")
        buf.write("\7\'\2\2\u016ab\3\2\2\2\u016b\u016c\7*\2\2\u016cd\3\2")
        buf.write("\2\2\u016d\u016e\7+\2\2\u016ef\3\2\2\2\u016f\u0170\7]")
        buf.write("\2\2\u0170h\3\2\2\2\u0171\u0172\7_\2\2\u0172j\3\2\2\2")
        buf.write("\u0173\u0174\7\60\2\2\u0174l\3\2\2\2\u0175\u0176\7.\2")
        buf.write("\2\u0176n\3\2\2\2\u0177\u0178\7<\2\2\u0178p\3\2\2\2\u0179")
        buf.write("\u017a\7=\2\2\u017ar\3\2\2\2\u017b\u017c\7}\2\2\u017c")
        buf.write("t\3\2\2\2\u017d\u017e\7\177\2\2\u017ev\3\2\2\2\u017f\u0180")
        buf.write("\7)\2\2\u0180x\3\2\2\2\u0181\u0182\7$\2\2\u0182z\3\2\2")
        buf.write("\2\u0183\u0185\t\t\2\2\u0184\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\b>\4\2\u0189|\3\2\2\2\u018a")
        buf.write("\u018b\13\2\2\2\u018b\u018c\b?\5\2\u018c~\3\2\2\2\u018d")
        buf.write("\u018e\13\2\2\2\u018e\u0080\3\2\2\2\u018f\u0190\13\2\2")
        buf.write("\2\u0190\u0082\3\2\2\2\16\2\u008b\u008f\u0095\u009a\u00a1")
        buf.write("\u00aa\u00ac\u00b5\u00bb\u00c4\u0186\6\3\6\2\3\7\3\b\2")
        buf.write("\2\3?\4")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    FLOAT_LIT = 2
    INT_LIT = 3
    STR_LIT = 4
    BOOL_LIT = 5
    ID = 6
    CMT_LINE = 7
    BREAK = 8
    CONTINUE = 9
    IF = 10
    ELSE = 11
    FOR = 12
    TRUE = 13
    FALSE = 14
    INT = 15
    FLOAT = 16
    BOOL = 17
    STRING = 18
    RETURN = 19
    NULL = 20
    CLASS = 21
    CONSTRUCTOR = 22
    VAR = 23
    SELF = 24
    NEW = 25
    VOID = 26
    CONST = 27
    FUNC = 28
    PLUS_OP = 29
    MINUS_OP = 30
    MUL_OP = 31
    SLASH = 32
    BACKSLASH = 33
    NOT_OP = 34
    AND_OP = 35
    OR_OP = 36
    EQUAL_OP = 37
    ASSIGN_OP = 38
    DECL_OP = 39
    DIFF_OP = 40
    LESS_OP = 41
    LESS_EQUAL_OP = 42
    GREATER_OP = 43
    GREATER_EQUAL_OP = 44
    CONCAT_OP = 45
    DIV_OP = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    DOT = 51
    COMMA = 52
    COLON = 53
    SEMICOLON = 54
    LCB = 55
    RCB = 56
    SIN_Q = 57
    DOU_Q = 58
    WS = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "':='", "'='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", "'%'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "':'", "';'", "'{'", "'}'", "'''", 
            "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT_LIT", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", 
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS_OP", "MINUS_OP", 
            "MUL_OP", "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", 
            "EQUAL_OP", "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
            "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "DIV_OP", "LP", 
            "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", 
            "RCB", "SIN_Q", "DOU_Q", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "FLOAT_LIT", "DECPART", "EXPPART", "INT_LIT", 
                  "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                  "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                  "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS_OP", 
                  "MINUS_OP", "MUL_OP", "SLASH", "BACKSLASH", "NOT_OP", 
                  "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", 
                  "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                  "CONCAT_OP", "DIV_OP", "LP", "RP", "LSB", "RSB", "DOT", 
                  "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "SIN_Q", 
                  "DOU_Q", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.INT_LIT_action 
            actions[5] = self.STR_LIT_action 
            actions[61] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
            	while self.text[0] == '0':
            		self.text = self.text[1:]

     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


