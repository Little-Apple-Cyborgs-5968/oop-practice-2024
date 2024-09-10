class Robot:
    '''Represents a generic robot'''
    def __init__(self, name):
        '''Initializes Robot in the off state'''
        self.name = name
        self.poweredOn = False
    
    def speak(self):
        '''Speaks- This method needs to be implemented by subclasses'''
        pass

    def on(self):
        '''Powers on the robot'''
        self.poweredOn = True
    
    def off(self):
        '''Powers off the robot'''
        self.poweredOn = False
    