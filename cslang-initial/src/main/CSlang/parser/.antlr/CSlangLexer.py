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
        buf.write("\u01cf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\3\64\5\64\u0141")
        buf.write("\n\64\3\64\3\64\5\64\u0145\n\64\3\65\3\65\7\65\u0149\n")
        buf.write("\65\f\65\16\65\u014c\13\65\3\66\3\66\5\66\u0150\n\66\3")
        buf.write("\66\3\66\3\67\6\67\u0155\n\67\r\67\16\67\u0156\38\38\3")
        buf.write("8\78\u015c\n8\f8\168\u015f\138\38\38\38\39\59\u0165\n")
        buf.write("9\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0177")
        buf.write("\n:\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u0182\n;\3<\3<\7<\u0186")
        buf.write("\n<\f<\16<\u0189\13<\3=\3=\6=\u018d\n=\r=\16=\u018e\3")
        buf.write(">\3>\3?\3?\3?\3?\7?\u0197\n?\f?\16?\u019a\13?\3?\3?\3")
        buf.write("@\3@\3@\3@\7@\u01a2\n@\f@\16@\u01a5\13@\3@\3@\3@\3@\3")
        buf.write("@\3A\6A\u01ad\nA\rA\16A\u01ae\3A\3A\3B\3B\3B\3C\3C\3C")
        buf.write("\3C\7C\u01ba\nC\fC\16C\u01bd\13C\3C\3C\3C\3D\3D\3D\7D")
        buf.write("\u01c5\nD\fD\16D\u01c8\13D\3D\3D\5D\u01cc\nD\3D\3D\4\u01a3")
        buf.write("\u01c6\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2")
        buf.write("m\66o\67q\2s\2u8w9y:{\2};\177<\u0081=\u0083>\u0085?\u0087")
        buf.write("@\3\2\13\3\2\62;\4\2GGgg\4\2--//\4\2$$^^\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17\"\"\3\2$$\2")
        buf.write("\u01e2\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u0089")
        buf.write("\3\2\2\2\5\u008b\3\2\2\2\7\u008e\3\2\2\2\t\u0094\3\2\2")
        buf.write("\2\13\u009d\3\2\2\2\r\u00a0\3\2\2\2\17\u00a5\3\2\2\2\21")
        buf.write("\u00a9\3\2\2\2\23\u00ad\3\2\2\2\25\u00b3\3\2\2\2\27\u00b8")
        buf.write("\3\2\2\2\31\u00bf\3\2\2\2\33\u00c6\3\2\2\2\35\u00cb\3")
        buf.write("\2\2\2\37\u00d1\3\2\2\2!\u00dd\3\2\2\2#\u00e1\3\2\2\2")
        buf.write("%\u00e6\3\2\2\2\'\u00ea\3\2\2\2)\u00ef\3\2\2\2+\u00f5")
        buf.write("\3\2\2\2-\u00fa\3\2\2\2/\u00fc\3\2\2\2\61\u00fe\3\2\2")
        buf.write("\2\63\u0100\3\2\2\2\65\u0102\3\2\2\2\67\u0104\3\2\2\2")
        buf.write("9\u0107\3\2\2\2;\u010a\3\2\2\2=\u010d\3\2\2\2?\u0110\3")
        buf.write("\2\2\2A\u0112\3\2\2\2C\u0115\3\2\2\2E\u0117\3\2\2\2G\u011a")
        buf.write("\3\2\2\2I\u011c\3\2\2\2K\u011f\3\2\2\2M\u0121\3\2\2\2")
        buf.write("O\u0123\3\2\2\2Q\u0125\3\2\2\2S\u0127\3\2\2\2U\u0129\3")
        buf.write("\2\2\2W\u012b\3\2\2\2Y\u012d\3\2\2\2[\u012f\3\2\2\2]\u0131")
        buf.write("\3\2\2\2_\u0133\3\2\2\2a\u0135\3\2\2\2c\u0137\3\2\2\2")
        buf.write("e\u0139\3\2\2\2g\u0144\3\2\2\2i\u0146\3\2\2\2k\u014d\3")
        buf.write("\2\2\2m\u0154\3\2\2\2o\u0158\3\2\2\2q\u0164\3\2\2\2s\u0176")
        buf.write("\3\2\2\2u\u0181\3\2\2\2w\u0183\3\2\2\2y\u018a\3\2\2\2")
        buf.write("{\u0190\3\2\2\2}\u0192\3\2\2\2\177\u019d\3\2\2\2\u0081")
        buf.write("\u01ac\3\2\2\2\u0083\u01b2\3\2\2\2\u0085\u01b5\3\2\2\2")
        buf.write("\u0087\u01c1\3\2\2\2\u0089\u008a\7^\2\2\u008a\4\3\2\2")
        buf.write("\2\u008b\u008c\7>\2\2\u008c\u008d\7/\2\2\u008d\6\3\2\2")
        buf.write("\2\u008e\u008f\7d\2\2\u008f\u0090\7t\2\2\u0090\u0091\7")
        buf.write("g\2\2\u0091\u0092\7c\2\2\u0092\u0093\7m\2\2\u0093\b\3")
        buf.write("\2\2\2\u0094\u0095\7e\2\2\u0095\u0096\7q\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\u0098\7v\2\2\u0098\u0099\7k\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7w\2\2\u009b\u009c\7g\2\2\u009c\n")
        buf.write("\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f\f")
        buf.write("\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\16\3\2\2\2\u00a5\u00a6")
        buf.write("\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\20")
        buf.write("\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\22\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7n\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\24\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7n\2\2\u00b7\26")
        buf.write("\3\2\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7i\2\2\u00be\30\3\2\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7p\2\2\u00c5\32\3\2\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\34\3\2\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0")
        buf.write("\7u\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\7e\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9")
        buf.write("\7e\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7t\2\2\u00dc \3\2\2\2\u00dd\u00de\7x\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7t\2\2\u00e0\"\3\2\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5$\3\2\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8\u00e9\7y\2\2\u00e9&\3\2\2\2\u00ea\u00eb")
        buf.write("\7x\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee(\3\2\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4*\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7e\2\2\u00f9,\3")
        buf.write("\2\2\2\u00fa\u00fb\7-\2\2\u00fb.\3\2\2\2\u00fc\u00fd\7")
        buf.write("/\2\2\u00fd\60\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff\62\3\2")
        buf.write("\2\2\u0100\u0101\7\61\2\2\u0101\64\3\2\2\2\u0102\u0103")
        buf.write("\7#\2\2\u0103\66\3\2\2\2\u0104\u0105\7(\2\2\u0105\u0106")
        buf.write("\7(\2\2\u01068\3\2\2\2\u0107\u0108\7~\2\2\u0108\u0109")
        buf.write("\7~\2\2\u0109:\3\2\2\2\u010a\u010b\7?\2\2\u010b\u010c")
        buf.write("\7?\2\2\u010c<\3\2\2\2\u010d\u010e\7<\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f>\3\2\2\2\u0110\u0111\7?\2\2\u0111@\3\2\2")
        buf.write("\2\u0112\u0113\7#\2\2\u0113\u0114\7?\2\2\u0114B\3\2\2")
        buf.write("\2\u0115\u0116\7>\2\2\u0116D\3\2\2\2\u0117\u0118\7>\2")
        buf.write("\2\u0118\u0119\7?\2\2\u0119F\3\2\2\2\u011a\u011b\7@\2")
        buf.write("\2\u011bH\3\2\2\2\u011c\u011d\7@\2\2\u011d\u011e\7?\2")
        buf.write("\2\u011eJ\3\2\2\2\u011f\u0120\7`\2\2\u0120L\3\2\2\2\u0121")
        buf.write("\u0122\7\'\2\2\u0122N\3\2\2\2\u0123\u0124\7*\2\2\u0124")
        buf.write("P\3\2\2\2\u0125\u0126\7+\2\2\u0126R\3\2\2\2\u0127\u0128")
        buf.write("\7]\2\2\u0128T\3\2\2\2\u0129\u012a\7_\2\2\u012aV\3\2\2")
        buf.write("\2\u012b\u012c\7\60\2\2\u012cX\3\2\2\2\u012d\u012e\7.")
        buf.write("\2\2\u012eZ\3\2\2\2\u012f\u0130\7<\2\2\u0130\\\3\2\2\2")
        buf.write("\u0131\u0132\7=\2\2\u0132^\3\2\2\2\u0133\u0134\7}\2\2")
        buf.write("\u0134`\3\2\2\2\u0135\u0136\7\177\2\2\u0136b\3\2\2\2\u0137")
        buf.write("\u0138\7)\2\2\u0138d\3\2\2\2\u0139\u013a\7$\2\2\u013a")
        buf.write("f\3\2\2\2\u013b\u013c\5m\67\2\u013c\u013d\5i\65\2\u013d")
        buf.write("\u0145\3\2\2\2\u013e\u0140\5m\67\2\u013f\u0141\5i\65\2")
        buf.write("\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3")
        buf.write("\2\2\2\u0142\u0143\5k\66\2\u0143\u0145\3\2\2\2\u0144\u013b")
        buf.write("\3\2\2\2\u0144\u013e\3\2\2\2\u0145h\3\2\2\2\u0146\u014a")
        buf.write("\5W,\2\u0147\u0149\t\2\2\2\u0148\u0147\3\2\2\2\u0149\u014c")
        buf.write("\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("j\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014f\t\3\2\2\u014e")
        buf.write("\u0150\t\4\2\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0152\5m\67\2\u0152l\3\2\2")
        buf.write("\2\u0153\u0155\t\2\2\2\u0154\u0153\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("n\3\2\2\2\u0158\u015d\5e\63\2\u0159\u015c\n\5\2\2\u015a")
        buf.write("\u015c\5s:\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\5")
        buf.write("e\63\2\u0161\u0162\b8\2\2\u0162p\3\2\2\2\u0163\u0165\7")
        buf.write("\17\2\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0167\7\f\2\2\u0167r\3\2\2\2\u0168")
        buf.write("\u0169\7^\2\2\u0169\u0177\7d\2\2\u016a\u016b\7^\2\2\u016b")
        buf.write("\u0177\7h\2\2\u016c\u016d\7^\2\2\u016d\u0177\7t\2\2\u016e")
        buf.write("\u016f\7^\2\2\u016f\u0177\7p\2\2\u0170\u0171\7^\2\2\u0171")
        buf.write("\u0177\7v\2\2\u0172\u0173\7^\2\2\u0173\u0177\7$\2\2\u0174")
        buf.write("\u0175\7^\2\2\u0175\u0177\7^\2\2\u0176\u0168\3\2\2\2\u0176")
        buf.write("\u016a\3\2\2\2\u0176\u016c\3\2\2\2\u0176\u016e\3\2\2\2")
        buf.write("\u0176\u0170\3\2\2\2\u0176\u0172\3\2\2\2\u0176\u0174\3")
        buf.write("\2\2\2\u0177t\3\2\2\2\u0178\u0179\7v\2\2\u0179\u017a\7")
        buf.write("t\2\2\u017a\u017b\7w\2\2\u017b\u0182\7g\2\2\u017c\u017d")
        buf.write("\7h\2\2\u017d\u017e\7c\2\2\u017e\u017f\7n\2\2\u017f\u0180")
        buf.write("\7u\2\2\u0180\u0182\7g\2\2\u0181\u0178\3\2\2\2\u0181\u017c")
        buf.write("\3\2\2\2\u0182v\3\2\2\2\u0183\u0187\t\6\2\2\u0184\u0186")
        buf.write("\5{>\2\u0185\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188x\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u018a\u018c\7B\2\2\u018b\u018d\5{>\2\u018c\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018fz\3\2\2\2\u0190\u0191\t\7\2\2\u0191")
        buf.write("|\3\2\2\2\u0192\u0193\7\61\2\2\u0193\u0194\7\61\2\2\u0194")
        buf.write("\u0198\3\2\2\2\u0195\u0197\n\b\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c")
        buf.write("\b?\3\2\u019c~\3\2\2\2\u019d\u019e\7\61\2\2\u019e\u019f")
        buf.write("\7,\2\2\u019f\u01a3\3\2\2\2\u01a0\u01a2\13\2\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3")
        buf.write("\2\2\2\u01a6\u01a7\7,\2\2\u01a7\u01a8\7\61\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01aa\b@\3\2\u01aa\u0080\3\2\2\2\u01ab")
        buf.write("\u01ad\t\t\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\3")
        buf.write("\2\2\2\u01b0\u01b1\bA\3\2\u01b1\u0082\3\2\2\2\u01b2\u01b3")
        buf.write("\13\2\2\2\u01b3\u01b4\bB\4\2\u01b4\u0084\3\2\2\2\u01b5")
        buf.write("\u01bb\5e\63\2\u01b6\u01ba\n\n\2\2\u01b7\u01b8\7^\2\2")
        buf.write("\u01b8\u01ba\7$\2\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01bf\5e\63\2\u01bf\u01c0\bC\5\2\u01c0\u0086\3\2\2\2")
        buf.write("\u01c1\u01c6\5e\63\2\u01c2\u01c5\n\n\2\2\u01c3\u01c5\5")
        buf.write("s:\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8")
        buf.write("\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7")
        buf.write("\u01cb\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01cc\5q9\2\u01ca")
        buf.write("\u01cc\7\2\2\3\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bD\6\2\u01ce\u0088\3")
        buf.write("\2\2\2\27\2\u0140\u0144\u014a\u014f\u0156\u015b\u015d")
        buf.write("\u0164\u0176\u0181\u0187\u018e\u0198\u01a3\u01ae\u01b9")
        buf.write("\u01bb\u01c4\u01c6\u01cb\7\38\2\b\2\2\3B\3\3C\4\3D\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSE = 6
    FOR = 7
    INT = 8
    FLOAT = 9
    BOOL = 10
    STRING = 11
    RETURN = 12
    NULL = 13
    CLASS = 14
    CONSTRUCTOR = 15
    VAR = 16
    SELF = 17
    NEW = 18
    VOID = 19
    CONST = 20
    FUNC = 21
    ADD_OP = 22
    SUB_OP = 23
    MUL_OP = 24
    DIV_OP = 25
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
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'int'", "'float'", "'bool'", "'string'", "'return'", "'null'", 
            "'class'", "'constructor'", "'var'", "'self'", "'new'", "'void'", 
            "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'!'", "'&&'", 
            "'||'", "'=='", "':='", "'='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "':'", "';'", "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", 
            "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
            "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
            "DIV_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
            "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
            "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", 
            "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "SIN_Q", 
            "DOU_Q", "FLOAT_LIT", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", 
            "AT_ID", "CMT_LINE", "CMT_BLOCK", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                  "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", 
                  "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                  "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", "RSB", "DOT", 
                  "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "SIN_Q", 
                  "DOU_Q", "FLOAT_LIT", "DECPART", "EXPPART", "INT_LIT", 
                  "STR_LIT", "NEWLINE", "ESCAPE", "BOOL_LIT", "ID", "AT_ID", 
                  "SEQUENCE", "CMT_LINE", "CMT_BLOCK", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[54] = self.STR_LIT_action 
            actions[64] = self.ERROR_CHAR_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.UNCLOSE_STRING_action 
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
            			raise IllegalEscape(self.text[1:-1]) 
            			break

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	string_error = self.text[1:]
            	if (string_error[-1] == "\n"):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     


