# fundamental data types
# int
print(5 + 10)
print(type(5 * 10))
print(5 ** 3)
print(10 // 3)  # what is the base numbers after division here is 3
print(10 % 3)  # What remains after division here is 1
# float
print(5 / 10)
print(type(5 / 4))
print(type(0.0))
print(type(0))
# String
print(type("Hi There"))
long_string = '''
WoW
0 0
___
'''
print(long_string)
print("it's\" sunny")  # whatever comes after\ tell python its string
print("\t it's\" \n sunny")  # \t add a tab  \n add a line
name,att='Alireza','Great'
print("hi {}, You are {}".format(name,att))  # two ways of formatted string
print(f" hi {name}, You are {att}")  # best way in my opinion
print(len(att))
print(att[-4:4:2])  # star:finish:step its called slicing
print(att[-1:1:-1])
print(att[::-2])
print(name.upper())
print(name.capitalize())
print(name.find("ir"))
print(name.replace("ir","el"))
# Boolean
True
False
# list
list_temp = [1, 2, 'notes', True]
print(list_temp[0::2])  # we cant have string[1] = 'a' because strings are immutable but  we have list_temp[1] = 'ss' because they are mutable
list_temp[0] = 'laptop'
new_list = list_temp  # with this equation we make a new address for same items in list_temp
new_list[0] = 'PC'
print(new_list)
print(list_temp)
new_list = list_temp[:]  # with this equation we make a copy of items in list_temp
new_list[0] = 'tablet'
print(new_list)
print(list_temp)
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
print(matrix[0][1])
print(len(matrix))
#list_temp adding
print(list_temp.append(100))  # at the end add an item
print(list_temp)
list_temp.insert(0,200)  # at index number 0 add 200
print(list_temp)
new_list2 = list_temp
list_temp.insert(0,300)
print(new_list2)
print(list_temp)
list_temp.extend([201,202,203,204])  # add a list_temp to the end of our list_temp
print(list_temp)
#list_temp removing
list_temp.pop()
print(list_temp)
list_temp.pop(1)  # remove an item with index number 1 or from the last and return it if print
print(list_temp)
list_temp.remove(202)  # remove first occurrence of an item which we give
print(list_temp)
list_temp.clear()  # remove the list_temp completely
print(list_temp)
#list methods
list_temp = [1, 2, 5, True,3,4]
print(list_temp.index(2,1,4))  # give index of value in given range,1-4
print(2 in list_temp)
print(list_temp.count((2)))
print(sorted(list_temp))  # sorted is a function that produce a new list_temp
print(list_temp)
list_temp.sort()  # sort just sort the list_temp in place
print(list_temp)
new_list = list_temp.copy()  # we can do the same as new_list = list_temp[:] with copy method
list_temp.reverse()
print(list_temp)
print(range(1,100))
print(list(range(100)))  # this way it show a list in range 0 to 100
sentence = '!'
print(sentence.join(['hi','alireza']))
print(' '.join(["Hi",'Alireza']))  # add every string in given list to the given string
#list unpacking
a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
# Dictionary
dictionary = {
    'a': [1,2,3],
    'b': 'who are you', #  the key should be unique so they will overwrite
    'b': 'Alireza you can do it',
    #[123]:'hello'  # we cant have list as key because key should be immutable
}
print(dictionary['b'])
print(dictionary.get('c'))  # with get if we dont have the key in dictionary, it returns none instead of error
print(dictionary.get('d','oops'))  # if we dont have key in dictionary, it shows the default we assign 'oops'
dictionary2 = dict(alireza="is the best")  # another way of making dictionary
print(dictionary2)
print([1,2,3] in dictionary.values())  # check in the values of dic otherwise it look at keys
print(dictionary.items())  # it return all the keys and values in tuple
dictionary2 = dictionary.copy()
print(dictionary2)
print(dictionary.update({'a': 55}))  # it changes the value of given key and if key not found it make one
print(dictionary.pop('a'))  # pop the value of given key
print(dictionary.popitem())  # remove as LIFO
dictionary.clear()
# Tuple
my_tuple = (1,2,3,4,5,5)  # they are like list but cant modify them or sort or reverse and only 2 method
print(my_tuple[1:2])  # a tuple with only one item has coma at end
print(my_tuple[1:4])
x,y,z,*rest = (6,7,8,9,10)
print(x,"\n",y,"\n",z,"\n",rest)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
# Set
my_set = {1,2,3,4,5,5}  # set are unordered and unique objects and cannot access by index
my_set.add(100)
my_set.add(2)
print(my_set)
my_list = [1,2,3,4,5,5]
print(set(my_list))  # delete the duplicates
print(1 in my_set)  # how to check some thing is in memory
print(len(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)
my_set = {4,5,6,7,8,9,10}
print(my_set)
print(new_set.difference(my_set))  # it gives what is in first set while it is not in second set
new_set.discard(100)
print(new_set)
print(new_set.intersection(my_set))  # prints out the intersection 4-5 (similar to &)
new_set.difference_update(my_set)  # it removes all elements of one set from another
print(new_set)
print(new_set.isdisjoint(my_set))  # if these two set have nothing in common it gives true
print(new_set.issubset(my_set))  # if one set members are all in other set <
print(new_set.union(my_set))  # united two set but remove any duplicates (similar to | )
print(new_set.issuperset(my_set))  # if one set have members of other set >
print(new_set.symmetric_difference(my_set))  # union of two set except their intersection
