# Modules means different python files together
# a utility module usually is just a file with only functions and we add like this
import test
import google_python_exercises.hello  # import a py from a folder
from google_python_exercises.hello import show  # we can import a particular function from a py file
from oogle_python_exercises.hello import *  # it will import every thing

print(__name__)  # gives the name of file and if it is the main running file, will be __main__
print(test)
print(google_python_exercises.hello)
show(7)

if __name__ == '__main__' :  # we want to run this only if it is the main file
    print('thats the main')
import random
# import re as reee  it will use 
my_list=[1,3,5,7,9]
print(random)
print(random.random())
print(random.randint(0,10))
print(random.choice([7,8,9,10,11]))  # will choose between numbers
print(random.shuffle(my_list))  # will shuffle the given list
print(my_list)

import sys

a=sys.argv[0]
b=sys.argv[0]
#  if we give argument it will use in other indexes such as 1 and 2 and by default index 0 is name of file
print(f'hello {a}, {b}')

from collections import Counter,defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,5]
sentence = 'blah blah blah blah blah blah'
print(Counter(li))  # it create a dictionary which count numbers of each item
print(Counter(sentence))

dictionary = defaultdict(lambda:'does not exist' ,{'a': 1, 'b': 2})  # we make it defaultdict which if we call something out of dict key
# it will call a default amount which should be callable
print(dictionary['c'])

d = OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['b']=2
d2['a']=1

print(d2==d)  # it is sensitive to the order of the adding items while it could be true in a normal dict


import datetime

print(datetime.time(5,45,2))  # show the number as time
print(datetime.date.today())  # show today date

import time

print(time.time())


from array import array
# we can increase list size any time but array use less memory and determine how much memory can be used
arr=array('i',[1,2,3])  # we first say what type of data it is going to use which here is int
print(arr[0])

