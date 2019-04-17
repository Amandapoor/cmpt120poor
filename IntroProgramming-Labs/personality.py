#Amanda Poor


#anger,disgust,fear,happiness,sadness,surprise
#reward(happiness,happy,fear,surprise,happiness,happiness)
#punish(anger,disgust,fear, sadness, sadness, sadness)
#threaten(anger, anger, fear, sadness, sadness, sadness)
#joke(anger,disgust,happiness, happiness,happiness,happines)


emotion = []
emotion == ["anger", "disgust","fear","happiness","sadness","surprise"] 
currEmotion = emotion[3]
action == ["reward","punish","threaten", "joke"]
#emotion = [0,


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
    while True:
        action = getInteraction()
        if action == 9:
            break
        currEmotion = lookupEmotion(currEmotion, action)
        showEmotion(currEmotion)
                     
def showEmotion(emotion):
    i = action
    j = currEmotion
    
    response = ["I'm so mad right now! Go away!", "You're annoying me! Please stop.",
                 "You're scaring me!","I'm so happy right now :)",
                 "I just want to cry and be alone","Wow! My day can't get any better!"]
    
    if emotionMatrix[i][j] == 0:
        print (response[0])
    elif emotionMatrix[i][j] == 1:
        print (response[1])
    elif emotionMatrix[i][j] == 2:
        print (response[2])
    elif emotionMatrix[i][j] == 3:
        print (response[3])
    elif emotionMatrix[i][j] == 4:
        print (response[4])
    elif emotionMatrix[i][j] == 5:
        print (response[5])
                     
                     

def introduction():
    print("In this program, you can reward, punish, joke, or threaten Al")
    
def main():
    introduction()
    getInteraction()
    lookupEmotion(currEmotion, action)
    primaryLoop()
    showEmotion(emotion)

        
main()        
                       

    

