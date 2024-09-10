from robot import Robot
from components.speaker import Speaker
import random

class BertieRobot(Robot):

    def __init__(self, name):
        '''Initializes robot'''

        #Initializing parent class
        Robot.__init__(self, name)
        #Initializing speaker
        self.speaker = Speaker(name)
        self.poweredOn = False
    
    def speak(self):
        num = random.random()
        if self.poweredOn:
            if (num < 0.3):
                self.speaker.speak("hi my name is bertie")
            elif (num < 0.6):
                self.speaker.speak("hi my name is bertie, the destroyer of worlds!!!!!!")
            else:
                self.speaker.speak("hi my name is bertie, i'm a very kind a pleasant robot")
            self.speaker.speak("hello dear mortal, you have been summoned by robot sumpremes to be smuthered in cute dancing pillow bears. good bye dear mortal!!!!!")
                
        else:
            print("i'm not alive!!!!!!!!help me!!!!!!!!!")