from robot import Robot
from components.speaker import Speaker


class ThomasBotMK69(Robot):

    def __init__(self, name):
        '''Initializes robot'''

        #Initializing parent class
        Robot.__init__(self, name)
        #Initializing speaker
        self.speaker = Speaker(name)
    
    def speak(self):
        '''Prints a message using the speaker if powered on'''
        if self.poweredOn:
            self.speaker.speak('IM IN PAIN!!!!!')
    
    def calculateSquare(self, n):
        '''Calculates and prints the square of n if powered on. If n > 1000, overloads and shuts down.'''
        if self.poweredOn:
            if n > 1000:
                self.speaker.speak('fregg sucks! and you do too!')
                self.off()
            else:
                self.speaker.speak(str(n ** 2))

