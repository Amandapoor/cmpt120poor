# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Amanda Poor
# Created: YYYY-MM-DD


    
def getName():
    #get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]

def getUname(name):
    return name[0]+ "." + name[1]
    
def getPassword(uname):
    password = input("Create a new password: ")
    while len(password) < 8:
        print("Make sure your password is at lest 8 letters")
        password = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured. Your new email address is", uname + "@marist.edu")

def main():

    name = getName()
    uname = getUname(name)
    password = getPassword(uname)


    
    
main()
