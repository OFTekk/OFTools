#
# coding:utf-8;

import sys
from antlr4 import *
from oftexmathLexer import oftexmathLexer
from oftexmathParser import oftexmathParser
from oftexmathListener import oftexmathListener
from kivy.app import App as KivyApp
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Operand(object):
    def __init__(self, val=0.0):
        if isinstance(val, (int, long, float)):
            self.value = val
            self.constant = True
            self.variable = False
        elif isinstance(val, str):
            self.value = val
            self.constant = False
            self.variable = True
        else:
            raise TypeError
        self.subset = None
        self.superset = None

    def isconstant(self):
        return self.constant

    def isvariable(self):
        return self.variable

    def getvalue(self):
        return self.value

    def setsubset(self, ss):
        if not isinstance(ss, Operand):
            raise TypeError
        self.subset = ss

    def setsuperset(self, ss):
        if not isinstance(ss, Operand):
            raise TypeError
        self.superset = ss

    def kivywidget(self):
        subs = None
        sups = None
        if self.subset:
            subs = self.subset.kivywidget()
            subs.size_hint_x *= 0.5
            subs.size_hint_y *= 0.5
        if self.superset:
            sups = self.superset.kivywidget()
            sups.size_hint_x *= 0.5
            sups.size_hint_y *= 0.5
        if subs and sups:
            lbl = Label(text=str(self.value))
            lbl.size_hint_x = 0.5
            lbl.size_hint_y = 1.0
            hlayout = BoxLayout()
            hlayout.orientation = 'horizontal'
            hlayout.size_hint_x = 1.0
            hlayout.size_hint_y = 1.0
            hlayout.add_widget(lbl)
            vlayout = BoxLayout()
            vlayout.orientation = 'vertical'
            vlayout.size_hint_x = 0.5
            vlayout.size_hint_y = 1.0
            vlayout.add_widget(sups)
            vlayout.add_widget(subs)
            hlayout.add_widget(vlayout)
            return hlayout
        elif subs:
            lbl = Label(text=str(self.value))
            lbl.size_hint_x = 0.5
            lbl.size_hint_y = 1.0
            hlayout = BoxLayout()
            hlayout.orientation = 'horizontal'
            hlayout.size_hint_x = 1.0
            hlayout.size_hint_y = 1.0
            hlayout.add_widget(lbl)
            vlayout = BoxLayout()
            vlayout.orientation = 'vertical'
            vlayout.size_hint_x = 0.5
            vlayout.size_hint_y = 1.0
            vlayout.add_widget(Label(text=''))
            vlayout.add_widget(subs)
            hlayout.add_widget(vlayout)
            return hlayout
        elif sups:
            lbl = Label(text=str(self.value))
            lbl.size_hint_x = 0.5
            lbl.size_hint_y = 1.0
            hlayout = BoxLayout()
            hlayout.orientation = 'horizontal'
            hlayout.size_hint_x = 1.0
            hlayout.size_hint_y = 1.0
            hlayout.add_widget(lbl)
            vlayout = BoxLayout()
            vlayout.orientation = 'vertical'
            vlayout.size_hint_x = 0.5
            vlayout.size_hint_y = 1.0
            vlayout.add_widget(sups)
            vlayout.add_widget(Label(text=''))
            hlayout.add_widget(vlayout)
            return hlayout
        else:
            lbl = Label(text=str(self.value))
            lbl.size_hint_x = 1.0
            lbl.size_hint_y = 1.0
            return lbl;


class Operator(object):
    def __init__(self, op='add', op1=None, op2=None):
        self.operation = None
        self.operand1 = None
        self.operand2 = None
        if not isinstance(op, str):
            raise TypeError
        if not isinstance(op1, (Operand, Operator)):
            raise TypeError
        if not isinstance(op2, (Operand, Operator)):
            raise TypeError
        if op in ('eq', 'add', 'sub', 'mul', 'div'):
            self.operation = op
            self.operand1 = op1
            self.operand2 = op2
        else:
            raise ValueError

    def evaluate(self):
        if isinstance(self.operand1, Operand) and isinstance(self.operand2, Operand):
            val1 = self.operand1.getvalue()
            val2 = self.operand2.getvalue()
            val1found = True
            val2found = True
            if self.operand1.isvariable():
                # TODO : variable search
                val1 = val1
                val1found = False
            if self.operand2.isvariable():
                # TODO : variable search
                val2 = val2
                val2found = False
            if val1found and val2found:
                if self.operation == 'add':
                    return val1 + val2
                elif self.operation == 'sub':
                    return val1 - val2
                elif self.operation == 'mul':
                    return val1 * val2
                elif self.operation == 'div':
                    return val1 / val2
                else:
                    return 'assignment to constant'
            else:
                if self.operation == 'add':
                    return str(val1) + '+' + str(val2)
                elif self.operation == 'sub':
                    return str(val1) + '-' + str(val2)
                elif self.operation == 'mul':
                    return str(val1) + '*' + str(val2)
                elif self.operation == 'div':
                    return str(val1) + '/' + str(val2)
                else:
                    return str(val1) + '=' + str(val2)


class LayoutGenerator(object):
    def __init__(self):
        self.childs = []

    def append(self, child):
        self.childs.append(child)
        return self

    def __iadd__(self, child):
        self.childs.append(child)
        return self


class Listener(oftexmathListener):

    class FormatContext(object):
        def __init__(self):
            self.bold = False
            self.italic = False
            self.script = False
            self.fraktur = False
            self.doublestruck = False
            self.sansserif = False
            self.font = 'FreeMath.ttf'
            self.stack = []

        def setbold(self):
            self.doublestruck = False
            self.monospace = False
            self.bold = True

        def clearbold(self):
            self.bold = False

        def setitalic(self):
            self.script = False
            self.fraktur = False
            self.doublestruck = False
            self.monospace = False
            self.italic = True

        def clearitalic(self):
            self.italic = False

        def setscript(self):
            self.italic = False
            self.fraktur = False
            self.doublestruck = False
            self.sansserif = False
            self.monospace = False
            self.script = True

        def clearscript(self):
            self.script = False

        def setfraktur(self):
            self.italic = False
            self.script = False
            self.doublestruck = False
            self.sansserif = False
            self.monospace = False
            self.fraktur = True

        def clearfraktur(self):
            self.fraktur = False

        def setdoublestruck(self):
            self.italic = False
            self.bold = False
            self.script = False
            self.fraktur = False
            self.sansserif = False
            self.monospace = False
            self.doublestruck = True

        def cleardoublestruck(self):
            self.doublestruck = False

        def setsansserif(self):
            self.script = False
            self.fraktur = False
            self.doublestruck = False
            self.monospace = False
            self.sansserif = True

        def clearsansserif(self):
            self.sansserif = False

        def setmonospace(self):
            self.italic = False
            self.bold = False
            self.script = False
            self.fraktur = False
            self.sansserif = False
            self.doublestruck = False
            self.monospace = True

        def clearmonospace(self):
            self.monospace = False

        def cleartype(self):
            self.script = False
            self.fraktur = False
            self.sansserif = False
            self.doublestruck = False
            self.monospace = False

        def clearemphasise(self):
            self.italic = False
            self.bold = False

        def setfontmono(self):
            self.font = 'FreeMono.ttf'

        def setfontsans(self):
            self.font = 'FreeSans.ttf'

        def setfontserif(self):
            self.font = 'FreeSerif.ttf'

        def setfontmath(self):
            self.font = 'FreeMath.ttf'

        def getfont(self):
            return self.font

        def isbolditalic(self):
            return self.bold and self.italic

        def isbold(self):
            return self.bold

        def isitalic(self):
            return self.italic

        def isscript(self):
            return self.script

        def isfraktur(self):
            return self.fraktur

        def isdoublestruck(self):
            return self.doublestruck

        def issansserif(self):
            return self.sansserif

        def ismonospace(self):
            return self.monospace

        def push(self):
            self.stack.append([self.bold, self.italic, self.script, self.fraktur, self.font])
            return len(self.stack)

        def pop(self):
            popped = self.stack.pop()
            if popped:
                self.bold = popped[0]
                self.italic = popped[1]
                self.script = popped[2]
                self.fraktur = popped[3]
                self.font = popped[4]
                return True
            return False

    def __init__(self, dbg=False, parser=None):
        super(Listener, self).__init__()
        self.debug = dbg
        self.parser = parser
        self.laystack = []
        self.subsetstack = []
        self.supersetstack = []
        self.lastlay = None
        self.lastvlay = None
        self.lastoperand = None
        self.wasselfstatekeyword = False
        self.lastenter = ''
        self.currentformat = Listener.FormatContext()

    def exitVariable(self, ctx):
        super(Listener, self).exitVariable(ctx)
        if self.debug:
            name = ''
            if ctx.VARIABLE():
                name += ctx.VARIABLE().getText()
            print 'Exited: variable: ' + name

    def exitSuperset(self, ctx):
        super(Listener, self).exitSuperset(ctx)
        self.lastvlay = None
        self.lastlay = self.laystack.pop()
        if self.debug:
            name = ''
            if ctx.VARIABLE():
                name += ctx.VARIABLE().getText() + ';'
            if ctx.NUMBER():
                name += ctx.NUMBER().getText()
            print 'Exited: superset: ' + name

    def exitSubwords(self, ctx):
        super(Listener, self).exitSubwords(ctx)
        if self.debug:
            print 'Exited: subwords'

    def exitSubset(self, ctx):
        self.lastoperand = self.subsetstack.pop()
        self.lastlay = self.laystack.pop()
        self.currentformat.pop()
        super(Listener, self).exitSubset(ctx)
        if self.debug:
            name = ''
            if ctx.VARIABLE():
                name += ctx.VARIABLE().getText() + ';'
            if ctx.NUMBER():
                name += ctx.NUMBER().getText()
            print 'Exited: subset: ' + name

    def exitSigns(self, ctx):
        super(Listener, self).exitSigns(ctx)
        if self.debug:
            print 'Exited: signs'

    def exitRowdelimit(self, ctx):
        super(Listener, self).exitRowdelimit(ctx)
        if self.debug:
            print 'Exited: rowdelimit'

    def exitNumber(self, ctx):
        super(Listener, self).exitNumber(ctx)
        if self.debug:
            print 'Exited: number'

    def exitMuldiv(self, ctx):
        super(Listener, self).exitMuldiv(ctx)
        if self.debug:
            print 'Exited: muldiv'

    def exitMul(self, ctx):
        super(Listener, self).exitMul(ctx)
        if self.debug:
            print 'Exited: mul'

    def exitMainwords(self, ctx):
        super(Listener, self).exitMainwords(ctx)
        if self.debug:
            print 'Exited: mainwords'

    def exitMainexpr(self, ctx):
        super(Listener, self).exitMainexpr(ctx)
        if self.debug:
            print 'Exited: mainexpr'

    def exitMain(self, ctx):
        super(Listener, self).exitMain(ctx)
        if self.debug:
            print 'Exited: main'

    def exitKeywords(self, ctx):
        super(Listener, self).exitKeywords(ctx)
        if self.wasselfstatekeyword:
            self.currentformat.pop()
        if self.debug:
            name = ''
            if ctx.KEYWORDS().getText():
                name += ctx.KEYWORDS().getText()
            print 'Exited: keywords: ' + name

    def exitInit(self, ctx):
        super(Listener, self).exitInit(ctx)
        if self.debug:
            print 'Exited: init'

    def exitExpr(self, ctx):
        super(Listener, self).exitExpr(ctx)
        self.currentformat.cleartype()
        self.currentformat.clearemphasise()
        if self.debug:
            print 'Exited: expr'

    def exitDiv(self, ctx):
        super(Listener, self).exitDiv(ctx)
        if self.debug:
            print 'Exited: div'

    def exitColformat(self, ctx):
        super(Listener, self).exitColformat(ctx)
        if self.debug:
            print 'Exited: colformat'

    def exitBraceoc(self, ctx):
        super(Listener, self).exitBraceoc(ctx)
        if self.debug:
            print 'Exited: braceoc'

    def exitAllinone(self, ctx):
        super(Listener, self).exitAllinone(ctx)
        self.currentformat.pop()
        if self.debug:
            print 'Exited: allinone'

    def enterVariable(self, ctx):
        super(Listener, self).enterVariable(ctx)
        if not len(self.laystack):
            self.lastvlay = None
        if not self.lastlay:
            self.lastlay = BoxLayout()
            self.lastlay.orientation = 'horizontal'
        value = 0
        if ctx.VARIABLE():
            val = ctx.VARIABLE().getText()
            try:
                value = float(val)
            except:
                value = str(val)
        value = self.variablecontexttounicode(value)
        # self.lastoperand = Operand(val=value)
        lbl = Label(text=value)
        lbl.font_name = self.currentformat.getfont()
        self.lastlay.add_widget(lbl)
        if self.debug:
            name = 'not retrieved'
            if ctx.VARIABLE():
                name = ctx.VARIABLE().getText()
            print 'Entered: variable: ' + name

    def enterSuperset(self, ctx):
        super(Listener, self).enterSuperset(ctx)
        self.supersetstack.append(self.lastoperand)
        self.laystack.append(self.lastlay)
        if self.lastvlay:
            self.lastlay = self.lastvlay.children[1]
        else:
            vlay = BoxLayout()
            vlay.orientation = 'vertical'
            hlay = BoxLayout()
            hlay.orientation = 'horizontal'
            vlay.add_widget(hlay)
            hlay = BoxLayout()
            hlay.orientation = 'horizontal'
            vlay.add_widget(hlay)
            self.lastvlay = vlay
            self.lastlay.add_widget(vlay)
            self.lastlay = vlay.children[1]
        if not ctx.allinone():
            if ctx.VARIABLE():
                self.lastlay.add_widget(Label(text=str(ctx.VARIABLE().getText())))
            if ctx.NUMBER():
                self.lastlay.add_widget(Label(text=str(ctx.NUMBER().getText())))
        if self.debug:
            name = ''
            if ctx.VARIABLE():
                name += ctx.VARIABLE().getText() + ';'
            if ctx.NUMBER():
                name += ctx.NUMBER().getText()
            print 'Entered: superset: ' + name

    def enterSubwords(self, ctx):
        super(Listener, self).enterSubwords(ctx)
        if self.debug:
            print 'Entered: subwords'

    def enterSubset(self, ctx):
        super(Listener, self).enterSubset(ctx)
        self.subsetstack.append(self.lastoperand)
        self.laystack.append(self.lastlay)
        vlay = BoxLayout()
        vlay.orientation = 'vertical'
        hlay = BoxLayout()
        hlay.orientation = 'horizontal'
        vlay.add_widget(hlay)
        hlay = BoxLayout()
        hlay.orientation = 'horizontal'
        vlay.add_widget(hlay)
        self.lastvlay = vlay
        self.lastlay.add_widget(vlay)
        self.lastlay = vlay.children[0]
        self.currentformat.push()
        self.currentformat.clearemphasise()
        self.currentformat.cleartype()
        if ctx.VARIABLE() or ctx.NUMBER():
            if ctx.VARIABLE():
                value = self.variablecontexttounicode(ctx.VARIABLE().getText())
                lbl = Label(text=value)
                lbl.font_name = self.currentformat.getfont()
                self.lastlay.add_widget(lbl)
            if ctx.NUMBER():
                self.lastlay.add_widget(Label(text=str(ctx.NUMBER().getText())))
        if self.debug:
            name = ''
            if ctx.VARIABLE():
                name += ctx.VARIABLE().getText() + ';'
            if ctx.NUMBER():
                name += ctx.NUMBER().getText()
            print 'Entered: subset: ' + name

    def enterSigns(self, ctx):
        super(Listener, self).enterSigns(ctx)
        if self.debug:
            print 'Entered: signs'

    def enterRowdelimit(self, ctx):
        super(Listener, self).enterRowdelimit(ctx)
        if self.debug:
            print 'Entered: rowdelimit'

    def enterNumber(self, ctx):
        super(Listener, self).enterNumber(ctx)
        if self.debug:
            print 'Entered: number'

    def enterMuldiv(self, ctx):
        super(Listener, self).enterMuldiv(ctx)
        if self.debug:
            print 'Entered: muldiv'

    def enterMul(self, ctx):
        super(Listener, self).enterMul(ctx)
        if self.debug:
            print 'Entered: mul'

    def enterMainwords(self, ctx):
        super(Listener, self).enterMainwords(ctx)
        if self.debug:
            print 'Entered: mainwords'

    def enterMainexpr(self, ctx):
        super(Listener, self).enterMainexpr(ctx)
        if self.debug:
            print 'Entered: mainexpr'

    def enterMain(self, ctx):
        super(Listener, self).enterMain(ctx)
        if self.debug:
            print 'Entered: main'

    def enterKeywords(self, ctx):
        super(Listener, self).enterKeywords(ctx)
        self.currentformat.push()
        if ctx.KEYWORDS():
            type = ctx.KEYWORDS().getText()
            if type == 'mathbf':
                self.currentformat.setbold()
                self.lastenter = 'keywords'
            elif type == 'mathit':
                self.currentformat.setitalic()
                self.lastenter = 'keywords'
            elif type == 'boldsymbol':
                self.currentformat.setitalic()
                self.currentformat.setbold()
                self.lastenter = 'keywords'
            elif type == 'sum':
                self.currentformat.cleartype()
                self.currentformat.clearemphasise()
                self.lastenter = 'selfkeywords'
        if self.debug:
            name = ''
            if ctx.KEYWORDS().getText():
                name += ctx.KEYWORDS().getText()
            print 'Entered: keywords: ' + name

    def enterInit(self, ctx):
        super(Listener, self).enterInit(ctx)
        if self.debug:
            print 'Entered: init'

    def enterExpr(self, ctx):
        super(Listener, self).enterExpr(ctx)
        if self.debug:
            print 'Entered: expr'

    def enterDiv(self, ctx):
        super(Listener, self).enterDiv(ctx)
        if self.debug:
            print 'Entered: div'

    def enterColformat(self, ctx):
        super(Listener, self).enterColformat(ctx)
        if self.debug:
            print 'Entered: colformat'

    def enterBraceoc(self, ctx):
        super(Listener, self).enterBraceoc(ctx)
        if self.debug:
            print 'Entered: braceoc'

    def enterAllinone(self, ctx):
        super(Listener, self).enterAllinone(ctx)
        if not self.lastenter == 'keywords':
            self.currentformat.push()
        if self.debug:
            print 'Entered: allinone'

    def variablecontexttounicode(self, value):
        self.currentformat.setfontmath()
        if self.currentformat.isbolditalic():
            if value == 'A':
                return u'\U0000D468'
            if value == 'B':
                return u'\U0000D469'
            if value == 'C':
                return u'\U0000D46A'
            if value == 'D':
                return u'\U0000D46B'
            if value == 'E':
                return u'\U0000D46C'
            if value == 'F':
                return u'\U0000D46D'
            if value == 'G':
                return u'\U0000D46E'
            if value == 'H':
                return u'\U0000D46F'
            if value == 'I':
                return u'\U0000D470'
            if value == 'J':
                return u'\U0000D471'
            if value == 'K':
                return u'\U0000D472'
            if value == 'L':
                return u'\U0000D473'
            if value == 'M':
                return u'\U0000D474'
            if value == 'N':
                return u'\U0000D475'
            if value == 'O':
                return u'\U0000D476'
            if value == 'P':
                return u'\U0000D477'
            if value == 'Q':
                return u'\U0000D478'
            if value == 'R':
                return u'\U0000D479'
            if value == 'S':
                return u'\U0000D47A'
            if value == 'T':
                return u'\U0000D47B'
            if value == 'U':
                return u'\U0000D47C'
            if value == 'V':
                return u'\U0000D47D'
            if value == 'W':
                return u'\U0000D47E'
            if value == 'X':
                return u'\U0000D47F'
            if value == 'Y':
                return u'\U0000D480'
            if value == 'Z':
                return u'\U0000D481'
            if value == 'a':
                return u'\U0000D482'
            if value == 'b':
                return u'\U0000D483'
            if value == 'c':
                return u'\U0000D484'
            if value == 'd':
                return u'\U0000D485'
            if value == 'e':
                return u'\U0000D486'
            if value == 'f':
                return u'\U0000D487'
            if value == 'g':
                return u'\U0000D488'
            if value == 'h':
                return u'\U0000D489'
            if value == 'i':
                return u'\U0000D48A'
            if value == 'j':
                return u'\U0000D48B'
            if value == 'k':
                return u'\U0000D48C'
            if value == 'l':
                return u'\U0000D48D'
            if value == 'm':
                return u'\U0000D48E'
            if value == 'n':
                return u'\U0000D48F'
            if value == 'o':
                return u'\U0000D490'
            if value == 'p':
                return u'\U0000D491'
            if value == 'q':
                return u'\U0000D492'
            if value == 'r':
                return u'\U0000D493'
            if value == 's':
                return u'\U0000D494'
            if value == 't':
                return u'\U0000D495'
            if value == 'u':
                return u'\U0000D496'
            if value == 'v':
                return u'\U0000D497'
            if value == 'w':
                return u'\U0000D498'
            if value == 'x':
                return u'\U0000D499'
            if value == 'y':
                return u'\U0000D49A'
            if value == 'z':
                return u'\U0000D49B'
        if self.currentformat.isbold():
            if value == 'A':
                return u'\U0000D400'
            if value == 'B':
                return u'\U0000D401'
            if value == 'C':
                return u'\U0000D402'
            if value == 'D':
                return u'\U0000D403'
            if value == 'E':
                return u'\U0000D404'
            if value == 'F':
                return u'\U0000D405'
            if value == 'G':
                return u'\U0000D406'
            if value == 'H':
                return u'\U0000D407'
            if value == 'I':
                return u'\U0000D408'
            if value == 'J':
                return u'\U0000D409'
            if value == 'K':
                return u'\U0000D40A'
            if value == 'L':
                return u'\U0000D40B'
            if value == 'M':
                return u'\U0000D40C'
            if value == 'N':
                return u'\U0000D40D'
            if value == 'O':
                return u'\U0000D40E'
            if value == 'P':
                return u'\U0000D40F'
            if value == 'Q':
                return u'\U0000D410'
            if value == 'R':
                return u'\U0000D411'
            if value == 'S':
                return u'\U0000D412'
            if value == 'T':
                return u'\U0000D413'
            if value == 'U':
                return u'\U0000D414'
            if value == 'V':
                return u'\U0000D415'
            if value == 'W':
                return u'\U0000D416'
            if value == 'X':
                return u'\U0000D417'
            if value == 'Y':
                return u'\U0000D418'
            if value == 'Z':
                return u'\U0000D419'
            if value == 'a':
                return u'\U0000D41A'
            if value == 'b':
                return u'\U0000D41B'
            if value == 'c':
                return u'\U0000D41C'
            if value == 'd':
                return u'\U0000D41D'
            if value == 'e':
                return u'\U0000D41E'
            if value == 'f':
                return u'\U0000D41F'
            if value == 'g':
                return u'\U0000D420'
            if value == 'h':
                return u'\U0000D421'
            if value == 'i':
                return u'\U0000D422'
            if value == 'j':
                return u'\U0000D423'
            if value == 'k':
                return u'\U0000D424'
            if value == 'l':
                return u'\U0000D425'
            if value == 'm':
                return u'\U0000D426'
            if value == 'n':
                return u'\U0000D427'
            if value == 'o':
                return u'\U0000D428'
            if value == 'p':
                return u'\U0000D429'
            if value == 'q':
                return u'\U0000D42A'
            if value == 'r':
                return u'\U0000D42B'
            if value == 's':
                return u'\U0000D42C'
            if value == 't':
                return u'\U0000D42D'
            if value == 'u':
                return u'\U0000D42E'
            if value == 'v':
                return u'\U0000D42F'
            if value == 'w':
                return u'\U0000D430'
            if value == 'x':
                return u'\U0000D431'
            if value == 'y':
                return u'\U0000D432'
            if value == 'z':
                return u'\U0000D433'
        if value == 'A':
            return u'\U0000D434'
        if value == 'B':
            return u'\U0000D435'
        if value == 'C':
            return u'\U0000D436'
        if value == 'D':
            return u'\U0000D437'
        if value == 'E':
            return u'\U0000D438'
        if value == 'F':
            return u'\U0000D439'
        if value == 'G':
            return u'\U0000D43A'
        if value == 'H':
            return u'\U0000D43B'
        if value == 'I':
            return u'\U0000D43C'
        if value == 'J':
            return u'\U0000D43D'
        if value == 'K':
            return u'\U0000D43E'
        if value == 'L':
            return u'\U0000D43F'
        if value == 'M':
            return u'\U0000D440'
        if value == 'N':
            return u'\U0000D441'
        if value == 'O':
            return u'\U0000D442'
        if value == 'P':
            return u'\U0000D443'
        if value == 'Q':
            return u'\U0000D444'
        if value == 'R':
            return u'\U0000D445'
        if value == 'S':
            return u'\U0000D446'
        if value == 'T':
            return u'\U0000D447'
        if value == 'U':
            return u'\U0000D448'
        if value == 'V':
            return u'\U0000D449'
        if value == 'W':
            return u'\U0000D44A'
        if value == 'X':
            return u'\U0000D44B'
        if value == 'Y':
            return u'\U0000D44C'
        if value == 'Z':
            return u'\U0000D44D'
        if value == 'a':
            return u'\U0000D44E'
        if value == 'b':
            return u'\U0000D44F'
        if value == 'c':
            return u'\U0000D450'
        if value == 'd':
            return u'\U0000D451'
        if value == 'e':
            return u'\U0000D452'
        if value == 'f':
            return u'\U0000D453'
        if value == 'g':
            return u'\U0000D454'
        if value == 'h':
            return u'\U0000210E' # warning this is actually planck constant
        if value == 'i':
            return u'\U0000D456'
        if value == 'j':
            return u'\U0000D457'
        if value == 'k':
            return u'\U0000D458'
        if value == 'l':
            return u'\U0000D459'
        if value == 'm':
            return u'\U0000D45A'
        if value == 'n':
            return u'\U0000D45B'
        if value == 'o':
            return u'\U0000D45C'
        if value == 'p':
            return u'\U0000D45D'
        if value == 'q':
            return u'\U0000D45E'
        if value == 'r':
            return u'\U0000D45F'
        if value == 's':
            return u'\U0000D460'
        if value == 't':
            return u'\U0000D461'
        if value == 'u':
            return u'\U0000D462'
        if value == 'v':
            return u'\U0000D463'
        if value == 'w':
            return u'\U0000D464'
        if value == 'x':
            return u'\U0000D465'
        if value == 'y':
            return u'\U0000D466'
        if value == 'z':
            return u'\U0000D467'

    def getlayout(self):
        if self.lastlay:
            return self.lastlay
        else:
            return Label(text='Nothing to show.')


class OFTexMathApp(KivyApp):
    def build(self):
        input = FileStream(self.input_file)
        lexer = oftexmathLexer(input)
        stream = CommonTokenStream(lexer)
        parser = oftexmathParser(stream)
        tree = parser.init()
        printer = Listener(dbg=True, parser=parser)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        return printer.getlayout()


if __name__ == '__main__':
    file = ""
    try:
        file = sys.argv[1]
    except:
        file = 'test.tex'
    app = OFTexMathApp()
    app.input_file = file
    sys.exit(app.run())

