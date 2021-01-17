


A=[]
while len(A) < 1:
    new_name=input("please add a new name: ").strip().capitalize()
    A.append(new_name)
print("sry list is full")
print(A)
for number in range(1,11): #range az mian in adad 

    print(number)

for n in [1,2,3,4]:

    print(n)

for l in "abcd":
    print (l)

for n in range(1,20,2): # be tartib start va stop va step

    print(n)


vowels=0
consonants=0
word=input("please enter a word: ")
for letter in word:
    if letter.lower() in "aeiou":
        print (letter)
        vowels=vowels+1
    elif letter == "":
        pass
    else:
        consonants=consonants+1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))


students={
    "male":["Tom","Bryan","Harry","Frank"],
    "female":["Sarah","Huda","Samantha","Emily"]
    }
for radif in students.keys(): # vaghti for in tarif mikonim esmi k mizarim mohem nis
    #masalan inja radif ya esm mohem nis chi bashe
    #ye variable hastan k tarif mishan
    for esm in students[radif]:
        if "a" not in esm:
            print(esm)
print([x for x in range(1,101) if x % 2==0]) #aalie

words=["the","quick","brown","fox","jumps","over"]
print([[w.upper(),w.lower(),len(w)] for w in words]) 




































