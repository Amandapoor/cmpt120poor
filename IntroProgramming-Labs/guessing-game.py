#guessing-game.py
#This program allows the user to guess a predetermined animal 
#Amanda Poor



def main():
    print("This program is thinking of an animal")
   
  
    animal = "elephant"

    while True:
        guess = input("Please guess the animal: ").lower()
      
    
        
        if animal == guess:
            print("Congrats, you guessed right.")
            opinion = input("Do you like this animal (enter y or n): ").lower()
            
            if opinion == 'y':
                print("Oh cool! I like them too!")

            else:
                print("Aww, why not...they're cute.")

            break

        elif guess == 'q':
            exit()   

        else:
            print("Please guess again")
        


   
   
main()
    
