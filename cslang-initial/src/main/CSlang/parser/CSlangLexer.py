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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01e1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\5\66\u0153\n\66\3\66\3\66\5\66\u0157\n\66\3")
        buf.write("\67\3\67\7\67\u015b\n\67\f\67\16\67\u015e\13\67\38\38")
        buf.write("\58\u0162\n8\38\38\39\69\u0167\n9\r9\169\u0168\3:\3:\3")
        buf.write(":\7:\u016e\n:\f:\16:\u0171\13:\3:\3:\3:\3;\5;\u0177\n")
        buf.write(";\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u0189")
        buf.write("\n<\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0194\n=\3>\3>\7>\u0198")
        buf.write("\n>\f>\16>\u019b\13>\3?\3?\6?\u019f\n?\r?\16?\u01a0\3")
        buf.write("@\3@\3A\3A\3A\3A\7A\u01a9\nA\fA\16A\u01ac\13A\3A\3A\3")
        buf.write("B\3B\3B\3B\7B\u01b4\nB\fB\16B\u01b7\13B\3B\3B\3B\3B\3")
        buf.write("B\3C\6C\u01bf\nC\rC\16C\u01c0\3C\3C\3D\3D\3D\3E\3E\3E")
        buf.write("\3E\7E\u01cc\nE\fE\16E\u01cf\13E\3E\3E\3E\3F\3F\3F\7F")
        buf.write("\u01d7\nF\fF\16F\u01da\13F\3F\3F\5F\u01de\nF\3F\3F\4\u01b5")
        buf.write("\u01d8\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m\2o\2q8s9u\2w\2y:{;}<\177\2\u0081=\u0083>\u0085?\u0087")
        buf.write("@\u0089A\u008bB\3\2\13\3\2\62;\4\2GGgg\4\2--//\4\2$$^")
        buf.write("^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17")
        buf.write("\"\"\3\2$$\2\u01f4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2q\3\2\2")
        buf.write("\2\2s\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u008f")
        buf.write("\3\2\2\2\7\u0092\3\2\2\2\t\u009a\3\2\2\2\13\u00a0\3\2")
        buf.write("\2\2\r\u00a6\3\2\2\2\17\u00af\3\2\2\2\21\u00b2\3\2\2\2")
        buf.write("\23\u00b7\3\2\2\2\25\u00bb\3\2\2\2\27\u00bf\3\2\2\2\31")
        buf.write("\u00c5\3\2\2\2\33\u00ca\3\2\2\2\35\u00d1\3\2\2\2\37\u00d8")
        buf.write("\3\2\2\2!\u00dd\3\2\2\2#\u00e3\3\2\2\2%\u00ef\3\2\2\2")
        buf.write("\'\u00f3\3\2\2\2)\u00f8\3\2\2\2+\u00fc\3\2\2\2-\u0101")
        buf.write("\3\2\2\2/\u0107\3\2\2\2\61\u010c\3\2\2\2\63\u010e\3\2")
        buf.write("\2\2\65\u0110\3\2\2\2\67\u0112\3\2\2\29\u0114\3\2\2\2")
        buf.write(";\u0116\3\2\2\2=\u0119\3\2\2\2?\u011c\3\2\2\2A\u011f\3")
        buf.write("\2\2\2C\u0122\3\2\2\2E\u0124\3\2\2\2G\u0127\3\2\2\2I\u0129")
        buf.write("\3\2\2\2K\u012c\3\2\2\2M\u012e\3\2\2\2O\u0131\3\2\2\2")
        buf.write("Q\u0133\3\2\2\2S\u0135\3\2\2\2U\u0137\3\2\2\2W\u0139\3")
        buf.write("\2\2\2Y\u013b\3\2\2\2[\u013d\3\2\2\2]\u013f\3\2\2\2_\u0141")
        buf.write("\3\2\2\2a\u0143\3\2\2\2c\u0145\3\2\2\2e\u0147\3\2\2\2")
        buf.write("g\u0149\3\2\2\2i\u014b\3\2\2\2k\u0156\3\2\2\2m\u0158\3")
        buf.write("\2\2\2o\u015f\3\2\2\2q\u0166\3\2\2\2s\u016a\3\2\2\2u\u0176")
        buf.write("\3\2\2\2w\u0188\3\2\2\2y\u0193\3\2\2\2{\u0195\3\2\2\2")
        buf.write("}\u019c\3\2\2\2\177\u01a2\3\2\2\2\u0081\u01a4\3\2\2\2")
        buf.write("\u0083\u01af\3\2\2\2\u0085\u01be\3\2\2\2\u0087\u01c4\3")
        buf.write("\2\2\2\u0089\u01c7\3\2\2\2\u008b\u01d3\3\2\2\2\u008d\u008e")
        buf.write("\7^\2\2\u008e\4\3\2\2\2\u008f\u0090\7>\2\2\u0090\u0091")
        buf.write("\7/\2\2\u0091\6\3\2\2\2\u0092\u0093\7R\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7q\2\2\u0095\u0096\7i\2\2\u0096\u0097")
        buf.write("\7t\2\2\u0097\u0098\7c\2\2\u0098\u0099\7o\2\2\u0099\b")
        buf.write("\3\2\2\2\u009a\u009b\7B\2\2\u009b\u009c\7o\2\2\u009c\u009d")
        buf.write("\7c\2\2\u009d\u009e\7k\2\2\u009e\u009f\7p\2\2\u009f\n")
        buf.write("\3\2\2\2\u00a0\u00a1\7d\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7m\2\2\u00a5\f")
        buf.write("\3\2\2\2\u00a6\u00a7\7e\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7g\2\2\u00ae\16")
        buf.write("\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7h\2\2\u00b1\20")
        buf.write("\3\2\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5")
        buf.write("\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\22\3\2\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7t\2\2\u00ba\24")
        buf.write("\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\26\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1")
        buf.write("\7n\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\30\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7n\2\2\u00c9\32")
        buf.write("\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7i\2\2\u00d0\34\3\2\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6\u00d7\7p\2\2\u00d7\36\3\2\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc \3\2\2\2\u00dd\u00de\7e\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\"\3\2\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb")
        buf.write("\7e\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7t\2\2\u00ee$\3\2\2\2\u00ef\u00f0\7x\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7t\2\2\u00f2&\3\2\2\2\u00f3\u00f4")
        buf.write("\7u\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7(\3\2\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7y\2\2\u00fb*\3\2\2\2\u00fc\u00fd")
        buf.write("\7x\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7f\2\2\u0100,\3\2\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105\7u\2\2\u0105\u0106")
        buf.write("\7v\2\2\u0106.\3\2\2\2\u0107\u0108\7h\2\2\u0108\u0109")
        buf.write("\7w\2\2\u0109\u010a\7p\2\2\u010a\u010b\7e\2\2\u010b\60")
        buf.write("\3\2\2\2\u010c\u010d\7-\2\2\u010d\62\3\2\2\2\u010e\u010f")
        buf.write("\7/\2\2\u010f\64\3\2\2\2\u0110\u0111\7,\2\2\u0111\66\3")
        buf.write("\2\2\2\u0112\u0113\7\61\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7#\2\2\u0115:\3\2\2\2\u0116\u0117\7(\2\2\u0117\u0118")
        buf.write("\7(\2\2\u0118<\3\2\2\2\u0119\u011a\7~\2\2\u011a\u011b")
        buf.write("\7~\2\2\u011b>\3\2\2\2\u011c\u011d\7?\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e@\3\2\2\2\u011f\u0120\7<\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121B\3\2\2\2\u0122\u0123\7?\2\2\u0123D\3\2\2")
        buf.write("\2\u0124\u0125\7#\2\2\u0125\u0126\7?\2\2\u0126F\3\2\2")
        buf.write("\2\u0127\u0128\7>\2\2\u0128H\3\2\2\2\u0129\u012a\7>\2")
        buf.write("\2\u012a\u012b\7?\2\2\u012bJ\3\2\2\2\u012c\u012d\7@\2")
        buf.write("\2\u012dL\3\2\2\2\u012e\u012f\7@\2\2\u012f\u0130\7?\2")
        buf.write("\2\u0130N\3\2\2\2\u0131\u0132\7`\2\2\u0132P\3\2\2\2\u0133")
        buf.write("\u0134\7\'\2\2\u0134R\3\2\2\2\u0135\u0136\7*\2\2\u0136")
        buf.write("T\3\2\2\2\u0137\u0138\7+\2\2\u0138V\3\2\2\2\u0139\u013a")
        buf.write("\7]\2\2\u013aX\3\2\2\2\u013b\u013c\7_\2\2\u013cZ\3\2\2")
        buf.write("\2\u013d\u013e\7\60\2\2\u013e\\\3\2\2\2\u013f\u0140\7")
        buf.write(".\2\2\u0140^\3\2\2\2\u0141\u0142\7<\2\2\u0142`\3\2\2\2")
        buf.write("\u0143\u0144\7=\2\2\u0144b\3\2\2\2\u0145\u0146\7}\2\2")
        buf.write("\u0146d\3\2\2\2\u0147\u0148\7\177\2\2\u0148f\3\2\2\2\u0149")
        buf.write("\u014a\7)\2\2\u014ah\3\2\2\2\u014b\u014c\7$\2\2\u014c")
        buf.write("j\3\2\2\2\u014d\u014e\5q9\2\u014e\u014f\5m\67\2\u014f")
        buf.write("\u0157\3\2\2\2\u0150\u0152\5q9\2\u0151\u0153\5m\67\2\u0152")
        buf.write("\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0155\5o8\2\u0155\u0157\3\2\2\2\u0156\u014d\3\2")
        buf.write("\2\2\u0156\u0150\3\2\2\2\u0157l\3\2\2\2\u0158\u015c\5")
        buf.write("[.\2\u0159\u015b\t\2\2\2\u015a\u0159\3\2\2\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("n\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0161\t\3\2\2\u0160")
        buf.write("\u0162\t\4\2\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0164\5q9\2\u0164p\3\2\2\2")
        buf.write("\u0165\u0167\t\2\2\2\u0166\u0165\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169r")
        buf.write("\3\2\2\2\u016a\u016f\5i\65\2\u016b\u016e\n\5\2\2\u016c")
        buf.write("\u016e\5w<\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0172\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\5")
        buf.write("i\65\2\u0173\u0174\b:\2\2\u0174t\3\2\2\2\u0175\u0177\7")
        buf.write("\17\2\2\u0176\u0175\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0179\7\f\2\2\u0179v\3\2\2\2\u017a")
        buf.write("\u017b\7^\2\2\u017b\u0189\7d\2\2\u017c\u017d\7^\2\2\u017d")
        buf.write("\u0189\7h\2\2\u017e\u017f\7^\2\2\u017f\u0189\7t\2\2\u0180")
        buf.write("\u0181\7^\2\2\u0181\u0189\7p\2\2\u0182\u0183\7^\2\2\u0183")
        buf.write("\u0189\7v\2\2\u0184\u0185\7^\2\2\u0185\u0189\7$\2\2\u0186")
        buf.write("\u0187\7^\2\2\u0187\u0189\7^\2\2\u0188\u017a\3\2\2\2\u0188")
        buf.write("\u017c\3\2\2\2\u0188\u017e\3\2\2\2\u0188\u0180\3\2\2\2")
        buf.write("\u0188\u0182\3\2\2\2\u0188\u0184\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0189x\3\2\2\2\u018a\u018b\7v\2\2\u018b\u018c\7")
        buf.write("t\2\2\u018c\u018d\7w\2\2\u018d\u0194\7g\2\2\u018e\u018f")
        buf.write("\7h\2\2\u018f\u0190\7c\2\2\u0190\u0191\7n\2\2\u0191\u0192")
        buf.write("\7u\2\2\u0192\u0194\7g\2\2\u0193\u018a\3\2\2\2\u0193\u018e")
        buf.write("\3\2\2\2\u0194z\3\2\2\2\u0195\u0199\t\6\2\2\u0196\u0198")
        buf.write("\5\177@\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a|\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019c\u019e\7B\2\2\u019d\u019f\5\177@\2")
        buf.write("\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e\3")
        buf.write("\2\2\2\u01a0\u01a1\3\2\2\2\u01a1~\3\2\2\2\u01a2\u01a3")
        buf.write("\t\7\2\2\u01a3\u0080\3\2\2\2\u01a4\u01a5\7\61\2\2\u01a5")
        buf.write("\u01a6\7\61\2\2\u01a6\u01aa\3\2\2\2\u01a7\u01a9\n\b\2")
        buf.write("\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ad\u01ae\bA\3\2\u01ae\u0082\3\2\2\2")
        buf.write("\u01af\u01b0\7\61\2\2\u01b0\u01b1\7,\2\2\u01b1\u01b5\3")
        buf.write("\2\2\2\u01b2\u01b4\13\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\7")
        buf.write(",\2\2\u01b9\u01ba\7\61\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\bB\3\2\u01bc\u0084\3\2\2\2\u01bd\u01bf\t\t\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\b")
        buf.write("C\3\2\u01c3\u0086\3\2\2\2\u01c4\u01c5\13\2\2\2\u01c5\u01c6")
        buf.write("\bD\4\2\u01c6\u0088\3\2\2\2\u01c7\u01cd\5i\65\2\u01c8")
        buf.write("\u01cc\n\n\2\2\u01c9\u01ca\7^\2\2\u01ca\u01cc\7$\2\2\u01cb")
        buf.write("\u01c8\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cf\3\2\2\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0\3")
        buf.write("\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\5i\65\2\u01d1\u01d2")
        buf.write("\bE\5\2\u01d2\u008a\3\2\2\2\u01d3\u01d8\5i\65\2\u01d4")
        buf.write("\u01d7\n\n\2\2\u01d5\u01d7\5w<\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d8\u01d6\3\2\2\2\u01d9\u01dd\3\2\2\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01db\u01de\5u;\2\u01dc\u01de\7\2\2\3\u01dd\u01db")
        buf.write("\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01e0\bF\6\2\u01e0\u008c\3\2\2\2\27\2\u0152\u0156\u015c")
        buf.write("\u0161\u0168\u016d\u016f\u0176\u0188\u0193\u0199\u01a0")
        buf.write("\u01aa\u01b5\u01c0\u01cb\u01cd\u01d6\u01d8\u01dd\7\3:")
        buf.write("\2\b\2\2\3D\3\3E\4\3F\5")
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
    SIN_Q = 51
    DOU_Q = 52
    FLOAT_LIT = 53
    INT_LIT = 54
    STR_LIT = 55
    BOOL_LIT = 56
    ID = 57
    AT_ID = 58
    CMT_LINE = 59
    CMT_BLOCK = 60
    WS = 61
    ERROR_CHAR = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'<-'", "'Program'", "'@main'", "'break'", "'continue'", 
            "'if'", "'else'", "'for'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'!'", "'&&'", "'||'", "'=='", "':='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'^'", "'%'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "':'", "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM_CLASS", "MAIN", "BREAK", "CONTINUE", "IF", "ELSE", 
            "FOR", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
            "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", 
            "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "AND_OP", 
            "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", 
            "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", 
            "MOD_OP", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", 
            "SEMICOLON", "LCB", "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "INT_LIT", 
            "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", "CMT_BLOCK", 
            "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "PROGRAM_CLASS", "MAIN", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", "STRING", 
                  "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                  "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "DIV_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
                  "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
                  "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", 
                  "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", "DECPART", "EXPPART", 
                  "INT_LIT", "STR_LIT", "NEWLINE", "ESCAPE", "BOOL_LIT", 
                  "ID", "AT_ID", "SEQUENCE", "CMT_LINE", "CMT_BLOCK", "WS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[56] = self.STR_LIT_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

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

     


