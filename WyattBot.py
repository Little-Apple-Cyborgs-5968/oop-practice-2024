from robot import Robot
from components.speaker import Speaker

class WyattBot(Robot):
    def __init__(self, name):
        Robot.__init__(self, name)
        self.speaker = Speaker(name)

    def speak(self):
        if self.poweredOn:
            print("Beep Boop!!")

    def Count(self):
        if self.poweredOn:
            number = int(input("<Wyatt>: How high do you want to count?: "))
            for x in range(number):
                self.speaker.speak(x+1)

    def exponential(self):
        if self.poweredOn:
            number = int(input("<Wyatt>: How high do you want to exponentially count?: "))
            for x in range(number):
                self.speaker.speak((2**(x+1)))

