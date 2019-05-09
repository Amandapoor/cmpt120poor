


from graphics import *

from calc_functions import *


def main():
    calc = Calculator()
    calc.__init__
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

    def createCanvas(self):
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
            result = self.engine.addbuttonsPressed(Key)
            if result == 'quit':
                break
            print(Key)
            self.display.setText(result)

class CalculatorEngine:
    def __init__(self):
        self.memory = Memory()
        self.equation = ""
     

    def addbuttonsPressed(self, Key):
        print(self.equation)
        if Key == "Clr":
            self.equation = ""
        elif Key == "Del":
            temp = self.equation.split()
            temp[-1] = ""
            self.equation = ""
            for i in temp:
                if i in ['+','-','*','/']:
                    self.equation += " " + i + " "
                else:
                    self.equation += i
        elif Key == "=":
            print(self.equation)
            if len(self.equation)>0:
                try:
                    
                    result=getEquation(self.equation.split())
                    self.equation = str(result)
                except:
                    self.equation = self.equation
        elif self.equation == "":
            if Key == 'MR':
                self.equation += (str(memory))
            elif Key not in ['+','-','*','/', '+/-']:
                self.equation += (Key)
        elif Key in ['+','-','*','/']:
                self.equation += (" " + Key + " ")
        elif Key == '+/-':
            temp = self.equation.split()
            temp[-1] = str(-1 * float((temp)[-1]))
            self.equation = ""
            for i in temp:
                if i in ['+','-','*','/']:
                    self.equation += " " + i + " "
                else:
                    self.equation += i
        elif Key == 'MR':
            if (self.equation.split())[-1] in [' + ',' - ',' * ',' / ']:
                self.equation +=(str(memory))
        else:
            self.equation +=  Key
            #self.equation[-1] = self.equation[-1] + Key
        return str(self.equation)
    
class Keypad:
    def __init__(self, win):
        self.win = win
        #self.keypad.graphics = self.createGraphics()
        self.buttons = self.createButtons()
    def createButtons(self):
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
            button = Button(size[i], labels[i], color[i])
            button.setPosition(coords[i][0], coords[i][1])
            button.draw(self.win)
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
    def __init__(self, size, label, color):
        self.size = size
        self.labelText = label
        self.position = Point(0,0)
        self.color = color
        p = self.position
        self.rectangle = Rectangle(p, Point(p.getX()+size, p.getY()+size))
        self.label = Text(Point(p.getX()+size/2, p.getY()+size/2),label)
        self.rectangle.setFill(self.color)

    def getLabel(self):
        return self.labelText
    
    def isClicked(self, point):
        if self.position.getX() <= point.getX() <= self.position.getX()+self.size and self.position.getY() <= point.getY() <= self.position.getY()+self.size:
            return True
        return False
    
    def setPosition(self,x,y):
        dx = x-self.position.getX()
        dy = y-self.position.getY()
        self.position.move(dx,dy)
        self.rectangle.move(dx,dy)
        self.label.move(dx,dy)
        
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
