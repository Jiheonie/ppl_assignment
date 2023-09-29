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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0222\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0092\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u0099\n\4\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u00a0\n\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00a8\n\6\f\6\16")
        buf.write("\6\u00ab\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00b3\n\7\f")
        buf.write("\7\16\7\u00b6\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00be\n")
        buf.write("\b\f\b\16\b\u00c1\13\b\3\t\3\t\3\t\5\t\u00c6\n\t\3\n\3")
        buf.write("\n\3\n\5\n\u00cb\n\n\3\13\3\13\5\13\u00cf\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00de")
        buf.write("\n\f\f\f\16\f\u00e1\13\f\3\r\3\r\5\r\u00e5\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f0\n\16")
        buf.write("\3\17\3\17\5\17\u00f4\n\17\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00fd\n\21\3\22\3\22\5\22\u0101\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0108\n\23\3\24\3\24\5\24\u010c")
        buf.write("\n\24\3\25\3\25\5\25\u0110\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\27\3\27\5\27\u0119\n\27\3\30\3\30\3\31\3\31\5\31")
        buf.write("\u011f\n\31\3\32\3\32\3\32\5\32\u0124\n\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0135\n\34\3\35\3\35\5\35\u0139\n\35\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u013f\n\36\3\37\3\37\5\37\u0143")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\5!\u014e\n!\3\"\3\"\3")
        buf.write("\"\5\"\u0153\n\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\5%\u0162\n%\3&\3&\5&\u0166\n&\3&\3&\3\'\3\'\5\'\u016c")
        buf.write("\n\'\3\'\3\'\3\'\3\'\3\'\3(\3(\5(\u0175\n(\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\5+\u0185\n+\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\5\62\u01ab\n\62\3\63\3\63\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u01bd\n\64\3\65\3\65\3\65\3\65\5\65\u01c3\n")
        buf.write("\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u01cf\n\66\3\67\3\67\3\67\3\67\38\38\58\u01d7\n")
        buf.write("8\38\38\38\38\58\u01dd\n8\39\39\39\39\39\39\39\39\3:\3")
        buf.write(":\3:\3;\3;\3;\3<\3<\5<\u01ef\n<\3<\3<\3=\3=\3=\5=\u01f6")
        buf.write("\n=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\5?\u0202\n?\3@\3@\5")
        buf.write("@\u0206\n@\3A\3A\3A\3A\3A\5A\u020d\nA\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3C\5C\u0217\nC\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\2\6")
        buf.write("\n\f\16\26F\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\2\13\4\2!!$(\3\2\37 ")
        buf.write("\3\2\32\33\5\2\3\3\34\35**\3\2\669\3\2\f\17\3\2:;\4\2")
        buf.write("\f\f\27\27\4\2\24\24\30\30\2\u0218\2\u008a\3\2\2\2\4\u0091")
        buf.write("\3\2\2\2\6\u0098\3\2\2\2\b\u009f\3\2\2\2\n\u00a1\3\2\2")
        buf.write("\2\f\u00ac\3\2\2\2\16\u00b7\3\2\2\2\20\u00c5\3\2\2\2\22")
        buf.write("\u00ca\3\2\2\2\24\u00ce\3\2\2\2\26\u00d0\3\2\2\2\30\u00e4")
        buf.write("\3\2\2\2\32\u00ef\3\2\2\2\34\u00f3\3\2\2\2\36\u00f5\3")
        buf.write("\2\2\2 \u00fc\3\2\2\2\"\u0100\3\2\2\2$\u0107\3\2\2\2&")
        buf.write("\u010b\3\2\2\2(\u010f\3\2\2\2*\u0111\3\2\2\2,\u0118\3")
        buf.write("\2\2\2.\u011a\3\2\2\2\60\u011e\3\2\2\2\62\u0120\3\2\2")
        buf.write("\2\64\u012a\3\2\2\2\66\u0134\3\2\2\28\u0138\3\2\2\2:\u013e")
        buf.write("\3\2\2\2<\u0142\3\2\2\2>\u0144\3\2\2\2@\u014d\3\2\2\2")
        buf.write("B\u0152\3\2\2\2D\u0154\3\2\2\2F\u0158\3\2\2\2H\u0161\3")
        buf.write("\2\2\2J\u0165\3\2\2\2L\u016b\3\2\2\2N\u0174\3\2\2\2P\u0176")
        buf.write("\3\2\2\2R\u017a\3\2\2\2T\u0184\3\2\2\2V\u0186\3\2\2\2")
        buf.write("X\u018a\3\2\2\2Z\u018e\3\2\2\2\\\u0195\3\2\2\2^\u019d")
        buf.write("\3\2\2\2`\u01a4\3\2\2\2b\u01aa\3\2\2\2d\u01ac\3\2\2\2")
        buf.write("f\u01bc\3\2\2\2h\u01c2\3\2\2\2j\u01ce\3\2\2\2l\u01d0\3")
        buf.write("\2\2\2n\u01d4\3\2\2\2p\u01de\3\2\2\2r\u01e6\3\2\2\2t\u01e9")
        buf.write("\3\2\2\2v\u01ec\3\2\2\2x\u01f5\3\2\2\2z\u01f9\3\2\2\2")
        buf.write("|\u0201\3\2\2\2~\u0205\3\2\2\2\u0080\u020c\3\2\2\2\u0082")
        buf.write("\u020e\3\2\2\2\u0084\u0216\3\2\2\2\u0086\u0218\3\2\2\2")
        buf.write("\u0088\u021c\3\2\2\2\u008a\u008b\5\4\3\2\u008b\u008c\7")
        buf.write("\2\2\3\u008c\3\3\2\2\2\u008d\u008e\5\60\31\2\u008e\u008f")
        buf.write("\5\4\3\2\u008f\u0092\3\2\2\2\u0090\u0092\5\60\31\2\u0091")
        buf.write("\u008d\3\2\2\2\u0091\u0090\3\2\2\2\u0092\5\3\2\2\2\u0093")
        buf.write("\u0094\5\b\5\2\u0094\u0095\7)\2\2\u0095\u0096\5\b\5\2")
        buf.write("\u0096\u0099\3\2\2\2\u0097\u0099\5\b\5\2\u0098\u0093\3")
        buf.write("\2\2\2\u0098\u0097\3\2\2\2\u0099\7\3\2\2\2\u009a\u009b")
        buf.write("\5\n\6\2\u009b\u009c\t\2\2\2\u009c\u009d\5\n\6\2\u009d")
        buf.write("\u00a0\3\2\2\2\u009e\u00a0\5\n\6\2\u009f\u009a\3\2\2\2")
        buf.write("\u009f\u009e\3\2\2\2\u00a0\t\3\2\2\2\u00a1\u00a2\b\6\1")
        buf.write("\2\u00a2\u00a3\5\f\7\2\u00a3\u00a9\3\2\2\2\u00a4\u00a5")
        buf.write("\f\4\2\2\u00a5\u00a6\t\3\2\2\u00a6\u00a8\5\f\7\2\u00a7")
        buf.write("\u00a4\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\13\3\2\2\2\u00ab\u00a9\3\2")
        buf.write("\2\2\u00ac\u00ad\b\7\1\2\u00ad\u00ae\5\16\b\2\u00ae\u00b4")
        buf.write("\3\2\2\2\u00af\u00b0\f\4\2\2\u00b0\u00b1\t\4\2\2\u00b1")
        buf.write("\u00b3\5\16\b\2\u00b2\u00af\3\2\2\2\u00b3\u00b6\3\2\2")
        buf.write("\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\r\3\2")
        buf.write("\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\b\b\1\2\u00b8\u00b9")
        buf.write("\5\20\t\2\u00b9\u00bf\3\2\2\2\u00ba\u00bb\f\4\2\2\u00bb")
        buf.write("\u00bc\t\5\2\2\u00bc\u00be\5\20\t\2\u00bd\u00ba\3\2\2")
        buf.write("\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0")
        buf.write("\3\2\2\2\u00c0\17\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3")
        buf.write("\7\36\2\2\u00c3\u00c6\5\20\t\2\u00c4\u00c6\5\22\n\2\u00c5")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\21\3\2\2\2\u00c7")
        buf.write("\u00c8\7\33\2\2\u00c8\u00cb\5\22\n\2\u00c9\u00cb\5\24")
        buf.write("\13\2\u00ca\u00c7\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\23")
        buf.write("\3\2\2\2\u00cc\u00cf\5\u0088E\2\u00cd\u00cf\5\26\f\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\25\3\2\2\2\u00d0")
        buf.write("\u00d1\b\f\1\2\u00d1\u00d2\5\30\r\2\u00d2\u00df\3\2\2")
        buf.write("\2\u00d3\u00d4\f\5\2\2\u00d4\u00d5\7/\2\2\u00d5\u00de")
        buf.write("\7:\2\2\u00d6\u00d7\f\4\2\2\u00d7\u00d8\7/\2\2\u00d8\u00d9")
        buf.write("\7:\2\2\u00d9\u00da\7+\2\2\u00da\u00db\5\"\22\2\u00db")
        buf.write("\u00dc\7,\2\2\u00dc\u00de\3\2\2\2\u00dd\u00d3\3\2\2\2")
        buf.write("\u00dd\u00d6\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3")
        buf.write("\2\2\2\u00df\u00e0\3\2\2\2\u00e0\27\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e2\u00e5\5H%\2\u00e3\u00e5\5\32\16\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\31\3\2\2\2\u00e6")
        buf.write("\u00f0\5> \2\u00e7\u00f0\5\34\17\2\u00e8\u00e9\7+\2\2")
        buf.write("\u00e9\u00ea\5\6\4\2\u00ea\u00eb\7,\2\2\u00eb\u00f0\3")
        buf.write("\2\2\2\u00ec\u00f0\7:\2\2\u00ed\u00f0\5N(\2\u00ee\u00f0")
        buf.write("\7\21\2\2\u00ef\u00e6\3\2\2\2\u00ef\u00e7\3\2\2\2\u00ef")
        buf.write("\u00e8\3\2\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00ee\3\2\2\2\u00f0\33\3\2\2\2\u00f1\u00f4\5\36")
        buf.write("\20\2\u00f2\u00f4\5\u0086D\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\35\3\2\2\2\u00f5\u00f6\t\6\2\2\u00f6")
        buf.write("\37\3\2\2\2\u00f7\u00f8\5\36\20\2\u00f8\u00f9\7\60\2\2")
        buf.write("\u00f9\u00fa\5 \21\2\u00fa\u00fd\3\2\2\2\u00fb\u00fd\5")
        buf.write("\36\20\2\u00fc\u00f7\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write("!\3\2\2\2\u00fe\u0101\5$\23\2\u00ff\u0101\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101#\3\2\2\2\u0102")
        buf.write("\u0103\5\6\4\2\u0103\u0104\7\60\2\2\u0104\u0105\5$\23")
        buf.write("\2\u0105\u0108\3\2\2\2\u0106\u0108\5\6\4\2\u0107\u0102")
        buf.write("\3\2\2\2\u0107\u0106\3\2\2\2\u0108%\3\2\2\2\u0109\u010c")
        buf.write("\5(\25\2\u010a\u010c\7\27\2\2\u010b\u0109\3\2\2\2\u010b")
        buf.write("\u010a\3\2\2\2\u010c\'\3\2\2\2\u010d\u0110\5,\27\2\u010e")
        buf.write("\u0110\5*\26\2\u010f\u010d\3\2\2\2\u010f\u010e\3\2\2\2")
        buf.write("\u0110)\3\2\2\2\u0111\u0112\7-\2\2\u0112\u0113\7\67\2")
        buf.write("\2\u0113\u0114\7.\2\2\u0114\u0115\5,\27\2\u0115+\3\2\2")
        buf.write("\2\u0116\u0119\5.\30\2\u0117\u0119\7:\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0118\u0117\3\2\2\2\u0119-\3\2\2\2\u011a\u011b")
        buf.write("\t\7\2\2\u011b/\3\2\2\2\u011c\u011f\5\62\32\2\u011d\u011f")
        buf.write("\5\64\33\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f")
        buf.write("\61\3\2\2\2\u0120\u0123\7\22\2\2\u0121\u0122\7:\2\2\u0122")
        buf.write("\u0124\7\4\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\u0126\7:\2\2\u0126\u0127\7")
        buf.write("\63\2\2\u0127\u0128\5\66\34\2\u0128\u0129\7\64\2\2\u0129")
        buf.write("\63\3\2\2\2\u012a\u012b\7\22\2\2\u012b\u012c\7\5\2\2\u012c")
        buf.write("\u012d\7\63\2\2\u012d\u012e\5:\36\2\u012e\u012f\7\64\2")
        buf.write("\2\u012f\65\3\2\2\2\u0130\u0131\58\35\2\u0131\u0132\5")
        buf.write("\66\34\2\u0132\u0135\3\2\2\2\u0133\u0135\3\2\2\2\u0134")
        buf.write("\u0130\3\2\2\2\u0134\u0133\3\2\2\2\u0135\67\3\2\2\2\u0136")
        buf.write("\u0139\5`\61\2\u0137\u0139\5T+\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u01399\3\2\2\2\u013a\u013b\5<\37\2\u013b")
        buf.write("\u013c\5:\36\2\u013c\u013f\3\2\2\2\u013d\u013f\3\2\2\2")
        buf.write("\u013e\u013a\3\2\2\2\u013e\u013d\3\2\2\2\u013f;\3\2\2")
        buf.write("\2\u0140\u0143\58\35\2\u0141\u0143\5\\/\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0141\3\2\2\2\u0143=\3\2\2\2\u0144\u0145")
        buf.write("\7\26\2\2\u0145\u0146\7:\2\2\u0146\u0147\7+\2\2\u0147")
        buf.write("\u0148\5\"\22\2\u0148\u0149\7,\2\2\u0149?\3\2\2\2\u014a")
        buf.write("\u014e\5D#\2\u014b\u014e\5J&\2\u014c\u014e\5P)\2\u014d")
        buf.write("\u014a\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014eA\3\2\2\2\u014f\u0153\5F$\2\u0150\u0153\5L\'\2\u0151")
        buf.write("\u0153\5R*\2\u0152\u014f\3\2\2\2\u0152\u0150\3\2\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153C\3\2\2\2\u0154\u0155\5\26\f\2\u0155")
        buf.write("\u0156\7/\2\2\u0156\u0157\7:\2\2\u0157E\3\2\2\2\u0158")
        buf.write("\u0159\5\26\f\2\u0159\u015a\7/\2\2\u015a\u015b\7:\2\2")
        buf.write("\u015b\u015c\7+\2\2\u015c\u015d\5\"\22\2\u015d\u015e\7")
        buf.write(",\2\2\u015eG\3\2\2\2\u015f\u0162\5J&\2\u0160\u0162\5L")
        buf.write("\'\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162I\3")
        buf.write("\2\2\2\u0163\u0164\7:\2\2\u0164\u0166\7/\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0168\7;\2\2\u0168K\3\2\2\2\u0169\u016a\7:\2\2\u016a")
        buf.write("\u016c\7/\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016e\7;\2\2\u016e\u016f\7")
        buf.write("+\2\2\u016f\u0170\5\"\22\2\u0170\u0171\7,\2\2\u0171M\3")
        buf.write("\2\2\2\u0172\u0175\5P)\2\u0173\u0175\5R*\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0173\3\2\2\2\u0175O\3\2\2\2\u0176\u0177")
        buf.write("\7\25\2\2\u0177\u0178\7/\2\2\u0178\u0179\t\b\2\2\u0179")
        buf.write("Q\3\2\2\2\u017a\u017b\7\25\2\2\u017b\u017c\7/\2\2\u017c")
        buf.write("\u017d\t\b\2\2\u017d\u017e\7+\2\2\u017e\u017f\5\"\22\2")
        buf.write("\u017f\u0180\7,\2\2\u0180S\3\2\2\2\u0181\u0185\5V,\2\u0182")
        buf.write("\u0185\5^\60\2\u0183\u0185\5X-\2\u0184\u0181\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0183\3\2\2\2\u0185U\3\2\2\2\u0186")
        buf.write("\u0187\7\31\2\2\u0187\u0188\7:\2\2\u0188\u0189\5Z.\2\u0189")
        buf.write("W\3\2\2\2\u018a\u018b\7\31\2\2\u018b\u018c\7;\2\2\u018c")
        buf.write("\u018d\5Z.\2\u018dY\3\2\2\2\u018e\u018f\7+\2\2\u018f\u0190")
        buf.write("\5~@\2\u0190\u0191\7,\2\2\u0191\u0192\7\61\2\2\u0192\u0193")
        buf.write("\5&\24\2\u0193\u0194\5z>\2\u0194[\3\2\2\2\u0195\u0196")
        buf.write("\7\31\2\2\u0196\u0197\7\6\2\2\u0197\u0198\7+\2\2\u0198")
        buf.write("\u0199\7,\2\2\u0199\u019a\7\61\2\2\u019a\u019b\t\t\2\2")
        buf.write("\u019b\u019c\5z>\2\u019c]\3\2\2\2\u019d\u019e\7\31\2\2")
        buf.write("\u019e\u019f\7\23\2\2\u019f\u01a0\7+\2\2\u01a0\u01a1\5")
        buf.write("~@\2\u01a1\u01a2\7,\2\2\u01a2\u01a3\5z>\2\u01a3_\3\2\2")
        buf.write("\2\u01a4\u01a5\t\n\2\2\u01a5\u01a6\5b\62\2\u01a6\u01a7")
        buf.write("\7\62\2\2\u01a7a\3\2\2\2\u01a8\u01ab\5f\64\2\u01a9\u01ab")
        buf.write("\5d\63\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("c\3\2\2\2\u01ac\u01ad\5h\65\2\u01ad\u01ae\7\61\2\2\u01ae")
        buf.write("\u01af\5(\25\2\u01afe\3\2\2\2\u01b0\u01b1\t\b\2\2\u01b1")
        buf.write("\u01b2\7\60\2\2\u01b2\u01b3\5f\64\2\u01b3\u01b4\7\60\2")
        buf.write("\2\u01b4\u01b5\5\6\4\2\u01b5\u01bd\3\2\2\2\u01b6\u01b7")
        buf.write("\t\b\2\2\u01b7\u01b8\7\61\2\2\u01b8\u01b9\5(\25\2\u01b9")
        buf.write("\u01ba\7#\2\2\u01ba\u01bb\5\6\4\2\u01bb\u01bd\3\2\2\2")
        buf.write("\u01bc\u01b0\3\2\2\2\u01bc\u01b6\3\2\2\2\u01bdg\3\2\2")
        buf.write("\2\u01be\u01bf\t\b\2\2\u01bf\u01c0\7\60\2\2\u01c0\u01c3")
        buf.write("\5h\65\2\u01c1\u01c3\t\b\2\2\u01c2\u01be\3\2\2\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c3i\3\2\2\2\u01c4\u01c5\5l\67\2\u01c5")
        buf.write("\u01c6\7\62\2\2\u01c6\u01cf\3\2\2\2\u01c7\u01cf\5n8\2")
        buf.write("\u01c8\u01cf\5p9\2\u01c9\u01cf\5r:\2\u01ca\u01cf\5t;\2")
        buf.write("\u01cb\u01cf\5v<\2\u01cc\u01cf\5x=\2\u01cd\u01cf\5`\61")
        buf.write("\2\u01ce\u01c4\3\2\2\2\u01ce\u01c7\3\2\2\2\u01ce\u01c8")
        buf.write("\3\2\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01ca\3\2\2\2\u01ce")
        buf.write("\u01cb\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2")
        buf.write("\u01cfk\3\2\2\2\u01d0\u01d1\5\24\13\2\u01d1\u01d2\7\"")
        buf.write("\2\2\u01d2\u01d3\5\6\4\2\u01d3m\3\2\2\2\u01d4\u01d6\7")
        buf.write("\t\2\2\u01d5\u01d7\5z>\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\5\6\4\2\u01d9")
        buf.write("\u01dc\5z>\2\u01da\u01db\7\n\2\2\u01db\u01dd\5z>\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01ddo\3\2\2\2\u01de")
        buf.write("\u01df\7\13\2\2\u01df\u01e0\5l\67\2\u01e0\u01e1\7\62\2")
        buf.write("\2\u01e1\u01e2\5\6\4\2\u01e2\u01e3\7\62\2\2\u01e3\u01e4")
        buf.write("\5l\67\2\u01e4\u01e5\5z>\2\u01e5q\3\2\2\2\u01e6\u01e7")
        buf.write("\7\7\2\2\u01e7\u01e8\7\62\2\2\u01e8s\3\2\2\2\u01e9\u01ea")
        buf.write("\7\b\2\2\u01ea\u01eb\7\62\2\2\u01ebu\3\2\2\2\u01ec\u01ee")
        buf.write("\7\20\2\2\u01ed\u01ef\5\6\4\2\u01ee\u01ed\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\7\62\2")
        buf.write("\2\u01f1w\3\2\2\2\u01f2\u01f6\5F$\2\u01f3\u01f6\5L\'\2")
        buf.write("\u01f4\u01f6\5R*\2\u01f5\u01f2\3\2\2\2\u01f5\u01f3\3\2")
        buf.write("\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8")
        buf.write("\7\62\2\2\u01f8y\3\2\2\2\u01f9\u01fa\7\63\2\2\u01fa\u01fb")
        buf.write("\5|?\2\u01fb\u01fc\7\64\2\2\u01fc{\3\2\2\2\u01fd\u01fe")
        buf.write("\5j\66\2\u01fe\u01ff\5|?\2\u01ff\u0202\3\2\2\2\u0200\u0202")
        buf.write("\3\2\2\2\u0201\u01fd\3\2\2\2\u0201\u0200\3\2\2\2\u0202")
        buf.write("}\3\2\2\2\u0203\u0206\5\u0080A\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0205\u0204\3\2\2\2\u0206\177\3\2\2\2\u0207")
        buf.write("\u0208\5\u0082B\2\u0208\u0209\7\60\2\2\u0209\u020a\5\u0080")
        buf.write("A\2\u020a\u020d\3\2\2\2\u020b\u020d\5\u0082B\2\u020c\u0207")
        buf.write("\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u0081\3\2\2\2\u020e")
        buf.write("\u020f\5\u0084C\2\u020f\u0210\7\61\2\2\u0210\u0211\5(")
        buf.write("\25\2\u0211\u0083\3\2\2\2\u0212\u0213\7:\2\2\u0213\u0214")
        buf.write("\7\60\2\2\u0214\u0217\5\u0084C\2\u0215\u0217\7:\2\2\u0216")
        buf.write("\u0212\3\2\2\2\u0216\u0215\3\2\2\2\u0217\u0085\3\2\2\2")
        buf.write("\u0218\u0219\7-\2\2\u0219\u021a\5 \21\2\u021a\u021b\7")
        buf.write(".\2\2\u021b\u0087\3\2\2\2\u021c\u021d\5\26\f\2\u021d\u021e")
        buf.write("\7-\2\2\u021e\u021f\5\6\4\2\u021f\u0220\7.\2\2\u0220\u0089")
        buf.write("\3\2\2\2/\u0091\u0098\u009f\u00a9\u00b4\u00bf\u00c5\u00ca")
        buf.write("\u00ce\u00dd\u00df\u00e4\u00ef\u00f3\u00fc\u0100\u0107")
        buf.write("\u010b\u010f\u0118\u011e\u0123\u0134\u0138\u013e\u0142")
        buf.write("\u014d\u0152\u0161\u0165\u016b\u0174\u0184\u01aa\u01bc")
        buf.write("\u01c2\u01ce\u01d6\u01dc\u01ee\u01f5\u0201\u0205\u020c")
        buf.write("\u0216")
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
                     "';'", "'{'", "'}'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAM_CLASS", 
                      "MAIN", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                      "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                      "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                      "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
                      "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", 
                      "GREATER_OP", "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", 
                      "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "COLON", 
                      "SEMICOLON", "LCB", "RCB", "DOU_Q", "FLOAT_LIT", "INT_LIT", 
                      "STR_LIT", "BOOL_LIT", "ID", "AT_ID", "CMT_LINE", 
                      "CMT_BLOCK", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

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
    RULE_ele_literal = 14
    RULE_ele_literal_list = 15
    RULE_exp_list = 16
    RULE_exp_prime = 17
    RULE_func_type = 18
    RULE_ref_type = 19
    RULE_array_type = 20
    RULE_ele_type = 21
    RULE_value_type = 22
    RULE_prog_decl = 23
    RULE_class_decl = 24
    RULE_program_class_decl = 25
    RULE_class_mem_list = 26
    RULE_class_mem = 27
    RULE_prog_class_mem_list = 28
    RULE_prog_class_mem = 29
    RULE_obj_cre = 30
    RULE_mem_access = 31
    RULE_method_access = 32
    RULE_inst_mem_access = 33
    RULE_inst_method_access = 34
    RULE_static_access = 35
    RULE_static_mem_access = 36
    RULE_static_method_access = 37
    RULE_self_access = 38
    RULE_self_mem_access = 39
    RULE_self_method_access = 40
    RULE_method_decl = 41
    RULE_func_decl = 42
    RULE_static_func_decl = 43
    RULE_expo_func = 44
    RULE_main_func_decl = 45
    RULE_constructor_decl = 46
    RULE_attr_decl = 47
    RULE_attr_decl_body = 48
    RULE_attr_decl_body_short = 49
    RULE_attr_decl_body_full = 50
    RULE_identifier_list = 51
    RULE_stmt = 52
    RULE_assign_stmt = 53
    RULE_if_stmt = 54
    RULE_for_stmt = 55
    RULE_break_stmt = 56
    RULE_continue_stmt = 57
    RULE_return_stmt = 58
    RULE_method_invocation_stmt = 59
    RULE_block_stmt = 60
    RULE_body = 61
    RULE_params_list = 62
    RULE_params_prime = 63
    RULE_params_1_type = 64
    RULE_id_list_not_null = 65
    RULE_array_lit = 66
    RULE_arr_ele = 67

    ruleNames =  [ "program", "prog_decl_list", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", 
                   "literal", "ele_literal", "ele_literal_list", "exp_list", 
                   "exp_prime", "func_type", "ref_type", "array_type", "ele_type", 
                   "value_type", "prog_decl", "class_decl", "program_class_decl", 
                   "class_mem_list", "class_mem", "prog_class_mem_list", 
                   "prog_class_mem", "obj_cre", "mem_access", "method_access", 
                   "inst_mem_access", "inst_method_access", "static_access", 
                   "static_mem_access", "static_method_access", "self_access", 
                   "self_mem_access", "self_method_access", "method_decl", 
                   "func_decl", "static_func_decl", "expo_func", "main_func_decl", 
                   "constructor_decl", "attr_decl", "attr_decl_body", "attr_decl_body_short", 
                   "attr_decl_body_full", "identifier_list", "stmt", "assign_stmt", 
                   "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invocation_stmt", "block_stmt", 
                   "body", "params_list", "params_prime", "params_1_type", 
                   "id_list_not_null", "array_lit", "arr_ele" ]

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
    DOU_Q=51
    FLOAT_LIT=52
    INT_LIT=53
    STR_LIT=54
    BOOL_LIT=55
    ID=56
    AT_ID=57
    CMT_LINE=58
    CMT_BLOCK=59
    WS=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62
    ERROR_CHAR=63

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
            self.state = 136
            self.prog_decl_list()
            self.state = 137
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.prog_decl()
                self.state = 140
                self.prog_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.exp1()
                self.state = 146
                self.match(CSlangParser.CONCAT_OP)
                self.state = 147
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.exp2(0)
                self.state = 153
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL_OP) | (1 << CSlangParser.DIFF_OP) | (1 << CSlangParser.LESS_OP) | (1 << CSlangParser.LESS_EQUAL_OP) | (1 << CSlangParser.GREATER_OP) | (1 << CSlangParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
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
            self.state = 160
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 162
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 163
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND_OP or _la==CSlangParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 164
                    self.exp3(0) 
                self.state = 169
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
            self.state = 171
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 175
                    self.exp4(0) 
                self.state = 180
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
            self.state = 182
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.T__0) | (1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.exp5() 
                self.state = 191
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(CSlangParser.NOT_OP)
                self.state = 193
                self.exp5()
                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
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
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(CSlangParser.SUB_OP)
                self.state = 198
                self.exp6()
                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
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
            self.state = 207
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 209
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 210
                        self.match(CSlangParser.DOT)
                        self.state = 211
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 212
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 213
                        self.match(CSlangParser.DOT)
                        self.state = 214
                        self.match(CSlangParser.ID)
                        self.state = 215
                        self.match(CSlangParser.LP)
                        self.state = 216
                        self.exp_list()
                        self.state = 217
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 223
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.static_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
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

        def self_access(self):
            return self.getTypedRuleContext(CSlangParser.Self_accessContext,0)


        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp10




    def exp10(self):

        localctx = CSlangParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp10)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.obj_cre()
                pass
            elif token in [CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.literal()
                pass
            elif token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(CSlangParser.LP)

                self.state = 231
                self.exp()
                self.state = 232
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 235
                self.self_access()
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 236
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

        def ele_literal(self):
            return self.getTypedRuleContext(CSlangParser.Ele_literalContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(CSlangParser.Array_litContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.ele_literal()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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


    class Ele_literalContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return CSlangParser.RULE_ele_literal




    def ele_literal(self):

        localctx = CSlangParser.Ele_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ele_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT))) != 0)):
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


    class Ele_literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele_literal(self):
            return self.getTypedRuleContext(CSlangParser.Ele_literalContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def ele_literal_list(self):
            return self.getTypedRuleContext(CSlangParser.Ele_literal_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_ele_literal_list




    def ele_literal_list(self):

        localctx = CSlangParser.Ele_literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ele_literal_list)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.ele_literal()
                self.state = 246
                self.match(CSlangParser.COMMA)
                self.state = 247
                self.ele_literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.ele_literal()
                pass


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
        self.enterRule(localctx, 32, self.RULE_exp_list)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.NOT_OP, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.exp_prime()
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
        self.enterRule(localctx, 34, self.RULE_exp_prime)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.exp()
                self.state = 257
                self.match(CSlangParser.COMMA)
                self.state = 258
                self.exp_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
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
        self.enterRule(localctx, 36, self.RULE_func_type)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LSB, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.ref_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 38, self.RULE_ref_type)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.ele_type()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
        self.enterRule(localctx, 40, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(CSlangParser.LSB)
            self.state = 272
            self.match(CSlangParser.INT_LIT)
            self.state = 273
            self.match(CSlangParser.RSB)
            self.state = 274
            self.ele_type()
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

        def value_type(self):
            return self.getTypedRuleContext(CSlangParser.Value_typeContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_ele_type




    def ele_type(self):

        localctx = CSlangParser.Ele_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ele_type)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.value_type()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(CSlangParser.ID)
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
        self.enterRule(localctx, 44, self.RULE_value_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
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
        self.enterRule(localctx, 46, self.RULE_prog_decl)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.class_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
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
        self.enterRule(localctx, 48, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(CSlangParser.CLASS)
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 287
                self.match(CSlangParser.ID)
                self.state = 288
                self.match(CSlangParser.T__1)


            self.state = 291
            self.match(CSlangParser.ID)
            self.state = 292
            self.match(CSlangParser.LCB)
            self.state = 293
            self.class_mem_list()
            self.state = 294
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
        self.enterRule(localctx, 50, self.RULE_program_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(CSlangParser.CLASS)
            self.state = 297
            self.match(CSlangParser.PROGRAM_CLASS)
            self.state = 298
            self.match(CSlangParser.LCB)
            self.state = 299
            self.prog_class_mem_list()
            self.state = 300
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
        self.enterRule(localctx, 52, self.RULE_class_mem_list)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.class_mem()
                self.state = 303
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
        self.enterRule(localctx, 54, self.RULE_class_mem)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.attr_decl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
        self.enterRule(localctx, 56, self.RULE_prog_class_mem_list)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.prog_class_mem()
                self.state = 313
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
        self.enterRule(localctx, 58, self.RULE_prog_class_mem)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.class_mem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
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
        self.enterRule(localctx, 60, self.RULE_obj_cre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(CSlangParser.NEW)
            self.state = 323
            self.match(CSlangParser.ID)
            self.state = 324
            self.match(CSlangParser.LP)
            self.state = 325
            self.exp_list()
            self.state = 326
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
        self.enterRule(localctx, 62, self.RULE_mem_access)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.inst_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.static_mem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
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
        self.enterRule(localctx, 64, self.RULE_method_access)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.inst_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.static_method_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
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
        self.enterRule(localctx, 66, self.RULE_inst_mem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.exp8(0)
            self.state = 339
            self.match(CSlangParser.DOT)
            self.state = 340
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
        self.enterRule(localctx, 68, self.RULE_inst_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.exp8(0)
            self.state = 343
            self.match(CSlangParser.DOT)
            self.state = 344
            self.match(CSlangParser.ID)
            self.state = 345
            self.match(CSlangParser.LP)
            self.state = 346
            self.exp_list()
            self.state = 347
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
        self.enterRule(localctx, 70, self.RULE_static_access)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.static_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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
        self.enterRule(localctx, 72, self.RULE_static_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 353
                self.match(CSlangParser.ID)
                self.state = 354
                self.match(CSlangParser.DOT)


            self.state = 357
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
        self.enterRule(localctx, 74, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 359
                self.match(CSlangParser.ID)
                self.state = 360
                self.match(CSlangParser.DOT)


            self.state = 363
            self.match(CSlangParser.AT_ID)
            self.state = 364
            self.match(CSlangParser.LP)
            self.state = 365
            self.exp_list()
            self.state = 366
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
        self.enterRule(localctx, 76, self.RULE_self_access)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.self_mem_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
        self.enterRule(localctx, 78, self.RULE_self_mem_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(CSlangParser.SELF)
            self.state = 373
            self.match(CSlangParser.DOT)
            self.state = 374
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
        self.enterRule(localctx, 80, self.RULE_self_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(CSlangParser.SELF)
            self.state = 377
            self.match(CSlangParser.DOT)
            self.state = 378
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 379
            self.match(CSlangParser.LP)
            self.state = 380
            self.exp_list()
            self.state = 381
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
        self.enterRule(localctx, 82, self.RULE_method_decl)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
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
        self.enterRule(localctx, 84, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(CSlangParser.FUNC)
            self.state = 389
            self.match(CSlangParser.ID)
            self.state = 390
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
        self.enterRule(localctx, 86, self.RULE_static_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(CSlangParser.FUNC)
            self.state = 393
            self.match(CSlangParser.AT_ID)
            self.state = 394
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
        self.enterRule(localctx, 88, self.RULE_expo_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(CSlangParser.LP)
            self.state = 397
            self.params_list()
            self.state = 398
            self.match(CSlangParser.RP)
            self.state = 399
            self.match(CSlangParser.COLON)
            self.state = 400
            self.func_type()
            self.state = 401
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

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_main_func_decl




    def main_func_decl(self):

        localctx = CSlangParser.Main_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_main_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(CSlangParser.FUNC)
            self.state = 404
            self.match(CSlangParser.MAIN)
            self.state = 405
            self.match(CSlangParser.LP)
            self.state = 406
            self.match(CSlangParser.RP)
            self.state = 407
            self.match(CSlangParser.COLON)
            self.state = 408
            _la = self._input.LA(1)
            if not(_la==CSlangParser.INT or _la==CSlangParser.VOID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 409
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
        self.enterRule(localctx, 92, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(CSlangParser.FUNC)
            self.state = 412
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 413
            self.match(CSlangParser.LP)
            self.state = 414
            self.params_list()
            self.state = 415
            self.match(CSlangParser.RP)
            self.state = 416
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
        self.enterRule(localctx, 94, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 419
            self.attr_decl_body()
            self.state = 420
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
        self.enterRule(localctx, 96, self.RULE_attr_decl_body)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.attr_decl_body_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
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
        self.enterRule(localctx, 98, self.RULE_attr_decl_body_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.identifier_list()
            self.state = 427
            self.match(CSlangParser.COLON)
            self.state = 428
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
        self.enterRule(localctx, 100, self.RULE_attr_decl_body_full)
        self._la = 0 # Token type
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 431
                self.match(CSlangParser.COMMA)
                self.state = 432
                self.attr_decl_body_full()
                self.state = 433
                self.match(CSlangParser.COMMA)
                self.state = 434
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self.match(CSlangParser.COLON)
                self.state = 438
                self.ref_type()
                self.state = 439
                self.match(CSlangParser.DECL_OP)
                self.state = 440
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
        self.enterRule(localctx, 102, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 445
                self.match(CSlangParser.COMMA)
                self.state = 446
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
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
        self.enterRule(localctx, 104, self.RULE_stmt)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.assign_stmt()
                self.state = 451
                self.match(CSlangParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 456
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 457
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 458
                self.method_invocation_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 459
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
        self.enterRule(localctx, 106, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.exp7()
            self.state = 463
            self.match(CSlangParser.ASSIGN_OP)
            self.state = 464
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
        self.enterRule(localctx, 108, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(CSlangParser.IF)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 467
                self.block_stmt()


            self.state = 470
            self.exp()
            self.state = 471
            self.block_stmt()
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 472
                self.match(CSlangParser.ELSE)
                self.state = 473
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
        self.enterRule(localctx, 110, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(CSlangParser.FOR)
            self.state = 477
            self.assign_stmt()
            self.state = 478
            self.match(CSlangParser.SEMICOLON)
            self.state = 479
            self.exp()
            self.state = 480
            self.match(CSlangParser.SEMICOLON)
            self.state = 481
            self.assign_stmt()
            self.state = 482
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
        self.enterRule(localctx, 112, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(CSlangParser.BREAK)
            self.state = 485
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
        self.enterRule(localctx, 114, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(CSlangParser.CONTINUE)
            self.state = 488
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
        self.enterRule(localctx, 116, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(CSlangParser.RETURN)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STR_LIT) | (1 << CSlangParser.BOOL_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 491
                self.exp()


            self.state = 494
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
        self.enterRule(localctx, 118, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 496
                self.inst_method_access()
                pass

            elif la_ == 2:
                self.state = 497
                self.static_method_access()
                pass

            elif la_ == 3:
                self.state = 498
                self.self_method_access()
                pass


            self.state = 501
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
        self.enterRule(localctx, 120, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(CSlangParser.LCB)
            self.state = 504
            self.body()
            self.state = 505
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
        self.enterRule(localctx, 122, self.RULE_body)
        try:
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.LP, CSlangParser.LSB, CSlangParser.FLOAT_LIT, CSlangParser.INT_LIT, CSlangParser.STR_LIT, CSlangParser.BOOL_LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.stmt()
                self.state = 508
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
        self.enterRule(localctx, 124, self.RULE_params_list)
        try:
            self.state = 515
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
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
        self.enterRule(localctx, 126, self.RULE_params_prime)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.params_1_type()
                self.state = 518
                self.match(CSlangParser.COMMA)
                self.state = 519
                self.params_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
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

        def id_list_not_null(self):
            return self.getTypedRuleContext(CSlangParser.Id_list_not_nullContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def ref_type(self):
            return self.getTypedRuleContext(CSlangParser.Ref_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params_1_type




    def params_1_type(self):

        localctx = CSlangParser.Params_1_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_params_1_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.id_list_not_null()
            self.state = 525
            self.match(CSlangParser.COLON)
            self.state = 526
            self.ref_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_list_not_nullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def id_list_not_null(self):
            return self.getTypedRuleContext(CSlangParser.Id_list_not_nullContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_id_list_not_null




    def id_list_not_null(self):

        localctx = CSlangParser.Id_list_not_nullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_id_list_not_null)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(CSlangParser.ID)
                self.state = 529
                self.match(CSlangParser.COMMA)
                self.state = 530
                self.id_list_not_null()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.match(CSlangParser.ID)
                pass


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

        def ele_literal_list(self):
            return self.getTypedRuleContext(CSlangParser.Ele_literal_listContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_lit




    def array_lit(self):

        localctx = CSlangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(CSlangParser.LSB)
            self.state = 535
            self.ele_literal_list()
            self.state = 536
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
        self.enterRule(localctx, 134, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.exp8(0)
            self.state = 539
            self.match(CSlangParser.LSB)
            self.state = 540
            self.exp()
            self.state = 541
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
         




