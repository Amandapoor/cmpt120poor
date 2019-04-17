#Amanda Poor


#anger,disgust,fear,happiness,sadness,surprise
#reward(happiness,happy,fear,surprise,happiness,happiness)
#punish(anger,disgust,fear, sadness, sadness, sadness)
#threaten(anger, anger, fear, sadness, sadness, sadness)
#joke(anger,disgust,happiness, happiness,happiness,happines)



emotion = ["anger", "disgust","fear","happiness","sadness","surprise"] 

action = ["reward","punish","threaten", "joke"]



def getInteraction():
    action = int(input("Specify an action (0-reward, 1-punish, 2-threaten, 3-joke, 9-quit): "))
    return action
   

def lookupEmotion(currEmotion, action):
    
    
    emotionMatrix = [[4,4,2,5,3,3],
                     [0,1,2,4,4,4],
                     [0,0,2,4,4,4],
                     [0,1,3,3,3,3]]
  
    return emotionMatrix[action][currEmotion]
                
    
def primaryLoop():
    currEmotion = 3
    while True:
        action = getInteraction()
        if action == 9:
            print("Goodbye")
            break
        currEmotion = lookupEmotion(currEmotion, action)
        showEmotion(currEmotion)
        
def showEmotion(currEmotion):

    
    response = ["I'm so mad right now! Go away!", "You're annoying me! Please stop.",
                 "You're scaring me!","I'm so happy right now :)",
                 "I just want to cry and be alone","Wow! My day can't get any better!"]
    print(response[currEmotion])
    
   
                     
                     

                     

def introduction():
    print("In this program, you can reward, punish, joke, or threaten Al")
    
def main():
    introduction()
    
    primaryLoop()
    

        
main()        
                       

    

