import random
class Dice(object):
   
    def __init__(self):
        pass
     
    def roll(self):
        roll=random.randrange(0, 6)
        return roll+1