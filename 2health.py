import random

health=50
difficulty=3
potion_health=int(random.randint(25,50)/ difficulty)#force to integer
print(potion_health)

health=health+potion_health
print(health)

