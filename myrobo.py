from robot import Robot
from components.speaker import Speaker
name = "bvdfbdbnngn"

class Myrobo(Robot):
    def __init__(self, name):
        '''Initializes Robot'''
        
        #initializing parent class
        Robot.__init__(self, name)

        #initializing speaker
        self.speaker = Speaker(name)
    
    def speak(self):
        '''Speaks'''
        if self.poweredOn:
            print("im am on holy gaucamole")
        else:
            print("ARGG! Mee voice box is not functioning HELP!!!!!!!!!!!!!")
    def baller(self, bingo):
        b = bingo
        print(self.name + " " + bingo)
