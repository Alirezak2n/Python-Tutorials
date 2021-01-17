list=["A",2,"24",54]
print(type(list))
print(list)

print(list[1])
print(list[0:3] )    #list[start:end:step]
#az start ta end ro chanta chanta beri

our_list=[1,2,[3,4],5,6]
print(our_list)
print(our_list[2])
print(our_list[2][1])   #az tu list dakheli ham entekhab mikonim


our_table=[[1,2,3],[4,5,6],[7,8,9]]
print(our_table)
print(our_table[1][0:2])

print(2 in our_table) # chizi dar digari hast ya na?
print([1,2,3] in our_table)

known_users=["Alice","Alireza","Elham","Aboli","Fred","Harry"]
print(len(known_users)) #tule list

L=[11,1,22,33,1,44]
del L[0]#index 0 ro pak mikone yani avalin adad
del L[1:2]
print(L)
L.remove(1)#dar inja ma nmidunim k vaghan 1 darim tu list ya na,index nist
# pas farghe del o remove dar dunestan ine ke bdunim che adad ya harfie
#age 2 ta 1 bashe avalisho pak mikone

while True:
    print("Hi my name is travis")
    name=input("What is your name?: ").strip().capitalize()
    #strip age eshtebahi space zadan beparune
    #va capitalize ta harfe aval bozorg she mesle list
    if name in known_users:
        print("come in {}!".format(name)) # az in ravesh ya print("come in",name)
        remove=input("would you like to be removed(y/n)?: ").strip().lower()#horufe kuchak mikone
        if remove == "y":
            print(known_users)
            known_users.remove(name)#remove baraye pak kardan
            print(known_users)
        elif remove =="n":
            print("good boy")
        
        
    else:
        print("get out {}!".format(name))
        add_me=input("hey wait!!  whould you like to be added? (y/n)").strip().lower()
        if add_me == "y":
            known_users.append(name)#ezafe kardan be list
        elif add_me== "n":
            print("heh bye then")
            
A=[2,5,4,98,7,85,3]
print(A)
# ezafe kardan be yek list nmitune b surat int ya str bashe age append nazanim
#A=A+1 nmishe va bayad be surat list bashe
A=A+[1]
A=A+["ali"]
A=A+list("eli")#harf harf ro add mikone vase horuf
A=A+list(str(123))#bayad dar list hamechi be surat str bashe ta add beshe
A=A.append(10)#A ro mikone 10 ta fazaye khali
A.insert(2,100)#ba insert dar index 2 adade 100 ro miare
A.append(10)#adade 10 ro ezafe mikone be tah
print(A)

s=[1,2,3]
s[0]=5#avalin index ro 5 mikone























            
    
