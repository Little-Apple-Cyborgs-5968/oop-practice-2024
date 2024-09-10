from Bombasticbot import Bombasticbot
from example import ExampleBot
from myrobo import Myrobo

if __name__ == "__main__":

    bot = Bombasticbot('bot')
    bot.speak()
    bot.on()
    bot.speak()
    bot.calculateSquare(4)
    bot.off()
    bot.speak()
    bot.on()
    bot.calculateSquare(3452324)
    
    
    bob = Myrobo("myrob")
    bob.baller(" schlorp")