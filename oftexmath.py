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
            tokens = self.parser.getTokenStream()
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
        super(Listener, self).exitSubset(ctx)
        if self.debug:
            tokens = self.parser.getTokenStream()
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
        if self.debug:
            print 'Exited: keywords'

    def exitInit(self, ctx):
        super(Listener, self).exitInit(ctx)
        if self.debug:
            print 'Exited: init'

    def exitExpr(self, ctx):
        super(Listener, self).exitExpr(ctx)
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
        self.lastoperand = Operand(val=value)
        self.lastlay.add_widget(Label(text=str(value)))
        if self.debug:
            tokens = self.parser.getTokenStream()
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
            tokens = self.parser.getTokenStream()
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
        if not ctx.allinone():
            if ctx.VARIABLE():
                self.lastlay.add_widget(Label(text=str(ctx.VARIABLE().getText())))
            if ctx.NUMBER():
                self.lastlay.add_widget(Label(text=str(ctx.NUMBER().getText())))
        if self.debug:
            tokens = self.parser.getTokenStream()
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
        if self.debug:
            print 'Entered: keywords'

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
        if self.debug:
            print 'Entered: allinone'

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

