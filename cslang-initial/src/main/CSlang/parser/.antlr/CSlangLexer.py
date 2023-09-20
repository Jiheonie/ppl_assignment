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
        buf.write("\u01a5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,")
        buf.write("\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\5\64\u013d\n\64\3\64\3")
        buf.write("\64\5\64\u0141\n\64\3\65\3\65\7\65\u0145\n\65\f\65\16")
        buf.write("\65\u0148\13\65\3\66\3\66\5\66\u014c\n\66\3\66\3\66\3")
        buf.write("\67\6\67\u0151\n\67\r\67\16\67\u0152\3\67\3\67\38\38\3")
        buf.write("8\38\38\78\u015c\n8\f8\168\u015f\138\38\38\38\38\39\3")
        buf.write("9\39\39\39\39\39\39\39\59\u016e\n9\3:\3:\7:\u0172\n:\f")
        buf.write(":\16:\u0175\13:\3;\3;\6;\u0179\n;\r;\16;\u017a\3<\3<\3")
        buf.write("=\3=\3=\3=\7=\u0183\n=\f=\16=\u0186\13=\3=\3=\3>\3>\3")
        buf.write(">\3>\7>\u018e\n>\f>\16>\u0191\13>\3>\3>\3>\3>\3>\3?\6")
        buf.write("?\u0199\n?\r?\16?\u019a\3?\3?\3@\3@\3@\3A\3A\3B\3B\3\u018f")
        buf.write("\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\66o\67")
        buf.write("q8s9u:w\2y;{<}=\177>\u0081?\u0083@\3\2\n\3\2\62;\4\2G")
        buf.write("Ggg\4\2--//\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17")
        buf.write("\17\5\2\n\f\16\17\"\"\2\u01ae\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2o\3\2")
        buf.write("\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\3\u0085\3\2\2\2\5\u0088\3\2\2\2\7\u008e\3\2\2")
        buf.write("\2\t\u0097\3\2\2\2\13\u009a\3\2\2\2\r\u009f\3\2\2\2\17")
        buf.write("\u00a3\3\2\2\2\21\u00a7\3\2\2\2\23\u00ad\3\2\2\2\25\u00b2")
        buf.write("\3\2\2\2\27\u00b9\3\2\2\2\31\u00c0\3\2\2\2\33\u00c5\3")
        buf.write("\2\2\2\35\u00cb\3\2\2\2\37\u00d7\3\2\2\2!\u00db\3\2\2")
        buf.write("\2#\u00e0\3\2\2\2%\u00e4\3\2\2\2\'\u00e9\3\2\2\2)\u00ef")
        buf.write("\3\2\2\2+\u00f4\3\2\2\2-\u00f6\3\2\2\2/\u00f8\3\2\2\2")
        buf.write("\61\u00fa\3\2\2\2\63\u00fc\3\2\2\2\65\u00fe\3\2\2\2\67")
        buf.write("\u0100\3\2\2\29\u0103\3\2\2\2;\u0106\3\2\2\2=\u0109\3")
        buf.write("\2\2\2?\u010c\3\2\2\2A\u010e\3\2\2\2C\u0111\3\2\2\2E\u0113")
        buf.write("\3\2\2\2G\u0116\3\2\2\2I\u0118\3\2\2\2K\u011b\3\2\2\2")
        buf.write("M\u011d\3\2\2\2O\u011f\3\2\2\2Q\u0121\3\2\2\2S\u0123\3")
        buf.write("\2\2\2U\u0125\3\2\2\2W\u0127\3\2\2\2Y\u0129\3\2\2\2[\u012b")
        buf.write("\3\2\2\2]\u012d\3\2\2\2_\u012f\3\2\2\2a\u0131\3\2\2\2")
        buf.write("c\u0133\3\2\2\2e\u0135\3\2\2\2g\u0140\3\2\2\2i\u0142\3")
        buf.write("\2\2\2k\u0149\3\2\2\2m\u0150\3\2\2\2o\u0156\3\2\2\2q\u016d")
        buf.write("\3\2\2\2s\u016f\3\2\2\2u\u0176\3\2\2\2w\u017c\3\2\2\2")
        buf.write("y\u017e\3\2\2\2{\u0189\3\2\2\2}\u0198\3\2\2\2\177\u019e")
        buf.write("\3\2\2\2\u0081\u01a1\3\2\2\2\u0083\u01a3\3\2\2\2\u0085")
        buf.write("\u0086\7>\2\2\u0086\u0087\7/\2\2\u0087\4\3\2\2\2\u0088")
        buf.write("\u0089\7d\2\2\u0089\u008a\7t\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7c\2\2\u008c\u008d\7m\2\2\u008d\6\3\2\2\2\u008e")
        buf.write("\u008f\7e\2\2\u008f\u0090\7q\2\2\u0090\u0091\7p\2\2\u0091")
        buf.write("\u0092\7v\2\2\u0092\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094")
        buf.write("\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096\b\3\2\2\2\u0097")
        buf.write("\u0098\7k\2\2\u0098\u0099\7h\2\2\u0099\n\3\2\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d")
        buf.write("\u009e\7g\2\2\u009e\f\3\2\2\2\u009f\u00a0\7h\2\2\u00a0")
        buf.write("\u00a1\7q\2\2\u00a1\u00a2\7t\2\2\u00a2\16\3\2\2\2\u00a3")
        buf.write("\u00a4\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7v\2\2\u00a6")
        buf.write("\20\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7n\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7v\2\2\u00ac")
        buf.write("\22\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af\7q\2\2\u00af")
        buf.write("\u00b0\7q\2\2\u00b0\u00b1\7n\2\2\u00b1\24\3\2\2\2\u00b2")
        buf.write("\u00b3\7u\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7i\2\2\u00b8")
        buf.write("\26\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7t\2\2\u00be")
        buf.write("\u00bf\7p\2\2\u00bf\30\3\2\2\2\u00c0\u00c1\7p\2\2\u00c1")
        buf.write("\u00c2\7w\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7n\2\2\u00c4")
        buf.write("\32\3\2\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7n\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7u\2\2\u00ca")
        buf.write("\34\3\2\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd\7q\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0\7v\2\2\u00d0")
        buf.write("\u00d1\7t\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3\7e\2\2\u00d3")
        buf.write("\u00d4\7v\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\36\3\2\2\2\u00d7\u00d8\7x\2\2\u00d8\u00d9\7c\2\2\u00d9")
        buf.write("\u00da\7t\2\2\u00da \3\2\2\2\u00db\u00dc\7u\2\2\u00dc")
        buf.write("\u00dd\7g\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7h\2\2\u00df")
        buf.write("\"\3\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7g\2\2\u00e2")
        buf.write("\u00e3\7y\2\2\u00e3$\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5")
        buf.write("\u00e6\7q\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7f\2\2\u00e8")
        buf.write("&\3\2\2\2\u00e9\u00ea\7e\2\2\u00ea\u00eb\7q\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee\7v\2\2\u00ee")
        buf.write("(\3\2\2\2\u00ef\u00f0\7h\2\2\u00f0\u00f1\7w\2\2\u00f1")
        buf.write("\u00f2\7p\2\2\u00f2\u00f3\7e\2\2\u00f3*\3\2\2\2\u00f4")
        buf.write("\u00f5\7-\2\2\u00f5,\3\2\2\2\u00f6\u00f7\7/\2\2\u00f7")
        buf.write(".\3\2\2\2\u00f8\u00f9\7,\2\2\u00f9\60\3\2\2\2\u00fa\u00fb")
        buf.write("\7\61\2\2\u00fb\62\3\2\2\2\u00fc\u00fd\7^\2\2\u00fd\64")
        buf.write("\3\2\2\2\u00fe\u00ff\7#\2\2\u00ff\66\3\2\2\2\u0100\u0101")
        buf.write("\7(\2\2\u0101\u0102\7(\2\2\u01028\3\2\2\2\u0103\u0104")
        buf.write("\7~\2\2\u0104\u0105\7~\2\2\u0105:\3\2\2\2\u0106\u0107")
        buf.write("\7?\2\2\u0107\u0108\7?\2\2\u0108<\3\2\2\2\u0109\u010a")
        buf.write("\7<\2\2\u010a\u010b\7?\2\2\u010b>\3\2\2\2\u010c\u010d")
        buf.write("\7?\2\2\u010d@\3\2\2\2\u010e\u010f\7#\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110B\3\2\2\2\u0111\u0112\7>\2\2\u0112D\3\2\2")
        buf.write("\2\u0113\u0114\7>\2\2\u0114\u0115\7?\2\2\u0115F\3\2\2")
        buf.write("\2\u0116\u0117\7@\2\2\u0117H\3\2\2\2\u0118\u0119\7@\2")
        buf.write("\2\u0119\u011a\7?\2\2\u011aJ\3\2\2\2\u011b\u011c\7`\2")
        buf.write("\2\u011cL\3\2\2\2\u011d\u011e\7\'\2\2\u011eN\3\2\2\2\u011f")
        buf.write("\u0120\7*\2\2\u0120P\3\2\2\2\u0121\u0122\7+\2\2\u0122")
        buf.write("R\3\2\2\2\u0123\u0124\7]\2\2\u0124T\3\2\2\2\u0125\u0126")
        buf.write("\7_\2\2\u0126V\3\2\2\2\u0127\u0128\7\60\2\2\u0128X\3\2")
        buf.write("\2\2\u0129\u012a\7.\2\2\u012aZ\3\2\2\2\u012b\u012c\7<")
        buf.write("\2\2\u012c\\\3\2\2\2\u012d\u012e\7=\2\2\u012e^\3\2\2\2")
        buf.write("\u012f\u0130\7}\2\2\u0130`\3\2\2\2\u0131\u0132\7\177\2")
        buf.write("\2\u0132b\3\2\2\2\u0133\u0134\7)\2\2\u0134d\3\2\2\2\u0135")
        buf.write("\u0136\7$\2\2\u0136f\3\2\2\2\u0137\u0138\5m\67\2\u0138")
        buf.write("\u0139\5i\65\2\u0139\u0141\3\2\2\2\u013a\u013c\5m\67\2")
        buf.write("\u013b\u013d\5i\65\2\u013c\u013b\3\2\2\2\u013c\u013d\3")
        buf.write("\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\5k\66\2\u013f\u0141")
        buf.write("\3\2\2\2\u0140\u0137\3\2\2\2\u0140\u013a\3\2\2\2\u0141")
        buf.write("h\3\2\2\2\u0142\u0146\5W,\2\u0143\u0145\t\2\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147j\3\2\2\2\u0148\u0146\3\2\2")
        buf.write("\2\u0149\u014b\t\3\2\2\u014a\u014c\t\4\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014e\5m\67\2\u014el\3\2\2\2\u014f\u0151\t\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\b")
        buf.write("\67\2\2\u0155n\3\2\2\2\u0156\u015d\5e\63\2\u0157\u015c")
        buf.write("\n\5\2\2\u0158\u0159\5\63\32\2\u0159\u015a\5e\63\2\u015a")
        buf.write("\u015c\3\2\2\2\u015b\u0157\3\2\2\2\u015b\u0158\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161")
        buf.write("\5e\63\2\u0161\u0162\3\2\2\2\u0162\u0163\b8\3\2\u0163")
        buf.write("p\3\2\2\2\u0164\u0165\7v\2\2\u0165\u0166\7t\2\2\u0166")
        buf.write("\u0167\7w\2\2\u0167\u016e\7g\2\2\u0168\u0169\7h\2\2\u0169")
        buf.write("\u016a\7c\2\2\u016a\u016b\7n\2\2\u016b\u016c\7u\2\2\u016c")
        buf.write("\u016e\7g\2\2\u016d\u0164\3\2\2\2\u016d\u0168\3\2\2\2")
        buf.write("\u016er\3\2\2\2\u016f\u0173\t\6\2\2\u0170\u0172\5w<\2")
        buf.write("\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3")
        buf.write("\2\2\2\u0173\u0174\3\2\2\2\u0174t\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0176\u0178\7B\2\2\u0177\u0179\5w<\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017bv\3\2\2\2\u017c\u017d\t\7\2\2\u017d")
        buf.write("x\3\2\2\2\u017e\u017f\7\61\2\2\u017f\u0180\7\61\2\2\u0180")
        buf.write("\u0184\3\2\2\2\u0181\u0183\n\b\2\2\u0182\u0181\3\2\2\2")
        buf.write("\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188")
        buf.write("\b=\4\2\u0188z\3\2\2\2\u0189\u018a\7\61\2\2\u018a\u018b")
        buf.write("\7,\2\2\u018b\u018f\3\2\2\2\u018c\u018e\13\2\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0192\u0193\7,\2\2\u0193\u0194\7\61\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\b>\4\2\u0196|\3\2\2\2\u0197\u0199")
        buf.write("\t\t\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019c\u019d\b?\4\2\u019d~\3\2\2\2\u019e\u019f\13\2\2")
        buf.write("\2\u019f\u01a0\b@\5\2\u01a0\u0080\3\2\2\2\u01a1\u01a2")
        buf.write("\13\2\2\2\u01a2\u0082\3\2\2\2\u01a3\u01a4\13\2\2\2\u01a4")
        buf.write("\u0084\3\2\2\2\20\2\u013c\u0140\u0146\u014b\u0152\u015b")
        buf.write("\u015d\u016d\u0173\u017a\u0184\u018f\u019a\6\3\67\2\3")
        buf.write("8\3\b\2\2\3@\4")
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
    INT = 7
    FLOAT = 8
    BOOL = 9
    STRING = 10
    RETURN = 11
    NULL = 12
    CLASS = 13
    CONSTRUCTOR = 14
    VAR = 15
    SELF = 16
    NEW = 17
    VOID = 18
    CONST = 19
    FUNC = 20
    ADD_OP = 21
    SUB_OP = 22
    MUL_OP = 23
    SLASH = 24
    BACKSLASH = 25
    NOT_OP = 26
    AND_OP = 27
    OR_OP = 28
    EQUAL_OP = 29
    ASSIGN_OP = 30
    DECL_OP = 31
    DIFF_OP = 32
    LESS_OP = 33
    LESS_EQUAL_OP = 34
    GREATER_OP = 35
    GREATER_EQUAL_OP = 36
    CONCAT_OP = 37
    MOD_OP = 38
    LP = 39
    RP = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    COLON = 45
    SEMICOLON = 46
    LCB = 47
    RCB = 48
    SIN_Q = 49
    DOU_Q = 50
    FLOAT_LIT = 51
    INT_LIT = 52
    STR_LIT = 53
    BOOL_LIT = 54
    ID = 55
    AT_ID = 56
    CMT_LINE = 57
    CMT_BLOCK = 58
    WS = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'int'", "'float'", "'bool'", "'string'", "'return'", "'null'", 
            "'class'", "'constructor'", "'var'", "'self'", "'new'", "'void'", 
            "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'!'", 
            "'&&'", "'||'", "'=='", "':='", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", 
            "','", "':'", "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", 
            "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
            "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
            "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", 
            "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
            "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", 
            "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", 
            "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "INT_LIT", "STR_LIT", 
            "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", "CMT_BLOCK", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", 
                  "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "SLASH", "BACKSLASH", 
                  "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
                  "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
                  "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", 
                  "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "DECPART", "EXPPART", 
                  "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "SEQUENCE", 
                  "CMT_LINE", "CMT_BLOCK", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[53] = self.INT_LIT_action 
            actions[54] = self.STR_LIT_action 
            actions[62] = self.ERROR_CHAR_action 
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
     


