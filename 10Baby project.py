import random
from random import choice #az bein ye library faghat yejasho var dare

baby=["who are you?","how old are you?","where are you?"]
answer=("a")
while answer != "dont know":
        
    #####A=random.randint(0,2) #yek ravesh k khodam raftam
    A= choice(baby)
    answer = input(A).lower()

print("okay")
    
