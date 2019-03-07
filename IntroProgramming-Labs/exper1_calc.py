# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 

  
  
# Take input from the user
number_1 = int(input("Enter first number: "))

print("""Please select operation
        1. Add
        2. Subtract
        3. Multiply 
        4. Divide""")

select = input("Select operations form 1, 2, 3, 4 :")

   
number_2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(number_1, "+", number_2, "=", add(number_1, number_2)) 
  
elif select == '2': 
    print(number_1, "-", number_2, "=", subtract(number_1, number_2)) 
  
elif select == '3': 
    print(number_1, "*", number_2, "=", multiply(number_1, number_2)) 
  
elif select == '4': 
    print(number_1, "/", number_2, "=", divide(number_1, number_2)) 
else: 
    print("Invalid input") 
