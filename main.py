#imports example ronot
from example import ExampleBot
from myrobo import Myrobo
from bertieRobot import BertieRobot

if __name__ == "__main__":

    #Testing Fred
    fred = ExampleBot('Fred')
    fred.speak()
    fred.on()
    fred.speak()
    fred.calculateSquare(4)
    fred.off()
    fred.speak()
    fred.on()
    fred.calculateSquare(3452324)

    bertie = BertieRobot('Bertie')
    bertie.speak()
    bertie.on()
    bertie.speak()
    bob = Myrobo("myrob")
    bob.baller(" schlorp")
