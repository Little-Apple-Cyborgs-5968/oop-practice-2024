# the robot and speaker files
from robot import Robot
from components.speaker import Speaker
#Declares a new class that extends the robot class
class ExampleBot(Robot):

    def __init__(self, name):
        '''Initializes robot'''

        #Initializing parent class
        Robot.__init__(self, name)
        #Initializing speaker
        self.speaker = Speaker(name)
    
    def speak(self):
        '''Prints a message using the speaker if powered on'''
        if self.poweredOn:
            self.speaker.speak('Beep Boop!')
    
    def calculateSquare(self, n):
        '''Calculates and prints the square of n if powered on. If n > 1000, overloads and shuts down.'''
        if self.poweredOn:
            if n > 1000:
                self.speaker.speak('Overloaded!')
                self.off()
            else:
                self.speaker.speak(str(n ** 2))
