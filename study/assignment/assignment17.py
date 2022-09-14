import random

class Dice:
        def roll(self):
            p=random.randint(1,6)
            q=random.randint(1,6)
            return q,p


dice=Dice()
print(dice.roll())