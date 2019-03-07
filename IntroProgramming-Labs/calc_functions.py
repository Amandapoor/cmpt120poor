#calc_functions.py
#Amanda Poor
#Intro Programming

def getEquation(equation):

    return equation

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

   
def main():
    equation = input("Enter an equation (use spaces in between): ").split()
    result = getEquation(equation)
    print ("The result of the equation is", result)
   

main()
            
