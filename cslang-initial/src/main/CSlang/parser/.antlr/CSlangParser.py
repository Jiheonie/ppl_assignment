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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u020a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u008a\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u0091")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\5\5\u0098\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\7\6\u00a0\n\6\f\6\16\6\u00a3\13\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\7\7\u00ab\n\7\f\7\16\7\u00ae\13\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\7\b\u00b6\n\b\f\b\16\b\u00b9\13\b\3\t")
        buf.write("\3\t\3\t\5\t\u00be\n\t\3\n\3\n\3\n\5\n\u00c3\n\n\3\13")
        buf.write("\3\13\5\13\u00c7\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\7\f\u00d6\n\f\f\f\16\f\u00d9\13\f")
        buf.write("\3\r\3\r\5\r\u00dd\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00e8\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00ef\n\17\3\20\3\20\5\20\u00f3\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u00fa\n\21\3\22\3\22\5\22\u00fe\n\22")
        buf.write("\3\23\3\23\5\23\u0102\n\23\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\5\26\u010d\n\26\3\27\3\27\3\27\5\27")
        buf.write("\u0112\n\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u0123\n\31\3\32")
        buf.write("\3\32\5\32\u0127\n\32\3\33\3\33\3\33\3\33\5\33\u012d\n")
        buf.write("\33\3\34\3\34\5\34\u0131\n\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\5\36\u013c\n\36\3\37\3\37\3\37\5")
        buf.write("\37\u0141\n\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\5\"\u0150\n\"\3#\3#\5#\u0154\n#\3#\3#\3$\3$\5$\u015a")
        buf.write("\n$\3$\3$\3$\3$\3$\3%\3%\5%\u0163\n%\3&\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u0173\n(\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\5/\u0199\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\5\61\u01ab\n\61\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01b1\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\5\63\u01bd\n\63\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\5\65\u01c5\n\65\3\65\3\65\3\65\3\65\5")
        buf.write("\65\u01cb\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\39\39\59\u01dd\n9\39\39\3:\3")
        buf.write(":\3:\5:\u01e4\n:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\5<\u01f0")
        buf.write("\n<\3=\3=\5=\u01f4\n=\3>\3>\3>\3>\3>\5>\u01fb\n>\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\2\6\n\f\16\26B\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\2\t\4\2")
        buf.write("!!$(\3\2\37 \3\2\32\33\5\2\3\3\34\35**\3\2\f\17\3\2;<")
        buf.write("\4\2\24\24\30\30\2\u0204\2\u0082\3\2\2\2\4\u0089\3\2\2")
        buf.write("\2\6\u0090\3\2\2\2\b\u0097\3\2\2\2\n\u0099\3\2\2\2\f\u00a4")
        buf.write("\3\2\2\2\16\u00af\3\2\2\2\20\u00bd\3\2\2\2\22\u00c2\3")
        buf.write("\2\2\2\24\u00c6\3\2\2\2\26\u00c8\3\2\2\2\30\u00dc\3\2")
        buf.write("\2\2\32\u00e7\3\2\2\2\34\u00ee\3\2\2\2\36\u00f2\3\2\2")
        buf.write("\2 \u00f9\3\2\2\2\"\u00fd\3\2\2\2$\u0101\3\2\2\2&\u0103")
        buf.write("\3\2\2\2(\u0105\3\2\2\2*\u010c\3\2\2\2,\u010e\3\2\2\2")
        buf.write(".\u0118\3\2\2\2\60\u0122\3\2\2\2\62\u0126\3\2\2\2\64\u012c")
        buf.write("\3\2\2\2\66\u0130\3\2\2\28\u0132\3\2\2\2:\u013b\3\2\2")
        buf.write("\2<\u0140\3\2\2\2>\u0142\3\2\2\2@\u0146\3\2\2\2B\u014f")
        buf.write("\3\2\2\2D\u0153\3\2\2\2F\u0159\3\2\2\2H\u0162\3\2\2\2")
        buf.write("J\u0164\3\2\2\2L\u0168\3\2\2\2N\u0172\3\2\2\2P\u0174\3")
        buf.write("\2\2\2R\u0178\3\2\2\2T\u017c\3\2\2\2V\u0183\3\2\2\2X\u018b")
        buf.write("\3\2\2\2Z\u0192\3\2\2\2\\\u0198\3\2\2\2^\u019a\3\2\2\2")
        buf.write("`\u01aa\3\2\2\2b\u01b0\3\2\2\2d\u01bc\3\2\2\2f\u01be\3")
        buf.write("\2\2\2h\u01c2\3\2\2\2j\u01cc\3\2\2\2l\u01d4\3\2\2\2n\u01d7")
        buf.write("\3\2\2\2p\u01da\3\2\2\2r\u01e3\3\2\2\2t\u01e7\3\2\2\2")
        buf.write("v\u01ef\3\2\2\2x\u01f3\3\2\2\2z\u01fa\3\2\2\2|\u01fc\3")
        buf.write("\2\2\2~\u0200\3\2\2\2\u0080\u0204\3\2\2\2\u0082\u0083")
        buf.write("\5\4\3\2\u0083\u0084\7\2\2\3\u0084\3\3\2\2\2\u0085\u0086")
        buf.write("\5*\26\2\u0086\u0087\5\4\3\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u008a\5*\26\2\u0089\u0085\3\2\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\5\3\2\2\2\u008b\u008c\5\b\5\2\u008c\u008d\7)\2")
        buf.write("\2\u008d\u008e\5\b\5\2\u008e\u0091\3\2\2\2\u008f\u0091")
        buf.write("\5\b\5\2\u0090\u008b\3\2\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\7\3\2\2\2\u0092\u0093\5\n\6\2\u0093\u0094\t\2\2\2\u0094")
        buf.write("\u0095\5\n\6\2\u0095\u0098\3\2\2\2\u0096\u0098\5\n\6\2")
        buf.write("\u0097\u0092\3\2\2\2\u0097\u0096\3\2\2\2\u0098\t\3\2\2")
        buf.write("\2\u0099\u009a\b\6\1\2\u009a\u009b\5\f\7\2\u009b\u00a1")
        buf.write("\3\2\2\2\u009c\u009d\f\4\2\2\u009d\u009e\t\3\2\2\u009e")
        buf.write("\u00a0\5\f\7\2\u009f\u009c\3\2\2\2\u00a0\u00a3\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\13\3\2")
        buf.write("\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\b\7\1\2\u00a5\u00a6")
        buf.write("\5\16\b\2\u00a6\u00ac\3\2\2\2\u00a7\u00a8\f\4\2\2\u00a8")
        buf.write("\u00a9\t\4\2\2\u00a9\u00ab\5\16\b\2\u00aa\u00a7\3\2\2")
        buf.write("\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\r\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0")
        buf.write("\b\b\1\2\u00b0\u00b1\5\20\t\2\u00b1\u00b7\3\2\2\2\u00b2")
        buf.write("\u00b3\f\4\2\2\u00b3\u00b4\t\5\2\2\u00b4\u00b6\5\20\t")
        buf.write("\2\u00b5\u00b2\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\17\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00ba\u00bb\7\36\2\2\u00bb\u00be\5\20\t\2\u00bc")
        buf.write("\u00be\5\22\n\2\u00bd\u00ba\3\2\2\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00be\21\3\2\2\2\u00bf\u00c0\7\33\2\2\u00c0\u00c3\5")
        buf.write("\22\n\2\u00c1\u00c3\5\24\13\2\u00c2\u00bf\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\23\3\2\2\2\u00c4\u00c7\5\u0080A\2")
        buf.write("\u00c5\u00c7\5\26\f\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\25\3\2\2\2\u00c8\u00c9\b\f\1\2\u00c9\u00ca")
        buf.write("\5\30\r\2\u00ca\u00d7\3\2\2\2\u00cb\u00cc\f\5\2\2\u00cc")
        buf.write("\u00cd\7/\2\2\u00cd\u00d6\7;\2\2\u00ce\u00cf\f\4\2\2\u00cf")
        buf.write("\u00d0\7/\2\2\u00d0\u00d1\7;\2\2\u00d1\u00d2\7+\2\2\u00d2")
        buf.write("\u00d3\5\36\20\2\u00d3\u00d4\7,\2\2\u00d4\u00d6\3\2\2")
        buf.write("\2\u00d5\u00cb\3\2\2\2\u00d5\u00ce\3\2\2\2\u00d6\u00d9")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\27\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dd\5B\"\2\u00db")
        buf.write("\u00dd\5\32\16\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2")
        buf.write("\2\u00dd\31\3\2\2\2\u00de\u00e8\58\35\2\u00df\u00e8\5")
        buf.write("\34\17\2\u00e0\u00e1\7+\2\2\u00e1\u00e2\5\6\4\2\u00e2")
        buf.write("\u00e3\7,\2\2\u00e3\u00e8\3\2\2\2\u00e4\u00e8\7;\2\2\u00e5")
        buf.write("\u00e8\5J&\2\u00e6\u00e8\7\21\2\2\u00e7\u00de\3\2\2\2")
        buf.write("\u00e7\u00df\3\2\2\2\u00e7\u00e0\3\2\2\2\u00e7\u00e4\3")
        buf.write("\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\33")
        buf.write("\3\2\2\2\u00e9\u00ef\78\2\2\u00ea\u00ef\7\67\2\2\u00eb")
        buf.write("\u00ef\79\2\2\u00ec\u00ef\7:\2\2\u00ed\u00ef\5~@\2\u00ee")
        buf.write("\u00e9\3\2\2\2\u00ee\u00ea\3\2\2\2\u00ee\u00eb\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\35\3\2")
        buf.write("\2\2\u00f0\u00f3\5 \21\2\u00f1\u00f3\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\37\3\2\2\2\u00f4\u00f5")
        buf.write("\5\6\4\2\u00f5\u00f6\7\60\2\2\u00f6\u00f7\5 \21\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00fa\5\6\4\2\u00f9\u00f4\3\2\2\2")
        buf.write("\u00f9\u00f8\3\2\2\2\u00fa!\3\2\2\2\u00fb\u00fe\5$\23")
        buf.write("\2\u00fc\u00fe\7\27\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fe#\3\2\2\2\u00ff\u0102\5&\24\2\u0100\u0102")
        buf.write("\5(\25\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("%\3\2\2\2\u0103\u0104\t\6\2\2\u0104\'\3\2\2\2\u0105\u0106")
        buf.write("\7-\2\2\u0106\u0107\78\2\2\u0107\u0108\7.\2\2\u0108\u0109")
        buf.write("\5&\24\2\u0109)\3\2\2\2\u010a\u010d\5,\27\2\u010b\u010d")
        buf.write("\5.\30\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("+\3\2\2\2\u010e\u0111\7\22\2\2\u010f\u0110\7;\2\2\u0110")
        buf.write("\u0112\7\4\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0114\7;\2\2\u0114\u0115\7")
        buf.write("\63\2\2\u0115\u0116\5\60\31\2\u0116\u0117\7\64\2\2\u0117")
        buf.write("-\3\2\2\2\u0118\u0119\7\22\2\2\u0119\u011a\7\5\2\2\u011a")
        buf.write("\u011b\7\63\2\2\u011b\u011c\5\64\33\2\u011c\u011d\7\64")
        buf.write("\2\2\u011d/\3\2\2\2\u011e\u011f\5\62\32\2\u011f\u0120")
        buf.write("\5\60\31\2\u0120\u0123\3\2\2\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u011e\3\2\2\2\u0122\u0121\3\2\2\2\u0123\61\3\2\2\2\u0124")
        buf.write("\u0127\5Z.\2\u0125\u0127\5N(\2\u0126\u0124\3\2\2\2\u0126")
        buf.write("\u0125\3\2\2\2\u0127\63\3\2\2\2\u0128\u0129\5\66\34\2")
        buf.write("\u0129\u012a\5\64\33\2\u012a\u012d\3\2\2\2\u012b\u012d")
        buf.write("\3\2\2\2\u012c\u0128\3\2\2\2\u012c\u012b\3\2\2\2\u012d")
        buf.write("\65\3\2\2\2\u012e\u0131\5\62\32\2\u012f\u0131\5V,\2\u0130")
        buf.write("\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131\67\3\2\2\2\u0132")
        buf.write("\u0133\7\26\2\2\u0133\u0134\7;\2\2\u0134\u0135\7+\2\2")
        buf.write("\u0135\u0136\5\36\20\2\u0136\u0137\7,\2\2\u01379\3\2\2")
        buf.write("\2\u0138\u013c\5> \2\u0139\u013c\5D#\2\u013a\u013c\5J")
        buf.write("&\2\u013b\u0138\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013a")
        buf.write("\3\2\2\2\u013c;\3\2\2\2\u013d\u0141\5@!\2\u013e\u0141")
        buf.write("\5F$\2\u013f\u0141\5L\'\2\u0140\u013d\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0140\u013f\3\2\2\2\u0141=\3\2\2\2\u0142\u0143")
        buf.write("\5\26\f\2\u0143\u0144\7/\2\2\u0144\u0145\7;\2\2\u0145")
        buf.write("?\3\2\2\2\u0146\u0147\5\26\f\2\u0147\u0148\7/\2\2\u0148")
        buf.write("\u0149\7;\2\2\u0149\u014a\7+\2\2\u014a\u014b\5\36\20\2")
        buf.write("\u014b\u014c\7,\2\2\u014cA\3\2\2\2\u014d\u0150\5D#\2\u014e")
        buf.write("\u0150\5F$\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("C\3\2\2\2\u0151\u0152\7;\2\2\u0152\u0154\7/\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155\u0156\7<\2\2\u0156E\3\2\2\2\u0157\u0158\7;\2\2")
        buf.write("\u0158\u015a\7/\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3")
        buf.write("\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\7<\2\2\u015c\u015d")
        buf.write("\7+\2\2\u015d\u015e\5\36\20\2\u015e\u015f\7,\2\2\u015f")
        buf.write("G\3\2\2\2\u0160\u0163\5J&\2\u0161\u0163\5L\'\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0161\3\2\2\2\u0163I\3\2\2\2\u0164\u0165")
        buf.write("\7\25\2\2\u0165\u0166\7/\2\2\u0166\u0167\t\7\2\2\u0167")
        buf.write("K\3\2\2\2\u0168\u0169\7\25\2\2\u0169\u016a\7/\2\2\u016a")
        buf.write("\u016b\t\7\2\2\u016b\u016c\7+\2\2\u016c\u016d\5\36\20")
        buf.write("\2\u016d\u016e\7,\2\2\u016eM\3\2\2\2\u016f\u0173\5P)\2")
        buf.write("\u0170\u0173\5X-\2\u0171\u0173\5R*\2\u0172\u016f\3\2\2")
        buf.write("\2\u0172\u0170\3\2\2\2\u0172\u0171\3\2\2\2\u0173O\3\2")
        buf.write("\2\2\u0174\u0175\7\31\2\2\u0175\u0176\7;\2\2\u0176\u0177")
        buf.write("\5T+\2\u0177Q\3\2\2\2\u0178\u0179\7\31\2\2\u0179\u017a")
        buf.write("\7<\2\2\u017a\u017b\5T+\2\u017bS\3\2\2\2\u017c\u017d\7")
        buf.write("+\2\2\u017d\u017e\5x=\2\u017e\u017f\7,\2\2\u017f\u0180")
        buf.write("\7\61\2\2\u0180\u0181\5\"\22\2\u0181\u0182\5t;\2\u0182")
        buf.write("U\3\2\2\2\u0183\u0184\7\31\2\2\u0184\u0185\7\6\2\2\u0185")
        buf.write("\u0186\7+\2\2\u0186\u0187\7,\2\2\u0187\u0188\7\61\2\2")
        buf.write("\u0188\u0189\7\27\2\2\u0189\u018a\5t;\2\u018aW\3\2\2\2")
        buf.write("\u018b\u018c\7\31\2\2\u018c\u018d\7\23\2\2\u018d\u018e")
        buf.write("\7+\2\2\u018e\u018f\5x=\2\u018f\u0190\7,\2\2\u0190\u0191")
        buf.write("\5t;\2\u0191Y\3\2\2\2\u0192\u0193\t\b\2\2\u0193\u0194")
        buf.write("\5\\/\2\u0194\u0195\7\62\2\2\u0195[\3\2\2\2\u0196\u0199")
        buf.write("\5`\61\2\u0197\u0199\5^\60\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199]\3\2\2\2\u019a\u019b\5b\62\2\u019b")
        buf.write("\u019c\7\61\2\2\u019c\u019d\5$\23\2\u019d_\3\2\2\2\u019e")
        buf.write("\u019f\t\7\2\2\u019f\u01a0\7\60\2\2\u01a0\u01a1\5`\61")
        buf.write("\2\u01a1\u01a2\7\60\2\2\u01a2\u01a3\5\6\4\2\u01a3\u01ab")
        buf.write("\3\2\2\2\u01a4\u01a5\t\7\2\2\u01a5\u01a6\7\61\2\2\u01a6")
        buf.write("\u01a7\5$\23\2\u01a7\u01a8\7#\2\2\u01a8\u01a9\5\6\4\2")
        buf.write("\u01a9\u01ab\3\2\2\2\u01aa\u019e\3\2\2\2\u01aa\u01a4\3")
        buf.write("\2\2\2\u01aba\3\2\2\2\u01ac\u01ad\t\7\2\2\u01ad\u01ae")
        buf.write("\7\60\2\2\u01ae\u01b1\5b\62\2\u01af\u01b1\t\7\2\2\u01b0")
        buf.write("\u01ac\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1c\3\2\2\2\u01b2")
        buf.write("\u01b3\5f\64\2\u01b3\u01b4\7\62\2\2\u01b4\u01bd\3\2\2")
        buf.write("\2\u01b5\u01bd\5h\65\2\u01b6\u01bd\5j\66\2\u01b7\u01bd")
        buf.write("\5l\67\2\u01b8\u01bd\5n8\2\u01b9\u01bd\5p9\2\u01ba\u01bd")
        buf.write("\5r:\2\u01bb\u01bd\5Z.\2\u01bc\u01b2\3\2\2\2\u01bc\u01b5")
        buf.write("\3\2\2\2\u01bc\u01b6\3\2\2\2\u01bc\u01b7\3\2\2\2\u01bc")
        buf.write("\u01b8\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bc\u01bb\3\2\2\2\u01bde\3\2\2\2\u01be\u01bf\5\24\13")
        buf.write("\2\u01bf\u01c0\7\"\2\2\u01c0\u01c1\5\6\4\2\u01c1g\3\2")
        buf.write("\2\2\u01c2\u01c4\7\t\2\2\u01c3\u01c5\5t;\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\5\6\4\2\u01c7\u01ca\5t;\2\u01c8\u01c9\7\n\2\2\u01c9")
        buf.write("\u01cb\5t;\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("i\3\2\2\2\u01cc\u01cd\7\13\2\2\u01cd\u01ce\5f\64\2\u01ce")
        buf.write("\u01cf\7\62\2\2\u01cf\u01d0\5\6\4\2\u01d0\u01d1\7\62\2")
        buf.write("\2\u01d1\u01d2\5f\64\2\u01d2\u01d3\5t;\2\u01d3k\3\2\2")
        buf.write("\2\u01d4\u01d5\7\7\2\2\u01d5\u01d6\7\62\2\2\u01d6m\3\2")
        buf.write("\2\2\u01d7\u01d8\7\b\2\2\u01d8\u01d9\7\62\2\2\u01d9o\3")
        buf.write("\2\2\2\u01da\u01dc\7\20\2\2\u01db\u01dd\5\6\4\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01df\7\62\2\2\u01dfq\3\2\2\2\u01e0\u01e4\5@!\2")
        buf.write("\u01e1\u01e4\5F$\2\u01e2\u01e4\5L\'\2\u01e3\u01e0\3\2")
        buf.write("\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e5\u01e6\7\62\2\2\u01e6s\3\2\2\2\u01e7\u01e8")
        buf.write("\7\63\2\2\u01e8\u01e9\5v<\2\u01e9\u01ea\7\64\2\2\u01ea")
        buf.write("u\3\2\2\2\u01eb\u01ec\5d\63\2\u01ec\u01ed\5v<\2\u01ed")
        buf.write("\u01f0\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01eb\3\2\2\2")
        buf.write("\u01ef\u01ee\3\2\2\2\u01f0w\3\2\2\2\u01f1\u01f4\5z>\2")
        buf.write("\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3")
        buf.write("\2\2\2\u01f4y\3\2\2\2\u01f5\u01f6\5|?\2\u01f6\u01f7\7")
        buf.write("\60\2\2\u01f7\u01f8\5z>\2\u01f8\u01fb\3\2\2\2\u01f9\u01fb")
        buf.write("\5|?\2\u01fa\u01f5\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb{")
        buf.write("\3\2\2\2\u01fc\u01fd\5b\62\2\u01fd\u01fe\7\61\2\2\u01fe")
        buf.write("\u01ff\5$\23\2\u01ff}\3\2\2\2\u0200\u0201\7-\2\2\u0201")
        buf.write("\u0202\5\36\20\2\u0202\u0203\7.\2\2\u0203\177\3\2\2\2")
        buf.write("\u0204\u0205\5\26\f\2\u0205\u0206\7-\2\2\u0206\u0207\5")
        buf.write("\6\4\2\u0207\u0208\7.\2\2\u0208\u0081\3\2\2\2,\u0089\u0090")
        buf.write("\u0097\u00a1\u00ac\u00b7\u00bd\u00c2\u00c6\u00d5\u00d7")
        buf.write("\u00dc\u00e7\u00ee\u00f2\u00f9\u00fd\u0101\u010c\u0111")
        buf.write("\u0122\u0126\u012c\u0130\u013b\u0140\u014f\u0153\u0159")
        buf.write("\u0162\u0172\u0198\u01aa\u01b0\u01bc\u01c4\u01ca\u01dc")
        buf.write("\u01e3\u01ef\u01f3\u01fa")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'<-'", "'Program'", "'@main'", 
                     "'break'", "'continue'", "'if'", "'else'", "'for'", 
                     "'int'", "'float'", "'bool'", "'string'", "'return'", 
                     "'null'", "'class'", "'constructor'", "'var'", "'self'", 
                     "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", 
                     "'*'", "'/'", "'!'", "'&&'", "'||'", "'=='", "':='", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", 
                     "'%'", "'('", "')'", "'['", "']'", "'.'", "','", "':'", 
                     "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAM_CLASS", 
                      "MAIN", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                      "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                      "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                      "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
                      "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
                      "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", 
                      "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", 
                      "SEMICOLON", "LCB", "RCB", "SIN_Q", "DOU_Q", "FLOAT_LIT", 
                      "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", 
                      "CMT_BLOCK", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_prog_decl_list = 1
    RULE_exp = 2
    RULE_exp1 = 3
    RULE_exp2 = 4
    RULE_exp3 = 5
    RULE_exp4 = 6
    RULE_exp5 = 7
    RULE_exp6 = 8
    RULE_exp7 = 9
    RULE_exp8 = 10
    RULE_exp9 = 11
    RULE_exp10 = 12
    RULE_literal = 13
    RULE_exp_list = 14
    RULE_exp_prime = 15
    RULE_func_type = 16
    RULE_ref_type = 17
    RULE_ele_type = 18
    RULE_array_type = 19
    RULE_prog_decl = 20
    RULE_class_decl = 21
    RULE_program_class_decl = 22
    RULE_class_mem_list = 23
    RULE_class_mem = 24
    RULE_prog_class_mem_list = 25
    RULE_prog_class_mem = 26
    RULE_obj_cre = 27
    RULE_mem_access = 28
    RULE_method_access = 29
    RULE_inst_mem_access = 30
    RULE_inst_method_access = 31
    RULE_static_access = 32
    RULE_static_mem_access = 33
    RULE_static_method_access = 34
    RULE_self_access = 35
    RULE_self_mem_access = 36
    RULE_self_method_access = 37
    RULE_method_decl = 38
    RULE_func_decl = 39
    RULE_static_func_decl = 40
    RULE_expo_func = 41
    RULE_main_func_decl = 42
    RULE_constructor_decl = 43
    RULE_attr_decl = 44
    RULE_attr_decl_body = 45
    RULE_attr_decl_body_short = 46
    RULE_attr_decl_body_full = 47
    RULE_identifier_list = 48
    RULE_stmt = 49
    RULE_assign_stmt = 50
    RULE_if_stmt = 51
    RULE_for_stmt = 52
    RULE_break_stmt = 53
    RULE_continue_stmt = 54
    RULE_return_stmt = 55
    RULE_method_invocation_stmt = 56
    RULE_block_stmt = 57
    RULE_body = 58
    RULE_params_list = 59
    RULE_params_prime = 60
    RULE_params_1_type = 61
    RULE_array_lit = 62
    RULE_arr_ele = 63

    ruleNames =  [ "program", "prog_decl_list", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", 
                   "literal", "exp_list", "exp_prime", "func_type", "ref_type", 
                   "ele_type", "array_type", "prog_decl", "class_decl", 
                   "program_class_decl", "class_mem_list", "class_mem", 
                   "prog_class_mem_list", "prog_class_mem", "obj_cre", "mem_access", 
                   "method_access", "inst_mem_access", "inst_method_access", 
                   "static_access", "static_mem_access", "static_method_access", 
                   "self_access", "self_mem_access", "self_method_access", 
                   "method_decl", "func_decl", "static_func_decl", "expo_func", 
                   "main_func_decl", "constructor_decl", "attr_decl", "attr_decl_body", 
                   "attr_decl_body_short", "attr_decl_body_full", "identifier_list", 
                   "stmt", "assign_stmt", "if_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "method_invocation_stmt", 
                   "block_stmt", "body", "params_list", "params_prime", 
                   "params_1_type", "array_lit", "arr_ele" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PROGRAM_CLASS=3
    MAIN=4
    BREAK=5
    CONTINUE=6
    IF=7
    ELSE=8
    FOR=9
    INT=10
    FLOAT=11
    BOOL=12
    STRING=13
    RETURN=14
    NULL=15
    CLASS=16
    CONSTRUCTOR=17
    VAR=18
    SELF=19
    NEW=20
    VOID=21
    CONST=22
    FUNC=23
    ADD_OP=24
    SUB_OP=25
    MUL_OP=26
    DIV_OP=27
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
    MOD_OP=40
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
    CMT_BLOCK=60
    WS=61
    ERROR_CHAR=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64

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




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.prog_decl_list()
            self.state = 129
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




    def prog_decl_list(self):

        localctx = CSlangParser.Prog_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog_decl_list)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.prog_decl()
                self.state = 132
                self.prog_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.prog_decl()
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




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.exp1()
                self.state = 138
                self.match(CSlangParser.CONCAT_OP)
                self.state = 139
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.exp2(0)
                self.state = 145
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL_OP) | (1 << CSlangParser.DIFF_OP) | (1 << CSlangParser.LESS_OP) | (1 << CSlangParser.LESS_EQUAL_OP) | (1 << CSlangParser.GREATER_OP) | (1 << CSlangParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 146
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
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



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 154
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 155
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND_OP or _la==CSlangParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 156
                    self.exp3(0) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 165
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 166
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 167
                    self.exp4(0) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.exp5() 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp5)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(CSlangParser.NOT_OP)
                self.state = 185
                self.exp5()
                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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




    def exp6(self):

        localctx = CSlangParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp6)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(CSlangParser.SUB_OP)
                self.state = 190
                self.exp6()
                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
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




    def exp7(self):

        localctx = CSlangParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp7)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 211
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 201
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 202
                        self.match(CSlangParser.DOT)
                        self.state = 203
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 204
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 205
                        self.match(CSlangParser.DOT)
                        self.state = 206
                        self.match(CSlangParser.ID)
                        self.state = 207
                        self.match(CSlangParser.LP)
                        self.state = 208
                        self.exp_list()
                        self.state = 209
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp9)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.static_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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


        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp10




    def exp10(self):

        localctx = CSlangParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp10)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.obj_cre()
                pass
            elif token in [CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.literal()
                pass
            elif token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(CSlangParser.LP)

                self.state = 223
                self.exp()
                self.state = 224
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.self_mem_access()
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.match(CSlangParser.NULL)
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




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self.match(CSlangParser.BOOL_LIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 235
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




    def exp_list(self):

        localctx = CSlangParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp_list)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
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




    def exp_prime(self):

        localctx = CSlangParser.Exp_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp_prime)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.exp()
                self.state = 243
                self.match(CSlangParser.COMMA)
                self.state = 244
                self.exp_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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




    def func_type(self):

        localctx = CSlangParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_type)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.ref_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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

        def ele_type(self):
            return self.getTypedRuleContext(CSlangParser.Ele_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_ref_type




    def ref_type(self):

        localctx = CSlangParser.Ref_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ref_type)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.ele_type()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
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


    class Ele_typeContext(ParserRuleContext):
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
            return CSlangParser.RULE_ele_type




    def ele_type(self):

        localctx = CSlangParser.Ele_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ele_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
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

        def ele_type(self):
            return self.getTypedRuleContext(CSlangParser.Ele_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(CSlangParser.LSB)
            self.state = 260
            self.match(CSlangParser.INT_LIT)
            self.state = 261
            self.match(CSlangParser.RSB)
            self.state = 262
            self.ele_type()
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

        def class_decl(self):
            return self.getTypedRuleContext(CSlangParser.Class_declContext,0)


        def program_class_decl(self):
            return self.getTypedRuleContext(CSlangParser.Program_class_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_prog_decl




    def prog_decl(self):

        localctx = CSlangParser.Prog_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_prog_decl)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.class_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.program_class_decl()
                pass


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




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(CSlangParser.CLASS)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 269
                self.match(CSlangParser.ID)
                self.state = 270
                self.match(CSlangParser.T__1)


            self.state = 273
            self.match(CSlangParser.ID)
            self.state = 274
            self.match(CSlangParser.LCB)
            self.state = 275
            self.class_mem_list()
            self.state = 276
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def PROGRAM_CLASS(self):
            return self.getToken(CSlangParser.PROGRAM_CLASS, 0)

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def prog_class_mem_list(self):
            return self.getTypedRuleContext(CSlangParser.Prog_class_mem_listContext,0)


        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program_class_decl




    def program_class_decl(self):

        localctx = CSlangParser.Program_class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_program_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(CSlangParser.CLASS)
            self.state = 279
            self.match(CSlangParser.PROGRAM_CLASS)
            self.state = 280
            self.match(CSlangParser.LCB)
            self.state = 281
            self.prog_class_mem_list()
            self.state = 282
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




    def class_mem_list(self):

        localctx = CSlangParser.Class_mem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_class_mem_list)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.class_mem()
                self.state = 285
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




    def class_mem(self):

        localctx = CSlangParser.Class_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_class_mem)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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


    class Prog_class_mem_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog_class_mem(self):
            return self.getTypedRuleContext(CSlangParser.Prog_class_memContext,0)


        def prog_class_mem_list(self):
            return self.getTypedRuleContext(CSlangParser.Prog_class_mem_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_prog_class_mem_list




    def prog_class_mem_list(self):

        localctx = CSlangParser.Prog_class_mem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_prog_class_mem_list)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.prog_class_mem()
                self.state = 295
                self.prog_class_mem_list()
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


    class Prog_class_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_mem(self):
            return self.getTypedRuleContext(CSlangParser.Class_memContext,0)


        def main_func_decl(self):
            return self.getTypedRuleContext(CSlangParser.Main_func_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_prog_class_mem




    def prog_class_mem(self):

        localctx = CSlangParser.Prog_class_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_prog_class_mem)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.class_mem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.main_func_decl()
                pass


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




    def obj_cre(self):

        localctx = CSlangParser.Obj_creContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_obj_cre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(CSlangParser.NEW)
            self.state = 305
            self.match(CSlangParser.ID)
            self.state = 306
            self.match(CSlangParser.LP)
            self.state = 307
            self.exp_list()
            self.state = 308
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




    def mem_access(self):

        localctx = CSlangParser.Mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_mem_access)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.inst_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.static_mem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
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




    def method_access(self):

        localctx = CSlangParser.Method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_method_access)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.inst_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.static_method_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
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




    def inst_mem_access(self):

        localctx = CSlangParser.Inst_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_inst_mem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.exp8(0)
            self.state = 321
            self.match(CSlangParser.DOT)
            self.state = 322
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




    def inst_method_access(self):

        localctx = CSlangParser.Inst_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_inst_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.exp8(0)
            self.state = 325
            self.match(CSlangParser.DOT)
            self.state = 326
            self.match(CSlangParser.ID)
            self.state = 327
            self.match(CSlangParser.LP)
            self.state = 328
            self.exp_list()
            self.state = 329
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




    def static_access(self):

        localctx = CSlangParser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_static_access)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.static_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
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




    def static_mem_access(self):

        localctx = CSlangParser.Static_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_static_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 335
                self.match(CSlangParser.ID)
                self.state = 336
                self.match(CSlangParser.DOT)


            self.state = 339
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




    def static_method_access(self):

        localctx = CSlangParser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 341
                self.match(CSlangParser.ID)
                self.state = 342
                self.match(CSlangParser.DOT)


            self.state = 345
            self.match(CSlangParser.AT_ID)
            self.state = 346
            self.match(CSlangParser.LP)
            self.state = 347
            self.exp_list()
            self.state = 348
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




    def self_access(self):

        localctx = CSlangParser.Self_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_self_access)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.self_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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




    def self_mem_access(self):

        localctx = CSlangParser.Self_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_self_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(CSlangParser.SELF)
            self.state = 355
            self.match(CSlangParser.DOT)
            self.state = 356
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




    def self_method_access(self):

        localctx = CSlangParser.Self_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_self_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(CSlangParser.SELF)
            self.state = 359
            self.match(CSlangParser.DOT)
            self.state = 360
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 361
            self.match(CSlangParser.LP)
            self.state = 362
            self.exp_list()
            self.state = 363
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




    def method_decl(self):

        localctx = CSlangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_method_decl)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
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




    def func_decl(self):

        localctx = CSlangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(CSlangParser.FUNC)
            self.state = 371
            self.match(CSlangParser.ID)
            self.state = 372
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
        self.enterRule(localctx, 80, self.RULE_static_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(CSlangParser.FUNC)
            self.state = 375
            self.match(CSlangParser.AT_ID)
            self.state = 376
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




    def expo_func(self):

        localctx = CSlangParser.Expo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expo_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(CSlangParser.LP)
            self.state = 379
            self.params_list()
            self.state = 380
            self.match(CSlangParser.RP)
            self.state = 381
            self.match(CSlangParser.COLON)
            self.state = 382
            self.func_type()
            self.state = 383
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def MAIN(self):
            return self.getToken(CSlangParser.MAIN, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_main_func_decl




    def main_func_decl(self):

        localctx = CSlangParser.Main_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_main_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(CSlangParser.FUNC)
            self.state = 386
            self.match(CSlangParser.MAIN)
            self.state = 387
            self.match(CSlangParser.LP)
            self.state = 388
            self.match(CSlangParser.RP)
            self.state = 389
            self.match(CSlangParser.COLON)
            self.state = 390
            self.match(CSlangParser.VOID)
            self.state = 391
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




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(CSlangParser.FUNC)
            self.state = 394
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 395
            self.match(CSlangParser.LP)
            self.state = 396
            self.params_list()
            self.state = 397
            self.match(CSlangParser.RP)
            self.state = 398
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




    def attr_decl(self):

        localctx = CSlangParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self.attr_decl_body()
            self.state = 402
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




    def attr_decl_body(self):

        localctx = CSlangParser.Attr_decl_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_attr_decl_body)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.attr_decl_body_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
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




    def attr_decl_body_short(self):

        localctx = CSlangParser.Attr_decl_body_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_attr_decl_body_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.identifier_list()
            self.state = 409
            self.match(CSlangParser.COLON)
            self.state = 410
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




    def attr_decl_body_full(self):

        localctx = CSlangParser.Attr_decl_body_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_attr_decl_body_full)
        self._la = 0 # Token type
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 413
                self.match(CSlangParser.COMMA)
                self.state = 414
                self.attr_decl_body_full()
                self.state = 415
                self.match(CSlangParser.COMMA)
                self.state = 416
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 419
                self.match(CSlangParser.COLON)
                self.state = 420
                self.ref_type()
                self.state = 421
                self.match(CSlangParser.DECL_OP)
                self.state = 422
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




    def identifier_list(self):

        localctx = CSlangParser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 427
                self.match(CSlangParser.COMMA)
                self.state = 428
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
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




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.assign_stmt()
                self.state = 433
                self.match(CSlangParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 438
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 439
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 440
                self.method_invocation_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 441
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




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.exp7()
            self.state = 445
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 446
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




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(CSlangParser.IF)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 449
                self.block_stmt()


            self.state = 452
            self.exp()
            self.state = 453
            self.block_stmt()
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 454
                self.match(CSlangParser.ELSE)
                self.state = 455
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




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(CSlangParser.FOR)
            self.state = 459
            self.assign_stmt()
            self.state = 460
            self.match(CSlangParser.SEMICOLON)
            self.state = 461
            self.exp()
            self.state = 462
            self.match(CSlangParser.SEMICOLON)
            self.state = 463
            self.assign_stmt()
            self.state = 464
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




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(CSlangParser.BREAK)
            self.state = 467
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




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(CSlangParser.CONTINUE)
            self.state = 470
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




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(CSlangParser.RETURN)
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 473
                self.exp()


            self.state = 476
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




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 478
                self.inst_method_access()
                pass

            elif la_ == 2:
                self.state = 479
                self.static_method_access()
                pass

            elif la_ == 3:
                self.state = 480
                self.self_method_access()
                pass


            self.state = 483
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




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(CSlangParser.LCB)
            self.state = 486
            self.body()
            self.state = 487
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




    def body(self):

        localctx = CSlangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_body)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.stmt()
                self.state = 490
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




    def params_list(self):

        localctx = CSlangParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_params_list)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
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




    def params_prime(self):

        localctx = CSlangParser.Params_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_params_prime)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.params_1_type()
                self.state = 500
                self.match(CSlangParser.COMMA)
                self.state = 501
                self.params_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
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




    def params_1_type(self):

        localctx = CSlangParser.Params_1_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_params_1_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.identifier_list()
            self.state = 507
            self.match(CSlangParser.COLON)
            self.state = 508
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




    def array_lit(self):

        localctx = CSlangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(CSlangParser.LSB)
            self.state = 511
            self.exp_list()
            self.state = 512
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




    def arr_ele(self):

        localctx = CSlangParser.Arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.exp8(0)
            self.state = 515
            self.match(CSlangParser.LSB)
            self.state = 516
            self.exp()
            self.state = 517
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
        self._predicates[4] = self.exp2_sempred
        self._predicates[5] = self.exp3_sempred
        self._predicates[6] = self.exp4_sempred
        self._predicates[10] = self.exp8_sempred
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
         




