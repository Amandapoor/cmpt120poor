# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Amanda Poor
# Created: 2019-02-25


#The list containing the first and last names was accidentally submitted into
#the first time I committed via git
def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]
#The function below was submitted the first time I committed via git    
def getUname(name):
    return name[0]+ "." + name[1]

    
#I accidentally had the getPassword function return the password if it passed
#the strength test for 8 characters the first time I committed via git. 
def getPassword(uname):
    print("Your username is:", uname)
    password = input("Create a new password: ")
    while len(password) < 8:
        print("Fool of a Took! That password is feeble!")
        print("Make sure your password is at least 8 letters")
        password = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Your password is: ", password)
    print("Account configured. Your new email address is", uname + "@marist.edu")

def main():
    name = getName()
    uname = getUname(name)
    password = getPassword(uname)


    

    
    
main()
