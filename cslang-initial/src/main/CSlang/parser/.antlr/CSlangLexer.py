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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u018d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u008a\n\3\3\3\3\3\5\3\u008e\n\3\3\4")
        buf.write("\3\4\7\4\u0092\n\4\f\4\16\4\u0095\13\4\3\5\3\5\5\5\u0099")
        buf.write("\n\5\3\5\3\5\3\6\6\6\u009e\n\6\r\6\16\6\u009f\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\7\7\u00a9\n\7\f\7\16\7\u00ac\13\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00b4\n\b\3\t\3\t\7\t\u00b8")
        buf.write("\n\t\f\t\16\t\u00bb\13\t\3\n\3\n\3\n\3\n\7\n\u00c1\n\n")
        buf.write("\f\n\16\n\u00c4\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\6=\u0181\n=\r=\16=\u0182")
        buf.write("\3=\3=\3>\3>\3>\3?\3?\3@\3@\2\2A\3\3\5\4\7\2\t\2\13\5")
        buf.write("\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!")
        buf.write("\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67")
        buf.write("\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/")
        buf.write("a\60c\61e\62g\63i\64k\65m\66o\67q8s9u:w;y<{=}>\177?\3")
        buf.write("\2\n\3\2\62;\4\2GGgg\4\2--//\3\2$$\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17\"\"\2\u0195\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\3\u0081\3\2\2\2\5\u008d\3\2\2\2\7\u008f\3\2\2\2\t")
        buf.write("\u0096\3\2\2\2\13\u009d\3\2\2\2\r\u00a3\3\2\2\2\17\u00b3")
        buf.write("\3\2\2\2\21\u00b5\3\2\2\2\23\u00bc\3\2\2\2\25\u00c7\3")
        buf.write("\2\2\2\27\u00cd\3\2\2\2\31\u00d6\3\2\2\2\33\u00d9\3\2")
        buf.write("\2\2\35\u00de\3\2\2\2\37\u00e2\3\2\2\2!\u00e7\3\2\2\2")
        buf.write("#\u00ed\3\2\2\2%\u00f1\3\2\2\2\'\u00f7\3\2\2\2)\u00fc")
        buf.write("\3\2\2\2+\u0103\3\2\2\2-\u010a\3\2\2\2/\u010f\3\2\2\2")
        buf.write("\61\u0115\3\2\2\2\63\u0121\3\2\2\2\65\u0125\3\2\2\2\67")
        buf.write("\u012a\3\2\2\29\u012e\3\2\2\2;\u0133\3\2\2\2=\u0139\3")
        buf.write("\2\2\2?\u013e\3\2\2\2A\u0140\3\2\2\2C\u0142\3\2\2\2E\u0144")
        buf.write("\3\2\2\2G\u0146\3\2\2\2I\u0148\3\2\2\2K\u014a\3\2\2\2")
        buf.write("M\u014d\3\2\2\2O\u0150\3\2\2\2Q\u0153\3\2\2\2S\u0156\3")
        buf.write("\2\2\2U\u0159\3\2\2\2W\u015b\3\2\2\2Y\u015e\3\2\2\2[\u0160")
        buf.write("\3\2\2\2]\u0163\3\2\2\2_\u0165\3\2\2\2a\u0167\3\2\2\2")
        buf.write("c\u0169\3\2\2\2e\u016b\3\2\2\2g\u016d\3\2\2\2i\u016f\3")
        buf.write("\2\2\2k\u0171\3\2\2\2m\u0173\3\2\2\2o\u0175\3\2\2\2q\u0177")
        buf.write("\3\2\2\2s\u0179\3\2\2\2u\u017b\3\2\2\2w\u017d\3\2\2\2")
        buf.write("y\u0180\3\2\2\2{\u0186\3\2\2\2}\u0189\3\2\2\2\177\u018b")
        buf.write("\3\2\2\2\u0081\u0082\7>\2\2\u0082\u0083\7/\2\2\u0083\4")
        buf.write("\3\2\2\2\u0084\u0085\5\13\6\2\u0085\u0086\5\7\4\2\u0086")
        buf.write("\u008e\3\2\2\2\u0087\u0089\5\13\6\2\u0088\u008a\5\7\4")
        buf.write("\2\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u008c\5\t\5\2\u008c\u008e\3\2\2\2\u008d")
        buf.write("\u0084\3\2\2\2\u008d\u0087\3\2\2\2\u008e\6\3\2\2\2\u008f")
        buf.write("\u0093\5i\65\2\u0090\u0092\t\2\2\2\u0091\u0090\3\2\2\2")
        buf.write("\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3")
        buf.write("\2\2\2\u0094\b\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0098")
        buf.write("\t\3\2\2\u0097\u0099\t\4\2\2\u0098\u0097\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5\13\6")
        buf.write("\2\u009b\n\3\2\2\2\u009c\u009e\t\2\2\2\u009d\u009c\3\2")
        buf.write("\2\2\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b\6\2\2\u00a2")
        buf.write("\f\3\2\2\2\u00a3\u00aa\5w<\2\u00a4\u00a9\n\5\2\2\u00a5")
        buf.write("\u00a6\5G$\2\u00a6\u00a7\5w<\2\u00a7\u00a9\3\2\2\2\u00a8")
        buf.write("\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3")
        buf.write("\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\5w<\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\b\7\3\2\u00b0\16\3\2\2\2\u00b1\u00b4")
        buf.write("\5\37\20\2\u00b2\u00b4\5!\21\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\20\3\2\2\2\u00b5\u00b9\t\6\2\2\u00b6")
        buf.write("\u00b8\t\7\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\22\3\2")
        buf.write("\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\7\61\2\2\u00bd\u00be")
        buf.write("\7\61\2\2\u00be\u00c2\3\2\2\2\u00bf\u00c1\n\b\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c5\u00c6\b\n\4\2\u00c6\24\3\2\2\2\u00c7\u00c8")
        buf.write("\7d\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb")
        buf.write("\7c\2\2\u00cb\u00cc\7m\2\2\u00cc\26\3\2\2\2\u00cd\u00ce")
        buf.write("\7e\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7w\2\2\u00d4\u00d5\7g\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7h\2\2\u00d8\32\3\2\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\34\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7t\2\2\u00e1\36\3\2\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\"\3\2\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7v\2\2\u00f0$\3\2\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7v\2\2\u00f6&\3\2\2\2\u00f7\u00f8")
        buf.write("\7d\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7n\2\2\u00fb(\3\2\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\u0102\7i\2\2\u0102*\3\2\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7g\2\2\u0105\u0106\7v\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7t\2\2\u0108\u0109\7p\2\2\u0109,\3")
        buf.write("\2\2\2\u010a\u010b\7p\2\2\u010b\u010c\7w\2\2\u010c\u010d")
        buf.write("\7n\2\2\u010d\u010e\7n\2\2\u010e.\3\2\2\2\u010f\u0110")
        buf.write("\7e\2\2\u0110\u0111\7n\2\2\u0111\u0112\7c\2\2\u0112\u0113")
        buf.write("\7u\2\2\u0113\u0114\7u\2\2\u0114\60\3\2\2\2\u0115\u0116")
        buf.write("\7e\2\2\u0116\u0117\7q\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7u\2\2\u0119\u011a\7v\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7e\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7t\2\2\u0120\62\3\2\2\2\u0121\u0122")
        buf.write("\7x\2\2\u0122\u0123\7c\2\2\u0123\u0124\7t\2\2\u0124\64")
        buf.write("\3\2\2\2\u0125\u0126\7u\2\2\u0126\u0127\7g\2\2\u0127\u0128")
        buf.write("\7n\2\2\u0128\u0129\7h\2\2\u0129\66\3\2\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7g\2\2\u012c\u012d\7y\2\2\u012d8\3")
        buf.write("\2\2\2\u012e\u012f\7x\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0132\7f\2\2\u0132:\3\2\2\2\u0133\u0134")
        buf.write("\7e\2\2\u0134\u0135\7q\2\2\u0135\u0136\7p\2\2\u0136\u0137")
        buf.write("\7u\2\2\u0137\u0138\7v\2\2\u0138<\3\2\2\2\u0139\u013a")
        buf.write("\7h\2\2\u013a\u013b\7w\2\2\u013b\u013c\7p\2\2\u013c\u013d")
        buf.write("\7e\2\2\u013d>\3\2\2\2\u013e\u013f\7-\2\2\u013f@\3\2\2")
        buf.write("\2\u0140\u0141\7/\2\2\u0141B\3\2\2\2\u0142\u0143\7,\2")
        buf.write("\2\u0143D\3\2\2\2\u0144\u0145\7\61\2\2\u0145F\3\2\2\2")
        buf.write("\u0146\u0147\7^\2\2\u0147H\3\2\2\2\u0148\u0149\7#\2\2")
        buf.write("\u0149J\3\2\2\2\u014a\u014b\7(\2\2\u014b\u014c\7(\2\2")
        buf.write("\u014cL\3\2\2\2\u014d\u014e\7~\2\2\u014e\u014f\7~\2\2")
        buf.write("\u014fN\3\2\2\2\u0150\u0151\7?\2\2\u0151\u0152\7?\2\2")
        buf.write("\u0152P\3\2\2\2\u0153\u0154\7<\2\2\u0154\u0155\7?\2\2")
        buf.write("\u0155R\3\2\2\2\u0156\u0157\7#\2\2\u0157\u0158\7?\2\2")
        buf.write("\u0158T\3\2\2\2\u0159\u015a\7>\2\2\u015aV\3\2\2\2\u015b")
        buf.write("\u015c\7>\2\2\u015c\u015d\7?\2\2\u015dX\3\2\2\2\u015e")
        buf.write("\u015f\7@\2\2\u015fZ\3\2\2\2\u0160\u0161\7@\2\2\u0161")
        buf.write("\u0162\7?\2\2\u0162\\\3\2\2\2\u0163\u0164\7`\2\2\u0164")
        buf.write("^\3\2\2\2\u0165\u0166\7\'\2\2\u0166`\3\2\2\2\u0167\u0168")
        buf.write("\7*\2\2\u0168b\3\2\2\2\u0169\u016a\7+\2\2\u016ad\3\2\2")
        buf.write("\2\u016b\u016c\7]\2\2\u016cf\3\2\2\2\u016d\u016e\7_\2")
        buf.write("\2\u016eh\3\2\2\2\u016f\u0170\7\60\2\2\u0170j\3\2\2\2")
        buf.write("\u0171\u0172\7.\2\2\u0172l\3\2\2\2\u0173\u0174\7<\2\2")
        buf.write("\u0174n\3\2\2\2\u0175\u0176\7=\2\2\u0176p\3\2\2\2\u0177")
        buf.write("\u0178\7}\2\2\u0178r\3\2\2\2\u0179\u017a\7\177\2\2\u017a")
        buf.write("t\3\2\2\2\u017b\u017c\7)\2\2\u017cv\3\2\2\2\u017d\u017e")
        buf.write("\7$\2\2\u017ex\3\2\2\2\u017f\u0181\t\t\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\b=\4\2")
        buf.write("\u0185z\3\2\2\2\u0186\u0187\13\2\2\2\u0187\u0188\b>\5")
        buf.write("\2\u0188|\3\2\2\2\u0189\u018a\13\2\2\2\u018a~\3\2\2\2")
        buf.write("\u018b\u018c\13\2\2\2\u018c\u0080\3\2\2\2\16\2\u0089\u008d")
        buf.write("\u0093\u0098\u009f\u00a8\u00aa\u00b3\u00b9\u00c2\u0182")
        buf.write("\6\3\6\2\3\7\3\b\2\2\3>\4")
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
    DIFF_OP = 39
    LESS_OP = 40
    LESS_EQUAL_OP = 41
    GREATER_OP = 42
    GREATER_EQUAL_OP = 43
    CONCAT_OP = 44
    DIV_OP = 45
    LP = 46
    RP = 47
    LSB = 48
    RSB = 49
    DOT = 50
    COMMA = 51
    COLON = 52
    SEMICOLON = 53
    LCB = 54
    RCB = 55
    SIN_Q = 56
    DOU_Q = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "':='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'^'", "'%'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "':'", "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT_LIT", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", 
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS_OP", "MINUS_OP", 
            "MUL_OP", "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", 
            "EQUAL_OP", "ASSIGN_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
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
                  "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DIFF_OP", 
                  "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
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
            actions[60] = self.ERROR_CHAR_action 
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
     


