#guessing-game.py
#This program allows the user to guess a predetermined animal 
#Amanda Poor



def main():
    print("This program is thinking of an animal")
   
  
    animal = "elephant"

    while True:
        guess = input("Please guess the animal (enter in lowercase) : ").lower()
      

        
        if animal == guess:
            print("Congrats")
            break
        
        elif guess == "quit":
           
            exit()

        else: 
            print("Please guess again")

       
            
       
                
   
   
main()
    
