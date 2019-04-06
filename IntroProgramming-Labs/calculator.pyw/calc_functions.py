#calc_functions.py
#Amanda Poor
#Intro Programming

def getEquation(equation):
    i = 0                
    while len(equation) > i and hasProductDivision(equation):
        if equation[i] == '*' or equation[i] == '/':
            equation = process(equation, i)
        i=i+1
        
    i = 0
    while len(equation) > i and hasAdditionSubtract(equation):
        if equation[i] == '+' or equation[i] == '-':
            equation = process (equation, i)
        i=i+1

    return float(equation [0])

def hasProductDivision(equation):
    if '*' in equation:
        return True
    elif '/' in equation:
        return True
    else:
        return False
    

def hasAdditionSubtract(equation):
    if '+' in equation:
        return True
    elif '-' in equation:
        return True
    else:
        return False
    
def multiply(x,y):
    return float(x) * float(y)

def divide(x,y):
    return float(x) / float(y)

def add(x,y):
    return float(x) + float(y)

def subtract(x,y):
    return float(x) - float(y)

    
def process(equation, i):
    if equation[i] == '*':
        result = multiply(equation [i-1], equation [i+1])
    elif equation[i] == '/':  
        result = divide(equation [i-1], equation [i+1])
    elif equation[i] == '+':
        result = add(equation [i-1], equation [i+1])
    elif equation[i] == '-':
        result = subtract(equation [i-1], equation [i+1])
    for j in range(3):
        del equation [i-1]
    equation.insert(i-1, str(result))
    print(equation)
    return equation
   
#def main():
    #equation = input("Enter an equation (use spaces in between): ").split()
    #result = getEquation(equation)
    #print ("The result of the equation is", result)
   


            
