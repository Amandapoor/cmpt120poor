

from graphics import *

from calc_functions import *


def createCanvas():
    win = GraphWin("Calculator",350, 450)
    win.setBackground("grey")
    return win

displayEquation=[]
displayString=""

def getCoords(i):
    coords = [[30,110],[90,110],[150,110],[210,110],[30,180],[90,180],
              [150,180],[210,180],[30,250],[90,250],[150,250],[210,250],
              [30,310],[90,310],[150,310],[210,310],[150,380],[210,380],
              [30,380],[270,110],[270,180],[270,250],[270,310]]
    return coords[i][0], coords[i][1]

def getLabel(i):
    labels = ['7','8','9','/','4','5','6','*','1','2','3'
              ,'+','+/-','0','.','-','Del','=','Clr','M+','M-','MR','MC']
    return labels[i]

def createButtons(win):
    color = ['pink','pink','pink','lightblue','pink','pink','pink','lightblue','pink',
             'pink','pink','lightblue','lightblue','pink','lightblue'
             ,'lightblue','lightblue','lightblue', 'yellow','lightgreen','lightgreen',
             'lightgreen','lightgreen']
    size = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]

    for i in range(23):
        x, y = getCoords(i)
        
        button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
        button.setFill(color[i])
        label = Text(Point(x+size[i]/2,y+size[i]/2),getLabel(i))
        label.setSize(18)
        button.draw(win)
        label.draw(win)


        
def createDisplay(win):

    rectangle = Rectangle(Point(30,30), Point(310,80)).draw(win)
    color2 = "white"
    rectangle.setFill(color2)
    text = Text(Point(250,50)," ")
    text.setSize(18)
    text.draw(win)

    return text
    
def getInput(mouse,display):
    for i in range(23):
        x,y = getCoords(i)
        if x<mouse.x < x+50 and y< mouse.y < y+50:
            print(getLabel(i))
            return getLabel(i)
            break

def addEquation(equation,label,memory):

    if len(equation) == 0:
        if label == 'MR':
            equation.append(str(memory))
        elif label not in ['+','-','*','/', '+/-']:
            equation.append(label)
    elif label in ['+','-','*','/']:
        equation.append(" " + label + " ")
    elif label == '+/-':
        equation[-1] = str(-1 * float(equation[-1]))
    elif label == 'MR':
        if equation[-1] in [' + ',' - ',' * ',' / ']:
            equation.append(str(memory))
    else:
        equation[-1] = equation[-1] + label
    return equation


def equationString(equation):
    equationString=""
    for i in range(len(equation)):
        equationString+=equation[i]
        equationString+=" "
    return equationString

    
def main():
    memory = 0
    result = 0
    win = createCanvas()
    display = createDisplay(win)
    equation = []
    coords = createButtons(win)
    while True:
        mouse = win.getMouse()
        label = getInput(mouse, display)
        if label == "=":
            print(equation)
            if len(equation)>0:
                try:
                    result=getEquation(equationString(equation).split())
                    display.setText(str(result))
                except:
                    continue
        elif label == "M+":
            print(equation)
            if len(equation)>0:
                try:
                    result=getEquation(equationString(equation).split())
                    memory = memory + result
                    display.setText(str(memory))
                except:
                    continue
        elif label == "M-":
            print(equation)
            if len(equation)>0:
                try:
                    result=getEquation(equationString(equation).split())
                    memory = memory - result
                    display.setText(str(memory))
                except:
                    continue

        elif label == "MC":
            print(equation)
            memory = 0
        
        elif label == "Del":
            if len(equation)==0:
                continue
            else:
                del equation[len(equation)-1]
            print(equation)
            display.setText(equationString(equation))
        elif label == "Clr":
            equation=[]
            display.setText(equationString(equation))
        elif label == None:
            continue
        else:
            equation = addEquation(equation, label,memory)
            display.setText(equationString(equation))


main()
