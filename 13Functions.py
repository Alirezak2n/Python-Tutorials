def ezafe(x,y):
    return x + y#age return nabashe hichi bar nmigardune faghat anjam mide
    
print(ezafe(2,6))

def ezafe(x,y):
    print(x + y)#hichi bra nmigardune va mesle return nist va dar memory nmibare

word="pen"
print(word[::-1])#harchi tush hast ro bar ax mikone

def barax(x):
    return (x[::-1])
print (barax([1,2,3,4]))

def about(name,age,likes): # name,age,likes parameter hastan na argument
    sentence = "meet {} they are {} years old and like {}".format(name,age,likes)
    return sentence

print (about("Alireza",23,"python"))#chizi ke b function midim argument na parameter
# argument ro bayad tu order khasi bgim ya mesle payin moshakhas konim
print (about(age=23,name="Ali",likes="me"))

def about(name,age,likes = "python"): #ye meghdar default baraye likes mizarim
    #k age chizi behesh nadim khodesh mizare
    #parameter ba default bayad akhar biyad va nmishe aval biyad
    sentence = "meet {} they are {} years old and like {}".format(name,age,likes)
    return sentence
print (about("Alireza",23))
#mishe default be hame dad k badan ham harchi mikhan bgiran

numbers=[1,2,3,4,5]
print (numbers)
print(*numbers) #alamate * unpack mikone
# be jaye dashtan ye list, 5 argument khahim dasht

def ezafe(*numbers): #vaghti nmidunim chanta argument dashte bashim, koli migire
    total = 0
    for number in numbers:
        total = total+number
    return(total)
print(ezafe(1,2,3,4,5,6))


def ezafe(x,y):
    return x + y
print(ezafe(y=1,x=2)) #keyword argument, che parametri kodume

my_dict={"name":"Alireza","age":26,"likes":"python"}
print(about(*my_dict))#ye * normal argument
print(about(**my_dict))#2 * keyword argument
#** keyword va value darim, *faghat argument aadi va harchandta k bkhaym
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
print(foo(huda="female",ziyad="male"))







