# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\u01f1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u0089\n\4\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0090\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u0097\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\7\7\u009f\n\7\f\7\16\7\u00a2\13\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\7\b\u00aa\n\b\f\b\16\b\u00ad\13\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\7\t\u00b5\n\t\f\t\16\t\u00b8\13")
        buf.write("\t\3\n\3\n\3\n\5\n\u00bd\n\n\3\13\3\13\3\13\5\13\u00c2")
        buf.write("\n\13\3\f\3\f\5\f\u00c6\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00d5\n\r\f\r\16\r\u00d8")
        buf.write("\13\r\3\16\3\16\5\16\u00dc\n\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00e6\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00ed\n\20\3\21\3\21\5\21\u00f1\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00f8\n\22\3\23\3\23\5\23\u00fc")
        buf.write("\n\23\3\24\3\24\5\24\u0100\n\24\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\5\27\u010c\n\27\3\30\3\30")
        buf.write("\3\30\5\30\u0111\n\30\3\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u011c\n\31\3\32\3\32\5\32\u0120\n\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\5\34\u012b")
        buf.write("\n\34\3\35\3\35\3\35\5\35\u0130\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u013f")
        buf.write("\n \3!\3!\5!\u0143\n!\3!\3!\3\"\3\"\5\"\u0149\n\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\5#\u0152\n#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3&\3&\3&\5&\u0162\n&\3\'\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3,\3,\5,\u0180\n,\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\5.\u0192\n.\3/\3/\3/\3/\5/\u0198")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01a4\n\60\3\61\3\61\3\61\3\61\3\62\3\62\5\62\u01ac")
        buf.write("\n\62\3\62\3\62\3\62\3\62\5\62\u01b2\n\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\5\66\u01c4\n\66\3\66\3\66\3\67\3\67\3")
        buf.write("\67\5\67\u01cb\n\67\3\67\3\67\38\38\38\38\39\39\39\39")
        buf.write("\59\u01d7\n9\3:\3:\5:\u01db\n:\3;\3;\3;\3;\3;\5;\u01e2")
        buf.write("\n;\3<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\2\6\f\16")
        buf.write("\20\30?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\t")
        buf.write("\4\2\37\37\"&\3\2\35\36\3\2\30\31\5\2\3\3\32\33((\3\2")
        buf.write("\n\r\3\29:\4\2\22\22\26\26\2\u01ee\2|\3\2\2\2\4\u0083")
        buf.write("\3\2\2\2\6\u0088\3\2\2\2\b\u008f\3\2\2\2\n\u0096\3\2\2")
        buf.write("\2\f\u0098\3\2\2\2\16\u00a3\3\2\2\2\20\u00ae\3\2\2\2\22")
        buf.write("\u00bc\3\2\2\2\24\u00c1\3\2\2\2\26\u00c5\3\2\2\2\30\u00c7")
        buf.write("\3\2\2\2\32\u00db\3\2\2\2\34\u00e5\3\2\2\2\36\u00ec\3")
        buf.write("\2\2\2 \u00f0\3\2\2\2\"\u00f7\3\2\2\2$\u00fb\3\2\2\2&")
        buf.write("\u00ff\3\2\2\2(\u0101\3\2\2\2*\u0103\3\2\2\2,\u010b\3")
        buf.write("\2\2\2.\u010d\3\2\2\2\60\u011b\3\2\2\2\62\u011f\3\2\2")
        buf.write("\2\64\u0121\3\2\2\2\66\u012a\3\2\2\28\u012f\3\2\2\2:\u0131")
        buf.write("\3\2\2\2<\u0135\3\2\2\2>\u013e\3\2\2\2@\u0142\3\2\2\2")
        buf.write("B\u0148\3\2\2\2D\u0151\3\2\2\2F\u0153\3\2\2\2H\u0157\3")
        buf.write("\2\2\2J\u0161\3\2\2\2L\u0163\3\2\2\2N\u0167\3\2\2\2P\u016b")
        buf.write("\3\2\2\2R\u0172\3\2\2\2T\u0179\3\2\2\2V\u017f\3\2\2\2")
        buf.write("X\u0181\3\2\2\2Z\u0191\3\2\2\2\\\u0197\3\2\2\2^\u01a3")
        buf.write("\3\2\2\2`\u01a5\3\2\2\2b\u01a9\3\2\2\2d\u01b3\3\2\2\2")
        buf.write("f\u01bb\3\2\2\2h\u01be\3\2\2\2j\u01c1\3\2\2\2l\u01ca\3")
        buf.write("\2\2\2n\u01ce\3\2\2\2p\u01d6\3\2\2\2r\u01da\3\2\2\2t\u01e1")
        buf.write("\3\2\2\2v\u01e3\3\2\2\2x\u01e7\3\2\2\2z\u01eb\3\2\2\2")
        buf.write("|}\5\4\3\2}~\7\2\2\3~\3\3\2\2\2\177\u0080\5\6\4\2\u0080")
        buf.write("\u0081\5\4\3\2\u0081\u0084\3\2\2\2\u0082\u0084\5\6\4\2")
        buf.write("\u0083\177\3\2\2\2\u0083\u0082\3\2\2\2\u0084\5\3\2\2\2")
        buf.write("\u0085\u0089\5\b\5\2\u0086\u0089\5^\60\2\u0087\u0089\5")
        buf.write(",\27\2\u0088\u0085\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087")
        buf.write("\3\2\2\2\u0089\7\3\2\2\2\u008a\u008b\5\n\6\2\u008b\u008c")
        buf.write("\7\'\2\2\u008c\u008d\5\n\6\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u0090\5\n\6\2\u008f\u008a\3\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\t\3\2\2\2\u0091\u0092\5\f\7\2\u0092\u0093\t\2\2")
        buf.write("\2\u0093\u0094\5\f\7\2\u0094\u0097\3\2\2\2\u0095\u0097")
        buf.write("\5\f\7\2\u0096\u0091\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\13\3\2\2\2\u0098\u0099\b\7\1\2\u0099\u009a\5\16\b\2\u009a")
        buf.write("\u00a0\3\2\2\2\u009b\u009c\f\4\2\2\u009c\u009d\t\3\2\2")
        buf.write("\u009d\u009f\5\16\b\2\u009e\u009b\3\2\2\2\u009f\u00a2")
        buf.write("\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\r\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\b\b\1\2\u00a4")
        buf.write("\u00a5\5\20\t\2\u00a5\u00ab\3\2\2\2\u00a6\u00a7\f\4\2")
        buf.write("\2\u00a7\u00a8\t\4\2\2\u00a8\u00aa\5\20\t\2\u00a9\u00a6")
        buf.write("\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\17\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae")
        buf.write("\u00af\b\t\1\2\u00af\u00b0\5\22\n\2\u00b0\u00b6\3\2\2")
        buf.write("\2\u00b1\u00b2\f\4\2\2\u00b2\u00b3\t\5\2\2\u00b3\u00b5")
        buf.write("\5\22\n\2\u00b4\u00b1\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\21\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b9\u00ba\7\34\2\2\u00ba\u00bd\5\22\n")
        buf.write("\2\u00bb\u00bd\5\24\13\2\u00bc\u00b9\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\23\3\2\2\2\u00be\u00bf\7\31\2\2\u00bf\u00c2")
        buf.write("\5\24\13\2\u00c0\u00c2\5\26\f\2\u00c1\u00be\3\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c6\5z>\2\u00c4")
        buf.write("\u00c6\5\30\r\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2")
        buf.write("\2\u00c6\27\3\2\2\2\u00c7\u00c8\b\r\1\2\u00c8\u00c9\5")
        buf.write("\32\16\2\u00c9\u00d6\3\2\2\2\u00ca\u00cb\f\5\2\2\u00cb")
        buf.write("\u00cc\7-\2\2\u00cc\u00d5\79\2\2\u00cd\u00ce\f\4\2\2\u00ce")
        buf.write("\u00cf\7-\2\2\u00cf\u00d0\79\2\2\u00d0\u00d1\7)\2\2\u00d1")
        buf.write("\u00d2\5 \21\2\u00d2\u00d3\7*\2\2\u00d3\u00d5\3\2\2\2")
        buf.write("\u00d4\u00ca\3\2\2\2\u00d4\u00cd\3\2\2\2\u00d5\u00d8\3")
        buf.write("\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\31")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00dc\5> \2\u00da\u00dc")
        buf.write("\5\34\17\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\33\3\2\2\2\u00dd\u00e6\5\64\33\2\u00de\u00e6\5\36\20")
        buf.write("\2\u00df\u00e0\7)\2\2\u00e0\u00e1\5\b\5\2\u00e1\u00e2")
        buf.write("\7*\2\2\u00e2\u00e6\3\2\2\2\u00e3\u00e6\79\2\2\u00e4\u00e6")
        buf.write("\5F$\2\u00e5\u00dd\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5\u00df")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6")
        buf.write("\35\3\2\2\2\u00e7\u00ed\7\66\2\2\u00e8\u00ed\7\65\2\2")
        buf.write("\u00e9\u00ed\7\67\2\2\u00ea\u00ed\78\2\2\u00eb\u00ed\5")
        buf.write("x=\2\u00ec\u00e7\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9")
        buf.write("\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write("\37\3\2\2\2\u00ee\u00f1\5\"\22\2\u00ef\u00f1\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1!\3\2\2\2\u00f2")
        buf.write("\u00f3\5\b\5\2\u00f3\u00f4\7.\2\2\u00f4\u00f5\5\"\22\2")
        buf.write("\u00f5\u00f8\3\2\2\2\u00f6\u00f8\5\b\5\2\u00f7\u00f2\3")
        buf.write("\2\2\2\u00f7\u00f6\3\2\2\2\u00f8#\3\2\2\2\u00f9\u00fc")
        buf.write("\5&\24\2\u00fa\u00fc\7\25\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc%\3\2\2\2\u00fd\u0100\5(\25\2\u00fe")
        buf.write("\u0100\5*\26\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2")
        buf.write("\u0100\'\3\2\2\2\u0101\u0102\t\6\2\2\u0102)\3\2\2\2\u0103")
        buf.write("\u0104\7+\2\2\u0104\u0105\7\66\2\2\u0105\u0106\7,\2\2")
        buf.write("\u0106\u0107\5(\25\2\u0107+\3\2\2\2\u0108\u010c\5.\30")
        buf.write("\2\u0109\u010c\5T+\2\u010a\u010c\5J&\2\u010b\u0108\3\2")
        buf.write("\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c-\3")
        buf.write("\2\2\2\u010d\u0110\7\20\2\2\u010e\u010f\79\2\2\u010f\u0111")
        buf.write("\7\4\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u0113\79\2\2\u0113\u0114\7\61\2\2")
        buf.write("\u0114\u0115\5\60\31\2\u0115\u0116\7\62\2\2\u0116/\3\2")
        buf.write("\2\2\u0117\u0118\5\62\32\2\u0118\u0119\5\60\31\2\u0119")
        buf.write("\u011c\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0117\3\2\2\2")
        buf.write("\u011b\u011a\3\2\2\2\u011c\61\3\2\2\2\u011d\u0120\5T+")
        buf.write("\2\u011e\u0120\5J&\2\u011f\u011d\3\2\2\2\u011f\u011e\3")
        buf.write("\2\2\2\u0120\63\3\2\2\2\u0121\u0122\7\24\2\2\u0122\u0123")
        buf.write("\79\2\2\u0123\u0124\7)\2\2\u0124\u0125\5 \21\2\u0125\u0126")
        buf.write("\7*\2\2\u0126\65\3\2\2\2\u0127\u012b\5:\36\2\u0128\u012b")
        buf.write("\5@!\2\u0129\u012b\5F$\2\u012a\u0127\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u0129\3\2\2\2\u012b\67\3\2\2\2\u012c\u0130")
        buf.write("\5<\37\2\u012d\u0130\5B\"\2\u012e\u0130\5H%\2\u012f\u012c")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130")
        buf.write("9\3\2\2\2\u0131\u0132\5\30\r\2\u0132\u0133\7-\2\2\u0133")
        buf.write("\u0134\79\2\2\u0134;\3\2\2\2\u0135\u0136\5\30\r\2\u0136")
        buf.write("\u0137\7-\2\2\u0137\u0138\79\2\2\u0138\u0139\7)\2\2\u0139")
        buf.write("\u013a\5 \21\2\u013a\u013b\7*\2\2\u013b=\3\2\2\2\u013c")
        buf.write("\u013f\5@!\2\u013d\u013f\5B\"\2\u013e\u013c\3\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013f?\3\2\2\2\u0140\u0141\79\2\2\u0141")
        buf.write("\u0143\7-\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0145\7:\2\2\u0145A\3\2\2\2")
        buf.write("\u0146\u0147\79\2\2\u0147\u0149\7-\2\2\u0148\u0146\3\2")
        buf.write("\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b")
        buf.write("\7:\2\2\u014b\u014c\7)\2\2\u014c\u014d\5 \21\2\u014d\u014e")
        buf.write("\7*\2\2\u014eC\3\2\2\2\u014f\u0152\5F$\2\u0150\u0152\5")
        buf.write("H%\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152E\3")
        buf.write("\2\2\2\u0153\u0154\7\23\2\2\u0154\u0155\7-\2\2\u0155\u0156")
        buf.write("\t\7\2\2\u0156G\3\2\2\2\u0157\u0158\7\23\2\2\u0158\u0159")
        buf.write("\7-\2\2\u0159\u015a\t\7\2\2\u015a\u015b\7)\2\2\u015b\u015c")
        buf.write("\5 \21\2\u015c\u015d\7*\2\2\u015dI\3\2\2\2\u015e\u0162")
        buf.write("\5L\'\2\u015f\u0162\5R*\2\u0160\u0162\5N(\2\u0161\u015e")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("K\3\2\2\2\u0163\u0164\7\27\2\2\u0164\u0165\79\2\2\u0165")
        buf.write("\u0166\5P)\2\u0166M\3\2\2\2\u0167\u0168\7\27\2\2\u0168")
        buf.write("\u0169\7:\2\2\u0169\u016a\5P)\2\u016aO\3\2\2\2\u016b\u016c")
        buf.write("\7)\2\2\u016c\u016d\5r:\2\u016d\u016e\7*\2\2\u016e\u016f")
        buf.write("\7/\2\2\u016f\u0170\5$\23\2\u0170\u0171\5n8\2\u0171Q\3")
        buf.write("\2\2\2\u0172\u0173\7\27\2\2\u0173\u0174\7\21\2\2\u0174")
        buf.write("\u0175\7)\2\2\u0175\u0176\5r:\2\u0176\u0177\7*\2\2\u0177")
        buf.write("\u0178\5n8\2\u0178S\3\2\2\2\u0179\u017a\t\b\2\2\u017a")
        buf.write("\u017b\5V,\2\u017b\u017c\7\60\2\2\u017cU\3\2\2\2\u017d")
        buf.write("\u0180\5Z.\2\u017e\u0180\5X-\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180W\3\2\2\2\u0181\u0182\5\\/\2\u0182")
        buf.write("\u0183\7/\2\2\u0183\u0184\5&\24\2\u0184Y\3\2\2\2\u0185")
        buf.write("\u0186\t\7\2\2\u0186\u0187\7.\2\2\u0187\u0188\5Z.\2\u0188")
        buf.write("\u0189\7.\2\2\u0189\u018a\5\b\5\2\u018a\u0192\3\2\2\2")
        buf.write("\u018b\u018c\t\7\2\2\u018c\u018d\7/\2\2\u018d\u018e\5")
        buf.write("&\24\2\u018e\u018f\7!\2\2\u018f\u0190\5\b\5\2\u0190\u0192")
        buf.write("\3\2\2\2\u0191\u0185\3\2\2\2\u0191\u018b\3\2\2\2\u0192")
        buf.write("[\3\2\2\2\u0193\u0194\t\7\2\2\u0194\u0195\7.\2\2\u0195")
        buf.write("\u0198\5\\/\2\u0196\u0198\t\7\2\2\u0197\u0193\3\2\2\2")
        buf.write("\u0197\u0196\3\2\2\2\u0198]\3\2\2\2\u0199\u019a\5`\61")
        buf.write("\2\u019a\u019b\7\60\2\2\u019b\u01a4\3\2\2\2\u019c\u01a4")
        buf.write("\5b\62\2\u019d\u01a4\5d\63\2\u019e\u01a4\5f\64\2\u019f")
        buf.write("\u01a4\5h\65\2\u01a0\u01a4\5j\66\2\u01a1\u01a4\5l\67\2")
        buf.write("\u01a2\u01a4\5T+\2\u01a3\u0199\3\2\2\2\u01a3\u019c\3\2")
        buf.write("\2\2\u01a3\u019d\3\2\2\2\u01a3\u019e\3\2\2\2\u01a3\u019f")
        buf.write("\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4_\3\2\2\2\u01a5\u01a6\5\26\f\2\u01a6")
        buf.write("\u01a7\7 \2\2\u01a7\u01a8\5\b\5\2\u01a8a\3\2\2\2\u01a9")
        buf.write("\u01ab\7\7\2\2\u01aa\u01ac\5n8\2\u01ab\u01aa\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\5\b\5\2")
        buf.write("\u01ae\u01b1\5n8\2\u01af\u01b0\7\b\2\2\u01b0\u01b2\5n")
        buf.write("8\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2c\3\2")
        buf.write("\2\2\u01b3\u01b4\7\t\2\2\u01b4\u01b5\5`\61\2\u01b5\u01b6")
        buf.write("\7\60\2\2\u01b6\u01b7\5\b\5\2\u01b7\u01b8\7\60\2\2\u01b8")
        buf.write("\u01b9\5`\61\2\u01b9\u01ba\5n8\2\u01bae\3\2\2\2\u01bb")
        buf.write("\u01bc\7\5\2\2\u01bc\u01bd\7\60\2\2\u01bdg\3\2\2\2\u01be")
        buf.write("\u01bf\7\6\2\2\u01bf\u01c0\7\60\2\2\u01c0i\3\2\2\2\u01c1")
        buf.write("\u01c3\7\16\2\2\u01c2\u01c4\5\b\5\2\u01c3\u01c2\3\2\2")
        buf.write("\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6")
        buf.write("\7\60\2\2\u01c6k\3\2\2\2\u01c7\u01cb\5<\37\2\u01c8\u01cb")
        buf.write("\5B\"\2\u01c9\u01cb\5H%\2\u01ca\u01c7\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("\u01cd\7\60\2\2\u01cdm\3\2\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write("\u01d0\5p9\2\u01d0\u01d1\7\62\2\2\u01d1o\3\2\2\2\u01d2")
        buf.write("\u01d3\5^\60\2\u01d3\u01d4\5p9\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d7\3\2\2\2\u01d6\u01d2\3\2\2\2\u01d6\u01d5\3\2\2\2")
        buf.write("\u01d7q\3\2\2\2\u01d8\u01db\5t;\2\u01d9\u01db\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01dbs\3\2\2")
        buf.write("\2\u01dc\u01dd\5v<\2\u01dd\u01de\7.\2\2\u01de\u01df\5")
        buf.write("t;\2\u01df\u01e2\3\2\2\2\u01e0\u01e2\5v<\2\u01e1\u01dc")
        buf.write("\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2u\3\2\2\2\u01e3\u01e4")
        buf.write("\5\\/\2\u01e4\u01e5\7/\2\2\u01e5\u01e6\5&\24\2\u01e6w")
        buf.write("\3\2\2\2\u01e7\u01e8\7+\2\2\u01e8\u01e9\5 \21\2\u01e9")
        buf.write("\u01ea\7,\2\2\u01eay\3\2\2\2\u01eb\u01ec\5\30\r\2\u01ec")
        buf.write("\u01ed\7+\2\2\u01ed\u01ee\5\b\5\2\u01ee\u01ef\7,\2\2\u01ef")
        buf.write("{\3\2\2\2+\u0083\u0088\u008f\u0096\u00a0\u00ab\u00b6\u00bc")
        buf.write("\u00c1\u00c5\u00d4\u00d6\u00db\u00e5\u00ec\u00f0\u00f7")
        buf.write("\u00fb\u00ff\u010b\u0110\u011b\u011f\u012a\u012f\u013e")
        buf.write("\u0142\u0148\u0151\u0161\u017f\u0191\u0197\u01a3\u01ab")
        buf.write("\u01b1\u01c3\u01ca\u01d6\u01da\u01e1")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'<-'", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'#self'", "'new'", "'void'", "'const'", "'func'", 
                     "'+'", "'-'", "'*'", "'/'", "'!'", "'&&'", "'||'", 
                     "'=='", "':='", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "':'", "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", 
                      "MUL_OP", "DIV_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", 
                      "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
                      "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", 
                      "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", 
                      "SEMICOLON", "LCB", "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", 
                      "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", 
                      "CMT_BLOCK", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_prog_decl_list = 1
    RULE_prog_decl = 2
    RULE_exp = 3
    RULE_exp1 = 4
    RULE_exp2 = 5
    RULE_exp3 = 6
    RULE_exp4 = 7
    RULE_exp5 = 8
    RULE_exp6 = 9
    RULE_exp7 = 10
    RULE_exp8 = 11
    RULE_exp9 = 12
    RULE_exp10 = 13
    RULE_literal = 14
    RULE_exp_list = 15
    RULE_exp_prime = 16
    RULE_func_type = 17
    RULE_ref_type = 18
    RULE_value_type = 19
    RULE_array_type = 20
    RULE_decl = 21
    RULE_class_decl = 22
    RULE_class_mem_list = 23
    RULE_class_mem = 24
    RULE_obj_cre = 25
    RULE_mem_access = 26
    RULE_method_access = 27
    RULE_inst_mem_access = 28
    RULE_inst_method_access = 29
    RULE_static_access = 30
    RULE_static_mem_access = 31
    RULE_static_method_access = 32
    RULE_self_access = 33
    RULE_self_mem_access = 34
    RULE_self_method_access = 35
    RULE_method_decl = 36
    RULE_func_decl = 37
    RULE_static_func_decl = 38
    RULE_expo_func = 39
    RULE_constructor_decl = 40
    RULE_attr_decl = 41
    RULE_attr_decl_body = 42
    RULE_attr_decl_body_short = 43
    RULE_attr_decl_body_full = 44
    RULE_identifier_list = 45
    RULE_stmt = 46
    RULE_assign_stmt = 47
    RULE_if_stmt = 48
    RULE_for_stmt = 49
    RULE_break_stmt = 50
    RULE_continue_stmt = 51
    RULE_return_stmt = 52
    RULE_method_invocation_stmt = 53
    RULE_block_stmt = 54
    RULE_body = 55
    RULE_params_list = 56
    RULE_params_prime = 57
    RULE_params_1_type = 58
    RULE_array_lit = 59
    RULE_arr_ele = 60

    ruleNames =  [ "program", "prog_decl_list", "prog_decl", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "exp9", "exp10", "literal", "exp_list", "exp_prime", 
                   "func_type", "ref_type", "value_type", "array_type", 
                   "decl", "class_decl", "class_mem_list", "class_mem", 
                   "obj_cre", "mem_access", "method_access", "inst_mem_access", 
                   "inst_method_access", "static_access", "static_mem_access", 
                   "static_method_access", "self_access", "self_mem_access", 
                   "self_method_access", "method_decl", "func_decl", "static_func_decl", 
                   "expo_func", "constructor_decl", "attr_decl", "attr_decl_body", 
                   "attr_decl_body_short", "attr_decl_body_full", "identifier_list", 
                   "stmt", "assign_stmt", "if_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "method_invocation_stmt", 
                   "block_stmt", "body", "params_list", "params_prime", 
                   "params_1_type", "array_lit", "arr_ele" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSE=6
    FOR=7
    INT=8
    FLOAT=9
    BOOL=10
    STRING=11
    RETURN=12
    NULL=13
    CLASS=14
    CONSTRUCTOR=15
    VAR=16
    SELF=17
    NEW=18
    VOID=19
    CONST=20
    FUNC=21
    ADD_OP=22
    SUB_OP=23
    MUL_OP=24
    DIV_OP=25
    NOT_OP=26
    AND_OP=27
    OR_OP=28
    EQUAL_OP=29
    ASSIGN_OP=30
    DECL_OP=31
    DIFF_OP=32
    LESS_OP=33
    LESS_EQUAL_OP=34
    GREATER_OP=35
    GREATER_EQUAL_OP=36
    CONCAT_OP=37
    MOD_OP=38
    LP=39
    RP=40
    LSB=41
    RSB=42
    DOT=43
    COMMA=44
    COLON=45
    SEMICOLON=46
    LCB=47
    RCB=48
    SIN_Q=49
    DOU_Q=50
    FLOAT_LIT=51
    INT_LIT=52
    STR_LIT=53
    BOOL_LIT=54
    ID=55
    AT_ID=56
    CMT_LINE=57
    CMT_BLOCK=58
    WS=59
    ERROR_CHAR=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62

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

        def prog_decl_list(self):
            return self.getTypedRuleContext(CSlangParser.Prog_decl_listContext,0)


        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.prog_decl_list()
            self.state = 123
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prog_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog_decl(self):
            return self.getTypedRuleContext(CSlangParser.Prog_declContext,0)


        def prog_decl_list(self):
            return self.getTypedRuleContext(CSlangParser.Prog_decl_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_prog_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg_decl_list" ):
                return visitor.visitProg_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def prog_decl_list(self):

        localctx = CSlangParser.Prog_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog_decl_list)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.prog_decl()
                self.state = 126
                self.prog_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.prog_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prog_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def decl(self):
            return self.getTypedRuleContext(CSlangParser.DeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_prog_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg_decl" ):
                return visitor.visitProg_decl(self)
            else:
                return visitor.visitChildren(self)




    def prog_decl(self):

        localctx = CSlangParser.Prog_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prog_decl)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.decl()
                pass


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


        def CONCAT_OP(self):
            return self.getToken(CSlangParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.exp1()
                self.state = 137
                self.match(CSlangParser.CONCAT_OP)
                self.state = 138
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp2Context,i)


        def EQUAL_OP(self):
            return self.getToken(CSlangParser.EQUAL_OP, 0)

        def DIFF_OP(self):
            return self.getToken(CSlangParser.DIFF_OP, 0)

        def GREATER_OP(self):
            return self.getToken(CSlangParser.GREATER_OP, 0)

        def GREATER_EQUAL_OP(self):
            return self.getToken(CSlangParser.GREATER_EQUAL_OP, 0)

        def LESS_EQUAL_OP(self):
            return self.getToken(CSlangParser.LESS_EQUAL_OP, 0)

        def LESS_OP(self):
            return self.getToken(CSlangParser.LESS_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.exp2(0)
                self.state = 144
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL_OP) | (1 << CSlangParser.DIFF_OP) | (1 << CSlangParser.LESS_OP) | (1 << CSlangParser.LESS_EQUAL_OP) | (1 << CSlangParser.GREATER_OP) | (1 << CSlangParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(CSlangParser.Exp2Context,0)


        def AND_OP(self):
            return self.getToken(CSlangParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(CSlangParser.OR_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 153
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 154
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND_OP or _la==CSlangParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 155
                    self.exp3(0) 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(CSlangParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def ADD_OP(self):
            return self.getToken(CSlangParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 164
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 165
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 166
                    self.exp4(0) 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(CSlangParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(CSlangParser.Exp4Context,0)


        def MUL_OP(self):
            return self.getToken(CSlangParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(CSlangParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(CSlangParser.MOD_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 175
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 176
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 177
                    self.exp5() 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(CSlangParser.NOT_OP, 0)

        def exp5(self):
            return self.getTypedRuleContext(CSlangParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(CSlangParser.Exp6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp5)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(CSlangParser.NOT_OP)
                self.state = 184
                self.exp5()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.exp6()
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def exp6(self):
            return self.getTypedRuleContext(CSlangParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(CSlangParser.Exp7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = CSlangParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp6)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(CSlangParser.SUB_OP)
                self.state = 189
                self.exp6()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_ele(self):
            return self.getTypedRuleContext(CSlangParser.Arr_eleContext,0)


        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = CSlangParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp7)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.exp8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(CSlangParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 200
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 201
                        self.match(CSlangParser.DOT)
                        self.state = 202
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 203
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 204
                        self.match(CSlangParser.DOT)
                        self.state = 205
                        self.match(CSlangParser.ID)
                        self.state = 206
                        self.match(CSlangParser.LP)
                        self.state = 207
                        self.exp_list()
                        self.state = 208
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_accessContext,0)


        def exp10(self):
            return self.getTypedRuleContext(CSlangParser.Exp10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp9)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.static_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj_cre(self):
            return self.getTypedRuleContext(CSlangParser.Obj_creContext,0)


        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def self_mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_mem_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = CSlangParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp10)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.obj_cre()
                pass
            elif token in [CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.literal()
                pass
            elif token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(CSlangParser.LP)

                self.state = 222
                self.exp()
                self.state = 223
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                self.self_mem_access()
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

        def BOOL_LIT(self):
            return self.getToken(CSlangParser.BOOL_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(CSlangParser.Array_litContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.match(CSlangParser.BOOL_LIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.array_lit()
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


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_prime(self):
            return self.getTypedRuleContext(CSlangParser.Exp_primeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = CSlangParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp_list)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.exp_prime()
                pass
            elif token in [CSlangParser.RP, CSlangParser.RSB]:
                self.enterOuterAlt(localctx, 2)

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


    class Exp_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def exp_prime(self):
            return self.getTypedRuleContext(CSlangParser.Exp_primeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_prime" ):
                return visitor.visitExp_prime(self)
            else:
                return visitor.visitChildren(self)




    def exp_prime(self):

        localctx = CSlangParser.Exp_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp_prime)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.exp()
                self.state = 241
                self.match(CSlangParser.COMMA)
                self.state = 242
                self.exp_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_func_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_type" ):
                return visitor.visitFunc_type(self)
            else:
                return visitor.visitChildren(self)




    def func_type(self):

        localctx = CSlangParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_type)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.ref_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(CSlangParser.VOID)
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


    class Ref_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_type(self):
            return self.getTypedRuleContext(CSlangParser.Value_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_ref_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef_type" ):
                return visitor.visitRef_type(self)
            else:
                return visitor.visitChildren(self)




    def ref_type(self):

        localctx = CSlangParser.Ref_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ref_type)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.value_type()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.array_type()
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


    class Value_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_value_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_type" ):
                return visitor.visitValue_type(self)
            else:
                return visitor.visitChildren(self)




    def value_type(self):

        localctx = CSlangParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_value_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def value_type(self):
            return self.getTypedRuleContext(CSlangParser.Value_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(CSlangParser.LSB)
            self.state = 258
            self.match(CSlangParser.INT_LIT)
            self.state = 259
            self.match(CSlangParser.RSB)
            self.state = 260
            self.value_type()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_decl)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
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

        def class_mem_list(self):
            return self.getTypedRuleContext(CSlangParser.Class_mem_listContext,0)


        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(CSlangParser.CLASS)
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(CSlangParser.ID)
                self.state = 269
                self.match(CSlangParser.T__1)


            self.state = 272
            self.match(CSlangParser.ID)
            self.state = 273
            self.match(CSlangParser.LCB)
            self.state = 274
            self.class_mem_list()
            self.state = 275
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_mem_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_mem(self):
            return self.getTypedRuleContext(CSlangParser.Class_memContext,0)


        def class_mem_list(self):
            return self.getTypedRuleContext(CSlangParser.Class_mem_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_mem_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem_list" ):
                return visitor.visitClass_mem_list(self)
            else:
                return visitor.visitChildren(self)




    def class_mem_list(self):

        localctx = CSlangParser.Class_mem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_class_mem_list)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.class_mem()
                self.state = 278
                self.class_mem_list()
                pass
            elif token in [CSlangParser.RCB]:
                self.enterOuterAlt(localctx, 2)

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


    class Class_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(CSlangParser.Method_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem" ):
                return visitor.visitClass_mem(self)
            else:
                return visitor.visitChildren(self)




    def class_mem(self):

        localctx = CSlangParser.Class_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_class_mem)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
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


    class Obj_creContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_obj_cre

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_cre" ):
                return visitor.visitObj_cre(self)
            else:
                return visitor.visitChildren(self)




    def obj_cre(self):

        localctx = CSlangParser.Obj_creContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_obj_cre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(CSlangParser.NEW)
            self.state = 288
            self.match(CSlangParser.ID)
            self.state = 289
            self.match(CSlangParser.LP)
            self.state = 290
            self.exp_list()
            self.state = 291
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inst_mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Inst_mem_accessContext,0)


        def static_mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_mem_accessContext,0)


        def self_mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_mem_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_mem_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem_access" ):
                return visitor.visitMem_access(self)
            else:
                return visitor.visitChildren(self)




    def mem_access(self):

        localctx = CSlangParser.Mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_mem_access)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.inst_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.static_mem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.self_mem_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inst_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Inst_method_accessContext,0)


        def static_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_accessContext,0)


        def self_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_method_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_access" ):
                return visitor.visitMethod_access(self)
            else:
                return visitor.visitChildren(self)




    def method_access(self):

        localctx = CSlangParser.Method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_access)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.inst_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.static_method_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 300
                self.self_method_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_mem_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_inst_mem_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_mem_access" ):
                return visitor.visitInst_mem_access(self)
            else:
                return visitor.visitChildren(self)




    def inst_mem_access(self):

        localctx = CSlangParser.Inst_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_inst_mem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.exp8(0)
            self.state = 304
            self.match(CSlangParser.DOT)
            self.state = 305
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_method_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_inst_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_method_access" ):
                return visitor.visitInst_method_access(self)
            else:
                return visitor.visitChildren(self)




    def inst_method_access(self):

        localctx = CSlangParser.Inst_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_inst_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.exp8(0)
            self.state = 308
            self.match(CSlangParser.DOT)
            self.state = 309
            self.match(CSlangParser.ID)
            self.state = 310
            self.match(CSlangParser.LP)
            self.state = 311
            self.exp_list()
            self.state = 312
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_mem_accessContext,0)


        def static_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_access" ):
                return visitor.visitStatic_access(self)
            else:
                return visitor.visitChildren(self)




    def static_access(self):

        localctx = CSlangParser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_static_access)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.static_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.static_method_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_mem_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_mem_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_mem_access" ):
                return visitor.visitStatic_mem_access(self)
            else:
                return visitor.visitChildren(self)




    def static_mem_access(self):

        localctx = CSlangParser.Static_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 318
                self.match(CSlangParser.ID)
                self.state = 319
                self.match(CSlangParser.DOT)


            self.state = 322
            self.match(CSlangParser.AT_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_access" ):
                return visitor.visitStatic_method_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_access(self):

        localctx = CSlangParser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 324
                self.match(CSlangParser.ID)
                self.state = 325
                self.match(CSlangParser.DOT)


            self.state = 328
            self.match(CSlangParser.AT_ID)
            self.state = 329
            self.match(CSlangParser.LP)
            self.state = 330
            self.exp_list()
            self.state = 331
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Self_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def self_mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_mem_accessContext,0)


        def self_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_method_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_self_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_access" ):
                return visitor.visitSelf_access(self)
            else:
                return visitor.visitChildren(self)




    def self_access(self):

        localctx = CSlangParser.Self_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_self_access)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.self_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.self_method_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Self_mem_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_self_mem_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_mem_access" ):
                return visitor.visitSelf_mem_access(self)
            else:
                return visitor.visitChildren(self)




    def self_mem_access(self):

        localctx = CSlangParser.Self_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_self_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(CSlangParser.SELF)
            self.state = 338
            self.match(CSlangParser.DOT)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
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


    class Self_method_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_self_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_method_access" ):
                return visitor.visitSelf_method_access(self)
            else:
                return visitor.visitChildren(self)




    def self_method_access(self):

        localctx = CSlangParser.Self_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_self_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(CSlangParser.SELF)
            self.state = 342
            self.match(CSlangParser.DOT)
            self.state = 343
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 344
            self.match(CSlangParser.LP)
            self.state = 345
            self.exp_list()
            self.state = 346
            self.match(CSlangParser.RP)
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


        def getRuleIndex(self):
            return CSlangParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = CSlangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_decl)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.static_func_decl()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = CSlangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(CSlangParser.FUNC)
            self.state = 354
            self.match(CSlangParser.ID)
            self.state = 355
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_func_decl" ):
                return visitor.visitStatic_func_decl(self)
            else:
                return visitor.visitChildren(self)




    def static_func_decl(self):

        localctx = CSlangParser.Static_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_static_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(CSlangParser.FUNC)
            self.state = 358
            self.match(CSlangParser.AT_ID)
            self.state = 359
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

        def params_list(self):
            return self.getTypedRuleContext(CSlangParser.Params_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def func_type(self):
            return self.getTypedRuleContext(CSlangParser.Func_typeContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expo_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpo_func" ):
                return visitor.visitExpo_func(self)
            else:
                return visitor.visitChildren(self)




    def expo_func(self):

        localctx = CSlangParser.Expo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expo_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(CSlangParser.LP)
            self.state = 362
            self.params_list()
            self.state = 363
            self.match(CSlangParser.RP)
            self.state = 364
            self.match(CSlangParser.COLON)
            self.state = 365
            self.func_type()
            self.state = 366
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

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def params_list(self):
            return self.getTypedRuleContext(CSlangParser.Params_listContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(CSlangParser.FUNC)
            self.state = 369
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 370
            self.match(CSlangParser.LP)
            self.state = 371
            self.params_list()
            self.state = 372
            self.match(CSlangParser.RP)
            self.state = 373
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

        def attr_decl_body(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_bodyContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = CSlangParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 376
            self.attr_decl_body()
            self.state = 377
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl_body_full(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_body_fullContext,0)


        def attr_decl_body_short(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_body_shortContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_body" ):
                return visitor.visitAttr_decl_body(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_body(self):

        localctx = CSlangParser.Attr_decl_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_attr_decl_body)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.attr_decl_body_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.attr_decl_body_short()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_body_shortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_body_short

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_body_short" ):
                return visitor.visitAttr_decl_body_short(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_body_short(self):

        localctx = CSlangParser.Attr_decl_body_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_attr_decl_body_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.identifier_list()
            self.state = 384
            self.match(CSlangParser.COLON)
            self.state = 385
            self.ref_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_body_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def attr_decl_body_full(self):
            return self.getTypedRuleContext(CSlangParser.Attr_decl_body_fullContext,0)


        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def DECL_OP(self):
            return self.getToken(CSlangParser.DECL_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_body_full

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_body_full" ):
                return visitor.visitAttr_decl_body_full(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_body_full(self):

        localctx = CSlangParser.Attr_decl_body_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_attr_decl_body_full)
        self._la = 0 # Token type
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 388
                self.match(CSlangParser.COMMA)
                self.state = 389
                self.attr_decl_body_full()
                self.state = 390
                self.match(CSlangParser.COMMA)
                self.state = 391
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 394
                self.match(CSlangParser.COLON)
                self.state = 395
                self.ref_type()
                self.state = 396
                self.match(CSlangParser.DECL_OP)
                self.state = 397
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_listContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = CSlangParser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 402
                self.match(CSlangParser.COMMA)
                self.state = 403
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(CSlangParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CSlangParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocation_stmtContext,0)


        def attr_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attr_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmt)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.assign_stmt()
                self.state = 408
                self.match(CSlangParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 414
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 415
                self.method_invocation_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 416
                self.attr_decl()
                pass


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

        def exp7(self):
            return self.getTypedRuleContext(CSlangParser.Exp7Context,0)


        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.exp7()
            self.state = 420
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 421
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_stmtContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(CSlangParser.IF)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 424
                self.block_stmt()


            self.state = 427
            self.exp()
            self.state = 428
            self.block_stmt()
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 429
                self.match(CSlangParser.ELSE)
                self.state = 430
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMICOLON)
            else:
                return self.getToken(CSlangParser.SEMICOLON, i)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(CSlangParser.FOR)
            self.state = 434
            self.assign_stmt()
            self.state = 435
            self.match(CSlangParser.SEMICOLON)
            self.state = 436
            self.exp()
            self.state = 437
            self.match(CSlangParser.SEMICOLON)
            self.state = 438
            self.assign_stmt()
            self.state = 439
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(CSlangParser.BREAK)
            self.state = 442
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(CSlangParser.CONTINUE)
            self.state = 445
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(CSlangParser.RETURN)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 448
                self.exp()


            self.state = 451
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def inst_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Inst_method_accessContext,0)


        def static_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_accessContext,0)


        def self_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_method_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 453
                self.inst_method_access()
                pass

            elif la_ == 2:
                self.state = 454
                self.static_method_access()
                pass

            elif la_ == 3:
                self.state = 455
                self.self_method_access()
                pass


            self.state = 458
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

        def body(self):
            return self.getTypedRuleContext(CSlangParser.BodyContext,0)


        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(CSlangParser.LCB)
            self.state = 461
            self.body()
            self.state = 462
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def body(self):
            return self.getTypedRuleContext(CSlangParser.BodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = CSlangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_body)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.stmt()
                self.state = 465
                self.body()
                pass
            elif token in [CSlangParser.RCB]:
                self.enterOuterAlt(localctx, 2)

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


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_prime(self):
            return self.getTypedRuleContext(CSlangParser.Params_primeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = CSlangParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_params_list)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.params_prime()
                pass
            elif token in [CSlangParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Params_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_1_type(self):
            return self.getTypedRuleContext(CSlangParser.Params_1_typeContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def params_prime(self):
            return self.getTypedRuleContext(CSlangParser.Params_primeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_prime" ):
                return visitor.visitParams_prime(self)
            else:
                return visitor.visitChildren(self)




    def params_prime(self):

        localctx = CSlangParser.Params_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_params_prime)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.params_1_type()
                self.state = 475
                self.match(CSlangParser.COMMA)
                self.state = 476
                self.params_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.params_1_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_1_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params_1_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_1_type" ):
                return visitor.visitParams_1_type(self)
            else:
                return visitor.visitChildren(self)




    def params_1_type(self):

        localctx = CSlangParser.Params_1_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_params_1_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.identifier_list()
            self.state = 482
            self.match(CSlangParser.COLON)
            self.state = 483
            self.ref_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = CSlangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(CSlangParser.LSB)
            self.state = 486
            self.exp_list()
            self.state = 487
            self.match(CSlangParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arr_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_ele" ):
                return visitor.visitArr_ele(self)
            else:
                return visitor.visitChildren(self)




    def arr_ele(self):

        localctx = CSlangParser.Arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.exp8(0)
            self.state = 490
            self.match(CSlangParser.LSB)
            self.state = 491
            self.exp()
            self.state = 492
            self.match(CSlangParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.exp2_sempred
        self._predicates[6] = self.exp3_sempred
        self._predicates[7] = self.exp4_sempred
        self._predicates[11] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




