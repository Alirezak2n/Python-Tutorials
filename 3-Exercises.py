
#Exercises
# birth_year = input("what year were you born? ")
# birth_year = 2020 - int(birth_year)
# print(f"\n you are {birth_year} years old")
# user = input("please give me your username :")
# password = input("please give me your pass: ")
# print(f"your username is {user} and your password {len(password) * '*'} is {len(password)} letters long")
print('####### Second one')
counter = 0
for item in (range(1,11)):
    counter = item+counter
print(counter)
print('####### third one')
picture=[
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
#  first way to show the christmas tree
i=0
while i < 6:
    for item in picture[i]:
        if item == 1:
            print('*', end='')  # the default value of end will add a new line but with end, it shows another thing
        else:
            print(' ', end='')
    print('')
    i+=1
#  Second way
for row in picture:
    for pixel in row:
        if pixel:  # we can use truthy value and just say if pixel which means if true(if exist)
            print('*', end='')
        else:
            print(' ', end='')
    print('')
print('####### forth one')
a_list=['a','b','c','b','d','m','n','n']
new_list=[]  # first way
for letter in a_list:
    a = a_list.index(letter)
    print(a)
    if letter in a_list[a+1:-1]:
        new_list.append(letter)
print(new_list)

new_list=[]  # second way
for letter in a_list:
    if a_list.count(letter) >1 and letter not in new_list:
        new_list.append(letter)
print(new_list)

new_list = {letter for letter in a_list if a_list.count(letter) > 1 }  # third way
print(new_list)
print('####### fifth one')
def highest_even(*args):
    a=list(args)
    a.sort(reverse=True)
    print(a)
    for number in a:
        if number %2 ==0:
            return number

print(highest_even(1,4,7,8,10,15,11,14,14,9,5,2))

print('####### Sixth one')

class SuperList(list):

    def __len__(self):  # we changed the function of list
        return 1000

li = SuperList()
li.extend([5,4,2,7])
print(li)
print(len(li))
print(isinstance(list,SuperList))

print('####### Seventh one')

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores )))

print('####### Eighth one')

my_list = [5,4,3]
a = [(0,2),(4,3),(9,9),(10,-1)]
print(list(map(lambda item: item**2,my_list)))

a.sort(key=lambda item: item[1])  # with lambda we use second index of every item
print(a)

print('####### Ninth one')
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:  # if it is true, run the function
      return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

print('####### Tenth one')
def fib(number):  # my way
    n1 = 0
    n2 = 1
    print(n1)
    for i in range(number-1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
    return f'for {number} time of fibonacci'

print(fib(5))

def fib2(number):  # second way in generator
    a=0
    b=1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp+b
    yield a
for x in fib2(20):
    print(x)



def fib3(number):  # third way in list which is more efficient
    a=0
    b=1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp+b
    return result

print(fib3(20))

print('####### Eleventh one')
from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open('translate.txt' , mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(text,translation)
        with open('translate-ja.txt' , mode='w',encoding="utf-8") as my_file2:  # we should set encoding to set my file
            my_file2.write(translation)
except FileNotFoundError as err:
    print('check your file',err)


print('####### Twelfth one')
import re
password = 'asfwhh314'
# generate password with at least 8 characters which ends with number

print(re.fullmatch(r'(^[a-zA-Z0-9$%#@]{8,}\d)',password))

print('####### Thirteenth one')




