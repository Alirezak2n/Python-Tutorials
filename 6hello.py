#ask name

name=input("what is your name?: ")
print(name)

#age
age=input("how old are you: ")#har chizi dar input yek noe string mishe
print(age)

#city

city=input("where are you from: ")
print(city)

#love
love=input("what do you love: ")
print(love)

#output

string="your name is{} & you are {} years old. you live in {} and you love{}"
output=string.format(name,age,city,love)#be tartib jay gozari mikone
print(output)

