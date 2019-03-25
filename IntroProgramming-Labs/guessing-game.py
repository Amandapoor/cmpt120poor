#guessing-game.py
#This program allows the user to guess a predetermined animal 
#Amanda Poor



def main():
    print("This program is thinking of an animal")
   
  
    animal = "elephant"

    while True:
        guess = input("Please guess the animal (enter in lowercase) : ")

        if animal == guess:
            print("Congrats")
            break

        else:
            print("Please guess again")

        
        
    
   
main()
    
