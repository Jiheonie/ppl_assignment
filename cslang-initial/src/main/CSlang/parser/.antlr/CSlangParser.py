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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\3\2\3\2\6\2p\n\2\r\2\16\2q\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3{\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u0082\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u008a\n\5")
        buf.write("\f\5\16\5\u008d\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0095")
        buf.write("\n\6\f\6\16\6\u0098\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00a0")
        buf.write("\n\7\f\7\16\7\u00a3\13\7\3\b\3\b\3\b\5\b\u00a8\n\b\3\t")
        buf.write("\3\t\3\t\5\t\u00ad\n\t\3\n\3\n\5\n\u00b1\n\n\3\13\3\13")
        buf.write("\3\13\5\13\u00b6\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00c0\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c7\n\r\3\16")
        buf.write("\3\16\3\16\7\16\u00cc\n\16\f\16\16\16\u00cf\13\16\3\17")
        buf.write("\3\17\5\17\u00d3\n\17\3\20\3\20\5\20\u00d7\n\20\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00e3")
        buf.write("\n\23\3\24\3\24\3\24\3\24\5\24\u00e9\n\24\3\24\3\24\3")
        buf.write("\24\7\24\u00ee\n\24\f\24\16\24\u00f1\13\24\3\24\3\24\3")
        buf.write("\25\3\25\5\25\u00f7\n\25\3\26\3\26\5\26\u00fb\n\26\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u0101\n\27\3\27\3\27\3\30\3\30\5")
        buf.write("\30\u0107\n\30\3\30\3\30\3\30\3\31\3\31\5\31\u010e\n\31")
        buf.write("\3\31\3\31\3\32\3\32\5\32\u0114\n\32\3\32\3\32\3\32\3")
        buf.write("\32\5\32\u011a\n\32\3\32\3\32\3\33\3\33\5\33\u0120\n\33")
        buf.write("\3\33\3\33\3\33\5\33\u0125\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u012d\n\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\5\37\u0139\n\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\5\"\u014a\n\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\5#\u0152\n#\3#\3#\3$\3$\3$\3$\3")
        buf.write("%\3%\5%\u015c\n%\3&\3&\3&\7&\u0161\n&\f&\16&\u0164\13")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u0175\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0180")
        buf.write("\n(\3)\3)\3)\3)\3*\3*\5*\u0188\n*\3*\3*\3*\3*\5*\u018e")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\5")
        buf.write(".\u01a0\n.\3.\3.\3/\3/\5/\u01a6\n/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\7\61\u01b0\n\61\f\61\16\61\u01b3\13\61")
        buf.write("\3\62\3\62\3\62\7\62\u01b8\n\62\f\62\16\62\u01bb\13\62")
        buf.write("\3\62\5\62\u01be\n\62\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\7\64\u01c7\n\64\f\64\16\64\u01ca\13\64\3\64\3\64\3")
        buf.write("\64\3\65\3\65\5\65\u01d1\n\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\2\5\b\n\f\67\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhj\2\t\4\2\37\37\"&\3\2\35\36\3\2\27\30\4\2\31\33")
        buf.write("((\3\2\t\f\3\29:\4\2\21\21\25\25\2\u01e3\2o\3\2\2\2\4")
        buf.write("z\3\2\2\2\6\u0081\3\2\2\2\b\u0083\3\2\2\2\n\u008e\3\2")
        buf.write("\2\2\f\u0099\3\2\2\2\16\u00a7\3\2\2\2\20\u00ac\3\2\2\2")
        buf.write("\22\u00b0\3\2\2\2\24\u00b5\3\2\2\2\26\u00bf\3\2\2\2\30")
        buf.write("\u00c6\3\2\2\2\32\u00c8\3\2\2\2\34\u00d2\3\2\2\2\36\u00d6")
        buf.write("\3\2\2\2 \u00d8\3\2\2\2\"\u00da\3\2\2\2$\u00e2\3\2\2\2")
        buf.write("&\u00e4\3\2\2\2(\u00f6\3\2\2\2*\u00fa\3\2\2\2,\u00fc\3")
        buf.write("\2\2\2.\u0106\3\2\2\2\60\u010d\3\2\2\2\62\u0113\3\2\2")
        buf.write("\2\64\u011f\3\2\2\2\66\u012c\3\2\2\28\u012e\3\2\2\2:\u0132")
        buf.write("\3\2\2\2<\u0136\3\2\2\2>\u013f\3\2\2\2@\u0143\3\2\2\2")
        buf.write("B\u0147\3\2\2\2D\u014e\3\2\2\2F\u0155\3\2\2\2H\u015b\3")
        buf.write("\2\2\2J\u015d\3\2\2\2L\u0174\3\2\2\2N\u017f\3\2\2\2P\u0181")
        buf.write("\3\2\2\2R\u0185\3\2\2\2T\u018f\3\2\2\2V\u0197\3\2\2\2")
        buf.write("X\u019a\3\2\2\2Z\u019d\3\2\2\2\\\u01a5\3\2\2\2^\u01a9")
        buf.write("\3\2\2\2`\u01b1\3\2\2\2b\u01bd\3\2\2\2d\u01bf\3\2\2\2")
        buf.write("f\u01c3\3\2\2\2h\u01ce\3\2\2\2j\u01d4\3\2\2\2lp\5\4\3")
        buf.write("\2mp\5N(\2np\5$\23\2ol\3\2\2\2om\3\2\2\2on\3\2\2\2pq\3")
        buf.write("\2\2\2qo\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\7\2\2\3t\3\3\2")
        buf.write("\2\2uv\5\6\4\2vw\7\'\2\2wx\5\6\4\2x{\3\2\2\2y{\5\6\4\2")
        buf.write("zu\3\2\2\2zy\3\2\2\2{\5\3\2\2\2|}\5\b\5\2}~\t\2\2\2~\177")
        buf.write("\5\b\5\2\177\u0082\3\2\2\2\u0080\u0082\5\b\5\2\u0081|")
        buf.write("\3\2\2\2\u0081\u0080\3\2\2\2\u0082\7\3\2\2\2\u0083\u0084")
        buf.write("\b\5\1\2\u0084\u0085\5\n\6\2\u0085\u008b\3\2\2\2\u0086")
        buf.write("\u0087\f\4\2\2\u0087\u0088\t\3\2\2\u0088\u008a\5\n\6\2")
        buf.write("\u0089\u0086\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3")
        buf.write("\2\2\2\u008b\u008c\3\2\2\2\u008c\t\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008e\u008f\b\6\1\2\u008f\u0090\5\f\7\2\u0090")
        buf.write("\u0096\3\2\2\2\u0091\u0092\f\4\2\2\u0092\u0093\t\4\2\2")
        buf.write("\u0093\u0095\5\f\7\2\u0094\u0091\3\2\2\2\u0095\u0098\3")
        buf.write("\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\13")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\b\7\1\2\u009a")
        buf.write("\u009b\5\16\b\2\u009b\u00a1\3\2\2\2\u009c\u009d\f\4\2")
        buf.write("\2\u009d\u009e\t\5\2\2\u009e\u00a0\5\16\b\2\u009f\u009c")
        buf.write("\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\r\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a5\7\34\2\2\u00a5\u00a8\5\16\b\2\u00a6\u00a8\5\20")
        buf.write("\t\2\u00a7\u00a4\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\17")
        buf.write("\3\2\2\2\u00a9\u00aa\7\30\2\2\u00aa\u00ad\5\20\t\2\u00ab")
        buf.write("\u00ad\5\22\n\2\u00ac\u00a9\3\2\2\2\u00ac\u00ab\3\2\2")
        buf.write("\2\u00ad\21\3\2\2\2\u00ae\u00b1\5j\66\2\u00af\u00b1\5")
        buf.write("\24\13\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\23\3\2\2\2\u00b2\u00b6\5*\26\2\u00b3\u00b6\5(\25\2\u00b4")
        buf.write("\u00b6\5\26\f\2\u00b5\u00b2\3\2\2\2\u00b5\u00b3\3\2\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\25\3\2\2\2\u00b7\u00c0\5")
        buf.write(",\27\2\u00b8\u00c0\5\30\r\2\u00b9\u00ba\7)\2\2\u00ba\u00bb")
        buf.write("\5\4\3\2\u00bb\u00bc\7*\2\2\u00bc\u00c0\3\2\2\2\u00bd")
        buf.write("\u00c0\79\2\2\u00be\u00c0\5D#\2\u00bf\u00b7\3\2\2\2\u00bf")
        buf.write("\u00b8\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00c0\27\3\2\2\2\u00c1\u00c7\7\66")
        buf.write("\2\2\u00c2\u00c7\7\65\2\2\u00c3\u00c7\7\67\2\2\u00c4\u00c7")
        buf.write("\78\2\2\u00c5\u00c7\5h\65\2\u00c6\u00c1\3\2\2\2\u00c6")
        buf.write("\u00c2\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7\31\3\2\2\2\u00c8\u00cd\5\4")
        buf.write("\3\2\u00c9\u00ca\7.\2\2\u00ca\u00cc\5\4\3\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\33\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0")
        buf.write("\u00d3\5\36\20\2\u00d1\u00d3\7\24\2\2\u00d2\u00d0\3\2")
        buf.write("\2\2\u00d2\u00d1\3\2\2\2\u00d3\35\3\2\2\2\u00d4\u00d7")
        buf.write("\5 \21\2\u00d5\u00d7\5\"\22\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\37\3\2\2\2\u00d8\u00d9\t\6\2\2\u00d9")
        buf.write("!\3\2\2\2\u00da\u00db\7+\2\2\u00db\u00dc\7\66\2\2\u00dc")
        buf.write("\u00dd\7,\2\2\u00dd\u00de\5 \21\2\u00de#\3\2\2\2\u00df")
        buf.write("\u00e3\5&\24\2\u00e0\u00e3\5F$\2\u00e1\u00e3\5\66\34\2")
        buf.write("\u00e2\u00df\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3")
        buf.write("\2\2\2\u00e3%\3\2\2\2\u00e4\u00e5\7\17\2\2\u00e5\u00e8")
        buf.write("\79\2\2\u00e6\u00e7\7\3\2\2\u00e7\u00e9\79\2\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00ef\7\61\2\2\u00eb\u00ee\5N(\2\u00ec\u00ee\5$\23\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3")
        buf.write("\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f2")
        buf.write("\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7\62\2\2\u00f3")
        buf.write("\'\3\2\2\2\u00f4\u00f7\5\60\31\2\u00f5\u00f7\5\64\33\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7)\3\2\2")
        buf.write("\2\u00f8\u00fb\5.\30\2\u00f9\u00fb\5\62\32\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb+\3\2\2\2\u00fc\u00fd")
        buf.write("\7\23\2\2\u00fd\u00fe\79\2\2\u00fe\u0100\7)\2\2\u00ff")
        buf.write("\u0101\5\32\16\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2")
        buf.write("\2\u0101\u0102\3\2\2\2\u0102\u0103\7*\2\2\u0103-\3\2\2")
        buf.write("\2\u0104\u0107\5\26\f\2\u0105\u0107\7\22\2\2\u0106\u0104")
        buf.write("\3\2\2\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\7-\2\2\u0109\u010a\79\2\2\u010a/\3\2\2\2\u010b")
        buf.write("\u010c\79\2\2\u010c\u010e\7-\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7:\2\2")
        buf.write("\u0110\61\3\2\2\2\u0111\u0114\5\26\f\2\u0112\u0114\7\22")
        buf.write("\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115\u0116\7-\2\2\u0116\u0117\79\2\2\u0117\u0119")
        buf.write("\7)\2\2\u0118\u011a\5\32\16\2\u0119\u0118\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\7*\2\2")
        buf.write("\u011c\63\3\2\2\2\u011d\u011e\79\2\2\u011e\u0120\7-\2")
        buf.write("\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0122\7:\2\2\u0122\u0124\7)\2\2\u0123\u0125")
        buf.write("\5\32\16\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0127\7*\2\2\u0127\65\3\2\2\2\u0128")
        buf.write("\u012d\58\35\2\u0129\u012d\5> \2\u012a\u012d\5:\36\2\u012b")
        buf.write("\u012d\5@!\2\u012c\u0128\3\2\2\2\u012c\u0129\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d\67\3\2\2\2\u012e")
        buf.write("\u012f\7\26\2\2\u012f\u0130\79\2\2\u0130\u0131\5<\37\2")
        buf.write("\u01319\3\2\2\2\u0132\u0133\7\26\2\2\u0133\u0134\7:\2")
        buf.write("\2\u0134\u0135\5<\37\2\u0135;\3\2\2\2\u0136\u0138\7)\2")
        buf.write("\2\u0137\u0139\5b\62\2\u0138\u0137\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\7*\2\2\u013b")
        buf.write("\u013c\7/\2\2\u013c\u013d\5\34\17\2\u013d\u013e\5^\60")
        buf.write("\2\u013e=\3\2\2\2\u013f\u0140\7\26\2\2\u0140\u0141\79")
        buf.write("\2\2\u0141\u0142\5B\"\2\u0142?\3\2\2\2\u0143\u0144\7\26")
        buf.write("\2\2\u0144\u0145\7:\2\2\u0145\u0146\5B\"\2\u0146A\3\2")
        buf.write("\2\2\u0147\u0149\7)\2\2\u0148\u014a\5b\62\2\u0149\u0148")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("\u014c\7*\2\2\u014c\u014d\5^\60\2\u014dC\3\2\2\2\u014e")
        buf.write("\u014f\t\7\2\2\u014f\u0151\7)\2\2\u0150\u0152\5\32\16")
        buf.write("\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0154\7*\2\2\u0154E\3\2\2\2\u0155\u0156")
        buf.write("\t\b\2\2\u0156\u0157\5H%\2\u0157\u0158\7\60\2\2\u0158")
        buf.write("G\3\2\2\2\u0159\u015c\5L\'\2\u015a\u015c\5J&\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015cI\3\2\2\2\u015d\u0162")
        buf.write("\t\7\2\2\u015e\u015f\7.\2\2\u015f\u0161\t\7\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0165\u0166\7/\2\2\u0166\u0167\5\36\20\2\u0167")
        buf.write("K\3\2\2\2\u0168\u0169\t\7\2\2\u0169\u016a\7.\2\2\u016a")
        buf.write("\u016b\5L\'\2\u016b\u016c\7.\2\2\u016c\u016d\5\4\3\2\u016d")
        buf.write("\u0175\3\2\2\2\u016e\u016f\t\7\2\2\u016f\u0170\7/\2\2")
        buf.write("\u0170\u0171\5\36\20\2\u0171\u0172\7!\2\2\u0172\u0173")
        buf.write("\5\4\3\2\u0173\u0175\3\2\2\2\u0174\u0168\3\2\2\2\u0174")
        buf.write("\u016e\3\2\2\2\u0175M\3\2\2\2\u0176\u0177\5P)\2\u0177")
        buf.write("\u0178\7\60\2\2\u0178\u0180\3\2\2\2\u0179\u0180\5R*\2")
        buf.write("\u017a\u0180\5T+\2\u017b\u0180\5V,\2\u017c\u0180\5X-\2")
        buf.write("\u017d\u0180\5Z.\2\u017e\u0180\5\\/\2\u017f\u0176\3\2")
        buf.write("\2\2\u017f\u0179\3\2\2\2\u017f\u017a\3\2\2\2\u017f\u017b")
        buf.write("\3\2\2\2\u017f\u017c\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180O\3\2\2\2\u0181\u0182\5\4\3\2\u0182")
        buf.write("\u0183\7 \2\2\u0183\u0184\5\4\3\2\u0184Q\3\2\2\2\u0185")
        buf.write("\u0187\7\6\2\2\u0186\u0188\5^\60\2\u0187\u0186\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\5")
        buf.write("\4\3\2\u018a\u018d\5^\60\2\u018b\u018c\7\7\2\2\u018c\u018e")
        buf.write("\5^\60\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("S\3\2\2\2\u018f\u0190\7\b\2\2\u0190\u0191\5P)\2\u0191")
        buf.write("\u0192\7\60\2\2\u0192\u0193\5\4\3\2\u0193\u0194\7\60\2")
        buf.write("\2\u0194\u0195\5P)\2\u0195\u0196\5^\60\2\u0196U\3\2\2")
        buf.write("\2\u0197\u0198\7\4\2\2\u0198\u0199\7\60\2\2\u0199W\3\2")
        buf.write("\2\2\u019a\u019b\7\5\2\2\u019b\u019c\7\60\2\2\u019cY\3")
        buf.write("\2\2\2\u019d\u019f\7\r\2\2\u019e\u01a0\5\4\3\2\u019f\u019e")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a2\7\60\2\2\u01a2[\3\2\2\2\u01a3\u01a6\5\62\32\2\u01a4")
        buf.write("\u01a6\5\64\33\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2")
        buf.write("\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\7\60\2\2\u01a8]\3\2")
        buf.write("\2\2\u01a9\u01aa\7\61\2\2\u01aa\u01ab\5`\61\2\u01ab\u01ac")
        buf.write("\7\62\2\2\u01ac_\3\2\2\2\u01ad\u01b0\5N(\2\u01ae\u01b0")
        buf.write("\5$\23\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0")
        buf.write("\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2a\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b9\5d\63")
        buf.write("\2\u01b5\u01b6\7.\2\2\u01b6\u01b8\5d\63\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01be\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01be\5f\64\2\u01bd\u01b4\3\2\2\2\u01bd\u01bc\3")
        buf.write("\2\2\2\u01bec\3\2\2\2\u01bf\u01c0\79\2\2\u01c0\u01c1\7")
        buf.write("/\2\2\u01c1\u01c2\5\36\20\2\u01c2e\3\2\2\2\u01c3\u01c8")
        buf.write("\79\2\2\u01c4\u01c5\7.\2\2\u01c5\u01c7\79\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01cb\u01cc\7/\2\2\u01cc\u01cd\5\36\20\2\u01cdg\3\2\2")
        buf.write("\2\u01ce\u01d0\7+\2\2\u01cf\u01d1\5\32\16\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d3\7,\2\2\u01d3i\3\2\2\2\u01d4\u01d5\79\2\2\u01d5")
        buf.write("\u01d6\7+\2\2\u01d6\u01d7\5\24\13\2\u01d7\u01d8\7,\2\2")
        buf.write("\u01d8k\3\2\2\2\61oqz\u0081\u008b\u0096\u00a1\u00a7\u00ac")
        buf.write("\u00b0\u00b5\u00bf\u00c6\u00cd\u00d2\u00d6\u00e2\u00e8")
        buf.write("\u00ed\u00ef\u00f6\u00fa\u0100\u0106\u010d\u0113\u0119")
        buf.write("\u011f\u0124\u012c\u0138\u0149\u0151\u015b\u0162\u0174")
        buf.write("\u017f\u0187\u018d\u019f\u01a5\u01af\u01b1\u01b9\u01bd")
        buf.write("\u01c8\u01d0")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'break'", "'continue'", "'if'", 
                     "'else'", "'for'", "'int'", "'float'", "'bool'", "'string'", 
                     "'return'", "'null'", "'class'", "'constructor'", "'var'", 
                     "'self'", "'new'", "'void'", "'const'", "'func'", "'+'", 
                     "'-'", "'*'", "'/'", "'\\'", "'!'", "'&&'", "'||'", 
                     "'=='", "':='", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "':'", "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "FOR", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
                      "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
                      "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "SLASH", "BACKSLASH", "NOT_OP", "AND_OP", "OR_OP", 
                      "EQUAL_OP", "ASSIGN_OP", "DECL_OP", "DIFF_OP", "LESS_OP", 
                      "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                      "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", "RSB", "DOT", 
                      "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "SIN_Q", 
                      "DOU_Q", "FLOAT_LIT", "INT_LIT", "STR_LIT", "BOOL_LIT", 
                      "ID", "AT_ID", "CMT_LINE", "CMT_BLOCK", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
    RULE_param = 49
    RULE_params_same_type = 50
    RULE_array_lit = 51
    RULE_arr_ele = 52

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
                   "body", "params_list", "param", "params_same_type", "array_lit", 
                   "arr_ele" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSE=5
    FOR=6
    INT=7
    FLOAT=8
    BOOL=9
    STRING=10
    RETURN=11
    NULL=12
    CLASS=13
    CONSTRUCTOR=14
    VAR=15
    SELF=16
    NEW=17
    VOID=18
    CONST=19
    FUNC=20
    ADD_OP=21
    SUB_OP=22
    MUL_OP=23
    SLASH=24
    BACKSLASH=25
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
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

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




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 109
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.exp()
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.stmt()
                    pass

                elif la_ == 3:
                    self.state = 108
                    self.decl()
                    pass


                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0)):
                    break

            self.state = 113
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




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.exp1()
                self.state = 116
                self.match(CSlangParser.CONCAT_OP)
                self.state = 117
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
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
        self.enterRule(localctx, 4, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.exp2(0)
                self.state = 123
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL_OP) | (1 << CSlangParser.DIFF_OP) | (1 << CSlangParser.LESS_OP) | (1 << CSlangParser.LESS_EQUAL_OP) | (1 << CSlangParser.GREATER_OP) | (1 << CSlangParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 124
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 132
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 133
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND_OP or _la==CSlangParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.exp3(0) 
                self.state = 139
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
            self.state = 141
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 143
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 144
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 145
                    self.exp4(0) 
                self.state = 150
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

        def SLASH(self):
            return self.getToken(CSlangParser.SLASH, 0)

        def BACKSLASH(self):
            return self.getToken(CSlangParser.BACKSLASH, 0)

        def MOD_OP(self):
            return self.getToken(CSlangParser.MOD_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp4



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
            self.state = 152
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 154
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 155
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL_OP) | (1 << CSlangParser.SLASH) | (1 << CSlangParser.BACKSLASH) | (1 << CSlangParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 156
                    self.exp5() 
                self.state = 161
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




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exp5)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(CSlangParser.NOT_OP)
                self.state = 163
                self.exp5()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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
        self.enterRule(localctx, 14, self.RULE_exp6)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(CSlangParser.SUB_OP)
                self.state = 168
                self.exp6()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
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
        self.enterRule(localctx, 16, self.RULE_exp7)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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




    def exp8(self):

        localctx = CSlangParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp8)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.inst_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.static_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
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




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp9)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.obj_cre()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(CSlangParser.LP)

                self.state = 184
                self.exp()
                self.state = 185
                self.match(CSlangParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.match(CSlangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
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




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [CSlangParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [CSlangParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(CSlangParser.BOOL_LIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
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




    def exp_list(self):

        localctx = CSlangParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.exp()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 199
                self.match(CSlangParser.COMMA)
                self.state = 200
                self.exp()
                self.state = 205
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




    def func_type(self):

        localctx = CSlangParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_type)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.ref_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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




    def ref_type(self):

        localctx = CSlangParser.Ref_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ref_type)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.value_type()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
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




    def value_type(self):

        localctx = CSlangParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_value_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
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




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(CSlangParser.LSB)
            self.state = 217
            self.match(CSlangParser.INT_LIT)
            self.state = 218
            self.match(CSlangParser.RSB)
            self.state = 219
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




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_decl)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.class_decl()
                pass
            elif token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
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




    def class_decl(self):

        localctx = CSlangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(CSlangParser.CLASS)
            self.state = 227
            self.match(CSlangParser.ID)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__0:
                self.state = 228
                self.match(CSlangParser.T__0)
                self.state = 229
                self.match(CSlangParser.ID)


            self.state = 232
            self.match(CSlangParser.LCB)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 235
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    self.state = 233
                    self.stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                    self.state = 234
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
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




    def static_access(self):

        localctx = CSlangParser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_static_access)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.static_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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




    def inst_access(self):

        localctx = CSlangParser.Inst_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_inst_access)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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




    def obj_cre(self):

        localctx = CSlangParser.Obj_creContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_obj_cre)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(CSlangParser.NEW)
            self.state = 251
            self.match(CSlangParser.ID)
            self.state = 252
            self.match(CSlangParser.LP)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 253
                self.exp_list()


            self.state = 256
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




    def mem_access(self):

        localctx = CSlangParser.Mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.state = 258
                self.exp9()
                pass
            elif token in [CSlangParser.SELF]:
                self.state = 259
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 262
            self.match(CSlangParser.DOT)
            self.state = 263
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




    def static_mem_access(self):

        localctx = CSlangParser.Static_mem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_static_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 265
                self.match(CSlangParser.ID)
                self.state = 266
                self.match(CSlangParser.DOT)


            self.state = 269
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




    def method_access(self):

        localctx = CSlangParser.Method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.state = 271
                self.exp9()
                pass
            elif token in [CSlangParser.SELF]:
                self.state = 272
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 275
            self.match(CSlangParser.DOT)
            self.state = 276
            self.match(CSlangParser.ID)
            self.state = 277
            self.match(CSlangParser.LP)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 278
                self.exp_list()


            self.state = 281
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




    def static_method_access(self):

        localctx = CSlangParser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 283
                self.match(CSlangParser.ID)
                self.state = 284
                self.match(CSlangParser.DOT)


            self.state = 287
            self.match(CSlangParser.AT_ID)
            self.state = 288
            self.match(CSlangParser.LP)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 289
                self.exp_list()


            self.state = 292
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




    def method_decl(self):

        localctx = CSlangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_method_decl)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.static_func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
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




    def func_decl(self):

        localctx = CSlangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(CSlangParser.FUNC)
            self.state = 301
            self.match(CSlangParser.ID)
            self.state = 302
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
        self.enterRule(localctx, 56, self.RULE_static_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(CSlangParser.FUNC)
            self.state = 305
            self.match(CSlangParser.AT_ID)
            self.state = 306
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




    def expo_func(self):

        localctx = CSlangParser.Expo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expo_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(CSlangParser.LP)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 309
                self.params_list()


            self.state = 312
            self.match(CSlangParser.RP)
            self.state = 313
            self.match(CSlangParser.COLON)
            self.state = 314
            self.func_type()
            self.state = 315
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




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(CSlangParser.FUNC)
            self.state = 318
            self.match(CSlangParser.ID)
            self.state = 319
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




    def static_constructor_decl(self):

        localctx = CSlangParser.Static_constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(CSlangParser.FUNC)
            self.state = 322
            self.match(CSlangParser.AT_ID)
            self.state = 323
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




    def expo_constructor(self):

        localctx = CSlangParser.Expo_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expo_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(CSlangParser.LP)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 326
                self.params_list()


            self.state = 329
            self.match(CSlangParser.RP)
            self.state = 330
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




    def func_call(self):

        localctx = CSlangParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 333
            self.match(CSlangParser.LP)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 334
                self.exp_list()


            self.state = 337
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




    def attr_decl(self):

        localctx = CSlangParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 340
            self.attr_decl_body()
            self.state = 341
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
        self.enterRule(localctx, 70, self.RULE_attr_decl_body)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.attr_decl_body_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
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




    def attr_decl_body_short(self):

        localctx = CSlangParser.Attr_decl_body_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_attr_decl_body_short)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
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
            while _la==CSlangParser.COMMA:
                self.state = 348
                self.match(CSlangParser.COMMA)
                self.state = 349
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 355
            self.match(CSlangParser.COLON)
            self.state = 356
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
        self.enterRule(localctx, 74, self.RULE_attr_decl_body_full)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self.match(CSlangParser.COMMA)
                self.state = 360
                self.attr_decl_body_full()
                self.state = 361
                self.match(CSlangParser.COMMA)
                self.state = 362
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 365
                self.match(CSlangParser.COLON)
                self.state = 366
                self.ref_type()
                self.state = 367
                self.match(CSlangParser.DECL_OP)
                self.state = 368
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




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.assign_stmt()
                self.state = 373
                self.match(CSlangParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 378
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 379
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 380
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




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.exp()
            self.state = 384
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 385
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
        self.enterRule(localctx, 80, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(CSlangParser.IF)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 388
                self.block_stmt()


            self.state = 391
            self.exp()
            self.state = 392
            self.block_stmt()
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 393
                self.match(CSlangParser.ELSE)
                self.state = 394
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
        self.enterRule(localctx, 82, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(CSlangParser.FOR)
            self.state = 398
            self.assign_stmt()
            self.state = 399
            self.match(CSlangParser.SEMICOLON)
            self.state = 400
            self.exp()
            self.state = 401
            self.match(CSlangParser.SEMICOLON)
            self.state = 402
            self.assign_stmt()
            self.state = 403
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
        self.enterRule(localctx, 84, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(CSlangParser.BREAK)
            self.state = 406
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
        self.enterRule(localctx, 86, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(CSlangParser.CONTINUE)
            self.state = 409
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
        self.enterRule(localctx, 88, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(CSlangParser.RETURN)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 412
                self.exp()


            self.state = 415
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




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 417
                self.method_access()
                pass

            elif la_ == 2:
                self.state = 418
                self.static_method_access()
                pass


            self.state = 421
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
        self.enterRule(localctx, 92, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(CSlangParser.LCB)
            self.state = 424
            self.body()
            self.state = 425
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




    def body(self):

        localctx = CSlangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CLASS) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 429
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                    self.state = 427
                    self.stmt()
                    pass
                elif token in [CSlangParser.CLASS, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                    self.state = 428
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 433
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

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParamContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def params_same_type(self):
            return self.getTypedRuleContext(CSlangParser.Params_same_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params_list




    def params_list(self):

        localctx = CSlangParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.param()
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.COMMA:
                    self.state = 435
                    self.match(CSlangParser.COMMA)
                    self.state = 436
                    self.param()
                    self.state = 441
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.params_same_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(CSlangParser.ID)
            self.state = 446
            self.match(CSlangParser.COLON)
            self.state = 447
            self.ref_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_same_typeContext(ParserRuleContext):
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
            return CSlangParser.RULE_params_same_type




    def params_same_type(self):

        localctx = CSlangParser.Params_same_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_params_same_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(CSlangParser.ID)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.COMMA:
                self.state = 450
                self.match(CSlangParser.COMMA)
                self.state = 451
                self.match(CSlangParser.ID)
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
            self.match(CSlangParser.COLON)
            self.state = 458
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




    def array_lit(self):

        localctx = CSlangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(CSlangParser.LSB)
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 461
                self.exp_list()


            self.state = 464
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




    def arr_ele(self):

        localctx = CSlangParser.Arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(CSlangParser.ID)
            self.state = 467
            self.match(CSlangParser.LSB)
            self.state = 468
            self.exp8()
            self.state = 469
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
         




