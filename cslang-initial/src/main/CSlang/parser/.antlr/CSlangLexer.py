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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u014f\n\65\3\65\3\65\5\65\u0153\n\65\3\66\3\66\7\66\u0157")
        buf.write("\n\66\f\66\16\66\u015a\13\66\3\67\3\67\5\67\u015e\n\67")
        buf.write("\3\67\3\67\38\68\u0163\n8\r8\168\u0164\38\38\39\39\39")
        buf.write("\79\u016c\n9\f9\169\u016f\139\39\39\39\3:\5:\u0175\n:")
        buf.write("\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u0187")
        buf.write("\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u0192\n<\3=\3=\7=\u0196")
        buf.write("\n=\f=\16=\u0199\13=\3>\3>\6>\u019d\n>\r>\16>\u019e\3")
        buf.write("?\3?\3@\3@\3@\3@\7@\u01a7\n@\f@\16@\u01aa\13@\3@\3@\3")
        buf.write("A\3A\3A\3A\7A\u01b2\nA\fA\16A\u01b5\13A\3A\3A\3A\3A\3")
        buf.write("A\3B\6B\u01bd\nB\rB\16B\u01be\3B\3B\3C\3C\3C\3C\7C\u01c7")
        buf.write("\nC\fC\16C\u01ca\13C\3C\3C\3C\3D\3D\3D\7D\u01d2\nD\fD")
        buf.write("\16D\u01d5\13D\3D\3D\5D\u01d9\nD\3D\3D\3E\3E\3E\4\u01b3")
        buf.write("\u01d3\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\2m\2o\67q8s\2u\2w9y:{;}\2\177<\u0081=\u0083>\u0085?\u0087")
        buf.write("@\u0089A\3\2\13\3\2\62;\4\2GGgg\4\2--//\4\2$$^^\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17\"\"\3")
        buf.write("\2$$\2\u01f2\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u008d\3\2\2\2\7\u0090")
        buf.write("\3\2\2\2\t\u0098\3\2\2\2\13\u009e\3\2\2\2\r\u00a4\3\2")
        buf.write("\2\2\17\u00ad\3\2\2\2\21\u00b0\3\2\2\2\23\u00b5\3\2\2")
        buf.write("\2\25\u00b9\3\2\2\2\27\u00bd\3\2\2\2\31\u00c3\3\2\2\2")
        buf.write("\33\u00c8\3\2\2\2\35\u00cf\3\2\2\2\37\u00d6\3\2\2\2!\u00db")
        buf.write("\3\2\2\2#\u00e1\3\2\2\2%\u00ed\3\2\2\2\'\u00f1\3\2\2\2")
        buf.write(")\u00f6\3\2\2\2+\u00fa\3\2\2\2-\u00ff\3\2\2\2/\u0105\3")
        buf.write("\2\2\2\61\u010a\3\2\2\2\63\u010c\3\2\2\2\65\u010e\3\2")
        buf.write("\2\2\67\u0110\3\2\2\29\u0112\3\2\2\2;\u0114\3\2\2\2=\u0117")
        buf.write("\3\2\2\2?\u011a\3\2\2\2A\u011d\3\2\2\2C\u0120\3\2\2\2")
        buf.write("E\u0122\3\2\2\2G\u0125\3\2\2\2I\u0127\3\2\2\2K\u012a\3")
        buf.write("\2\2\2M\u012c\3\2\2\2O\u012f\3\2\2\2Q\u0131\3\2\2\2S\u0133")
        buf.write("\3\2\2\2U\u0135\3\2\2\2W\u0137\3\2\2\2Y\u0139\3\2\2\2")
        buf.write("[\u013b\3\2\2\2]\u013d\3\2\2\2_\u013f\3\2\2\2a\u0141\3")
        buf.write("\2\2\2c\u0143\3\2\2\2e\u0145\3\2\2\2g\u0147\3\2\2\2i\u0152")
        buf.write("\3\2\2\2k\u0154\3\2\2\2m\u015b\3\2\2\2o\u0162\3\2\2\2")
        buf.write("q\u0168\3\2\2\2s\u0174\3\2\2\2u\u0186\3\2\2\2w\u0191\3")
        buf.write("\2\2\2y\u0193\3\2\2\2{\u019a\3\2\2\2}\u01a0\3\2\2\2\177")
        buf.write("\u01a2\3\2\2\2\u0081\u01ad\3\2\2\2\u0083\u01bc\3\2\2\2")
        buf.write("\u0085\u01c2\3\2\2\2\u0087\u01ce\3\2\2\2\u0089\u01dc\3")
        buf.write("\2\2\2\u008b\u008c\7^\2\2\u008c\4\3\2\2\2\u008d\u008e")
        buf.write("\7>\2\2\u008e\u008f\7/\2\2\u008f\6\3\2\2\2\u0090\u0091")
        buf.write("\7R\2\2\u0091\u0092\7t\2\2\u0092\u0093\7q\2\2\u0093\u0094")
        buf.write("\7i\2\2\u0094\u0095\7t\2\2\u0095\u0096\7c\2\2\u0096\u0097")
        buf.write("\7o\2\2\u0097\b\3\2\2\2\u0098\u0099\7B\2\2\u0099\u009a")
        buf.write("\7o\2\2\u009a\u009b\7c\2\2\u009b\u009c\7k\2\2\u009c\u009d")
        buf.write("\7p\2\2\u009d\n\3\2\2\2\u009e\u009f\7d\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7m\2\2\u00a3\f\3\2\2\2\u00a4\u00a5\7e\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\16\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7g\2\2\u00b4\22")
        buf.write("\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\24\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\26\3\2\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\30\3\2\2\2\u00c3\u00c4")
        buf.write("\7d\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7n\2\2\u00c7\32\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\34\3\2\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7w\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7p\2\2\u00d5\36")
        buf.write("\3\2\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9")
        buf.write("\7n\2\2\u00d9\u00da\7n\2\2\u00da \3\2\2\2\u00db\u00dc")
        buf.write("\7e\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7c\2\2\u00de\u00df")
        buf.write("\7u\2\2\u00df\u00e0\7u\2\2\u00e0\"\3\2\2\2\u00e1\u00e2")
        buf.write("\7e\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7w\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7t\2\2\u00ec$\3\2\2\2\u00ed\u00ee")
        buf.write("\7x\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7t\2\2\u00f0&\3")
        buf.write("\2\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4")
        buf.write("\7n\2\2\u00f4\u00f5\7h\2\2\u00f5(\3\2\2\2\u00f6\u00f7")
        buf.write("\7p\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7y\2\2\u00f9*\3")
        buf.write("\2\2\2\u00fa\u00fb\7x\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7f\2\2\u00fe,\3\2\2\2\u00ff\u0100")
        buf.write("\7e\2\2\u0100\u0101\7q\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7u\2\2\u0103\u0104\7v\2\2\u0104.\3\2\2\2\u0105\u0106")
        buf.write("\7h\2\2\u0106\u0107\7w\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7e\2\2\u0109\60\3\2\2\2\u010a\u010b\7-\2\2\u010b\62\3")
        buf.write("\2\2\2\u010c\u010d\7/\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7,\2\2\u010f\66\3\2\2\2\u0110\u0111\7\61\2\2\u01118\3")
        buf.write("\2\2\2\u0112\u0113\7#\2\2\u0113:\3\2\2\2\u0114\u0115\7")
        buf.write("(\2\2\u0115\u0116\7(\2\2\u0116<\3\2\2\2\u0117\u0118\7")
        buf.write("~\2\2\u0118\u0119\7~\2\2\u0119>\3\2\2\2\u011a\u011b\7")
        buf.write("?\2\2\u011b\u011c\7?\2\2\u011c@\3\2\2\2\u011d\u011e\7")
        buf.write("<\2\2\u011e\u011f\7?\2\2\u011fB\3\2\2\2\u0120\u0121\7")
        buf.write("?\2\2\u0121D\3\2\2\2\u0122\u0123\7#\2\2\u0123\u0124\7")
        buf.write("?\2\2\u0124F\3\2\2\2\u0125\u0126\7>\2\2\u0126H\3\2\2\2")
        buf.write("\u0127\u0128\7>\2\2\u0128\u0129\7?\2\2\u0129J\3\2\2\2")
        buf.write("\u012a\u012b\7@\2\2\u012bL\3\2\2\2\u012c\u012d\7@\2\2")
        buf.write("\u012d\u012e\7?\2\2\u012eN\3\2\2\2\u012f\u0130\7`\2\2")
        buf.write("\u0130P\3\2\2\2\u0131\u0132\7\'\2\2\u0132R\3\2\2\2\u0133")
        buf.write("\u0134\7*\2\2\u0134T\3\2\2\2\u0135\u0136\7+\2\2\u0136")
        buf.write("V\3\2\2\2\u0137\u0138\7]\2\2\u0138X\3\2\2\2\u0139\u013a")
        buf.write("\7_\2\2\u013aZ\3\2\2\2\u013b\u013c\7\60\2\2\u013c\\\3")
        buf.write("\2\2\2\u013d\u013e\7.\2\2\u013e^\3\2\2\2\u013f\u0140\7")
        buf.write("<\2\2\u0140`\3\2\2\2\u0141\u0142\7=\2\2\u0142b\3\2\2\2")
        buf.write("\u0143\u0144\7}\2\2\u0144d\3\2\2\2\u0145\u0146\7\177\2")
        buf.write("\2\u0146f\3\2\2\2\u0147\u0148\7$\2\2\u0148h\3\2\2\2\u0149")
        buf.write("\u014a\5o8\2\u014a\u014b\5k\66\2\u014b\u0153\3\2\2\2\u014c")
        buf.write("\u014e\5o8\2\u014d\u014f\5k\66\2\u014e\u014d\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\5m\67\2")
        buf.write("\u0151\u0153\3\2\2\2\u0152\u0149\3\2\2\2\u0152\u014c\3")
        buf.write("\2\2\2\u0153j\3\2\2\2\u0154\u0158\5[.\2\u0155\u0157\t")
        buf.write("\2\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159l\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015d\t\3\2\2\u015c\u015e\t\4\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0160\5o8\2\u0160n\3\2\2\2\u0161\u0163\t\2\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167")
        buf.write("\b8\2\2\u0167p\3\2\2\2\u0168\u016d\5g\64\2\u0169\u016c")
        buf.write("\n\5\2\2\u016a\u016c\5u;\2\u016b\u0169\3\2\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u0170\u0171\5g\64\2\u0171\u0172\b9\3\2\u0172r\3\2\2\2")
        buf.write("\u0173\u0175\7\17\2\2\u0174\u0173\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\7\f\2\2\u0177")
        buf.write("t\3\2\2\2\u0178\u0179\7^\2\2\u0179\u0187\7d\2\2\u017a")
        buf.write("\u017b\7^\2\2\u017b\u0187\7h\2\2\u017c\u017d\7^\2\2\u017d")
        buf.write("\u0187\7t\2\2\u017e\u017f\7^\2\2\u017f\u0187\7p\2\2\u0180")
        buf.write("\u0181\7^\2\2\u0181\u0187\7v\2\2\u0182\u0183\7^\2\2\u0183")
        buf.write("\u0187\7^\2\2\u0184\u0185\7^\2\2\u0185\u0187\7$\2\2\u0186")
        buf.write("\u0178\3\2\2\2\u0186\u017a\3\2\2\2\u0186\u017c\3\2\2\2")
        buf.write("\u0186\u017e\3\2\2\2\u0186\u0180\3\2\2\2\u0186\u0182\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0187v\3\2\2\2\u0188\u0189")
        buf.write("\7v\2\2\u0189\u018a\7t\2\2\u018a\u018b\7w\2\2\u018b\u0192")
        buf.write("\7g\2\2\u018c\u018d\7h\2\2\u018d\u018e\7c\2\2\u018e\u018f")
        buf.write("\7n\2\2\u018f\u0190\7u\2\2\u0190\u0192\7g\2\2\u0191\u0188")
        buf.write("\3\2\2\2\u0191\u018c\3\2\2\2\u0192x\3\2\2\2\u0193\u0197")
        buf.write("\t\6\2\2\u0194\u0196\5}?\2\u0195\u0194\3\2\2\2\u0196\u0199")
        buf.write("\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("z\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019c\7B\2\2\u019b")
        buf.write("\u019d\5}?\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f|\3\2\2\2\u01a0")
        buf.write("\u01a1\t\7\2\2\u01a1~\3\2\2\2\u01a2\u01a3\7\61\2\2\u01a3")
        buf.write("\u01a4\7\61\2\2\u01a4\u01a8\3\2\2\2\u01a5\u01a7\n\b\2")
        buf.write("\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01ab\u01ac\b@\4\2\u01ac\u0080\3\2\2\2")
        buf.write("\u01ad\u01ae\7\61\2\2\u01ae\u01af\7,\2\2\u01af\u01b3\3")
        buf.write("\2\2\2\u01b0\u01b2\13\2\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b5\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\7")
        buf.write(",\2\2\u01b7\u01b8\7\61\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba")
        buf.write("\bA\4\2\u01ba\u0082\3\2\2\2\u01bb\u01bd\t\t\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\b")
        buf.write("B\4\2\u01c1\u0084\3\2\2\2\u01c2\u01c8\5g\64\2\u01c3\u01c7")
        buf.write("\n\n\2\2\u01c4\u01c5\7^\2\2\u01c5\u01c7\7$\2\2\u01c6\u01c3")
        buf.write("\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5g\64\2\u01cc\u01cd\b")
        buf.write("C\5\2\u01cd\u0086\3\2\2\2\u01ce\u01d3\5g\64\2\u01cf\u01d2")
        buf.write("\n\n\2\2\u01d0\u01d2\5u;\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d9\5s:\2\u01d7\u01d9\7\2\2\3\u01d8\u01d6\3\2")
        buf.write("\2\2\u01d8\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db")
        buf.write("\bD\6\2\u01db\u0088\3\2\2\2\u01dc\u01dd\13\2\2\2\u01dd")
        buf.write("\u01de\bE\7\2\u01de\u008a\3\2\2\2\27\2\u014e\u0152\u0158")
        buf.write("\u015d\u0164\u016b\u016d\u0174\u0186\u0191\u0197\u019e")
        buf.write("\u01a8\u01b3\u01be\u01c6\u01c8\u01d1\u01d3\u01d8\b\38")
        buf.write("\2\39\3\b\2\2\3C\4\3D\5\3E\6")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    PROGRAM_CLASS = 3
    MAIN = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELSE = 8
    FOR = 9
    INT = 10
    FLOAT = 11
    BOOL = 12
    STRING = 13
    RETURN = 14
    NULL = 15
    CLASS = 16
    CONSTRUCTOR = 17
    VAR = 18
    SELF = 19
    NEW = 20
    VOID = 21
    CONST = 22
    FUNC = 23
    ADD_OP = 24
    SUB_OP = 25
    MUL_OP = 26
    DIV_OP = 27
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
    MOD_OP = 40
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
    DOU_Q = 51
    FLOAT_LIT = 52
    INT_LIT = 53
    STR_LIT = 54
    BOOL_LIT = 55
    ID = 56
    AT_ID = 57
    CMT_LINE = 58
    CMT_BLOCK = 59
    WS = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'<-'", "'Program'", "'@main'", "'break'", "'continue'", 
            "'if'", "'else'", "'for'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'!'", "'&&'", "'||'", "'=='", "':='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'^'", "'%'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "':'", "';'", "'{'", "'}'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM_CLASS", "MAIN", "BREAK", "CONTINUE", "IF", "ELSE", 
            "FOR", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
            "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", 
            "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "AND_OP", 
            "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", 
            "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", 
            "MOD_OP", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", 
            "SEMICOLON", "LCB", "RCB", "DOU_Q", "FLOAT_LIT", "INT_LIT", 
            "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", "CMT_BLOCK", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "PROGRAM_CLASS", "MAIN", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", "STRING", 
                  "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                  "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "DIV_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
                  "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
                  "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", 
                  "RCB", "DOU_Q", "FLOAT_LIT", "DECPART", "EXPPART", "INT_LIT", 
                  "STR_LIT", "NEWLINE", "ESCAPE", "BOOL_LIT", "ID", "AT_ID", 
                  "SEQUENCE", "CMT_LINE", "CMT_BLOCK", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[54] = self.INT_LIT_action 
            actions[55] = self.STR_LIT_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	for i in self.text:
            		if i != '0' or self.text == '0':
            			break
            		self.text = self.text[1:] 

     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	esc_list = ['b', 'f', 'r', 'n', 't', '"', '\\']
            	for idx in range(1, len(self.text) - 2):
            		if self.text[idx] == '\\' and self.text[idx+1] not in esc_list:
            			raise IllegalEscape(self.text[1:idx + 2]) 
            			break

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	string_error = self.text[1:]
            	if (string_error[-1] == "\n"):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


