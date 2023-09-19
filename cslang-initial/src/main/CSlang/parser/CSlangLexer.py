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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0199\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u0148\n\66\3\66\3\66\5")
        buf.write("\66\u014c\n\66\3\67\3\67\7\67\u0150\n\67\f\67\16\67\u0153")
        buf.write("\13\67\38\38\58\u0157\n8\38\38\39\69\u015c\n9\r9\169\u015d")
        buf.write("\39\39\3:\3:\3:\3:\3:\7:\u0167\n:\f:\16:\u016a\13:\3:")
        buf.write("\3:\3:\3:\3;\3;\5;\u0172\n;\3<\3<\7<\u0176\n<\f<\16<\u0179")
        buf.write("\13<\3=\3=\6=\u017d\n=\r=\16=\u017e\3>\3>\3>\3>\7>\u0185")
        buf.write("\n>\f>\16>\u0188\13>\3>\3>\3?\6?\u018d\n?\r?\16?\u018e")
        buf.write("\3?\3?\3@\3@\3@\3A\3A\3B\3B\2\2C\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m\2o\2q8s9u:w;y<{=}>\177?\u0081")
        buf.write("@\u0083A\3\2\n\3\2\62;\4\2GGgg\4\2--//\3\2$$\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17\"\"\2\u01a2")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2")
        buf.write("\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3")
        buf.write("\2\2\2\5\u0088\3\2\2\2\7\u008e\3\2\2\2\t\u0097\3\2\2\2")
        buf.write("\13\u009a\3\2\2\2\r\u009f\3\2\2\2\17\u00a3\3\2\2\2\21")
        buf.write("\u00a8\3\2\2\2\23\u00ae\3\2\2\2\25\u00b2\3\2\2\2\27\u00b8")
        buf.write("\3\2\2\2\31\u00bd\3\2\2\2\33\u00c4\3\2\2\2\35\u00cb\3")
        buf.write("\2\2\2\37\u00d0\3\2\2\2!\u00d6\3\2\2\2#\u00e2\3\2\2\2")
        buf.write("%\u00e6\3\2\2\2\'\u00eb\3\2\2\2)\u00ef\3\2\2\2+\u00f4")
        buf.write("\3\2\2\2-\u00fa\3\2\2\2/\u00ff\3\2\2\2\61\u0101\3\2\2")
        buf.write("\2\63\u0103\3\2\2\2\65\u0105\3\2\2\2\67\u0107\3\2\2\2")
        buf.write("9\u0109\3\2\2\2;\u010b\3\2\2\2=\u010e\3\2\2\2?\u0111\3")
        buf.write("\2\2\2A\u0114\3\2\2\2C\u0117\3\2\2\2E\u0119\3\2\2\2G\u011c")
        buf.write("\3\2\2\2I\u011e\3\2\2\2K\u0121\3\2\2\2M\u0123\3\2\2\2")
        buf.write("O\u0126\3\2\2\2Q\u0128\3\2\2\2S\u012a\3\2\2\2U\u012c\3")
        buf.write("\2\2\2W\u012e\3\2\2\2Y\u0130\3\2\2\2[\u0132\3\2\2\2]\u0134")
        buf.write("\3\2\2\2_\u0136\3\2\2\2a\u0138\3\2\2\2c\u013a\3\2\2\2")
        buf.write("e\u013c\3\2\2\2g\u013e\3\2\2\2i\u0140\3\2\2\2k\u014b\3")
        buf.write("\2\2\2m\u014d\3\2\2\2o\u0154\3\2\2\2q\u015b\3\2\2\2s\u0161")
        buf.write("\3\2\2\2u\u0171\3\2\2\2w\u0173\3\2\2\2y\u017a\3\2\2\2")
        buf.write("{\u0180\3\2\2\2}\u018c\3\2\2\2\177\u0192\3\2\2\2\u0081")
        buf.write("\u0195\3\2\2\2\u0083\u0197\3\2\2\2\u0085\u0086\7>\2\2")
        buf.write("\u0086\u0087\7/\2\2\u0087\4\3\2\2\2\u0088\u0089\7d\2\2")
        buf.write("\u0089\u008a\7t\2\2\u008a\u008b\7g\2\2\u008b\u008c\7c")
        buf.write("\2\2\u008c\u008d\7m\2\2\u008d\6\3\2\2\2\u008e\u008f\7")
        buf.write("e\2\2\u008f\u0090\7q\2\2\u0090\u0091\7p\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7g\2\2\u0096\b\3\2\2\2\u0097\u0098")
        buf.write("\7k\2\2\u0098\u0099\7h\2\2\u0099\n\3\2\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\f\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7t\2\2\u00a2\16\3\2\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\20\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7c\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\22\3\2\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\24\3\2\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u00b7\7v\2\2\u00b7\26\3\2\2\2\u00b8\u00b9")
        buf.write("\7d\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7n\2\2\u00bc\30\3\2\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7i\2\2\u00c3\32\3\2\2\2\u00c4\u00c5")
        buf.write("\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7p\2\2\u00ca\34")
        buf.write("\3\2\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7n\2\2\u00cf\36\3\2\2\2\u00d0\u00d1")
        buf.write("\7e\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7u\2\2\u00d5 \3\2\2\2\u00d6\u00d7")
        buf.write("\7e\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7w\2\2\u00dd\u00de\7e\2\2\u00de\u00df\7v\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7t\2\2\u00e1\"\3\2\2\2\u00e2\u00e3")
        buf.write("\7x\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7t\2\2\u00e5$\3")
        buf.write("\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7n\2\2\u00e9\u00ea\7h\2\2\u00ea&\3\2\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7y\2\2\u00ee(\3")
        buf.write("\2\2\2\u00ef\u00f0\7x\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7k\2\2\u00f2\u00f3\7f\2\2\u00f3*\3\2\2\2\u00f4\u00f5")
        buf.write("\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7v\2\2\u00f9,\3\2\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe.\3\2\2\2\u00ff\u0100\7-\2\2\u0100\60\3\2")
        buf.write("\2\2\u0101\u0102\7/\2\2\u0102\62\3\2\2\2\u0103\u0104\7")
        buf.write(",\2\2\u0104\64\3\2\2\2\u0105\u0106\7\61\2\2\u0106\66\3")
        buf.write("\2\2\2\u0107\u0108\7^\2\2\u01088\3\2\2\2\u0109\u010a\7")
        buf.write("#\2\2\u010a:\3\2\2\2\u010b\u010c\7(\2\2\u010c\u010d\7")
        buf.write("(\2\2\u010d<\3\2\2\2\u010e\u010f\7~\2\2\u010f\u0110\7")
        buf.write("~\2\2\u0110>\3\2\2\2\u0111\u0112\7?\2\2\u0112\u0113\7")
        buf.write("?\2\2\u0113@\3\2\2\2\u0114\u0115\7<\2\2\u0115\u0116\7")
        buf.write("?\2\2\u0116B\3\2\2\2\u0117\u0118\7?\2\2\u0118D\3\2\2\2")
        buf.write("\u0119\u011a\7#\2\2\u011a\u011b\7?\2\2\u011bF\3\2\2\2")
        buf.write("\u011c\u011d\7>\2\2\u011dH\3\2\2\2\u011e\u011f\7>\2\2")
        buf.write("\u011f\u0120\7?\2\2\u0120J\3\2\2\2\u0121\u0122\7@\2\2")
        buf.write("\u0122L\3\2\2\2\u0123\u0124\7@\2\2\u0124\u0125\7?\2\2")
        buf.write("\u0125N\3\2\2\2\u0126\u0127\7`\2\2\u0127P\3\2\2\2\u0128")
        buf.write("\u0129\7\'\2\2\u0129R\3\2\2\2\u012a\u012b\7*\2\2\u012b")
        buf.write("T\3\2\2\2\u012c\u012d\7+\2\2\u012dV\3\2\2\2\u012e\u012f")
        buf.write("\7]\2\2\u012fX\3\2\2\2\u0130\u0131\7_\2\2\u0131Z\3\2\2")
        buf.write("\2\u0132\u0133\7\60\2\2\u0133\\\3\2\2\2\u0134\u0135\7")
        buf.write(".\2\2\u0135^\3\2\2\2\u0136\u0137\7<\2\2\u0137`\3\2\2\2")
        buf.write("\u0138\u0139\7=\2\2\u0139b\3\2\2\2\u013a\u013b\7}\2\2")
        buf.write("\u013bd\3\2\2\2\u013c\u013d\7\177\2\2\u013df\3\2\2\2\u013e")
        buf.write("\u013f\7)\2\2\u013fh\3\2\2\2\u0140\u0141\7$\2\2\u0141")
        buf.write("j\3\2\2\2\u0142\u0143\5q9\2\u0143\u0144\5m\67\2\u0144")
        buf.write("\u014c\3\2\2\2\u0145\u0147\5q9\2\u0146\u0148\5m\67\2\u0147")
        buf.write("\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\5o8\2\u014a\u014c\3\2\2\2\u014b\u0142\3\2")
        buf.write("\2\2\u014b\u0145\3\2\2\2\u014cl\3\2\2\2\u014d\u0151\5")
        buf.write("[.\2\u014e\u0150\t\2\2\2\u014f\u014e\3\2\2\2\u0150\u0153")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("n\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0156\t\3\2\2\u0155")
        buf.write("\u0157\t\4\2\2\u0156\u0155\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158\u0159\5q9\2\u0159p\3\2\2\2")
        buf.write("\u015a\u015c\t\2\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0160\b9\2\2\u0160r\3\2\2\2\u0161\u0168")
        buf.write("\5i\65\2\u0162\u0167\n\5\2\2\u0163\u0164\5\67\34\2\u0164")
        buf.write("\u0165\5i\65\2\u0165\u0167\3\2\2\2\u0166\u0162\3\2\2\2")
        buf.write("\u0166\u0163\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3")
        buf.write("\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016b\u016c\5i\65\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016e\b:\3\2\u016et\3\2\2\2\u016f\u0172\5\17\b\2\u0170")
        buf.write("\u0172\5\21\t\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2")
        buf.write("\2\u0172v\3\2\2\2\u0173\u0177\t\6\2\2\u0174\u0176\t\7")
        buf.write("\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178x\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u017a\u017c\7B\2\2\u017b\u017d\t\7\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017fz\3\2\2\2\u0180\u0181\7\61\2")
        buf.write("\2\u0181\u0182\7\61\2\2\u0182\u0186\3\2\2\2\u0183\u0185")
        buf.write("\n\b\2\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0189\u018a\b>\4\2\u018a|\3\2\2\2")
        buf.write("\u018b\u018d\t\t\2\2\u018c\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190\u0191\b?\4\2\u0191~\3\2\2\2\u0192\u0193")
        buf.write("\13\2\2\2\u0193\u0194\b@\5\2\u0194\u0080\3\2\2\2\u0195")
        buf.write("\u0196\13\2\2\2\u0196\u0082\3\2\2\2\u0197\u0198\13\2\2")
        buf.write("\2\u0198\u0084\3\2\2\2\17\2\u0147\u014b\u0151\u0156\u015d")
        buf.write("\u0166\u0168\u0171\u0177\u017e\u0186\u018e\6\39\2\3:\3")
        buf.write("\b\2\2\3@\4")
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
    AT_ID = 58
    CMT_LINE = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

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
            "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
                  "EXPPART", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "AT_ID", 
                  "CMT_LINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
     


