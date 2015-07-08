# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .oftexmathListener import oftexmathListener
else:
    from oftexmathListener import oftexmathListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\26\u0157\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\3\2\6\2*\n\2\r\2\16\2+\3\3\6\3/")
        buf.write(u"\n\3\r\3\16\3\60\3\3\6\3\64\n\3\r\3\16\3\65\5\38\n\3")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4B\n\4\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\6\5J\n\5\r\5\16\5K\3\5\3\5\3\6\3\6\3\7\3")
        buf.write(u"\7\5\7T\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b^\n\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bh\n\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\5\br\n\b\5\bt\n\b\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\5\t~\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\5\t\u0088\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write(u"\5\t\u0092\n\t\5\t\u0094\n\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a3\n\f\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ae\n\r\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\6\16\u00ba\n")
        buf.write(u"\16\r\16\16\16\u00bb\3\16\3\16\5\16\u00c0\n\16\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\6\17\u00cc")
        buf.write(u"\n\17\r\17\16\17\u00cd\3\17\3\17\5\17\u00d2\n\17\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00de")
        buf.write(u"\n\21\3\21\3\21\3\21\5\21\u00e3\n\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00f0\n\21")
        buf.write(u"\f\21\16\21\u00f3\13\21\3\21\3\21\3\21\5\21\u00f8\n\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0103")
        buf.write(u"\n\21\f\21\16\21\u0106\13\21\3\21\3\21\5\21\u010a\n\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\7\21\u0117\n\21\f\21\16\21\u011a\13\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0124\n\21\f\21\16")
        buf.write(u"\21\u0127\13\21\3\21\3\21\3\21\5\21\u012c\n\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0137\n\21")
        buf.write(u"\f\21\16\21\u013a\13\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\7\21\u0144\n\21\f\21\16\21\u0147\13\21\3\21")
        buf.write(u"\3\21\5\21\u014b\n\21\3\21\3\21\5\21\u014f\n\21\3\22")
        buf.write(u"\3\22\3\23\3\23\3\24\3\24\3\24\2\2\25\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\34\36 \"$&\2\4\3\2\r\17\3\2\3\4\u01bc")
        buf.write(u"\2)\3\2\2\2\4\67\3\2\2\2\6A\3\2\2\2\bC\3\2\2\2\nO\3\2")
        buf.write(u"\2\2\fS\3\2\2\2\16s\3\2\2\2\20\u0093\3\2\2\2\22\u0095")
        buf.write(u"\3\2\2\2\24\u0097\3\2\2\2\26\u00a2\3\2\2\2\30\u00ad\3")
        buf.write(u"\2\2\2\32\u00bf\3\2\2\2\34\u00d1\3\2\2\2\36\u00d3\3\2")
        buf.write(u"\2\2 \u014e\3\2\2\2\"\u0150\3\2\2\2$\u0152\3\2\2\2&\u0154")
        buf.write(u"\3\2\2\2(*\5\4\3\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3")
        buf.write(u"\2\2\2,\3\3\2\2\2-/\5\36\20\2.-\3\2\2\2/\60\3\2\2\2\60")
        buf.write(u".\3\2\2\2\60\61\3\2\2\2\618\3\2\2\2\62\64\5\6\4\2\63")
        buf.write(u"\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2")
        buf.write(u"\668\3\2\2\2\67.\3\2\2\2\67\63\3\2\2\28\5\3\2\2\29B\5")
        buf.write(u"\b\5\2:B\5\26\f\2;B\5\30\r\2<B\5 \21\2=B\5\f\7\2>B\5")
        buf.write(u"\n\6\2?B\5\22\n\2@B\5\24\13\2A9\3\2\2\2A:\3\2\2\2A;\3")
        buf.write(u"\2\2\2A<\3\2\2\2A=\3\2\2\2A>\3\2\2\2A?\3\2\2\2A@\3\2")
        buf.write(u"\2\2B\7\3\2\2\2CI\7\13\2\2DJ\5\b\5\2EJ\5\f\7\2FJ\5\26")
        buf.write(u"\f\2GJ\5\30\r\2HJ\5\n\6\2ID\3\2\2\2IE\3\2\2\2IF\3\2\2")
        buf.write(u"\2IG\3\2\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2")
        buf.write(u"LM\3\2\2\2MN\7\f\2\2N\t\3\2\2\2OP\t\2\2\2P\13\3\2\2\2")
        buf.write(u"QT\5\16\b\2RT\5\20\t\2SQ\3\2\2\2SR\3\2\2\2T\r\3\2\2\2")
        buf.write(u"UV\5\26\f\2V]\7\20\2\2W^\5\b\5\2X^\5\30\r\2Y^\5 \21\2")
        buf.write(u"Z^\5\26\f\2[^\5\20\t\2\\^\5\16\b\2]W\3\2\2\2]X\3\2\2")
        buf.write(u"\2]Y\3\2\2\2]Z\3\2\2\2][\3\2\2\2]\\\3\2\2\2^t\3\2\2\2")
        buf.write(u"_`\5\30\r\2`g\7\20\2\2ah\5\b\5\2bh\5 \21\2ch\5\26\f\2")
        buf.write(u"dh\5\30\r\2eh\5\20\t\2fh\5\16\b\2ga\3\2\2\2gb\3\2\2\2")
        buf.write(u"gc\3\2\2\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2ht\3\2\2\2ij")
        buf.write(u"\5 \21\2jq\7\20\2\2kr\5\b\5\2lr\5\26\f\2mr\5\30\r\2n")
        buf.write(u"r\5 \21\2or\5\20\t\2pr\5\16\b\2qk\3\2\2\2ql\3\2\2\2q")
        buf.write(u"m\3\2\2\2qn\3\2\2\2qo\3\2\2\2qp\3\2\2\2rt\3\2\2\2sU\3")
        buf.write(u"\2\2\2s_\3\2\2\2si\3\2\2\2t\17\3\2\2\2uv\5\26\f\2v}\7")
        buf.write(u"\21\2\2w~\5\b\5\2x~\5\30\r\2y~\5 \21\2z~\5\26\f\2{~\5")
        buf.write(u"\20\t\2|~\5\16\b\2}w\3\2\2\2}x\3\2\2\2}y\3\2\2\2}z\3")
        buf.write(u"\2\2\2}{\3\2\2\2}|\3\2\2\2~\u0094\3\2\2\2\177\u0080\5")
        buf.write(u"\30\r\2\u0080\u0087\7\21\2\2\u0081\u0088\5\b\5\2\u0082")
        buf.write(u"\u0088\5 \21\2\u0083\u0088\5\26\f\2\u0084\u0088\5\30")
        buf.write(u"\r\2\u0085\u0088\5\20\t\2\u0086\u0088\5\16\b\2\u0087")
        buf.write(u"\u0081\3\2\2\2\u0087\u0082\3\2\2\2\u0087\u0083\3\2\2")
        buf.write(u"\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0086")
        buf.write(u"\3\2\2\2\u0088\u0094\3\2\2\2\u0089\u008a\5 \21\2\u008a")
        buf.write(u"\u0091\7\21\2\2\u008b\u0092\5\b\5\2\u008c\u0092\5\26")
        buf.write(u"\f\2\u008d\u0092\5\30\r\2\u008e\u0092\5 \21\2\u008f\u0092")
        buf.write(u"\5\20\t\2\u0090\u0092\5\16\b\2\u0091\u008b\3\2\2\2\u0091")
        buf.write(u"\u008c\3\2\2\2\u0091\u008d\3\2\2\2\u0091\u008e\3\2\2")
        buf.write(u"\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\u0094")
        buf.write(u"\3\2\2\2\u0093u\3\2\2\2\u0093\177\3\2\2\2\u0093\u0089")
        buf.write(u"\3\2\2\2\u0094\21\3\2\2\2\u0095\u0096\7\n\2\2\u0096\23")
        buf.write(u"\3\2\2\2\u0097\u0098\7\22\2\2\u0098\25\3\2\2\2\u0099")
        buf.write(u"\u00a3\7\3\2\2\u009a\u009b\7\3\2\2\u009b\u00a3\5\32\16")
        buf.write(u"\2\u009c\u009d\7\3\2\2\u009d\u00a3\5\34\17\2\u009e\u009f")
        buf.write(u"\7\3\2\2\u009f\u00a0\5\32\16\2\u00a0\u00a1\5\34\17\2")
        buf.write(u"\u00a1\u00a3\3\2\2\2\u00a2\u0099\3\2\2\2\u00a2\u009a")
        buf.write(u"\3\2\2\2\u00a2\u009c\3\2\2\2\u00a2\u009e\3\2\2\2\u00a3")
        buf.write(u"\27\3\2\2\2\u00a4\u00ae\7\4\2\2\u00a5\u00a6\7\4\2\2\u00a6")
        buf.write(u"\u00ae\5\32\16\2\u00a7\u00a8\7\4\2\2\u00a8\u00ae\5\34")
        buf.write(u"\17\2\u00a9\u00aa\7\4\2\2\u00aa\u00ab\5\32\16\2\u00ab")
        buf.write(u"\u00ac\5\34\17\2\u00ac\u00ae\3\2\2\2\u00ad\u00a4\3\2")
        buf.write(u"\2\2\u00ad\u00a5\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ad\u00a9")
        buf.write(u"\3\2\2\2\u00ae\31\3\2\2\2\u00af\u00b0\7\6\2\2\u00b0\u00c0")
        buf.write(u"\t\3\2\2\u00b1\u00b2\7\6\2\2\u00b2\u00b9\7\b\2\2\u00b3")
        buf.write(u"\u00ba\5\b\5\2\u00b4\u00ba\5\26\f\2\u00b5\u00ba\5\30")
        buf.write(u"\r\2\u00b6\u00ba\5 \21\2\u00b7\u00ba\5\f\7\2\u00b8\u00ba")
        buf.write(u"\5\n\6\2\u00b9\u00b3\3\2\2\2\u00b9\u00b4\3\2\2\2\u00b9")
        buf.write(u"\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2")
        buf.write(u"\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9")
        buf.write(u"\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write(u"\u00be\7\t\2\2\u00be\u00c0\3\2\2\2\u00bf\u00af\3\2\2")
        buf.write(u"\2\u00bf\u00b1\3\2\2\2\u00c0\33\3\2\2\2\u00c1\u00c2\7")
        buf.write(u"\7\2\2\u00c2\u00d2\t\3\2\2\u00c3\u00c4\7\7\2\2\u00c4")
        buf.write(u"\u00cb\7\b\2\2\u00c5\u00cc\5\b\5\2\u00c6\u00cc\5\26\f")
        buf.write(u"\2\u00c7\u00cc\5\30\r\2\u00c8\u00cc\5 \21\2\u00c9\u00cc")
        buf.write(u"\5\f\7\2\u00ca\u00cc\5\n\6\2\u00cb\u00c5\3\2\2\2\u00cb")
        buf.write(u"\u00c6\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cb\u00c8\3\2\2")
        buf.write(u"\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write(u"\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write(u"\u00cf\3\2\2\2\u00cf\u00d0\7\t\2\2\u00d0\u00d2\3\2\2")
        buf.write(u"\2\u00d1\u00c1\3\2\2\2\u00d1\u00c3\3\2\2\2\u00d2\35\3")
        buf.write(u"\2\2\2\u00d3\u00d4\7\5\2\2\u00d4\u00d5\5\"\22\2\u00d5")
        buf.write(u"\u00d6\7\b\2\2\u00d6\u00d7\5$\23\2\u00d7\u00d8\7\t\2")
        buf.write(u"\2\u00d8\37\3\2\2\2\u00d9\u00da\7\5\2\2\u00da\u00dd\5")
        buf.write(u"&\24\2\u00db\u00de\5\32\16\2\u00dc\u00de\5\34\17\2\u00dd")
        buf.write(u"\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2")
        buf.write(u"\2\u00de\u014f\3\2\2\2\u00df\u00e0\7\5\2\2\u00e0\u00e2")
        buf.write(u"\5&\24\2\u00e1\u00e3\5\32\16\2\u00e2\u00e1\3\2\2\2\u00e2")
        buf.write(u"\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\5\34\17")
        buf.write(u"\2\u00e5\u014f\3\2\2\2\u00e6\u00e7\7\5\2\2\u00e7\u00e8")
        buf.write(u"\5&\24\2\u00e8\u00f1\7\b\2\2\u00e9\u00f0\5\b\5\2\u00ea")
        buf.write(u"\u00f0\5\26\f\2\u00eb\u00f0\5\30\r\2\u00ec\u00f0\5 \21")
        buf.write(u"\2\u00ed\u00f0\5\f\7\2\u00ee\u00f0\5\n\6\2\u00ef\u00e9")
        buf.write(u"\3\2\2\2\u00ef\u00ea\3\2\2\2\u00ef\u00eb\3\2\2\2\u00ef")
        buf.write(u"\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2")
        buf.write(u"\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2")
        buf.write(u"\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4")
        buf.write(u"\u00f7\7\t\2\2\u00f5\u00f8\5\32\16\2\u00f6\u00f8\5\34")
        buf.write(u"\17\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8")
        buf.write(u"\3\2\2\2\u00f8\u014f\3\2\2\2\u00f9\u00fa\7\5\2\2\u00fa")
        buf.write(u"\u00fb\5&\24\2\u00fb\u0104\7\b\2\2\u00fc\u0103\5\b\5")
        buf.write(u"\2\u00fd\u0103\5\26\f\2\u00fe\u0103\5\30\r\2\u00ff\u0103")
        buf.write(u"\5 \21\2\u0100\u0103\5\f\7\2\u0101\u0103\5\n\6\2\u0102")
        buf.write(u"\u00fc\3\2\2\2\u0102\u00fd\3\2\2\2\u0102\u00fe\3\2\2")
        buf.write(u"\2\u0102\u00ff\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0101")
        buf.write(u"\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104")
        buf.write(u"\u0105\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2")
        buf.write(u"\2\u0107\u0109\7\t\2\2\u0108\u010a\5\32\16\2\u0109\u0108")
        buf.write(u"\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write(u"\u010c\5\34\17\2\u010c\u014f\3\2\2\2\u010d\u010e\7\5")
        buf.write(u"\2\2\u010e\u010f\5&\24\2\u010f\u0118\7\b\2\2\u0110\u0117")
        buf.write(u"\5\b\5\2\u0111\u0117\5\26\f\2\u0112\u0117\5\30\r\2\u0113")
        buf.write(u"\u0117\5 \21\2\u0114\u0117\5\f\7\2\u0115\u0117\5\n\6")
        buf.write(u"\2\u0116\u0110\3\2\2\2\u0116\u0111\3\2\2\2\u0116\u0112")
        buf.write(u"\3\2\2\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0116")
        buf.write(u"\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2")
        buf.write(u"\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u0118")
        buf.write(u"\3\2\2\2\u011b\u011c\7\t\2\2\u011c\u0125\7\b\2\2\u011d")
        buf.write(u"\u0124\5\b\5\2\u011e\u0124\5\26\f\2\u011f\u0124\5\30")
        buf.write(u"\r\2\u0120\u0124\5 \21\2\u0121\u0124\5\f\7\2\u0122\u0124")
        buf.write(u"\5\n\6\2\u0123\u011d\3\2\2\2\u0123\u011e\3\2\2\2\u0123")
        buf.write(u"\u011f\3\2\2\2\u0123\u0120\3\2\2\2\u0123\u0121\3\2\2")
        buf.write(u"\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123")
        buf.write(u"\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write(u"\u0125\3\2\2\2\u0128\u012b\7\t\2\2\u0129\u012c\5\32\16")
        buf.write(u"\2\u012a\u012c\5\34\17\2\u012b\u0129\3\2\2\2\u012b\u012a")
        buf.write(u"\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u014f\3\2\2\2\u012d")
        buf.write(u"\u012e\7\5\2\2\u012e\u012f\5&\24\2\u012f\u0138\7\b\2")
        buf.write(u"\2\u0130\u0137\5\b\5\2\u0131\u0137\5\26\f\2\u0132\u0137")
        buf.write(u"\5\30\r\2\u0133\u0137\5 \21\2\u0134\u0137\5\f\7\2\u0135")
        buf.write(u"\u0137\5\n\6\2\u0136\u0130\3\2\2\2\u0136\u0131\3\2\2")
        buf.write(u"\2\u0136\u0132\3\2\2\2\u0136\u0133\3\2\2\2\u0136\u0134")
        buf.write(u"\3\2\2\2\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138")
        buf.write(u"\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2")
        buf.write(u"\2\u013a\u0138\3\2\2\2\u013b\u013c\7\t\2\2\u013c\u0145")
        buf.write(u"\7\b\2\2\u013d\u0144\5\b\5\2\u013e\u0144\5\26\f\2\u013f")
        buf.write(u"\u0144\5\30\r\2\u0140\u0144\5 \21\2\u0141\u0144\5\f\7")
        buf.write(u"\2\u0142\u0144\5\n\6\2\u0143\u013d\3\2\2\2\u0143\u013e")
        buf.write(u"\3\2\2\2\u0143\u013f\3\2\2\2\u0143\u0140\3\2\2\2\u0143")
        buf.write(u"\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2")
        buf.write(u"\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148")
        buf.write(u"\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u014a\7\t\2\2\u0149")
        buf.write(u"\u014b\5\32\16\2\u014a\u0149\3\2\2\2\u014a\u014b\3\2")
        buf.write(u"\2\2\u014b\u014c\3\2\2\2\u014c\u014d\5\34\17\2\u014d")
        buf.write(u"\u014f\3\2\2\2\u014e\u00d9\3\2\2\2\u014e\u00df\3\2\2")
        buf.write(u"\2\u014e\u00e6\3\2\2\2\u014e\u00f9\3\2\2\2\u014e\u010d")
        buf.write(u"\3\2\2\2\u014e\u012d\3\2\2\2\u014f!\3\2\2\2\u0150\u0151")
        buf.write(u"\7\23\2\2\u0151#\3\2\2\2\u0152\u0153\7\24\2\2\u0153%")
        buf.write(u"\3\2\2\2\u0154\u0155\7\25\2\2\u0155\'\3\2\2\2-+\60\65")
        buf.write(u"\67AIKS]gqs}\u0087\u0091\u0093\u00a2\u00ad\u00b9\u00bb")
        buf.write(u"\u00bf\u00cb\u00cd\u00d1\u00dd\u00e2\u00ef\u00f1\u00f7")
        buf.write(u"\u0102\u0104\u0109\u0116\u0118\u0123\u0125\u012b\u0136")
        buf.write(u"\u0138\u0143\u0145\u014a\u014e")
        return buf.getvalue()
		

class oftexmathParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'\\'", 
                     u"'_'", u"'^'", u"'{'", u"'}'", u"'&'", u"'('", u"')'", 
                     u"'='", u"'+'", u"'-'", u"'*'", u"'/'", u"'\\\\'" ]

    symbolicNames = [ u"<INVALID>", u"VARIABLE", u"NUMBER", u"BACKSLASH", 
                      u"SUBSET", u"SUPERSET", u"LEFTBRACE", u"RIGHTBRACE", 
                      u"COLFORMAT", u"BRACEOPEN", u"BRACECLOSE", u"EQ", 
                      u"PLUS", u"MINUS", u"MUL", u"DIV", u"ROWDELIMIT", 
                      u"MAINWORDS", u"SUBWORDS", u"KEYWORDS", u"WS" ]

    RULE_init = 0
    RULE_main = 1
    RULE_allinone = 2
    RULE_braceoc = 3
    RULE_signs = 4
    RULE_muldiv = 5
    RULE_mul = 6
    RULE_div = 7
    RULE_colformat = 8
    RULE_rowdelimit = 9
    RULE_variable = 10
    RULE_number = 11
    RULE_subset = 12
    RULE_superset = 13
    RULE_mainexpr = 14
    RULE_expr = 15
    RULE_mainwords = 16
    RULE_subwords = 17
    RULE_keywords = 18

    ruleNames =  [ u"init", u"main", u"allinone", u"braceoc", u"signs", 
                   u"muldiv", u"mul", u"div", u"colformat", u"rowdelimit", 
                   u"variable", u"number", u"subset", u"superset", u"mainexpr", 
                   u"expr", u"mainwords", u"subwords", u"keywords" ]

    EOF = Token.EOF
    VARIABLE=1
    NUMBER=2
    BACKSLASH=3
    SUBSET=4
    SUPERSET=5
    LEFTBRACE=6
    RIGHTBRACE=7
    COLFORMAT=8
    BRACEOPEN=9
    BRACECLOSE=10
    EQ=11
    PLUS=12
    MINUS=13
    MUL=14
    DIV=15
    ROWDELIMIT=16
    MAINWORDS=17
    SUBWORDS=18
    KEYWORDS=19
    WS=20

    def __init__(self, input):
        super(oftexmathParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.InitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def main(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.MainContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.MainContext,i)


        def getRuleIndex(self):
            return oftexmathParser.RULE_init

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterInit(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitInit(self)




    def init(self):

        localctx = oftexmathParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38 
                self.main()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.COLFORMAT) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS) | (1 << oftexmathParser.ROWDELIMIT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.MainContext, self).__init__(parent, invokingState)
            self.parser = parser

        def mainexpr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.MainexprContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.MainexprContext,i)


        def allinone(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.AllinoneContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.AllinoneContext,i)


        def getRuleIndex(self):
            return oftexmathParser.RULE_main

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterMain(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitMain(self)




    def main(self):

        localctx = oftexmathParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.state = 53
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 43 
                        self.mainexpr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 46 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 48 
                        self.allinone()

                    else:
                        raise NoViableAltException(self)
                    self.state = 51 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AllinoneContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.AllinoneContext, self).__init__(parent, invokingState)
            self.parser = parser

        def braceoc(self):
            return self.getTypedRuleContext(oftexmathParser.BraceocContext,0)


        def variable(self):
            return self.getTypedRuleContext(oftexmathParser.VariableContext,0)


        def number(self):
            return self.getTypedRuleContext(oftexmathParser.NumberContext,0)


        def expr(self):
            return self.getTypedRuleContext(oftexmathParser.ExprContext,0)


        def muldiv(self):
            return self.getTypedRuleContext(oftexmathParser.MuldivContext,0)


        def signs(self):
            return self.getTypedRuleContext(oftexmathParser.SignsContext,0)


        def colformat(self):
            return self.getTypedRuleContext(oftexmathParser.ColformatContext,0)


        def rowdelimit(self):
            return self.getTypedRuleContext(oftexmathParser.RowdelimitContext,0)


        def getRuleIndex(self):
            return oftexmathParser.RULE_allinone

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterAllinone(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitAllinone(self)




    def allinone(self):

        localctx = oftexmathParser.AllinoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_allinone)
        try:
            self.state = 63
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55 
                self.braceoc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56 
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57 
                self.number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58 
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59 
                self.muldiv()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60 
                self.signs()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61 
                self.colformat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 62 
                self.rowdelimit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BraceocContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.BraceocContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BRACEOPEN(self):
            return self.getToken(oftexmathParser.BRACEOPEN, 0)

        def BRACECLOSE(self):
            return self.getToken(oftexmathParser.BRACECLOSE, 0)

        def braceoc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.BraceocContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.BraceocContext,i)


        def muldiv(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.MuldivContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.MuldivContext,i)


        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.VariableContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.VariableContext,i)


        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.NumberContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.NumberContext,i)


        def signs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.SignsContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.SignsContext,i)


        def getRuleIndex(self):
            return oftexmathParser.RULE_braceoc

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterBraceoc(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitBraceoc(self)




    def braceoc(self):

        localctx = oftexmathParser.BraceocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_braceoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(oftexmathParser.BRACEOPEN)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 66 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 67 
                    self.muldiv()
                    pass

                elif la_ == 3:
                    self.state = 68 
                    self.variable()
                    pass

                elif la_ == 4:
                    self.state = 69 
                    self.number()
                    pass

                elif la_ == 5:
                    self.state = 70 
                    self.signs()
                    pass


                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0)):
                    break

            self.state = 75
            self.match(oftexmathParser.BRACECLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SignsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.SignsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(oftexmathParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(oftexmathParser.MINUS, 0)

        def EQ(self):
            return self.getToken(oftexmathParser.EQ, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_signs

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterSigns(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitSigns(self)




    def signs(self):

        localctx = oftexmathParser.SignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_signs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MuldivContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.MuldivContext, self).__init__(parent, invokingState)
            self.parser = parser

        def mul(self):
            return self.getTypedRuleContext(oftexmathParser.MulContext,0)


        def div(self):
            return self.getTypedRuleContext(oftexmathParser.DivContext,0)


        def getRuleIndex(self):
            return oftexmathParser.RULE_muldiv

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterMuldiv(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitMuldiv(self)




    def muldiv(self):

        localctx = oftexmathParser.MuldivContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_muldiv)
        try:
            self.state = 81
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79 
                self.mul()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80 
                self.div()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.MulContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.VariableContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.VariableContext,i)


        def MUL(self):
            return self.getToken(oftexmathParser.MUL, 0)

        def braceoc(self):
            return self.getTypedRuleContext(oftexmathParser.BraceocContext,0)


        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.NumberContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.NumberContext,i)


        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.ExprContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.ExprContext,i)


        def div(self):
            return self.getTypedRuleContext(oftexmathParser.DivContext,0)


        def mul(self):
            return self.getTypedRuleContext(oftexmathParser.MulContext,0)


        def getRuleIndex(self):
            return oftexmathParser.RULE_mul

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterMul(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitMul(self)




    def mul(self):

        localctx = oftexmathParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mul)
        try:
            self.state = 113
            token = self._input.LA(1)
            if token in [oftexmathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83 
                self.variable()
                self.state = 84
                self.match(oftexmathParser.MUL)
                self.state = 91
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 85 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 86 
                    self.number()
                    pass

                elif la_ == 3:
                    self.state = 87 
                    self.expr()
                    pass

                elif la_ == 4:
                    self.state = 88 
                    self.variable()
                    pass

                elif la_ == 5:
                    self.state = 89 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 90 
                    self.mul()
                    pass



            elif token in [oftexmathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93 
                self.number()
                self.state = 94
                self.match(oftexmathParser.MUL)
                self.state = 101
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 95 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 96 
                    self.expr()
                    pass

                elif la_ == 3:
                    self.state = 97 
                    self.variable()
                    pass

                elif la_ == 4:
                    self.state = 98 
                    self.number()
                    pass

                elif la_ == 5:
                    self.state = 99 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 100 
                    self.mul()
                    pass



            elif token in [oftexmathParser.BACKSLASH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103 
                self.expr()
                self.state = 104
                self.match(oftexmathParser.MUL)
                self.state = 111
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 105 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 106 
                    self.variable()
                    pass

                elif la_ == 3:
                    self.state = 107 
                    self.number()
                    pass

                elif la_ == 4:
                    self.state = 108 
                    self.expr()
                    pass

                elif la_ == 5:
                    self.state = 109 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 110 
                    self.mul()
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

    class DivContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.DivContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.VariableContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.VariableContext,i)


        def DIV(self):
            return self.getToken(oftexmathParser.DIV, 0)

        def braceoc(self):
            return self.getTypedRuleContext(oftexmathParser.BraceocContext,0)


        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.NumberContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.NumberContext,i)


        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.ExprContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.ExprContext,i)


        def div(self):
            return self.getTypedRuleContext(oftexmathParser.DivContext,0)


        def mul(self):
            return self.getTypedRuleContext(oftexmathParser.MulContext,0)


        def getRuleIndex(self):
            return oftexmathParser.RULE_div

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterDiv(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitDiv(self)




    def div(self):

        localctx = oftexmathParser.DivContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_div)
        try:
            self.state = 145
            token = self._input.LA(1)
            if token in [oftexmathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115 
                self.variable()
                self.state = 116
                self.match(oftexmathParser.DIV)
                self.state = 123
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 117 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 118 
                    self.number()
                    pass

                elif la_ == 3:
                    self.state = 119 
                    self.expr()
                    pass

                elif la_ == 4:
                    self.state = 120 
                    self.variable()
                    pass

                elif la_ == 5:
                    self.state = 121 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 122 
                    self.mul()
                    pass



            elif token in [oftexmathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125 
                self.number()
                self.state = 126
                self.match(oftexmathParser.DIV)
                self.state = 133
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 127 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 128 
                    self.expr()
                    pass

                elif la_ == 3:
                    self.state = 129 
                    self.variable()
                    pass

                elif la_ == 4:
                    self.state = 130 
                    self.number()
                    pass

                elif la_ == 5:
                    self.state = 131 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 132 
                    self.mul()
                    pass



            elif token in [oftexmathParser.BACKSLASH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135 
                self.expr()
                self.state = 136
                self.match(oftexmathParser.DIV)
                self.state = 143
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 137 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 138 
                    self.variable()
                    pass

                elif la_ == 3:
                    self.state = 139 
                    self.number()
                    pass

                elif la_ == 4:
                    self.state = 140 
                    self.expr()
                    pass

                elif la_ == 5:
                    self.state = 141 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 142 
                    self.mul()
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

    class ColformatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.ColformatContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COLFORMAT(self):
            return self.getToken(oftexmathParser.COLFORMAT, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_colformat

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterColformat(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitColformat(self)




    def colformat(self):

        localctx = oftexmathParser.ColformatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_colformat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(oftexmathParser.COLFORMAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowdelimitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.RowdelimitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ROWDELIMIT(self):
            return self.getToken(oftexmathParser.ROWDELIMIT, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_rowdelimit

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterRowdelimit(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitRowdelimit(self)




    def rowdelimit(self):

        localctx = oftexmathParser.RowdelimitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_rowdelimit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(oftexmathParser.ROWDELIMIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.VariableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(oftexmathParser.VARIABLE, 0)

        def subset(self):
            return self.getTypedRuleContext(oftexmathParser.SubsetContext,0)


        def superset(self):
            return self.getTypedRuleContext(oftexmathParser.SupersetContext,0)


        def getRuleIndex(self):
            return oftexmathParser.RULE_variable

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterVariable(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitVariable(self)




    def variable(self):

        localctx = oftexmathParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable)
        try:
            self.state = 160
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(oftexmathParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(oftexmathParser.VARIABLE)
                self.state = 153 
                self.subset()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.match(oftexmathParser.VARIABLE)
                self.state = 155 
                self.superset()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(oftexmathParser.VARIABLE)
                self.state = 157 
                self.subset()
                self.state = 158 
                self.superset()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(oftexmathParser.NUMBER, 0)

        def subset(self):
            return self.getTypedRuleContext(oftexmathParser.SubsetContext,0)


        def superset(self):
            return self.getTypedRuleContext(oftexmathParser.SupersetContext,0)


        def getRuleIndex(self):
            return oftexmathParser.RULE_number

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitNumber(self)




    def number(self):

        localctx = oftexmathParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_number)
        try:
            self.state = 171
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(oftexmathParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(oftexmathParser.NUMBER)
                self.state = 164 
                self.subset()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(oftexmathParser.NUMBER)
                self.state = 166 
                self.superset()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.match(oftexmathParser.NUMBER)
                self.state = 168 
                self.subset()
                self.state = 169 
                self.superset()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubsetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.SubsetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SUBSET(self):
            return self.getToken(oftexmathParser.SUBSET, 0)

        def VARIABLE(self):
            return self.getToken(oftexmathParser.VARIABLE, 0)

        def NUMBER(self):
            return self.getToken(oftexmathParser.NUMBER, 0)

        def LEFTBRACE(self):
            return self.getToken(oftexmathParser.LEFTBRACE, 0)

        def RIGHTBRACE(self):
            return self.getToken(oftexmathParser.RIGHTBRACE, 0)

        def braceoc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.BraceocContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.BraceocContext,i)


        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.VariableContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.VariableContext,i)


        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.NumberContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.NumberContext,i)


        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.ExprContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.ExprContext,i)


        def muldiv(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.MuldivContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.MuldivContext,i)


        def signs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.SignsContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.SignsContext,i)


        def getRuleIndex(self):
            return oftexmathParser.RULE_subset

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterSubset(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitSubset(self)




    def subset(self):

        localctx = oftexmathParser.SubsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subset)
        self._la = 0 # Token type
        try:
            self.state = 189
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(oftexmathParser.SUBSET)
                self.state = 174
                _la = self._input.LA(1)
                if not(_la==oftexmathParser.VARIABLE or _la==oftexmathParser.NUMBER):
                    self._errHandler.recoverInline(self)
                self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(oftexmathParser.SUBSET)
                self.state = 176
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 183
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        self.state = 177 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 178 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 179 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 180 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 181 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 182 
                        self.signs()
                        pass


                    self.state = 185 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0)):
                        break

                self.state = 187
                self.match(oftexmathParser.RIGHTBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SupersetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.SupersetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SUPERSET(self):
            return self.getToken(oftexmathParser.SUPERSET, 0)

        def VARIABLE(self):
            return self.getToken(oftexmathParser.VARIABLE, 0)

        def NUMBER(self):
            return self.getToken(oftexmathParser.NUMBER, 0)

        def LEFTBRACE(self):
            return self.getToken(oftexmathParser.LEFTBRACE, 0)

        def RIGHTBRACE(self):
            return self.getToken(oftexmathParser.RIGHTBRACE, 0)

        def braceoc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.BraceocContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.BraceocContext,i)


        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.VariableContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.VariableContext,i)


        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.NumberContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.NumberContext,i)


        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.ExprContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.ExprContext,i)


        def muldiv(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.MuldivContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.MuldivContext,i)


        def signs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.SignsContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.SignsContext,i)


        def getRuleIndex(self):
            return oftexmathParser.RULE_superset

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterSuperset(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitSuperset(self)




    def superset(self):

        localctx = oftexmathParser.SupersetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_superset)
        self._la = 0 # Token type
        try:
            self.state = 207
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(oftexmathParser.SUPERSET)
                self.state = 192
                _la = self._input.LA(1)
                if not(_la==oftexmathParser.VARIABLE or _la==oftexmathParser.NUMBER):
                    self._errHandler.recoverInline(self)
                self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(oftexmathParser.SUPERSET)
                self.state = 194
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 201
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        self.state = 195 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 196 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 197 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 198 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 199 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 200 
                        self.signs()
                        pass


                    self.state = 203 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0)):
                        break

                self.state = 205
                self.match(oftexmathParser.RIGHTBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.MainexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BACKSLASH(self):
            return self.getToken(oftexmathParser.BACKSLASH, 0)

        def mainwords(self):
            return self.getTypedRuleContext(oftexmathParser.MainwordsContext,0)


        def LEFTBRACE(self):
            return self.getToken(oftexmathParser.LEFTBRACE, 0)

        def subwords(self):
            return self.getTypedRuleContext(oftexmathParser.SubwordsContext,0)


        def RIGHTBRACE(self):
            return self.getToken(oftexmathParser.RIGHTBRACE, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_mainexpr

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterMainexpr(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitMainexpr(self)




    def mainexpr(self):

        localctx = oftexmathParser.MainexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_mainexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(oftexmathParser.BACKSLASH)
            self.state = 210 
            self.mainwords()
            self.state = 211
            self.match(oftexmathParser.LEFTBRACE)
            self.state = 212 
            self.subwords()
            self.state = 213
            self.match(oftexmathParser.RIGHTBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BACKSLASH(self):
            return self.getToken(oftexmathParser.BACKSLASH, 0)

        def keywords(self):
            return self.getTypedRuleContext(oftexmathParser.KeywordsContext,0)


        def subset(self):
            return self.getTypedRuleContext(oftexmathParser.SubsetContext,0)


        def superset(self):
            return self.getTypedRuleContext(oftexmathParser.SupersetContext,0)


        def LEFTBRACE(self, i=None):
            if i is None:
                return self.getTokens(oftexmathParser.LEFTBRACE)
            else:
                return self.getToken(oftexmathParser.LEFTBRACE, i)

        def RIGHTBRACE(self, i=None):
            if i is None:
                return self.getTokens(oftexmathParser.RIGHTBRACE)
            else:
                return self.getToken(oftexmathParser.RIGHTBRACE, i)

        def braceoc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.BraceocContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.BraceocContext,i)


        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.VariableContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.VariableContext,i)


        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.NumberContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.NumberContext,i)


        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.ExprContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.ExprContext,i)


        def muldiv(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.MuldivContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.MuldivContext,i)


        def signs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.SignsContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.SignsContext,i)


        def getRuleIndex(self):
            return oftexmathParser.RULE_expr

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitExpr(self)




    def expr(self):

        localctx = oftexmathParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 332
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(oftexmathParser.BACKSLASH)
                self.state = 216 
                self.keywords()
                self.state = 219
                token = self._input.LA(1)
                if token in [oftexmathParser.SUBSET]:
                    self.state = 217 
                    self.subset()
                    pass
                elif token in [oftexmathParser.SUPERSET]:
                    self.state = 218 
                    self.superset()
                    pass
                elif token in [oftexmathParser.EOF, oftexmathParser.VARIABLE, oftexmathParser.NUMBER, oftexmathParser.BACKSLASH, oftexmathParser.RIGHTBRACE, oftexmathParser.COLFORMAT, oftexmathParser.BRACEOPEN, oftexmathParser.BRACECLOSE, oftexmathParser.EQ, oftexmathParser.PLUS, oftexmathParser.MINUS, oftexmathParser.MUL, oftexmathParser.DIV, oftexmathParser.ROWDELIMIT]:
                    pass
                else:
                    raise NoViableAltException(self)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(oftexmathParser.BACKSLASH)
                self.state = 222 
                self.keywords()
                self.state = 224
                _la = self._input.LA(1)
                if _la==oftexmathParser.SUBSET:
                    self.state = 223 
                    self.subset()


                self.state = 226 
                self.superset()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(oftexmathParser.BACKSLASH)
                self.state = 229 
                self.keywords()
                self.state = 230
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0):
                    self.state = 237
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 231 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 232 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 233 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 234 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 235 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 236 
                        self.signs()
                        pass


                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 242
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 245
                token = self._input.LA(1)
                if token in [oftexmathParser.SUBSET]:
                    self.state = 243 
                    self.subset()
                    pass
                elif token in [oftexmathParser.SUPERSET]:
                    self.state = 244 
                    self.superset()
                    pass
                elif token in [oftexmathParser.EOF, oftexmathParser.VARIABLE, oftexmathParser.NUMBER, oftexmathParser.BACKSLASH, oftexmathParser.RIGHTBRACE, oftexmathParser.COLFORMAT, oftexmathParser.BRACEOPEN, oftexmathParser.BRACECLOSE, oftexmathParser.EQ, oftexmathParser.PLUS, oftexmathParser.MINUS, oftexmathParser.MUL, oftexmathParser.DIV, oftexmathParser.ROWDELIMIT]:
                    pass
                else:
                    raise NoViableAltException(self)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.match(oftexmathParser.BACKSLASH)
                self.state = 248 
                self.keywords()
                self.state = 249
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0):
                    self.state = 256
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 250 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 251 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 252 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 253 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 254 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 255 
                        self.signs()
                        pass


                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 261
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 263
                _la = self._input.LA(1)
                if _la==oftexmathParser.SUBSET:
                    self.state = 262 
                    self.subset()


                self.state = 265 
                self.superset()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(oftexmathParser.BACKSLASH)
                self.state = 268 
                self.keywords()
                self.state = 269
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0):
                    self.state = 276
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        self.state = 270 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 271 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 272 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 273 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 274 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 275 
                        self.signs()
                        pass


                    self.state = 280
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 281
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 282
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0):
                    self.state = 289
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 283 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 284 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 285 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 286 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 287 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 288 
                        self.signs()
                        pass


                    self.state = 293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 294
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 297
                token = self._input.LA(1)
                if token in [oftexmathParser.SUBSET]:
                    self.state = 295 
                    self.subset()
                    pass
                elif token in [oftexmathParser.SUPERSET]:
                    self.state = 296 
                    self.superset()
                    pass
                elif token in [oftexmathParser.EOF, oftexmathParser.VARIABLE, oftexmathParser.NUMBER, oftexmathParser.BACKSLASH, oftexmathParser.RIGHTBRACE, oftexmathParser.COLFORMAT, oftexmathParser.BRACEOPEN, oftexmathParser.BRACECLOSE, oftexmathParser.EQ, oftexmathParser.PLUS, oftexmathParser.MINUS, oftexmathParser.MUL, oftexmathParser.DIV, oftexmathParser.ROWDELIMIT]:
                    pass
                else:
                    raise NoViableAltException(self)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 299
                self.match(oftexmathParser.BACKSLASH)
                self.state = 300 
                self.keywords()
                self.state = 301
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0):
                    self.state = 308
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 302 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 303 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 304 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 305 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 306 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 307 
                        self.signs()
                        pass


                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 313
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 314
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS))) != 0):
                    self.state = 321
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 315 
                        self.braceoc()
                        pass

                    elif la_ == 2:
                        self.state = 316 
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 317 
                        self.number()
                        pass

                    elif la_ == 4:
                        self.state = 318 
                        self.expr()
                        pass

                    elif la_ == 5:
                        self.state = 319 
                        self.muldiv()
                        pass

                    elif la_ == 6:
                        self.state = 320 
                        self.signs()
                        pass


                    self.state = 325
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 326
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 328
                _la = self._input.LA(1)
                if _la==oftexmathParser.SUBSET:
                    self.state = 327 
                    self.subset()


                self.state = 330 
                self.superset()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainwordsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.MainwordsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MAINWORDS(self):
            return self.getToken(oftexmathParser.MAINWORDS, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_mainwords

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterMainwords(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitMainwords(self)




    def mainwords(self):

        localctx = oftexmathParser.MainwordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mainwords)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(oftexmathParser.MAINWORDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubwordsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.SubwordsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SUBWORDS(self):
            return self.getToken(oftexmathParser.SUBWORDS, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_subwords

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterSubwords(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitSubwords(self)




    def subwords(self):

        localctx = oftexmathParser.SubwordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_subwords)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(oftexmathParser.SUBWORDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(oftexmathParser.KeywordsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def KEYWORDS(self):
            return self.getToken(oftexmathParser.KEYWORDS, 0)

        def getRuleIndex(self):
            return oftexmathParser.RULE_keywords

        def enterRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.enterKeywords(self)

        def exitRule(self, listener):
            if isinstance( listener, oftexmathListener ):
                listener.exitKeywords(self)




    def keywords(self):

        localctx = oftexmathParser.KeywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_keywords)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(oftexmathParser.KEYWORDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




