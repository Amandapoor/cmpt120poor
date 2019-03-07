



                
def getEquation():
    return input("Enter an equation(use spaces in between): ").split()
    
<<<<<<< HEAD
def calculate(equation):
          
    i = 0                
    while len(equation) > 1 and hasProductDivision(equation):
        if equation [i] == '*' or equation [i] == '/':
            equation = process(equation, i)
            i = 0
        else:
            i = i + 1
                     
    while len(equation) > 1 and hasAdditionSubtract(equation):
        if equation[i] == '+' or equation [i] == '-':
            equation = process (equation, i)
            i = 0
        else:
            i = i + 1
    return float(equation [0])
=======
def getPassword(uname):
    password = input("Create a new password: ")
    getPasswordstrength(password, uname) # This should be in a while loop
    
>>>>>>> 689f56e53cc8f795c3d6822ac765978208562d39


def hasProductDivision(equation):
    
    
   
    if '*' in equation:
        return True

    if '/' in equation:
        return True
    else:
        return False
    

def hasAdditionSubtract(equation):
    if '+' in equation:
        return True
    
    if '-' in equation:
        return True
    else:
        return False
    
               
                     
def process(equation, i):
    if i == '*':
        return equation [i-1] * equation[i+1]
    elif i == '/':  
        return equation [i-1] / equation[i+1]
    elif i == '+':
        return equation [i-1] + equation[i+1]
    elif i == '-':
        return equation [i-1] - equation[i+1]

def result():
    print("The result of your equation is", result) 
    


    
def main():
    equation = getEquation()
    result = calculate(equation)
    print ("The result of the equation is", result)
   

main()
            
