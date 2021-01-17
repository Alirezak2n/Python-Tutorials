our_tuple=1,2,3,"A","B","C" #tuple yek variable ba bishtar az yek moteghayere
our_tuple=(1,2,3,"A","B","C") #be khater shenasayi behtar intori minevisan 
print(type(our_tuple))
print(our_tuple[0:3])

#fargh asli tuple o list ine k list bade sakht ghabele taghyire ama tuple na
#string ha ham taghyir na pazire

#####our_tuple[1]=100

tuple()#chizaye dg ro tabdil be tuple mikone
A,B,C=(1,2,3)#chandta ro assign konim ham zaman
print("A class:",type(A))
print(A)
G,H,I="789"#chandta ro assign konim ham zaman
print("G class:",type(A))
print(G)

my_dictionary={"Alireza":25,"Bob":27,"Elham":17,"Elnaz":22 }
# tarife dictionary, age "" nabashe, donbale variable migarde k tarif shode bashe
print(my_dictionary["Alireza"])#baraye entekhabe key az [] estefade karde
print(my_dictionary["Alireza"])
my_dictionary["Alireza"]=26#taghyire data
print(my_dictionary["Alireza"])

del my_dictionary["Bob"]#pak kardan yek key
print(my_dictionary)
print(my_dictionary.keys()) #.keys baraye didan key ha hastesh
print(my_dictionary.items())

#####my_dictionary.keys()[0] # dictionary ro nmishe tike tike did

#bayad list kard ta beshe did

a=list(my_dictionary)
print(a[1])
print(list(my_dictionary.values())[1:])
print(my_dictionary.items())

######print((my_dictionary.values())[1:]) nmishe values ro mostaghim tike tike kard
#dictionary order nadare
#tanha rah dastresi be dade estefade az key hastesh va na value

print("#"*27)
students = {"Alice":26,
            "Bob":27,
            "Claire":17,
            "Dan":21,
            "Emma":22}
print(students)

students = {"Alice":["ID001",26,"A"],
            "Bob":["ID002",27,"B"],
            "Claire":["ID003",17,"C"],
            "Dan":["ID004",21,"D"],
            "Emma":["ID002",22,"E"]}
print(students)

print(students["Claire"][0])#faghat print kardane id yek nafar
print(students["Dan"][1:])

students = {"Alice":{"id":"ID001","age":26,"grade":"A"},
            "Bob":{"id":"ID002","age":27,"grade":"B"},
            "Claire":{"id":"ID003","age":17,"grade":"C"},
            "Dan":{"id":"ID004","age":21,"grade":"D"},
            "Emma":{"id":"ID005","age":22,"grade":"E"}}
print(students)

print(students["Dan"]["age"])
print(students["Emma"]["id"])




























