

from graphics import *

from calc_functions import *


def createCanvas():
    win = GraphWin("Calculator",600, 620)
    win.setBackground("grey")
    return win

displayEquation=[]
displayString=""

def getCoords(i):
    coords = [[75,120],[165,120],[255,120],[345,120],[75,220],[165,220],
              [255,220],[345,220],[75,320],[165,320],[255,320],[345,320],
              [75,420],[165,420],[255,420],[345,420],[255,520],[345,520],
              [75,520],[435,120],[435,220],[435,320],[435,420]]
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
    size = [80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80]

    for i in range(23):
        x, y = getCoords(i)
        
        button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
        button.setFill(color[i])
        label = Text(Point(x+size[i]/2,y+size[i]/2),getLabel(i))
        label.setSize(22)
        button.draw(win)
        label.draw(win)


        
def createDisplay(win):

    rectangle = Rectangle(Point(75,20), Point(515,100)).draw(win)
    color2 = "white"
    rectangle.setFill(color2)
    text = Text(Point(400,60)," ")
    text.setSize(22)
    text.draw(win)

    return text
    
def getInput(mouse,display):
    for i in range(23):
        x,y = getCoords(i)
        if x<mouse.x < x+80 and y< mouse.y < y+80:
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
