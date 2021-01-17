
import random

class coin:
    def __init__ (self,rare = False ,clean = True,heads=True,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)


        self.is_rare = rare
        self.is_clean = clean
        self.heads=heads

        if self.is_rare:
            self.value = self.org_value*1.25
        else:
            self.value = self.org_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color
            
    def rust(self):
        self.color = self.rusty_color
    def clean(self):
        self.color = self.clean_color
    def __del__(self):
        print('coin spent')
    def flip(self):
        options = [True,False]
        choice = random.choice(options)
        self.heads = choice
        

class pound(coin):
    def __init__(self):
        data={'org_value':1,
              'clean_color':'gold',
              'rusty_color':'greenish',
              'num_edges':1,
              'diamete':22.5,
              'thickness':3.15,
              'mass':9.5}
        super().__init__(**data)
   
one_pound = pound()
print(one_pound.color)

one_pound.rust()
print(one_pound.color)


