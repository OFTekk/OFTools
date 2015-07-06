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
        buf.write(u"\26\u015d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\3\2\6\2*\n\2\r\2\16\2+\3\3\3\3\3")
        buf.write(u"\3\7\3\61\n\3\f\3\16\3\64\13\3\3\3\3\3\3\3\7\39\n\3\f")
        buf.write(u"\3\16\3<\13\3\3\3\3\3\3\3\5\3A\n\3\3\4\6\4D\n\4\r\4\16")
        buf.write(u"\4E\3\4\3\4\3\4\7\4K\n\4\f\4\16\4N\13\4\3\4\6\4Q\n\4")
        buf.write(u"\r\4\16\4R\3\4\3\4\7\4W\n\4\f\4\16\4Z\13\4\3\4\6\4]\n")
        buf.write(u"\4\r\4\16\4^\3\4\3\4\7\4c\n\4\f\4\16\4f\13\4\3\4\6\4")
        buf.write(u"i\n\4\r\4\16\4j\3\4\3\4\7\4o\n\4\f\4\16\4r\13\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4|\n\4\3\5\3\5\7\5\u0080")
        buf.write(u"\n\5\f\5\16\5\u0083\13\5\3\5\3\5\3\6\3\6\3\7\3\7\5\7")
        buf.write(u"\u008b\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0095")
        buf.write(u"\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a9\n\b\5\b\u00ab")
        buf.write(u"\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00b5\n\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00bf\n\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c9\n\t\5\t\u00cb\n\t")
        buf.write(u"\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\5\f\u00da\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write(u"\5\r\u00e5\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write(u"\u00ee\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00f7")
        buf.write(u"\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0155")
        buf.write(u"\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\2\2\25\2\4\6")
        buf.write(u"\b\n\f\16\20\22\24\26\30\32\34\36 \"$&\2\4\3\2\r\17\3")
        buf.write(u"\2\3\4\u019c\2)\3\2\2\2\4@\3\2\2\2\6{\3\2\2\2\b}\3\2")
        buf.write(u"\2\2\n\u0086\3\2\2\2\f\u008a\3\2\2\2\16\u00aa\3\2\2\2")
        buf.write(u"\20\u00ca\3\2\2\2\22\u00cc\3\2\2\2\24\u00ce\3\2\2\2\26")
        buf.write(u"\u00d9\3\2\2\2\30\u00e4\3\2\2\2\32\u00ed\3\2\2\2\34\u00f6")
        buf.write(u"\3\2\2\2\36\u00f8\3\2\2\2 \u0154\3\2\2\2\"\u0156\3\2")
        buf.write(u"\2\2$\u0158\3\2\2\2&\u015a\3\2\2\2(*\5\4\3\2)(\3\2\2")
        buf.write(u"\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\3\3\2\2\2-\62\5\36")
        buf.write(u"\20\2.\61\5\6\4\2/\61\5\36\20\2\60.\3\2\2\2\60/\3\2\2")
        buf.write(u"\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63A\3\2")
        buf.write(u"\2\2\64\62\3\2\2\2\65:\5\36\20\2\669\5\6\4\2\679\5\36")
        buf.write(u"\20\28\66\3\2\2\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3")
        buf.write(u"\2\2\2;=\3\2\2\2<:\3\2\2\2=>\5\36\20\2>A\3\2\2\2?A\5")
        buf.write(u"\6\4\2@-\3\2\2\2@\65\3\2\2\2@?\3\2\2\2A\5\3\2\2\2BD\5")
        buf.write(u"\b\5\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FL\3\2")
        buf.write(u"\2\2GK\5\26\f\2HK\5\30\r\2IK\5 \21\2JG\3\2\2\2JH\3\2")
        buf.write(u"\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M|\3\2\2")
        buf.write(u"\2NL\3\2\2\2OQ\5\26\f\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2\2")
        buf.write(u"RS\3\2\2\2SX\3\2\2\2TW\5\30\r\2UW\5 \21\2VT\3\2\2\2V")
        buf.write(u"U\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y|\3\2\2\2ZX\3")
        buf.write(u"\2\2\2[]\5\30\r\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3")
        buf.write(u"\2\2\2_d\3\2\2\2`c\5\26\f\2ac\5 \21\2b`\3\2\2\2ba\3\2")
        buf.write(u"\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2e|\3\2\2\2fd\3\2\2")
        buf.write(u"\2gi\5 \21\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2")
        buf.write(u"kp\3\2\2\2lo\5\26\f\2mo\5\30\r\2nl\3\2\2\2nm\3\2\2\2")
        buf.write(u"or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q|\3\2\2\2rp\3\2\2\2s|")
        buf.write(u"\5\f\7\2t|\5\n\6\2uv\5\22\n\2vw\b\4\1\2w|\3\2\2\2xy\5")
        buf.write(u"\24\13\2yz\b\4\1\2z|\3\2\2\2{C\3\2\2\2{P\3\2\2\2{\\\3")
        buf.write(u"\2\2\2{h\3\2\2\2{s\3\2\2\2{t\3\2\2\2{u\3\2\2\2{x\3\2")
        buf.write(u"\2\2|\7\3\2\2\2}\u0081\7\13\2\2~\u0080\5\6\4\2\177~\3")
        buf.write(u"\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082")
        buf.write(u"\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084")
        buf.write(u"\u0085\7\f\2\2\u0085\t\3\2\2\2\u0086\u0087\t\2\2\2\u0087")
        buf.write(u"\13\3\2\2\2\u0088\u008b\5\16\b\2\u0089\u008b\5\20\t\2")
        buf.write(u"\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\r\3\2")
        buf.write(u"\2\2\u008c\u008d\5\26\f\2\u008d\u0094\7\20\2\2\u008e")
        buf.write(u"\u0095\5\b\5\2\u008f\u0095\5\30\r\2\u0090\u0095\5 \21")
        buf.write(u"\2\u0091\u0095\5\26\f\2\u0092\u0095\5\20\t\2\u0093\u0095")
        buf.write(u"\5\16\b\2\u0094\u008e\3\2\2\2\u0094\u008f\3\2\2\2\u0094")
        buf.write(u"\u0090\3\2\2\2\u0094\u0091\3\2\2\2\u0094\u0092\3\2\2")
        buf.write(u"\2\u0094\u0093\3\2\2\2\u0095\u00ab\3\2\2\2\u0096\u0097")
        buf.write(u"\5\30\r\2\u0097\u009e\7\20\2\2\u0098\u009f\5\b\5\2\u0099")
        buf.write(u"\u009f\5 \21\2\u009a\u009f\5\26\f\2\u009b\u009f\5\30")
        buf.write(u"\r\2\u009c\u009f\5\20\t\2\u009d\u009f\5\16\b\2\u009e")
        buf.write(u"\u0098\3\2\2\2\u009e\u0099\3\2\2\2\u009e\u009a\3\2\2")
        buf.write(u"\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d")
        buf.write(u"\3\2\2\2\u009f\u00ab\3\2\2\2\u00a0\u00a1\5 \21\2\u00a1")
        buf.write(u"\u00a8\7\20\2\2\u00a2\u00a9\5\b\5\2\u00a3\u00a9\5\26")
        buf.write(u"\f\2\u00a4\u00a9\5\30\r\2\u00a5\u00a9\5 \21\2\u00a6\u00a9")
        buf.write(u"\5\20\t\2\u00a7\u00a9\5\16\b\2\u00a8\u00a2\3\2\2\2\u00a8")
        buf.write(u"\u00a3\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a5\3\2\2")
        buf.write(u"\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ab")
        buf.write(u"\3\2\2\2\u00aa\u008c\3\2\2\2\u00aa\u0096\3\2\2\2\u00aa")
        buf.write(u"\u00a0\3\2\2\2\u00ab\17\3\2\2\2\u00ac\u00ad\5\26\f\2")
        buf.write(u"\u00ad\u00b4\7\21\2\2\u00ae\u00b5\5\b\5\2\u00af\u00b5")
        buf.write(u"\5\30\r\2\u00b0\u00b5\5 \21\2\u00b1\u00b5\5\26\f\2\u00b2")
        buf.write(u"\u00b5\5\20\t\2\u00b3\u00b5\5\16\b\2\u00b4\u00ae\3\2")
        buf.write(u"\2\2\u00b4\u00af\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b4\u00b1")
        buf.write(u"\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write(u"\u00cb\3\2\2\2\u00b6\u00b7\5\30\r\2\u00b7\u00be\7\21")
        buf.write(u"\2\2\u00b8\u00bf\5\b\5\2\u00b9\u00bf\5 \21\2\u00ba\u00bf")
        buf.write(u"\5\26\f\2\u00bb\u00bf\5\30\r\2\u00bc\u00bf\5\20\t\2\u00bd")
        buf.write(u"\u00bf\5\16\b\2\u00be\u00b8\3\2\2\2\u00be\u00b9\3\2\2")
        buf.write(u"\2\u00be\u00ba\3\2\2\2\u00be\u00bb\3\2\2\2\u00be\u00bc")
        buf.write(u"\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\u00cb\3\2\2\2\u00c0")
        buf.write(u"\u00c1\5 \21\2\u00c1\u00c8\7\21\2\2\u00c2\u00c9\5\b\5")
        buf.write(u"\2\u00c3\u00c9\5\26\f\2\u00c4\u00c9\5\30\r\2\u00c5\u00c9")
        buf.write(u"\5 \21\2\u00c6\u00c9\5\20\t\2\u00c7\u00c9\5\16\b\2\u00c8")
        buf.write(u"\u00c2\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c8\u00c4\3\2\2")
        buf.write(u"\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7")
        buf.write(u"\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00ac\3\2\2\2\u00ca")
        buf.write(u"\u00b6\3\2\2\2\u00ca\u00c0\3\2\2\2\u00cb\21\3\2\2\2\u00cc")
        buf.write(u"\u00cd\7\n\2\2\u00cd\23\3\2\2\2\u00ce\u00cf\7\22\2\2")
        buf.write(u"\u00cf\25\3\2\2\2\u00d0\u00da\7\3\2\2\u00d1\u00d2\7\3")
        buf.write(u"\2\2\u00d2\u00da\5\32\16\2\u00d3\u00d4\7\3\2\2\u00d4")
        buf.write(u"\u00da\5\34\17\2\u00d5\u00d6\7\3\2\2\u00d6\u00d7\5\32")
        buf.write(u"\16\2\u00d7\u00d8\5\34\17\2\u00d8\u00da\3\2\2\2\u00d9")
        buf.write(u"\u00d0\3\2\2\2\u00d9\u00d1\3\2\2\2\u00d9\u00d3\3\2\2")
        buf.write(u"\2\u00d9\u00d5\3\2\2\2\u00da\27\3\2\2\2\u00db\u00e5\7")
        buf.write(u"\4\2\2\u00dc\u00dd\7\4\2\2\u00dd\u00e5\5\32\16\2\u00de")
        buf.write(u"\u00df\7\4\2\2\u00df\u00e5\5\34\17\2\u00e0\u00e1\7\4")
        buf.write(u"\2\2\u00e1\u00e2\5\32\16\2\u00e2\u00e3\5\34\17\2\u00e3")
        buf.write(u"\u00e5\3\2\2\2\u00e4\u00db\3\2\2\2\u00e4\u00dc\3\2\2")
        buf.write(u"\2\u00e4\u00de\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e5\31\3")
        buf.write(u"\2\2\2\u00e6\u00e7\7\6\2\2\u00e7\u00ee\t\3\2\2\u00e8")
        buf.write(u"\u00e9\7\6\2\2\u00e9\u00ea\7\b\2\2\u00ea\u00eb\5\6\4")
        buf.write(u"\2\u00eb\u00ec\7\t\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00e6")
        buf.write(u"\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ee\33\3\2\2\2\u00ef\u00f0")
        buf.write(u"\7\7\2\2\u00f0\u00f7\t\3\2\2\u00f1\u00f2\7\7\2\2\u00f2")
        buf.write(u"\u00f3\7\b\2\2\u00f3\u00f4\5\6\4\2\u00f4\u00f5\7\t\2")
        buf.write(u"\2\u00f5\u00f7\3\2\2\2\u00f6\u00ef\3\2\2\2\u00f6\u00f1")
        buf.write(u"\3\2\2\2\u00f7\35\3\2\2\2\u00f8\u00f9\7\5\2\2\u00f9\u00fa")
        buf.write(u"\5\"\22\2\u00fa\u00fb\7\b\2\2\u00fb\u00fc\5$\23\2\u00fc")
        buf.write(u"\u00fd\b\20\1\2\u00fd\u00fe\7\t\2\2\u00fe\37\3\2\2\2")
        buf.write(u"\u00ff\u0100\7\5\2\2\u0100\u0155\5&\24\2\u0101\u0102")
        buf.write(u"\7\5\2\2\u0102\u0155\5&\24\2\u0103\u0104\7\5\2\2\u0104")
        buf.write(u"\u0105\5&\24\2\u0105\u0106\7\b\2\2\u0106\u0107\5\6\4")
        buf.write(u"\2\u0107\u0108\7\t\2\2\u0108\u0155\3\2\2\2\u0109\u010a")
        buf.write(u"\7\5\2\2\u010a\u010b\5&\24\2\u010b\u010c\5\32\16\2\u010c")
        buf.write(u"\u0155\3\2\2\2\u010d\u010e\7\5\2\2\u010e\u010f\5&\24")
        buf.write(u"\2\u010f\u0110\7\b\2\2\u0110\u0111\5\6\4\2\u0111\u0112")
        buf.write(u"\7\t\2\2\u0112\u0113\5\32\16\2\u0113\u0155\3\2\2\2\u0114")
        buf.write(u"\u0115\7\5\2\2\u0115\u0116\5&\24\2\u0116\u0117\5\34\17")
        buf.write(u"\2\u0117\u0155\3\2\2\2\u0118\u0119\7\5\2\2\u0119\u011a")
        buf.write(u"\5&\24\2\u011a\u011b\7\b\2\2\u011b\u011c\5\6\4\2\u011c")
        buf.write(u"\u011d\7\t\2\2\u011d\u011e\5\34\17\2\u011e\u0155\3\2")
        buf.write(u"\2\2\u011f\u0120\7\5\2\2\u0120\u0121\5&\24\2\u0121\u0122")
        buf.write(u"\5\32\16\2\u0122\u0123\5\34\17\2\u0123\u0155\3\2\2\2")
        buf.write(u"\u0124\u0125\7\5\2\2\u0125\u0126\5&\24\2\u0126\u0127")
        buf.write(u"\7\b\2\2\u0127\u0128\5\6\4\2\u0128\u0129\7\t\2\2\u0129")
        buf.write(u"\u012a\5\32\16\2\u012a\u012b\5\34\17\2\u012b\u0155\3")
        buf.write(u"\2\2\2\u012c\u012d\7\5\2\2\u012d\u012e\5&\24\2\u012e")
        buf.write(u"\u012f\7\b\2\2\u012f\u0130\5\6\4\2\u0130\u0131\7\t\2")
        buf.write(u"\2\u0131\u0132\7\b\2\2\u0132\u0133\5\6\4\2\u0133\u0134")
        buf.write(u"\7\t\2\2\u0134\u0155\3\2\2\2\u0135\u0136\7\5\2\2\u0136")
        buf.write(u"\u0137\5&\24\2\u0137\u0138\7\b\2\2\u0138\u0139\5\6\4")
        buf.write(u"\2\u0139\u013a\7\t\2\2\u013a\u013b\7\b\2\2\u013b\u013c")
        buf.write(u"\5\6\4\2\u013c\u013d\7\t\2\2\u013d\u013e\5\32\16\2\u013e")
        buf.write(u"\u0155\3\2\2\2\u013f\u0140\7\5\2\2\u0140\u0141\5&\24")
        buf.write(u"\2\u0141\u0142\7\b\2\2\u0142\u0143\5\6\4\2\u0143\u0144")
        buf.write(u"\7\t\2\2\u0144\u0145\7\b\2\2\u0145\u0146\5\6\4\2\u0146")
        buf.write(u"\u0147\7\t\2\2\u0147\u0148\5\34\17\2\u0148\u0155\3\2")
        buf.write(u"\2\2\u0149\u014a\7\5\2\2\u014a\u014b\5&\24\2\u014b\u014c")
        buf.write(u"\7\b\2\2\u014c\u014d\5\6\4\2\u014d\u014e\7\t\2\2\u014e")
        buf.write(u"\u014f\7\b\2\2\u014f\u0150\5\6\4\2\u0150\u0151\7\t\2")
        buf.write(u"\2\u0151\u0152\5\32\16\2\u0152\u0153\5\34\17\2\u0153")
        buf.write(u"\u0155\3\2\2\2\u0154\u00ff\3\2\2\2\u0154\u0101\3\2\2")
        buf.write(u"\2\u0154\u0103\3\2\2\2\u0154\u0109\3\2\2\2\u0154\u010d")
        buf.write(u"\3\2\2\2\u0154\u0114\3\2\2\2\u0154\u0118\3\2\2\2\u0154")
        buf.write(u"\u011f\3\2\2\2\u0154\u0124\3\2\2\2\u0154\u012c\3\2\2")
        buf.write(u"\2\u0154\u0135\3\2\2\2\u0154\u013f\3\2\2\2\u0154\u0149")
        buf.write(u"\3\2\2\2\u0155!\3\2\2\2\u0156\u0157\7\23\2\2\u0157#\3")
        buf.write(u"\2\2\2\u0158\u0159\7\24\2\2\u0159%\3\2\2\2\u015a\u015b")
        buf.write(u"\7\25\2\2\u015b\'\3\2\2\2$+\60\628:@EJLRVX^bdjnp{\u0081")
        buf.write(u"\u008a\u0094\u009e\u00a8\u00aa\u00b4\u00be\u00c8\u00ca")
        buf.write(u"\u00d9\u00e4\u00ed\u00f6\u0154")
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
            self.state = 62
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43 
                self.mainexpr()
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 46
                        la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                        if la_ == 1:
                            self.state = 44 
                            self.allinone()
                            pass

                        elif la_ == 2:
                            self.state = 45 
                            self.mainexpr()
                            pass

                 
                    self.state = 50
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51 
                self.mainexpr()
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 54
                        la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                        if la_ == 1:
                            self.state = 52 
                            self.allinone()
                            pass

                        elif la_ == 2:
                            self.state = 53 
                            self.mainexpr()
                            pass

                 
                    self.state = 58
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 59 
                self.mainexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61 
                self.allinone()
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
            self.state = 121
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 64 
                        self.braceoc()

                    else:
                        raise NoViableAltException(self)
                    self.state = 67 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 72
                        token = self._input.LA(1)
                        if token in [oftexmathParser.VARIABLE]:
                            self.state = 69 
                            self.variable()

                        elif token in [oftexmathParser.NUMBER]:
                            self.state = 70 
                            self.number()

                        elif token in [oftexmathParser.BACKSLASH]:
                            self.state = 71 
                            self.expr()

                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 76
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 77 
                        self.variable()

                    else:
                        raise NoViableAltException(self)
                    self.state = 80 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 84
                        token = self._input.LA(1)
                        if token in [oftexmathParser.NUMBER]:
                            self.state = 82 
                            self.number()

                        elif token in [oftexmathParser.BACKSLASH]:
                            self.state = 83 
                            self.expr()

                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 88
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 89 
                        self.number()

                    else:
                        raise NoViableAltException(self)
                    self.state = 92 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 96
                        token = self._input.LA(1)
                        if token in [oftexmathParser.VARIABLE]:
                            self.state = 94 
                            self.variable()

                        elif token in [oftexmathParser.BACKSLASH]:
                            self.state = 95 
                            self.expr()

                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 100
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 101 
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 104 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 108
                        token = self._input.LA(1)
                        if token in [oftexmathParser.VARIABLE]:
                            self.state = 106 
                            self.variable()

                        elif token in [oftexmathParser.NUMBER]:
                            self.state = 107 
                            self.number()

                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 112
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113 
                self.muldiv()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114 
                self.signs()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115 
                self.colformat()
                0,1
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 118 
                self.rowdelimit()
                0,1
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

        def allinone(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.AllinoneContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.AllinoneContext,i)


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
            self.state = 123
            self.match(oftexmathParser.BRACEOPEN)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << oftexmathParser.VARIABLE) | (1 << oftexmathParser.NUMBER) | (1 << oftexmathParser.BACKSLASH) | (1 << oftexmathParser.COLFORMAT) | (1 << oftexmathParser.BRACEOPEN) | (1 << oftexmathParser.EQ) | (1 << oftexmathParser.PLUS) | (1 << oftexmathParser.MINUS) | (1 << oftexmathParser.ROWDELIMIT))) != 0):
                self.state = 124 
                self.allinone()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
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
            self.state = 132
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
            self.state = 136
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134 
                self.mul()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135 
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
            self.state = 168
            token = self._input.LA(1)
            if token in [oftexmathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138 
                self.variable()
                self.state = 139
                self.match(oftexmathParser.MUL)
                self.state = 146
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 140 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 141 
                    self.number()
                    pass

                elif la_ == 3:
                    self.state = 142 
                    self.expr()
                    pass

                elif la_ == 4:
                    self.state = 143 
                    self.variable()
                    pass

                elif la_ == 5:
                    self.state = 144 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 145 
                    self.mul()
                    pass



            elif token in [oftexmathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148 
                self.number()
                self.state = 149
                self.match(oftexmathParser.MUL)
                self.state = 156
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 150 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 151 
                    self.expr()
                    pass

                elif la_ == 3:
                    self.state = 152 
                    self.variable()
                    pass

                elif la_ == 4:
                    self.state = 153 
                    self.number()
                    pass

                elif la_ == 5:
                    self.state = 154 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 155 
                    self.mul()
                    pass



            elif token in [oftexmathParser.BACKSLASH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158 
                self.expr()
                self.state = 159
                self.match(oftexmathParser.MUL)
                self.state = 166
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 160 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 161 
                    self.variable()
                    pass

                elif la_ == 3:
                    self.state = 162 
                    self.number()
                    pass

                elif la_ == 4:
                    self.state = 163 
                    self.expr()
                    pass

                elif la_ == 5:
                    self.state = 164 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 165 
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
            self.state = 200
            token = self._input.LA(1)
            if token in [oftexmathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170 
                self.variable()
                self.state = 171
                self.match(oftexmathParser.DIV)
                self.state = 178
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 172 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 173 
                    self.number()
                    pass

                elif la_ == 3:
                    self.state = 174 
                    self.expr()
                    pass

                elif la_ == 4:
                    self.state = 175 
                    self.variable()
                    pass

                elif la_ == 5:
                    self.state = 176 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 177 
                    self.mul()
                    pass



            elif token in [oftexmathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180 
                self.number()
                self.state = 181
                self.match(oftexmathParser.DIV)
                self.state = 188
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 182 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 183 
                    self.expr()
                    pass

                elif la_ == 3:
                    self.state = 184 
                    self.variable()
                    pass

                elif la_ == 4:
                    self.state = 185 
                    self.number()
                    pass

                elif la_ == 5:
                    self.state = 186 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 187 
                    self.mul()
                    pass



            elif token in [oftexmathParser.BACKSLASH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190 
                self.expr()
                self.state = 191
                self.match(oftexmathParser.DIV)
                self.state = 198
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 192 
                    self.braceoc()
                    pass

                elif la_ == 2:
                    self.state = 193 
                    self.variable()
                    pass

                elif la_ == 3:
                    self.state = 194 
                    self.number()
                    pass

                elif la_ == 4:
                    self.state = 195 
                    self.expr()
                    pass

                elif la_ == 5:
                    self.state = 196 
                    self.div()
                    pass

                elif la_ == 6:
                    self.state = 197 
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
            self.state = 202
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
            self.state = 204
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
            self.state = 215
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(oftexmathParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(oftexmathParser.VARIABLE)
                self.state = 208 
                self.subset()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(oftexmathParser.VARIABLE)
                self.state = 210 
                self.superset()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.match(oftexmathParser.VARIABLE)
                self.state = 212 
                self.subset()
                self.state = 213 
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
            self.state = 226
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(oftexmathParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(oftexmathParser.NUMBER)
                self.state = 219 
                self.subset()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(oftexmathParser.NUMBER)
                self.state = 221 
                self.superset()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(oftexmathParser.NUMBER)
                self.state = 223 
                self.subset()
                self.state = 224 
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

        def allinone(self):
            return self.getTypedRuleContext(oftexmathParser.AllinoneContext,0)


        def RIGHTBRACE(self):
            return self.getToken(oftexmathParser.RIGHTBRACE, 0)

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
            self.state = 235
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(oftexmathParser.SUBSET)
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==oftexmathParser.VARIABLE or _la==oftexmathParser.NUMBER):
                    self._errHandler.recoverInline(self)
                self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(oftexmathParser.SUBSET)
                self.state = 231
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 232 
                self.allinone()
                self.state = 233
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

        def allinone(self):
            return self.getTypedRuleContext(oftexmathParser.AllinoneContext,0)


        def RIGHTBRACE(self):
            return self.getToken(oftexmathParser.RIGHTBRACE, 0)

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
            self.state = 244
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(oftexmathParser.SUPERSET)
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==oftexmathParser.VARIABLE or _la==oftexmathParser.NUMBER):
                    self._errHandler.recoverInline(self)
                self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(oftexmathParser.SUPERSET)
                self.state = 240
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 241 
                self.allinone()
                self.state = 242
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
            self.state = 246
            self.match(oftexmathParser.BACKSLASH)
            self.state = 247 
            self.mainwords()
            self.state = 248
            self.match(oftexmathParser.LEFTBRACE)
            self.state = 249 
            self.subwords()
            0,1
            self.state = 251
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


        def LEFTBRACE(self, i=None):
            if i is None:
                return self.getTokens(oftexmathParser.LEFTBRACE)
            else:
                return self.getToken(oftexmathParser.LEFTBRACE, i)

        def allinone(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(oftexmathParser.AllinoneContext)
            else:
                return self.getTypedRuleContext(oftexmathParser.AllinoneContext,i)


        def RIGHTBRACE(self, i=None):
            if i is None:
                return self.getTokens(oftexmathParser.RIGHTBRACE)
            else:
                return self.getToken(oftexmathParser.RIGHTBRACE, i)

        def subset(self):
            return self.getTypedRuleContext(oftexmathParser.SubsetContext,0)


        def superset(self):
            return self.getTypedRuleContext(oftexmathParser.SupersetContext,0)


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
        try:
            self.state = 338
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(oftexmathParser.BACKSLASH)
                self.state = 254 
                self.keywords()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(oftexmathParser.BACKSLASH)
                self.state = 256 
                self.keywords()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(oftexmathParser.BACKSLASH)
                self.state = 258 
                self.keywords()
                self.state = 259
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 260 
                self.allinone()
                self.state = 261
                self.match(oftexmathParser.RIGHTBRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.match(oftexmathParser.BACKSLASH)
                self.state = 264 
                self.keywords()
                self.state = 265 
                self.subset()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(oftexmathParser.BACKSLASH)
                self.state = 268 
                self.keywords()
                self.state = 269
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 270 
                self.allinone()
                self.state = 271
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 272 
                self.subset()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 274
                self.match(oftexmathParser.BACKSLASH)
                self.state = 275 
                self.keywords()
                self.state = 276 
                self.superset()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 278
                self.match(oftexmathParser.BACKSLASH)
                self.state = 279 
                self.keywords()
                self.state = 280
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 281 
                self.allinone()
                self.state = 282
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 283 
                self.superset()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 285
                self.match(oftexmathParser.BACKSLASH)
                self.state = 286 
                self.keywords()
                self.state = 287 
                self.subset()
                self.state = 288 
                self.superset()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 290
                self.match(oftexmathParser.BACKSLASH)
                self.state = 291 
                self.keywords()
                self.state = 292
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 293 
                self.allinone()
                self.state = 294
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 295 
                self.subset()
                self.state = 296 
                self.superset()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 298
                self.match(oftexmathParser.BACKSLASH)
                self.state = 299 
                self.keywords()
                self.state = 300
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 301 
                self.allinone()
                self.state = 302
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 303
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 304 
                self.allinone()
                self.state = 305
                self.match(oftexmathParser.RIGHTBRACE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 307
                self.match(oftexmathParser.BACKSLASH)
                self.state = 308 
                self.keywords()
                self.state = 309
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 310 
                self.allinone()
                self.state = 311
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 312
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 313 
                self.allinone()
                self.state = 314
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 315 
                self.subset()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 317
                self.match(oftexmathParser.BACKSLASH)
                self.state = 318 
                self.keywords()
                self.state = 319
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 320 
                self.allinone()
                self.state = 321
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 322
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 323 
                self.allinone()
                self.state = 324
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 325 
                self.superset()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 327
                self.match(oftexmathParser.BACKSLASH)
                self.state = 328 
                self.keywords()
                self.state = 329
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 330 
                self.allinone()
                self.state = 331
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 332
                self.match(oftexmathParser.LEFTBRACE)
                self.state = 333 
                self.allinone()
                self.state = 334
                self.match(oftexmathParser.RIGHTBRACE)
                self.state = 335 
                self.subset()
                self.state = 336 
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
            self.state = 340
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
            self.state = 342
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
            self.state = 344
            self.match(oftexmathParser.KEYWORDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




