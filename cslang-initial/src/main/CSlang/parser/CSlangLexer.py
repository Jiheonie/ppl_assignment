# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u0146\n\66\3\66\3\66\5\66\u014a\n")
        buf.write("\66\3\67\3\67\7\67\u014e\n\67\f\67\16\67\u0151\13\67\3")
        buf.write("8\38\58\u0155\n8\38\38\39\69\u015a\n9\r9\169\u015b\39")
        buf.write("\39\3:\3:\3:\3:\3:\7:\u0165\n:\f:\16:\u0168\13:\3:\3:")
        buf.write("\3:\3:\3;\3;\5;\u0170\n;\3<\3<\7<\u0174\n<\f<\16<\u0177")
        buf.write("\13<\3=\3=\3=\3=\7=\u017d\n=\f=\16=\u0180\13=\3=\3=\3")
        buf.write(">\6>\u0185\n>\r>\16>\u0186\3>\3>\3?\3?\3?\3@\3@\3A\3A")
        buf.write("\2\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2")
        buf.write("q8s9u:w;y<{=}>\177?\u0081@\3\2\n\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2")
        buf.write("\n\f\16\17\"\"\2\u0199\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3")
        buf.write("\u0083\3\2\2\2\5\u0086\3\2\2\2\7\u008c\3\2\2\2\t\u0095")
        buf.write("\3\2\2\2\13\u0098\3\2\2\2\r\u009d\3\2\2\2\17\u00a1\3\2")
        buf.write("\2\2\21\u00a6\3\2\2\2\23\u00ac\3\2\2\2\25\u00b0\3\2\2")
        buf.write("\2\27\u00b6\3\2\2\2\31\u00bb\3\2\2\2\33\u00c2\3\2\2\2")
        buf.write("\35\u00c9\3\2\2\2\37\u00ce\3\2\2\2!\u00d4\3\2\2\2#\u00e0")
        buf.write("\3\2\2\2%\u00e4\3\2\2\2\'\u00e9\3\2\2\2)\u00ed\3\2\2\2")
        buf.write("+\u00f2\3\2\2\2-\u00f8\3\2\2\2/\u00fd\3\2\2\2\61\u00ff")
        buf.write("\3\2\2\2\63\u0101\3\2\2\2\65\u0103\3\2\2\2\67\u0105\3")
        buf.write("\2\2\29\u0107\3\2\2\2;\u0109\3\2\2\2=\u010c\3\2\2\2?\u010f")
        buf.write("\3\2\2\2A\u0112\3\2\2\2C\u0115\3\2\2\2E\u0117\3\2\2\2")
        buf.write("G\u011a\3\2\2\2I\u011c\3\2\2\2K\u011f\3\2\2\2M\u0121\3")
        buf.write("\2\2\2O\u0124\3\2\2\2Q\u0126\3\2\2\2S\u0128\3\2\2\2U\u012a")
        buf.write("\3\2\2\2W\u012c\3\2\2\2Y\u012e\3\2\2\2[\u0130\3\2\2\2")
        buf.write("]\u0132\3\2\2\2_\u0134\3\2\2\2a\u0136\3\2\2\2c\u0138\3")
        buf.write("\2\2\2e\u013a\3\2\2\2g\u013c\3\2\2\2i\u013e\3\2\2\2k\u0149")
        buf.write("\3\2\2\2m\u014b\3\2\2\2o\u0152\3\2\2\2q\u0159\3\2\2\2")
        buf.write("s\u015f\3\2\2\2u\u016f\3\2\2\2w\u0171\3\2\2\2y\u0178\3")
        buf.write("\2\2\2{\u0184\3\2\2\2}\u018a\3\2\2\2\177\u018d\3\2\2\2")
        buf.write("\u0081\u018f\3\2\2\2\u0083\u0084\7>\2\2\u0084\u0085\7")
        buf.write("/\2\2\u0085\4\3\2\2\2\u0086\u0087\7d\2\2\u0087\u0088\7")
        buf.write("t\2\2\u0088\u0089\7g\2\2\u0089\u008a\7c\2\2\u008a\u008b")
        buf.write("\7m\2\2\u008b\6\3\2\2\2\u008c\u008d\7e\2\2\u008d\u008e")
        buf.write("\7q\2\2\u008e\u008f\7p\2\2\u008f\u0090\7v\2\2\u0090\u0091")
        buf.write("\7k\2\2\u0091\u0092\7p\2\2\u0092\u0093\7w\2\2\u0093\u0094")
        buf.write("\7g\2\2\u0094\b\3\2\2\2\u0095\u0096\7k\2\2\u0096\u0097")
        buf.write("\7h\2\2\u0097\n\3\2\2\2\u0098\u0099\7g\2\2\u0099\u009a")
        buf.write("\7n\2\2\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c\f")
        buf.write("\3\2\2\2\u009d\u009e\7h\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\16\3\2\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7g\2\2\u00a5\20")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9")
        buf.write("\7n\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab\22")
        buf.write("\3\2\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\24\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\26\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7n\2\2\u00ba\30")
        buf.write("\3\2\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\32\3\2\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7p\2\2\u00c8\34\3\2\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\36\3\2\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0")
        buf.write("\7n\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3 \3\2\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7w\2\2\u00db\u00dc")
        buf.write("\7e\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\"\3\2\2\2\u00e0\u00e1\7x\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7t\2\2\u00e3$\3\2\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7h\2\2\u00e8&\3\2\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7y\2\2\u00ec(\3\2\2\2\u00ed\u00ee")
        buf.write("\7x\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7f\2\2\u00f1*\3\2\2\2\u00f2\u00f3\7e\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7,\3\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7e\2\2\u00fc.\3")
        buf.write("\2\2\2\u00fd\u00fe\7-\2\2\u00fe\60\3\2\2\2\u00ff\u0100")
        buf.write("\7/\2\2\u0100\62\3\2\2\2\u0101\u0102\7,\2\2\u0102\64\3")
        buf.write("\2\2\2\u0103\u0104\7\61\2\2\u0104\66\3\2\2\2\u0105\u0106")
        buf.write("\7^\2\2\u01068\3\2\2\2\u0107\u0108\7#\2\2\u0108:\3\2\2")
        buf.write("\2\u0109\u010a\7(\2\2\u010a\u010b\7(\2\2\u010b<\3\2\2")
        buf.write("\2\u010c\u010d\7~\2\2\u010d\u010e\7~\2\2\u010e>\3\2\2")
        buf.write("\2\u010f\u0110\7?\2\2\u0110\u0111\7?\2\2\u0111@\3\2\2")
        buf.write("\2\u0112\u0113\7<\2\2\u0113\u0114\7?\2\2\u0114B\3\2\2")
        buf.write("\2\u0115\u0116\7?\2\2\u0116D\3\2\2\2\u0117\u0118\7#\2")
        buf.write("\2\u0118\u0119\7?\2\2\u0119F\3\2\2\2\u011a\u011b\7>\2")
        buf.write("\2\u011bH\3\2\2\2\u011c\u011d\7>\2\2\u011d\u011e\7?\2")
        buf.write("\2\u011eJ\3\2\2\2\u011f\u0120\7@\2\2\u0120L\3\2\2\2\u0121")
        buf.write("\u0122\7@\2\2\u0122\u0123\7?\2\2\u0123N\3\2\2\2\u0124")
        buf.write("\u0125\7`\2\2\u0125P\3\2\2\2\u0126\u0127\7\'\2\2\u0127")
        buf.write("R\3\2\2\2\u0128\u0129\7*\2\2\u0129T\3\2\2\2\u012a\u012b")
        buf.write("\7+\2\2\u012bV\3\2\2\2\u012c\u012d\7]\2\2\u012dX\3\2\2")
        buf.write("\2\u012e\u012f\7_\2\2\u012fZ\3\2\2\2\u0130\u0131\7\60")
        buf.write("\2\2\u0131\\\3\2\2\2\u0132\u0133\7.\2\2\u0133^\3\2\2\2")
        buf.write("\u0134\u0135\7<\2\2\u0135`\3\2\2\2\u0136\u0137\7=\2\2")
        buf.write("\u0137b\3\2\2\2\u0138\u0139\7}\2\2\u0139d\3\2\2\2\u013a")
        buf.write("\u013b\7\177\2\2\u013bf\3\2\2\2\u013c\u013d\7)\2\2\u013d")
        buf.write("h\3\2\2\2\u013e\u013f\7$\2\2\u013fj\3\2\2\2\u0140\u0141")
        buf.write("\5q9\2\u0141\u0142\5m\67\2\u0142\u014a\3\2\2\2\u0143\u0145")
        buf.write("\5q9\2\u0144\u0146\5m\67\2\u0145\u0144\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\5o8\2\u0148\u014a")
        buf.write("\3\2\2\2\u0149\u0140\3\2\2\2\u0149\u0143\3\2\2\2\u014a")
        buf.write("l\3\2\2\2\u014b\u014f\5[.\2\u014c\u014e\t\2\2\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150n\3\2\2\2\u0151\u014f\3\2\2")
        buf.write("\2\u0152\u0154\t\3\2\2\u0153\u0155\t\4\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0157\5q9\2\u0157p\3\2\2\2\u0158\u015a\t\2\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\b")
        buf.write("9\2\2\u015er\3\2\2\2\u015f\u0166\5i\65\2\u0160\u0165\n")
        buf.write("\5\2\2\u0161\u0162\5\67\34\2\u0162\u0163\5i\65\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0160\3\2\2\2\u0164\u0161\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3")
        buf.write("\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a")
        buf.write("\5i\65\2\u016a\u016b\3\2\2\2\u016b\u016c\b:\3\2\u016c")
        buf.write("t\3\2\2\2\u016d\u0170\5\17\b\2\u016e\u0170\5\21\t\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170v\3\2\2\2\u0171")
        buf.write("\u0175\t\6\2\2\u0172\u0174\t\7\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176x\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179")
        buf.write("\7\61\2\2\u0179\u017a\7\61\2\2\u017a\u017e\3\2\2\2\u017b")
        buf.write("\u017d\n\b\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\b=\4\2\u0182z\3")
        buf.write("\2\2\2\u0183\u0185\t\t\2\2\u0184\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\b>\4\2\u0189|\3\2\2\2\u018a")
        buf.write("\u018b\13\2\2\2\u018b\u018c\b?\5\2\u018c~\3\2\2\2\u018d")
        buf.write("\u018e\13\2\2\2\u018e\u0080\3\2\2\2\u018f\u0190\13\2\2")
        buf.write("\2\u0190\u0082\3\2\2\2\16\2\u0145\u0149\u014f\u0154\u015b")
        buf.write("\u0164\u0166\u016f\u0175\u017e\u0186\6\39\2\3:\3\b\2\2")
        buf.write("\3?\4")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSE = 5
    FOR = 6
    TRUE = 7
    FALSE = 8
    INT = 9
    FLOAT = 10
    BOOL = 11
    STRING = 12
    RETURN = 13
    NULL = 14
    CLASS = 15
    CONSTRUCTOR = 16
    VAR = 17
    SELF = 18
    NEW = 19
    VOID = 20
    CONST = 21
    FUNC = 22
    PLUS_OP = 23
    MINUS_OP = 24
    MUL_OP = 25
    SLASH = 26
    BACKSLASH = 27
    NOT_OP = 28
    AND_OP = 29
    OR_OP = 30
    EQUAL_OP = 31
    ASSIGN_OP = 32
    DECL_OP = 33
    DIFF_OP = 34
    LESS_OP = 35
    LESS_EQUAL_OP = 36
    GREATER_OP = 37
    GREATER_EQUAL_OP = 38
    CONCAT_OP = 39
    DIV_OP = 40
    LP = 41
    RP = 42
    LSB = 43
    RSB = 44
    DOT = 45
    COMMA = 46
    COLON = 47
    SEMICOLON = 48
    LCB = 49
    RCB = 50
    SIN_Q = 51
    DOU_Q = 52
    FLOAT_LIT = 53
    INT_LIT = 54
    STR_LIT = 55
    BOOL_LIT = 56
    ID = 57
    CMT_LINE = 58
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
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS_OP", "MINUS_OP", 
            "MUL_OP", "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", 
            "EQUAL_OP", "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
            "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "DIV_OP", "LP", 
            "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", 
            "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "INT_LIT", "STR_LIT", 
            "BOOL_LIT", "ID", "CMT_LINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "PLUS_OP", "MINUS_OP", "MUL_OP", "SLASH", 
                  "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", 
                  "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
                  "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "DIV_OP", 
                  "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", 
                  "LCB", "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "DECPART", 
                  "EXPPART", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "CMT_LINE", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[55] = self.INT_LIT_action 
            actions[56] = self.STR_LIT_action 
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
     


