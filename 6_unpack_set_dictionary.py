

person = ('Nana', 25, 'piza')
# unpack mikonim person ro
# chandta ro ba ham takhsis midim
name, age, food = person

print(name)
print(age)
print(food)
person2 = ["ali", 26, "eli"]
name, age, food = person2

print(name)
print(age)
print(food)

# dictionary order nadare o nmishe tekrari dasht

dic = {'banana', 'blueberry'}
dic.add("kiwi")
# add mikone
print(dic)
# farghe set o dictionary ine k set key o value
# nadare faghat data gheyre tekrari dare
# vali dictionary ha key o value daran
lis = [1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 8, 6]
no_duplicate = set(lis)
print(no_duplicate)

library1 = {'harry', 'hungry', 'ali'}
library2 = {'harry', 'eli'}
print(library2.union(library1))
# union baes mishe 2ta set ro ba ham edgham konim
print(library2.intersection(library1))
# intersection un chizi k eshterak ro mide
print(library2.difference(library1))
# un chizi k tu lib2 bashe ama tu lib1 nabashe

print(library1.clear())

dictionary = {'ali': 20, 'eli': 25, 'elnaz': 10}
print(dictionary['ali'])
# faghat value hamun key ro print mikone
print(dictionary.get("amo"))
# get baes mishe age nabashe bede none be jaye error

contacts = {"amir": 921,
            "abolfazt": ['0912', "akbar"]}
print(contacts)
# dic tu dic
contacts = {"amir": {'phone': 921, 'email': "aboli@g"},
            "abolfazt": ['0912', "akbar"]}
print(contacts["amir"]["email"])

sen="i am going to be the best python coder " \
    "and will have a great life with elham"
word_count={
    "I":1,"elham":1,'python':1
}
word_count["elham"] = word_count["elham"]+1
print(contacts.items())
#hamasho mide
print(contacts.keys())
#key haro mide
print(contacts.values())
#value haro mide
print(word_count)
word_count.pop("I")
#ye ite ro az dictionary pop mikone
print(word_count)
word_count.popitem()
#akharin item pop mikone
print(word_count)

d= {(1,2):1,5:7}
print(d.keys())


