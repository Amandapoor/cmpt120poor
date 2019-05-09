


from graphics import *

from calc_functions import *


def main():
    calc = Calculator()
    cal.__init__
    calc.run()
    
    

class Calculator:
    
    def __init__(self):
        self.canvas = self.createGraphics()
	
        self.display = Display()
	
        self.display.draw(self.canvas)
        self.keypad= Keypad()
        self.keypad.draw(self.canvas)
        self.engine = CalculatorEngine()

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
            key = self.keypad.getKeyPressed()
            result = self.engine.addKeyPressed(key)
            if result == 'quit':
                break
            self.display.setText(result)

class CalculatorEngine:
    def __init__(self):
        self.memory = Memory()
	#self.equation = " "
	
    def addKeyPressed(self,Key):
        if Key in ['M+', 'M-', 'MR', 'MC']:
            self.memory.process(key,self.equation)
            return self.equation
        elif Key == '=':
            return self.solve()

class Keypad:
    def __init__(self):
        self.keypad.graphics = self.createGraphics()
	
	#self.win =
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
                      
        for i in len(coords):
            button = Button(coords, label)
            button.append(button)
        return buttons

    def getKeyPressed(self):
        p = self.win.getMouse()
        return self.checkKey(p)
    def checkKey(self, p):
        for b in self.buttons:
            if b.isPressed(p):
                return b.getLabel()
                      

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
