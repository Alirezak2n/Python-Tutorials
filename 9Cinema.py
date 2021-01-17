films= {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    print("please choose one of our films: ",films.keys())
    choice = input("What film do you prefer?: ").strip().title()
    #title har chanta kalame ro bozorg mikone

    if choice in films:
        pass #mige ke faghat edame bede age chize dgi nadasht
        age = int(input("how old are you?: ").strip())
        #input hamishe string zakhire mikone va vase hamin bayad int kardesh

        if age >=films[choice][0]:

            if films[choice][1] > 0:

                print("enjoy film")
            else:
                print("we dont have ticket")
            
            
            films[choice][1]=films[choice][1] - 1
        else:
            print("you are a kid")

            
        
    else:
        print("we dont have it")
    
