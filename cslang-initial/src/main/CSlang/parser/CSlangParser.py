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
        buf.write("\u01d1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\3\2\3\2\6\2n\n\2\r\2\16\2o\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3y\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u0080")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u0088\n\5\f\5\16\5\u008b")
        buf.write("\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0093\n\6\f\6\16\6\u0096")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u009e\n\7\f\7\16\7\u00a1")
        buf.write("\13\7\3\b\3\b\3\b\5\b\u00a6\n\b\3\t\3\t\3\t\5\t\u00ab")
        buf.write("\n\t\3\n\3\n\5\n\u00af\n\n\3\13\3\13\3\13\5\13\u00b4\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00be\n\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u00c5\n\r\3\16\3\16\3\16\7\16\u00ca")
        buf.write("\n\16\f\16\16\16\u00cd\13\16\3\17\3\17\5\17\u00d1\n\17")
        buf.write("\3\20\3\20\5\20\u00d5\n\20\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\5\23\u00e1\n\23\3\24\3\24\3\24")
        buf.write("\5\24\u00e6\n\24\3\24\3\24\3\24\3\24\7\24\u00ec\n\24\f")
        buf.write("\24\16\24\u00ef\13\24\3\24\3\24\3\25\3\25\5\25\u00f5\n")
        buf.write("\25\3\26\3\26\5\26\u00f9\n\26\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00ff\n\27\3\27\3\27\3\30\3\30\5\30\u0105\n\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\5\31\u010c\n\31\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u0112\n\32\3\32\3\32\3\32\3\32\5\32\u0118\n\32\3")
        buf.write("\32\3\32\3\33\3\33\5\33\u011e\n\33\3\33\3\33\3\33\5\33")
        buf.write("\u0123\n\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u012b\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\5\37\u0137\n\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3!\3!\3!\3!\3\"\3\"\5\"\u0148\n\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\5#\u0150\n#\3#\3#\3$\3$\3$\3$\3%\3%\5%\u015a\n%\3&\3")
        buf.write("&\3&\7&\u015f\n&\f&\16&\u0162\13&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0173\n\'\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3(\5(\u017e\n(\3)\3)\3)\3)\3*\3")
        buf.write("*\5*\u0186\n*\3*\3*\3*\3*\5*\u018c\n*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\5.\u019e\n.\3.\3.\3/\3")
        buf.write("/\5/\u01a4\n/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\7\61")
        buf.write("\u01ae\n\61\f\61\16\61\u01b1\13\61\3\62\3\62\3\62\7\62")
        buf.write("\u01b6\n\62\f\62\16\62\u01b9\13\62\3\63\3\63\3\63\7\63")
        buf.write("\u01be\n\63\f\63\16\63\u01c1\13\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\5\64\u01c8\n\64\3\64\3\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\2\5\b\n\f\66\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("\2\t\4\2\37\37\"&\3\2\35\36\3\2\30\31\5\2\3\3\32\33((")
        buf.write("\3\2\n\r\3\29:\4\2\22\22\26\26\2\u01da\2m\3\2\2\2\4x\3")
        buf.write("\2\2\2\6\177\3\2\2\2\b\u0081\3\2\2\2\n\u008c\3\2\2\2\f")
        buf.write("\u0097\3\2\2\2\16\u00a5\3\2\2\2\20\u00aa\3\2\2\2\22\u00ae")
        buf.write("\3\2\2\2\24\u00b3\3\2\2\2\26\u00bd\3\2\2\2\30\u00c4\3")
        buf.write("\2\2\2\32\u00c6\3\2\2\2\34\u00d0\3\2\2\2\36\u00d4\3\2")
        buf.write("\2\2 \u00d6\3\2\2\2\"\u00d8\3\2\2\2$\u00e0\3\2\2\2&\u00e2")
        buf.write("\3\2\2\2(\u00f4\3\2\2\2*\u00f8\3\2\2\2,\u00fa\3\2\2\2")
        buf.write(".\u0104\3\2\2\2\60\u010b\3\2\2\2\62\u0111\3\2\2\2\64\u011d")
        buf.write("\3\2\2\2\66\u012a\3\2\2\28\u012c\3\2\2\2:\u0130\3\2\2")
        buf.write("\2<\u0134\3\2\2\2>\u013d\3\2\2\2@\u0141\3\2\2\2B\u0145")
        buf.write("\3\2\2\2D\u014c\3\2\2\2F\u0153\3\2\2\2H\u0159\3\2\2\2")
        buf.write("J\u015b\3\2\2\2L\u0172\3\2\2\2N\u017d\3\2\2\2P\u017f\3")
        buf.write("\2\2\2R\u0183\3\2\2\2T\u018d\3\2\2\2V\u0195\3\2\2\2X\u0198")
        buf.write("\3\2\2\2Z\u019b\3\2\2\2\\\u01a3\3\2\2\2^\u01a7\3\2\2\2")
        buf.write("`\u01af\3\2\2\2b\u01b2\3\2\2\2d\u01ba\3\2\2\2f\u01c5\3")
        buf.write("\2\2\2h\u01cb\3\2\2\2jn\5\4\3\2kn\5N(\2ln\5$\23\2mj\3")
        buf.write("\2\2\2mk\3\2\2\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2")
        buf.write("\2pq\3\2\2\2qr\7\2\2\3r\3\3\2\2\2st\5\6\4\2tu\7\'\2\2")
        buf.write("uv\5\6\4\2vy\3\2\2\2wy\5\6\4\2xs\3\2\2\2xw\3\2\2\2y\5")
        buf.write("\3\2\2\2z{\5\b\5\2{|\t\2\2\2|}\5\b\5\2}\u0080\3\2\2\2")
        buf.write("~\u0080\5\b\5\2\177z\3\2\2\2\177~\3\2\2\2\u0080\7\3\2")
        buf.write("\2\2\u0081\u0082\b\5\1\2\u0082\u0083\5\n\6\2\u0083\u0089")
        buf.write("\3\2\2\2\u0084\u0085\f\4\2\2\u0085\u0086\t\3\2\2\u0086")
        buf.write("\u0088\5\n\6\2\u0087\u0084\3\2\2\2\u0088\u008b\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\t\3\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008c\u008d\b\6\1\2\u008d\u008e")
        buf.write("\5\f\7\2\u008e\u0094\3\2\2\2\u008f\u0090\f\4\2\2\u0090")
        buf.write("\u0091\t\4\2\2\u0091\u0093\5\f\7\2\u0092\u008f\3\2\2\2")
        buf.write("\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3")
        buf.write("\2\2\2\u0095\13\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098")
        buf.write("\b\7\1\2\u0098\u0099\5\16\b\2\u0099\u009f\3\2\2\2\u009a")
        buf.write("\u009b\f\4\2\2\u009b\u009c\t\5\2\2\u009c\u009e\5\16\b")
        buf.write("\2\u009d\u009a\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\r\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00a3\7\34\2\2\u00a3\u00a6\5\16\b\2\u00a4")
        buf.write("\u00a6\5\20\t\2\u00a5\u00a2\3\2\2\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\17\3\2\2\2\u00a7\u00a8\7\31\2\2\u00a8\u00ab\5")
        buf.write("\20\t\2\u00a9\u00ab\5\22\n\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\21\3\2\2\2\u00ac\u00af\5h\65\2\u00ad")
        buf.write("\u00af\5\24\13\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2")
        buf.write("\2\u00af\23\3\2\2\2\u00b0\u00b4\5*\26\2\u00b1\u00b4\5")
        buf.write("(\25\2\u00b2\u00b4\5\26\f\2\u00b3\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\25\3\2\2\2\u00b5")
        buf.write("\u00be\5,\27\2\u00b6\u00be\5\30\r\2\u00b7\u00b8\7)\2\2")
        buf.write("\u00b8\u00b9\5\4\3\2\u00b9\u00ba\7*\2\2\u00ba\u00be\3")
        buf.write("\2\2\2\u00bb\u00be\79\2\2\u00bc\u00be\5D#\2\u00bd\u00b5")
        buf.write("\3\2\2\2\u00bd\u00b6\3\2\2\2\u00bd\u00b7\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\27\3\2\2\2\u00bf")
        buf.write("\u00c5\7\66\2\2\u00c0\u00c5\7\65\2\2\u00c1\u00c5\7\67")
        buf.write("\2\2\u00c2\u00c5\78\2\2\u00c3\u00c5\5f\64\2\u00c4\u00bf")
        buf.write("\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c1\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\31\3\2\2\2\u00c6")
        buf.write("\u00cb\5\4\3\2\u00c7\u00c8\7.\2\2\u00c8\u00ca\5\4\3\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\33\3\2\2\2\u00cd\u00cb")
        buf.write("\3\2\2\2\u00ce\u00d1\5\36\20\2\u00cf\u00d1\7\25\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\35\3\2\2\2\u00d2")
        buf.write("\u00d5\5 \21\2\u00d3\u00d5\5\"\22\2\u00d4\u00d2\3\2\2")
        buf.write("\2\u00d4\u00d3\3\2\2\2\u00d5\37\3\2\2\2\u00d6\u00d7\t")
        buf.write("\6\2\2\u00d7!\3\2\2\2\u00d8\u00d9\7+\2\2\u00d9\u00da\7")
        buf.write("\66\2\2\u00da\u00db\7,\2\2\u00db\u00dc\5 \21\2\u00dc#")
        buf.write("\3\2\2\2\u00dd\u00e1\5&\24\2\u00de\u00e1\5F$\2\u00df\u00e1")
        buf.write("\5\66\34\2\u00e0\u00dd\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e1%\3\2\2\2\u00e2\u00e5\7\20\2\2\u00e3")
        buf.write("\u00e4\79\2\2\u00e4\u00e6\7\4\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\7")
        buf.write("9\2\2\u00e8\u00ed\7\61\2\2\u00e9\u00ec\5N(\2\u00ea\u00ec")
        buf.write("\5$\23\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\7")
        buf.write("\62\2\2\u00f1\'\3\2\2\2\u00f2\u00f5\5\60\31\2\u00f3\u00f5")
        buf.write("\5\64\33\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5")
        buf.write(")\3\2\2\2\u00f6\u00f9\5.\30\2\u00f7\u00f9\5\62\32\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9+\3\2\2\2\u00fa")
        buf.write("\u00fb\7\24\2\2\u00fb\u00fc\79\2\2\u00fc\u00fe\7)\2\2")
        buf.write("\u00fd\u00ff\5\32\16\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\7*\2\2\u0101")
        buf.write("-\3\2\2\2\u0102\u0105\5\26\f\2\u0103\u0105\7\23\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106\u0107\7-\2\2\u0107\u0108\79\2\2\u0108/\3\2\2\2")
        buf.write("\u0109\u010a\79\2\2\u010a\u010c\7-\2\2\u010b\u0109\3\2")
        buf.write("\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e")
        buf.write("\7:\2\2\u010e\61\3\2\2\2\u010f\u0112\5\26\f\2\u0110\u0112")
        buf.write("\7\23\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\7-\2\2\u0114\u0115\79\2\2\u0115")
        buf.write("\u0117\7)\2\2\u0116\u0118\5\32\16\2\u0117\u0116\3\2\2")
        buf.write("\2\u0117\u0118\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a")
        buf.write("\7*\2\2\u011a\63\3\2\2\2\u011b\u011c\79\2\2\u011c\u011e")
        buf.write("\7-\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u0120\7:\2\2\u0120\u0122\7)\2\2\u0121")
        buf.write("\u0123\5\32\16\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2")
        buf.write("\2\u0123\u0124\3\2\2\2\u0124\u0125\7*\2\2\u0125\65\3\2")
        buf.write("\2\2\u0126\u012b\58\35\2\u0127\u012b\5> \2\u0128\u012b")
        buf.write("\5:\36\2\u0129\u012b\5@!\2\u012a\u0126\3\2\2\2\u012a\u0127")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("\67\3\2\2\2\u012c\u012d\7\27\2\2\u012d\u012e\79\2\2\u012e")
        buf.write("\u012f\5<\37\2\u012f9\3\2\2\2\u0130\u0131\7\27\2\2\u0131")
        buf.write("\u0132\7:\2\2\u0132\u0133\5<\37\2\u0133;\3\2\2\2\u0134")
        buf.write("\u0136\7)\2\2\u0135\u0137\5b\62\2\u0136\u0135\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\7")
        buf.write("*\2\2\u0139\u013a\7/\2\2\u013a\u013b\5\34\17\2\u013b\u013c")
        buf.write("\5^\60\2\u013c=\3\2\2\2\u013d\u013e\7\27\2\2\u013e\u013f")
        buf.write("\79\2\2\u013f\u0140\5B\"\2\u0140?\3\2\2\2\u0141\u0142")
        buf.write("\7\27\2\2\u0142\u0143\7:\2\2\u0143\u0144\5B\"\2\u0144")
        buf.write("A\3\2\2\2\u0145\u0147\7)\2\2\u0146\u0148\5b\62\2\u0147")
        buf.write("\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\7*\2\2\u014a\u014b\5^\60\2\u014bC\3\2\2\2")
        buf.write("\u014c\u014d\t\7\2\2\u014d\u014f\7)\2\2\u014e\u0150\5")
        buf.write("\32\16\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0152\7*\2\2\u0152E\3\2\2\2\u0153")
        buf.write("\u0154\t\b\2\2\u0154\u0155\5H%\2\u0155\u0156\7\60\2\2")
        buf.write("\u0156G\3\2\2\2\u0157\u015a\5L\'\2\u0158\u015a\5J&\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015aI\3\2\2\2\u015b")
        buf.write("\u0160\t\7\2\2\u015c\u015d\7.\2\2\u015d\u015f\t\7\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3")
        buf.write("\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0163\u0164\7/\2\2\u0164\u0165\5\36\20\2\u0165")
        buf.write("K\3\2\2\2\u0166\u0167\t\7\2\2\u0167\u0168\7.\2\2\u0168")
        buf.write("\u0169\5L\'\2\u0169\u016a\7.\2\2\u016a\u016b\5\4\3\2\u016b")
        buf.write("\u0173\3\2\2\2\u016c\u016d\t\7\2\2\u016d\u016e\7/\2\2")
        buf.write("\u016e\u016f\5\36\20\2\u016f\u0170\7!\2\2\u0170\u0171")
        buf.write("\5\4\3\2\u0171\u0173\3\2\2\2\u0172\u0166\3\2\2\2\u0172")
        buf.write("\u016c\3\2\2\2\u0173M\3\2\2\2\u0174\u0175\5P)\2\u0175")
        buf.write("\u0176\7\60\2\2\u0176\u017e\3\2\2\2\u0177\u017e\5R*\2")
        buf.write("\u0178\u017e\5T+\2\u0179\u017e\5V,\2\u017a\u017e\5X-\2")
        buf.write("\u017b\u017e\5Z.\2\u017c\u017e\5\\/\2\u017d\u0174\3\2")
        buf.write("\2\2\u017d\u0177\3\2\2\2\u017d\u0178\3\2\2\2\u017d\u0179")
        buf.write("\3\2\2\2\u017d\u017a\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017eO\3\2\2\2\u017f\u0180\5\4\3\2\u0180")
        buf.write("\u0181\7 \2\2\u0181\u0182\5\4\3\2\u0182Q\3\2\2\2\u0183")
        buf.write("\u0185\7\7\2\2\u0184\u0186\5^\60\2\u0185\u0184\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\5")
        buf.write("\4\3\2\u0188\u018b\5^\60\2\u0189\u018a\7\b\2\2\u018a\u018c")
        buf.write("\5^\60\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("S\3\2\2\2\u018d\u018e\7\t\2\2\u018e\u018f\5P)\2\u018f")
        buf.write("\u0190\7\60\2\2\u0190\u0191\5\4\3\2\u0191\u0192\7\60\2")
        buf.write("\2\u0192\u0193\5P)\2\u0193\u0194\5^\60\2\u0194U\3\2\2")
        buf.write("\2\u0195\u0196\7\5\2\2\u0196\u0197\7\60\2\2\u0197W\3\2")
        buf.write("\2\2\u0198\u0199\7\6\2\2\u0199\u019a\7\60\2\2\u019aY\3")
        buf.write("\2\2\2\u019b\u019d\7\16\2\2\u019c\u019e\5\4\3\2\u019d")
        buf.write("\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a0\7\60\2\2\u01a0[\3\2\2\2\u01a1\u01a4\5\62")
        buf.write("\32\2\u01a2\u01a4\5\64\33\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7\60\2")
        buf.write("\2\u01a6]\3\2\2\2\u01a7\u01a8\7\61\2\2\u01a8\u01a9\5`")
        buf.write("\61\2\u01a9\u01aa\7\62\2\2\u01aa_\3\2\2\2\u01ab\u01ae")
        buf.write("\5N(\2\u01ac\u01ae\5$\23\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0a\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2")
        buf.write("\u01b7\5d\63\2\u01b3\u01b4\7.\2\2\u01b4\u01b6\5d\63\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b7\u01b8\3\2\2\2\u01b8c\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bf\79\2\2\u01bb\u01bc\7.\2\2\u01bc\u01be")
        buf.write("\79\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c2\u01c3\7/\2\2\u01c3\u01c4\5")
        buf.write("\36\20\2\u01c4e\3\2\2\2\u01c5\u01c7\7+\2\2\u01c6\u01c8")
        buf.write("\5\32\16\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01ca\7,\2\2\u01cag\3\2\2\2\u01cb")
        buf.write("\u01cc\79\2\2\u01cc\u01cd\7+\2\2\u01cd\u01ce\5\24\13\2")
        buf.write("\u01ce\u01cf\7,\2\2\u01cfi\3\2\2\2\60mox\177\u0089\u0094")
        buf.write("\u009f\u00a5\u00aa\u00ae\u00b3\u00bd\u00c4\u00cb\u00d0")
        buf.write("\u00d4\u00e0\u00e5\u00eb\u00ed\u00f4\u00f8\u00fe\u0104")
        buf.write("\u010b\u0111\u0117\u011d\u0122\u012a\u0136\u0147\u014f")
        buf.write("\u0159\u0160\u0172\u017d\u0185\u018b\u019d\u01a3\u01ad")
        buf.write("\u01af\u01b7\u01bf\u01c7")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'<-'", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'self'", "'new'", "'void'", "'const'", "'func'", 
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
    RULE_exp = 1
    RULE_exp1 = 2
    RULE_exp2 = 3
    RULE_exp3 = 4
    RULE_exp4 = 5
    RULE_exp5 = 6
    RULE_exp6 = 7
    RULE_exp7 = 8
    RULE_exp8 = 9
    RULE_exp9 = 10
    RULE_literal = 11
    RULE_exp_list = 12
    RULE_func_type = 13
    RULE_ref_type = 14
    RULE_value_type = 15
    RULE_array_type = 16
    RULE_decl = 17
    RULE_class_decl = 18
    RULE_static_access = 19
    RULE_inst_access = 20
    RULE_obj_cre = 21
    RULE_mem_access = 22
    RULE_static_mem_access = 23
    RULE_method_access = 24
    RULE_static_method_access = 25
    RULE_method_decl = 26
    RULE_func_decl = 27
    RULE_static_func_decl = 28
    RULE_expo_func = 29
    RULE_constructor_decl = 30
    RULE_static_constructor_decl = 31
    RULE_expo_constructor = 32
    RULE_func_call = 33
    RULE_attr_decl = 34
    RULE_attr_decl_body = 35
    RULE_attr_decl_body_short = 36
    RULE_attr_decl_body_full = 37
    RULE_stmt = 38
    RULE_assign_stmt = 39
    RULE_if_stmt = 40
    RULE_for_stmt = 41
    RULE_break_stmt = 42
    RULE_continue_stmt = 43
    RULE_return_stmt = 44
    RULE_method_invocation_stmt = 45
    RULE_block_stmt = 46
    RULE_body = 47
    RULE_params_list = 48
    RULE_params_1_type = 49
    RULE_array_lit = 50
    RULE_arr_ele = 51

    ruleNames =  [ "program", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "literal", "exp_list", 
                   "func_type", "ref_type", "value_type", "array_type", 
                   "decl", "class_decl", "static_access", "inst_access", 
                   "obj_cre", "mem_access", "static_mem_access", "method_access", 
                   "static_method_access", "method_decl", "func_decl", "static_func_decl", 
                   "expo_func", "constructor_decl", "static_constructor_decl", 
                   "expo_constructor", "func_call", "attr_decl", "attr_decl_body", 
                   "attr_decl_body_short", "attr_decl_body_full", "stmt", 
                   "assign_stmt", "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invocation_stmt", "block_stmt", 
                   "body", "params_list", "params_1_type", "array_lit", 
                   "arr_ele" ]

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

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.DeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.DeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 104
                    self.exp()
                    pass

                elif la_ == 2:
                    self.state = 105
                    self.stmt()
                    pass

                elif la_ == 3:
                    self.state = 106
                    self.decl()
                    pass


                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0)):
                    break

            self.state = 111
            self.match(CSlangParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.exp1()
                self.state = 114
                self.match(CSlangParser.CONCAT_OP)
                self.state = 115
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
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
        self.enterRule(localctx, 4, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.exp2(0)
                self.state = 121
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL_OP) | (1 << CSlangParser.DIFF_OP) | (1 << CSlangParser.LESS_OP) | (1 << CSlangParser.LESS_EQUAL_OP) | (1 << CSlangParser.GREATER_OP) | (1 << CSlangParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 130
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 131
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND_OP or _la==CSlangParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.exp3(0) 
                self.state = 137
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 141
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 142
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 143
                    self.exp4(0) 
                self.state = 148
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 154
                    self.exp5() 
                self.state = 159
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
        self.enterRule(localctx, 12, self.RULE_exp5)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(CSlangParser.NOT_OP)
                self.state = 161
                self.exp5()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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
        self.enterRule(localctx, 14, self.RULE_exp6)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(CSlangParser.SUB_OP)
                self.state = 166
                self.exp6()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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
        self.enterRule(localctx, 16, self.RULE_exp7)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.exp8()
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

        def inst_access(self):
            return self.getTypedRuleContext(CSlangParser.Inst_accessContext,0)


        def static_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_accessContext,0)


        def exp9(self):
            return self.getTypedRuleContext(CSlangParser.Exp9Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = CSlangParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp8)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.inst_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.static_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
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

        def func_call(self):
            return self.getTypedRuleContext(CSlangParser.Func_callContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp9)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.obj_cre()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.match(CSlangParser.LP)

                self.state = 182
                self.exp()
                self.state = 183
                self.match(CSlangParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.match(CSlangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.func_call()
                pass


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
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(CSlangParser.BOOL_LIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 193
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = CSlangParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.exp()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 197
                self.match(CSlangParser.COMMA)
                self.state = 198
                self.exp()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 26, self.RULE_func_type)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.ref_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
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
        self.enterRule(localctx, 28, self.RULE_ref_type)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.value_type()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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
        self.enterRule(localctx, 30, self.RULE_value_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
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
        self.enterRule(localctx, 32, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(CSlangParser.LSB)
            self.state = 215
            self.match(CSlangParser.INT_LIT)
            self.state = 216
            self.match(CSlangParser.RSB)
            self.state = 217
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
        self.enterRule(localctx, 34, self.RULE_decl)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
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

        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.DeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.DeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(CSlangParser.CLASS)
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 225
                self.match(CSlangParser.ID)
                self.state = 226
                self.match(CSlangParser.T__1)


            self.state = 229
            self.match(CSlangParser.ID)
            self.state = 230
            self.match(CSlangParser.LCB)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 233
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    self.state = 231
                    self.stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                    self.state = 232
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self.match(CSlangParser.RCB)
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
        self.enterRule(localctx, 38, self.RULE_static_access)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.static_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.static_method_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mem_access(self):
            return self.getTypedRuleContext(CSlangParser.Mem_accessContext,0)


        def method_access(self):
            return self.getTypedRuleContext(CSlangParser.Method_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_inst_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_access" ):
                return visitor.visitInst_access(self)
            else:
                return visitor.visitChildren(self)




    def inst_access(self):

        localctx = CSlangParser.Inst_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_inst_access)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.method_access()
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

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_obj_cre

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_cre" ):
                return visitor.visitObj_cre(self)
            else:
                return visitor.visitChildren(self)




    def obj_cre(self):

        localctx = CSlangParser.Obj_creContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_obj_cre)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(CSlangParser.NEW)
            self.state = 249
            self.match(CSlangParser.ID)
            self.state = 250
            self.match(CSlangParser.LP)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 251
                self.exp_list()


            self.state = 254
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

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def exp9(self):
            return self.getTypedRuleContext(CSlangParser.Exp9Context,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_mem_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem_access" ):
                return visitor.visitMem_access(self)
            else:
                return visitor.visitChildren(self)




    def mem_access(self):

        localctx = CSlangParser.Mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.state = 256
                self.exp9()
                pass
            elif token in [CSlangParser.SELF]:
                self.state = 257
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 260
            self.match(CSlangParser.DOT)
            self.state = 261
            self.match(CSlangParser.ID)
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
        self.enterRule(localctx, 46, self.RULE_static_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 263
                self.match(CSlangParser.ID)
                self.state = 264
                self.match(CSlangParser.DOT)


            self.state = 267
            self.match(CSlangParser.AT_ID)
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

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp9(self):
            return self.getTypedRuleContext(CSlangParser.Exp9Context,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_access" ):
                return visitor.visitMethod_access(self)
            else:
                return visitor.visitChildren(self)




    def method_access(self):

        localctx = CSlangParser.Method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.state = 269
                self.exp9()
                pass
            elif token in [CSlangParser.SELF]:
                self.state = 270
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 273
            self.match(CSlangParser.DOT)
            self.state = 274
            self.match(CSlangParser.ID)
            self.state = 275
            self.match(CSlangParser.LP)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 276
                self.exp_list()


            self.state = 279
            self.match(CSlangParser.RP)
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

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_access" ):
                return visitor.visitStatic_method_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_access(self):

        localctx = CSlangParser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 281
                self.match(CSlangParser.ID)
                self.state = 282
                self.match(CSlangParser.DOT)


            self.state = 285
            self.match(CSlangParser.AT_ID)
            self.state = 286
            self.match(CSlangParser.LP)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 287
                self.exp_list()


            self.state = 290
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


        def static_constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Static_constructor_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = CSlangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_method_decl)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.static_func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.static_constructor_decl()
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
        self.enterRule(localctx, 54, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(CSlangParser.FUNC)
            self.state = 299
            self.match(CSlangParser.ID)
            self.state = 300
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
        self.enterRule(localctx, 56, self.RULE_static_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(CSlangParser.FUNC)
            self.state = 303
            self.match(CSlangParser.AT_ID)
            self.state = 304
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

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def func_type(self):
            return self.getTypedRuleContext(CSlangParser.Func_typeContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(CSlangParser.Params_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expo_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpo_func" ):
                return visitor.visitExpo_func(self)
            else:
                return visitor.visitChildren(self)




    def expo_func(self):

        localctx = CSlangParser.Expo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expo_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(CSlangParser.LP)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 307
                self.params_list()


            self.state = 310
            self.match(CSlangParser.RP)
            self.state = 311
            self.match(CSlangParser.COLON)
            self.state = 312
            self.func_type()
            self.state = 313
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expo_constructor(self):
            return self.getTypedRuleContext(CSlangParser.Expo_constructorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(CSlangParser.FUNC)
            self.state = 316
            self.match(CSlangParser.ID)
            self.state = 317
            self.expo_constructor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def expo_constructor(self):
            return self.getTypedRuleContext(CSlangParser.Expo_constructorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_constructor_decl" ):
                return visitor.visitStatic_constructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def static_constructor_decl(self):

        localctx = CSlangParser.Static_constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(CSlangParser.FUNC)
            self.state = 320
            self.match(CSlangParser.AT_ID)
            self.state = 321
            self.expo_constructor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expo_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(CSlangParser.Params_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expo_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpo_constructor" ):
                return visitor.visitExpo_constructor(self)
            else:
                return visitor.visitChildren(self)




    def expo_constructor(self):

        localctx = CSlangParser.Expo_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expo_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(CSlangParser.LP)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 324
                self.params_list()


            self.state = 327
            self.match(CSlangParser.RP)
            self.state = 328
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = CSlangParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 331
            self.match(CSlangParser.LP)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 332
                self.exp_list()


            self.state = 335
            self.match(CSlangParser.RP)
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
        self.enterRule(localctx, 68, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 338
            self.attr_decl_body()
            self.state = 339
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
        self.enterRule(localctx, 70, self.RULE_attr_decl_body)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.attr_decl_body_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def AT_ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.AT_ID)
            else:
                return self.getToken(CSlangParser.AT_ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_attr_decl_body_short

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_body_short" ):
                return visitor.visitAttr_decl_body_short(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_body_short(self):

        localctx = CSlangParser.Attr_decl_body_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_attr_decl_body_short)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 346
                self.match(CSlangParser.COMMA)
                self.state = 347
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 353
            self.match(CSlangParser.COLON)
            self.state = 354
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
        self.enterRule(localctx, 74, self.RULE_attr_decl_body_full)
        self._la = 0 # Token type
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 357
                self.match(CSlangParser.COMMA)
                self.state = 358
                self.attr_decl_body_full()
                self.state = 359
                self.match(CSlangParser.COMMA)
                self.state = 360
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.match(CSlangParser.COLON)
                self.state = 364
                self.ref_type()
                self.state = 365
                self.match(CSlangParser.DECL_OP)
                self.state = 366
                self.exp()
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


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.assign_stmt()
                self.state = 371
                self.match(CSlangParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 377
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 378
                self.method_invocation_stmt()
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.exp()
            self.state = 382
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 383
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
        self.enterRule(localctx, 80, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(CSlangParser.IF)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 386
                self.block_stmt()


            self.state = 389
            self.exp()
            self.state = 390
            self.block_stmt()
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 391
                self.match(CSlangParser.ELSE)
                self.state = 392
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
        self.enterRule(localctx, 82, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(CSlangParser.FOR)
            self.state = 396
            self.assign_stmt()
            self.state = 397
            self.match(CSlangParser.SEMICOLON)
            self.state = 398
            self.exp()
            self.state = 399
            self.match(CSlangParser.SEMICOLON)
            self.state = 400
            self.assign_stmt()
            self.state = 401
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
        self.enterRule(localctx, 84, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(CSlangParser.BREAK)
            self.state = 404
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
        self.enterRule(localctx, 86, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(CSlangParser.CONTINUE)
            self.state = 407
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
        self.enterRule(localctx, 88, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(CSlangParser.RETURN)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 410
                self.exp()


            self.state = 413
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

        def method_access(self):
            return self.getTypedRuleContext(CSlangParser.Method_accessContext,0)


        def static_method_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_accessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 415
                self.method_access()
                pass

            elif la_ == 2:
                self.state = 416
                self.static_method_access()
                pass


            self.state = 419
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
        self.enterRule(localctx, 92, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(CSlangParser.LCB)
            self.state = 422
            self.body()
            self.state = 423
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.DeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.DeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = CSlangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 427
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    self.state = 425
                    self.stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                    self.state = 426
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def params_1_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Params_1_typeContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Params_1_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = CSlangParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.params_1_type()
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 433
                self.match(CSlangParser.COMMA)
                self.state = 434
                self.params_1_type()
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_params_1_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_1_type" ):
                return visitor.visitParams_1_type(self)
            else:
                return visitor.visitChildren(self)




    def params_1_type(self):

        localctx = CSlangParser.Params_1_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_params_1_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(CSlangParser.ID)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 441
                self.match(CSlangParser.COMMA)
                self.state = 442
                self.match(CSlangParser.ID)
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 448
            self.match(CSlangParser.COLON)
            self.state = 449
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

        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = CSlangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(CSlangParser.LSB)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 452
                self.exp_list()


            self.state = 455
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


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
        self.enterRule(localctx, 102, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(CSlangParser.ID)
            self.state = 458
            self.match(CSlangParser.LSB)
            self.state = 459
            self.exp8()
            self.state = 460
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
        self._predicates[3] = self.exp2_sempred
        self._predicates[4] = self.exp3_sempred
        self._predicates[5] = self.exp4_sempred
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
         




