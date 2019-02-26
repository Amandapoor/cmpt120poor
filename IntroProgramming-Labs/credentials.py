# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Amanda Poor
# Created: 2019-02-25

def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]

def getUname(name):
    return name[0]+ "." + name[1]

def getPasswordstrength(password, uname):
    if len(password) < 8:
        print("Fool of a Took! That password is feeble!")
        print("Make sure your password is at least 8 letters")
        password = input("Create a new password: ")
    if password.lower() == password:
        print("Fool of a Took! That password is feeble!")
        print("Make at least one character, but not all, upper case: ")
        password = input("Create a new password: ")
    if password.upper() == password:
        print("Fool of a Took! That password is feeble!")
        print("Make at least one character, but not all, lower case: ")
        password = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Your username is ", uname)
    print("Your password is: ", password)
    print("Account configured. Your new email address is", uname + "@marist.edu")
   

    
def getPassword(uname):
    password = input("Create a new password: ")
    getPasswordstrength(password, uname)
    

def main():
    name = getName()
    uname = getUname(name)
    password = getPassword(uname)


    

    
    
main()
