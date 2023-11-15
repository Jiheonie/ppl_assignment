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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\5\63\u013d\n\63\3\63\3")
        buf.write("\63\5\63\u0141\n\63\3\64\3\64\7\64\u0145\n\64\f\64\16")
        buf.write("\64\u0148\13\64\3\65\3\65\5\65\u014c\n\65\3\65\3\65\3")
        buf.write("\66\6\66\u0151\n\66\r\66\16\66\u0152\3\66\3\66\3\67\3")
        buf.write("\67\3\67\7\67\u015a\n\67\f\67\16\67\u015d\13\67\3\67\3")
        buf.write("\67\3\67\38\58\u0163\n8\38\38\39\39\39\39\39\39\39\39")
        buf.write("\39\39\39\39\39\39\59\u0175\n9\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\5:\u0180\n:\3;\3;\7;\u0184\n;\f;\16;\u0187\13;\3")
        buf.write("<\3<\6<\u018b\n<\r<\16<\u018c\3=\3=\3>\3>\3>\3>\7>\u0195")
        buf.write("\n>\f>\16>\u0198\13>\3>\3>\3?\3?\3?\3?\7?\u01a0\n?\f?")
        buf.write("\16?\u01a3\13?\3?\3?\3?\3?\3?\3@\6@\u01ab\n@\r@\16@\u01ac")
        buf.write("\3@\3@\3A\3A\3A\3A\7A\u01b5\nA\fA\16A\u01b8\13A\3A\3A")
        buf.write("\3A\3B\3B\3B\7B\u01c0\nB\fB\16B\u01c3\13B\3B\3B\5B\u01c7")
        buf.write("\nB\3B\3B\3C\3C\3C\4\u01a1\u01c1\2D\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\2i\2k\65m\66o\2q\2s\67u8w9y\2{:};\177")
        buf.write("<\u0081=\u0083>\u0085?\3\2\13\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n")
        buf.write("\f\16\17\"\"\3\2$$\2\u01e0\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3")
        buf.write("\u0087\3\2\2\2\5\u0089\3\2\2\2\7\u008f\3\2\2\2\t\u0098")
        buf.write("\3\2\2\2\13\u009b\3\2\2\2\r\u00a0\3\2\2\2\17\u00a4\3\2")
        buf.write("\2\2\21\u00a8\3\2\2\2\23\u00ae\3\2\2\2\25\u00b3\3\2\2")
        buf.write("\2\27\u00ba\3\2\2\2\31\u00c1\3\2\2\2\33\u00c6\3\2\2\2")
        buf.write("\35\u00cc\3\2\2\2\37\u00d8\3\2\2\2!\u00dc\3\2\2\2#\u00e1")
        buf.write("\3\2\2\2%\u00e5\3\2\2\2\'\u00ea\3\2\2\2)\u00f0\3\2\2\2")
        buf.write("+\u00f5\3\2\2\2-\u00f7\3\2\2\2/\u00f9\3\2\2\2\61\u00fb")
        buf.write("\3\2\2\2\63\u00fd\3\2\2\2\65\u00ff\3\2\2\2\67\u0102\3")
        buf.write("\2\2\29\u0105\3\2\2\2;\u0108\3\2\2\2=\u010b\3\2\2\2?\u010d")
        buf.write("\3\2\2\2A\u0110\3\2\2\2C\u0112\3\2\2\2E\u0115\3\2\2\2")
        buf.write("G\u0117\3\2\2\2I\u011a\3\2\2\2K\u011c\3\2\2\2M\u011e\3")
        buf.write("\2\2\2O\u0120\3\2\2\2Q\u0122\3\2\2\2S\u0124\3\2\2\2U\u0126")
        buf.write("\3\2\2\2W\u0128\3\2\2\2Y\u012a\3\2\2\2[\u012c\3\2\2\2")
        buf.write("]\u012e\3\2\2\2_\u0130\3\2\2\2a\u0132\3\2\2\2c\u0134\3")
        buf.write("\2\2\2e\u0140\3\2\2\2g\u0142\3\2\2\2i\u0149\3\2\2\2k\u0150")
        buf.write("\3\2\2\2m\u0156\3\2\2\2o\u0162\3\2\2\2q\u0174\3\2\2\2")
        buf.write("s\u017f\3\2\2\2u\u0181\3\2\2\2w\u0188\3\2\2\2y\u018e\3")
        buf.write("\2\2\2{\u0190\3\2\2\2}\u019b\3\2\2\2\177\u01aa\3\2\2\2")
        buf.write("\u0081\u01b0\3\2\2\2\u0083\u01bc\3\2\2\2\u0085\u01ca\3")
        buf.write("\2\2\2\u0087\u0088\7^\2\2\u0088\4\3\2\2\2\u0089\u008a")
        buf.write("\7d\2\2\u008a\u008b\7t\2\2\u008b\u008c\7g\2\2\u008c\u008d")
        buf.write("\7c\2\2\u008d\u008e\7m\2\2\u008e\6\3\2\2\2\u008f\u0090")
        buf.write("\7e\2\2\u0090\u0091\7q\2\2\u0091\u0092\7p\2\2\u0092\u0093")
        buf.write("\7v\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7w\2\2\u0096\u0097\7g\2\2\u0097\b\3\2\2\2\u0098\u0099")
        buf.write("\7k\2\2\u0099\u009a\7h\2\2\u009a\n\3\2\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\f\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7t\2\2\u00a3\16\3\2\2\2\u00a4\u00a5")
        buf.write("\7k\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7v\2\2\u00a7\20")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7n\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7v\2\2\u00ad\22")
        buf.write("\3\2\2\2\u00ae\u00af\7d\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7n\2\2\u00b2\24\3\2\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7i\2\2\u00b9\26")
        buf.write("\3\2\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\30\3\2\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7w\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5\7n\2\2\u00c5\32")
        buf.write("\3\2\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7u\2\2\u00cb\34")
        buf.write("\3\2\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7t\2\2\u00d7\36")
        buf.write("\3\2\2\2\u00d8\u00d9\7x\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db \3\2\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7h\2\2\u00e0\"")
        buf.write("\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7y\2\2\u00e4$\3\2\2\2\u00e5\u00e6\7x\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7f\2\2\u00e9&\3")
        buf.write("\2\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7v\2\2\u00ef(\3")
        buf.write("\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7e\2\2\u00f4*\3\2\2\2\u00f5\u00f6")
        buf.write("\7-\2\2\u00f6,\3\2\2\2\u00f7\u00f8\7/\2\2\u00f8.\3\2\2")
        buf.write("\2\u00f9\u00fa\7,\2\2\u00fa\60\3\2\2\2\u00fb\u00fc\7\61")
        buf.write("\2\2\u00fc\62\3\2\2\2\u00fd\u00fe\7#\2\2\u00fe\64\3\2")
        buf.write("\2\2\u00ff\u0100\7(\2\2\u0100\u0101\7(\2\2\u0101\66\3")
        buf.write("\2\2\2\u0102\u0103\7~\2\2\u0103\u0104\7~\2\2\u01048\3")
        buf.write("\2\2\2\u0105\u0106\7?\2\2\u0106\u0107\7?\2\2\u0107:\3")
        buf.write("\2\2\2\u0108\u0109\7<\2\2\u0109\u010a\7?\2\2\u010a<\3")
        buf.write("\2\2\2\u010b\u010c\7?\2\2\u010c>\3\2\2\2\u010d\u010e\7")
        buf.write("#\2\2\u010e\u010f\7?\2\2\u010f@\3\2\2\2\u0110\u0111\7")
        buf.write(">\2\2\u0111B\3\2\2\2\u0112\u0113\7>\2\2\u0113\u0114\7")
        buf.write("?\2\2\u0114D\3\2\2\2\u0115\u0116\7@\2\2\u0116F\3\2\2\2")
        buf.write("\u0117\u0118\7@\2\2\u0118\u0119\7?\2\2\u0119H\3\2\2\2")
        buf.write("\u011a\u011b\7`\2\2\u011bJ\3\2\2\2\u011c\u011d\7\'\2\2")
        buf.write("\u011dL\3\2\2\2\u011e\u011f\7*\2\2\u011fN\3\2\2\2\u0120")
        buf.write("\u0121\7+\2\2\u0121P\3\2\2\2\u0122\u0123\7]\2\2\u0123")
        buf.write("R\3\2\2\2\u0124\u0125\7_\2\2\u0125T\3\2\2\2\u0126\u0127")
        buf.write("\7\60\2\2\u0127V\3\2\2\2\u0128\u0129\7.\2\2\u0129X\3\2")
        buf.write("\2\2\u012a\u012b\7<\2\2\u012bZ\3\2\2\2\u012c\u012d\7=")
        buf.write("\2\2\u012d\\\3\2\2\2\u012e\u012f\7}\2\2\u012f^\3\2\2\2")
        buf.write("\u0130\u0131\7\177\2\2\u0131`\3\2\2\2\u0132\u0133\7$\2")
        buf.write("\2\u0133b\3\2\2\2\u0134\u0135\7>\2\2\u0135\u0136\7/\2")
        buf.write("\2\u0136d\3\2\2\2\u0137\u0138\5k\66\2\u0138\u0139\5g\64")
        buf.write("\2\u0139\u0141\3\2\2\2\u013a\u013c\5k\66\2\u013b\u013d")
        buf.write("\5g\64\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u013f\5i\65\2\u013f\u0141\3\2\2\2")
        buf.write("\u0140\u0137\3\2\2\2\u0140\u013a\3\2\2\2\u0141f\3\2\2")
        buf.write("\2\u0142\u0146\5U+\2\u0143\u0145\t\2\2\2\u0144\u0143\3")
        buf.write("\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147h\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b")
        buf.write("\t\3\2\2\u014a\u014c\t\4\2\2\u014b\u014a\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\5k\66\2")
        buf.write("\u014ej\3\2\2\2\u014f\u0151\t\2\2\2\u0150\u014f\3\2\2")
        buf.write("\2\u0151\u0152\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\b\66\2\2\u0155")
        buf.write("l\3\2\2\2\u0156\u015b\5a\61\2\u0157\u015a\n\5\2\2\u0158")
        buf.write("\u015a\5q9\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\5")
        buf.write("a\61\2\u015f\u0160\b\67\3\2\u0160n\3\2\2\2\u0161\u0163")
        buf.write("\7\17\2\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\7\f\2\2\u0165p\3\2\2\2\u0166")
        buf.write("\u0167\7^\2\2\u0167\u0175\7d\2\2\u0168\u0169\7^\2\2\u0169")
        buf.write("\u0175\7h\2\2\u016a\u016b\7^\2\2\u016b\u0175\7t\2\2\u016c")
        buf.write("\u016d\7^\2\2\u016d\u0175\7p\2\2\u016e\u016f\7^\2\2\u016f")
        buf.write("\u0175\7v\2\2\u0170\u0171\7^\2\2\u0171\u0175\7^\2\2\u0172")
        buf.write("\u0173\7^\2\2\u0173\u0175\7$\2\2\u0174\u0166\3\2\2\2\u0174")
        buf.write("\u0168\3\2\2\2\u0174\u016a\3\2\2\2\u0174\u016c\3\2\2\2")
        buf.write("\u0174\u016e\3\2\2\2\u0174\u0170\3\2\2\2\u0174\u0172\3")
        buf.write("\2\2\2\u0175r\3\2\2\2\u0176\u0177\7v\2\2\u0177\u0178\7")
        buf.write("t\2\2\u0178\u0179\7w\2\2\u0179\u0180\7g\2\2\u017a\u017b")
        buf.write("\7h\2\2\u017b\u017c\7c\2\2\u017c\u017d\7n\2\2\u017d\u017e")
        buf.write("\7u\2\2\u017e\u0180\7g\2\2\u017f\u0176\3\2\2\2\u017f\u017a")
        buf.write("\3\2\2\2\u0180t\3\2\2\2\u0181\u0185\t\6\2\2\u0182\u0184")
        buf.write("\5y=\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186v\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0188\u018a\7B\2\2\u0189\u018b\5y=\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018dx\3\2\2\2\u018e\u018f\t\7\2\2\u018f")
        buf.write("z\3\2\2\2\u0190\u0191\7\61\2\2\u0191\u0192\7\61\2\2\u0192")
        buf.write("\u0196\3\2\2\2\u0193\u0195\n\b\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a")
        buf.write("\b>\4\2\u019a|\3\2\2\2\u019b\u019c\7\61\2\2\u019c\u019d")
        buf.write("\7,\2\2\u019d\u01a1\3\2\2\2\u019e\u01a0\13\2\2\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3")
        buf.write("\2\2\2\u01a4\u01a5\7,\2\2\u01a5\u01a6\7\61\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a8\b?\4\2\u01a8~\3\2\2\2\u01a9\u01ab")
        buf.write("\t\t\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\b@\4\2\u01af\u0080\3\2\2\2\u01b0\u01b6\5")
        buf.write("a\61\2\u01b1\u01b5\n\n\2\2\u01b2\u01b3\7^\2\2\u01b3\u01b5")
        buf.write("\7$\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\5")
        buf.write("a\61\2\u01ba\u01bb\bA\5\2\u01bb\u0082\3\2\2\2\u01bc\u01c1")
        buf.write("\5a\61\2\u01bd\u01c0\n\n\2\2\u01be\u01c0\5q9\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c6\3\2\2\2")
        buf.write("\u01c3\u01c1\3\2\2\2\u01c4\u01c7\5o8\2\u01c5\u01c7\7\2")
        buf.write("\2\3\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\bB\6\2\u01c9\u0084\3\2\2\2\u01ca")
        buf.write("\u01cb\13\2\2\2\u01cb\u01cc\bC\7\2\u01cc\u0086\3\2\2\2")
        buf.write("\27\2\u013c\u0140\u0146\u014b\u0152\u0159\u015b\u0162")
        buf.write("\u0174\u017f\u0185\u018c\u0196\u01a1\u01ac\u01b4\u01b6")
        buf.write("\u01bf\u01c1\u01c6\b\3\66\2\3\67\3\b\2\2\3A\4\3B\5\3C")
        buf.write("\6")
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
    DIV_OP = 24
    NOT_OP = 25
    AND_OP = 26
    OR_OP = 27
    EQUAL_OP = 28
    ASSIGN_OP = 29
    DECL_OP = 30
    DIFF_OP = 31
    LESS_OP = 32
    LESS_EQUAL_OP = 33
    GREATER_OP = 34
    GREATER_EQUAL_OP = 35
    CONCAT_OP = 36
    MOD_OP = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    DOT = 42
    COMMA = 43
    COLON = 44
    SEMICOLON = 45
    LCB = 46
    RCB = 47
    DOU_Q = 48
    INHERIT = 49
    FLOAT_LIT = 50
    INT_LIT = 51
    STR_LIT = 52
    BOOL_LIT = 53
    ID = 54
    AT_ID = 55
    CMT_LINE = 56
    CMT_BLOCK = 57
    WS = 58
    ILLEGAL_ESCAPE = 59
    UNCLOSE_STRING = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'int'", "'float'", "'bool'", "'string'", "'return'", "'null'", 
            "'class'", "'constructor'", "'var'", "'self'", "'new'", "'void'", 
            "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'!'", "'&&'", 
            "'||'", "'=='", "':='", "'='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "':'", "';'", "'{'", "'}'", "'\"'", "'<-'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", 
            "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
            "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
            "DIV_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
            "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
            "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", 
            "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "DOU_Q", 
            "INHERIT", "FLOAT_LIT", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", 
            "AT_ID", "CMT_LINE", "CMT_BLOCK", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", 
                  "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                  "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", 
                  "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                  "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", "RSB", "DOT", 
                  "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "DOU_Q", 
                  "INHERIT", "FLOAT_LIT", "DECPART", "EXPPART", "INT_LIT", 
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
            actions[52] = self.INT_LIT_action 
            actions[53] = self.STR_LIT_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ERROR_CHAR_action 
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
     


