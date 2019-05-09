


from graphics import *

from calc_functions import *


def main():
    calc = Calculator()
    cal.__init__
    calc.run()
    
    
class Calculator:
    
    def __init__(self):
        self.win = self.createCanvas()
        self.display = Display(self.win)
        self.Keypad = Keypad(self.win)
        self.engine = CalculatorEngine()
        #self.canvas = self.createGraphics()
        #self.display = Display()
        #self.display.draw(self.canvas)
        #self.keypad= Keypad()
        #self.keypad.draw(self.canvas)
        #self.engine = CalculatorEngine()

    def createCanvas(self)
        win = GraphWin('calculator', 350, 450)
        win.setBackground('grey')
        return win

    def createGraphics(self):
		#same as previous projects return canvas
        rectangle = Rectangle(Point(30,30), Point(310,80)).draw(win)
        color2 = "white"
        rectangle.setFill(color2)
        text = Text(Point(250,50)," ")
        text.setSize(18)
        text.draw(win)

    def run(self):
        while True:
            Key = self.Keypad.getKeyPressed()
            result = self.engine.addbuttonsPressed(key)
            if result == 'quit':
                break
            print(Key)
            self.display.setText(result)

class CalculatorEngine:
    def __init__(self):
        self.memory = Memory()
	self.equation = " "

    def insertAnswer(Key, equation, last):
        if Key == 'Del':
            return self.equation[:len(self.equation)-1]
        else:
            if isOperator(Key) and isNumber(last) or isNumber(Key) and isOperator
                return self.equation + " " + Key
            else:
                return self.equation + Key

    def addbuttonsPressed(self, Key):
        if Key == "=":
            result = getEquation(self.equation.split())
            return
        elif Key == "+/-":
            print(self.equation.split())
            result = -result
            display.setText(str(result))
            equation = str(result)
            print (result)
        elif Key in ['M+', 'M-', 'MR', 'MC']:
            self.memory.getEquation(self.equation.split())
            return self.equation
        elif Key == "CLR"
            equation = ' '
            display.setText(equation)
            return
        else:
            equation = insertAnswer(Key, equation, last)
            last = Key
            return
    

class Keypad:
    def __init__(self, win):
        self.win = win
        #self.keypad.graphics = self.createGraphics()
        self.buttons = self.createButtons()
    def createButtons(self, win):
        coords = [[30,110],[90,110],[150,110],[210,110],[30,180],[90,180],
                  [150,180],[210,180],[30,250],[90,250],[150,250],[210,250],
                  [30,310],[90,310],[150,310],[210,310],[150,380],[210,380],
                  [30,380],[270,110],[270,180],[270,250],[270,310]]
                      
        labels = ['7','8','9','/','4','5','6','*','1','2','3'
                  ,'+','+/-','0','.','-','Del','=','Clr','M+','M-','MR','MC']
                      
        color = ['pink','pink','pink','lightblue','pink','pink','pink','lightblue','pink',
                 'pink','pink','lightblue','lightblue','pink','lightblue'
                 ,'lightblue','lightblue','lightblue', 'yellow','lightgreen','lightgreen',
                 'lightgreen','lightgreen']

        size = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,
                50,50,50,50,50,50,50,50,50]
        buttons = []

        for i in range(len(labels)):
            button = Buttons(size[i], labels[i])
            button.setPosition(coords[i][0], coords[i][1])
            button.setColor(color[i])
            button.draw(win)
            buttons.append(button)
        return buttons
    
                      
        #for i in len(coords):
            #button = Button(coords, label)
            #button.append(button)
        #return buttons

    def getKeyPressed(self):
        p = self.win.getMouse()
        return self.checkKey(p)
    def checkKey(self, p):
        for b in self.buttons:
            if b.isClicked(p):
                return b.getLabel()


class Button:
    def __init__(self, size, label):
        self.size = size
        self.labelText = label
        self.position = Point(0,0)
        #self.
        p = self.position
        self.rectangle = Rectangle(p, Point(p.getX()+size[0], p.getY()+size[1]))
        self.label = Text(Point(p.getX()+size/2, p.getY()+size/2),label)
        self.rectangle.setFill(self.color)
    def getLabel(self):
        return self.labelText
    def isClicked(self, point):
        if self.position.getX()<=point.getX()<=self.position.getX()+self.size)
            return True
        return False
    def setPosition(self,x,y):
        dx = x-self.position.getX()
        dy = y-self.position.getY()
        self.position.move(dx,dy)
        self.rectangle.move(dx,dy)
        self.label.move(dx,dy)
    def setColor(self,color):
        self.color = color
        self.rectangle.setFill(color)
    def draw(self,win):
        self.rectangle.draw(win)
        self.label.draw(win)

        
class Display:
    def __init__(self,win):
        self.win = win
        rectangle = Rectangle(Point(30,30),Point(310,80)).draw(win)
        color = 'white'
        rectangle.setFill(color)
        self.rectangle = rectangle
        #size=
        self.label = Text(Point(250,50), ' ')
        self.label.draw(win)
        return
    def setText(self,text):
        self.label.setText(text)

class Memory:  	
    def __init__(self):
        self.value = 0
    def getValue(self):
        return self.value 		
    def add(self, value):			
        self.value += value
    def subtract(self, value):
        self.value -= value
    def clear(self, value):
        self.value = 0

main()
