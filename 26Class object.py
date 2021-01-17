#objects are instances of clases
import random
class pound:


    def __init__(self,rare=False):

        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            
        
        self.color="gold"
        self.edge=1
        self.diameter=22.5
        self.thickness=3.15
        self.heads=True
    def rust(self):
        self.color = 'greenish'

    def clean(self):
        self.color = 'goldy'

    def flip(self):
        options = [True,False]
        choice = random.choice(options)
        self.heads = choice
    def __del__(self):
        print('coin spent')

coin1=pound()
print(coin1.value)
print(type(coin1))
coin1.color="greenish"
print(coin1.color)

coin2 = pound()
print(coin2.color)

coin1.value = 1.25
print(coin1.value)
coin3 = pound(rare=True)
print(coin3.value)

coin4 = pound()
print(coin4.color)

coin4.rust()
print(coin4.color)

coin4.clean()
print(coin4.color)

coin5 = pound()
print(coin5.heads)
coin5.flip()
print(coin5.heads)

coin6 = pound()
print(coin6)
del coin6
print(coin6)


