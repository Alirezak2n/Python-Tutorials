# Functional Programming means seperate data and methods and functions. clear, easy to extend, maintain and memory effiicient and not repeated
# pure function: give the same output with same input every time, no side effect and change nothing outside the scope for example a print in a function
# map
def multiply_2(li):
    li2=[]
    for num in li:
        li2.append(num*2)
    return li2
print(multiply_2([1,2,3]))


# with map we just tell the function what we need in return of data
def multiply_2map(li):
    return li*2

my_list = [1,2,3]
print(list(map(multiply_2map,my_list)))  # It means i give some data and this data acted by this function
print(my_list)  # it doesnt change the original list
# map: when we have some thing to iterate and change like change email to capital we can use map


# filter
# it will filter items based on the function we give
def only_odd(item):
    if item % 2:
        return True
    else:
        return False
print(only_odd(5))

def only_odd_filter(item):
    return item %2 !=0

print(list(filter(only_odd_filter,my_list)))  # we should not call function "()" we should just point the direction

# zip
# it will add data together for example to add phone numbers and users and type and number of data doesnt matter
your_list=(10,20,30)
def merge(item1,item2):
    for i in range(3):
        merged=(item1[i],item2[i])
    return merged

print(merge(my_list,your_list))

print(list(zip(my_list,your_list)))  # it shouldnt be exactly list it just should be iterable to add together

# reduce
from functools import reduce
# we should import reduce

def accumulator(acc,item):  # acc will be the initial value which we give it 0 here
    print(acc,item)
    return acc + item

print(reduce(accumulator,my_list,0))  # reduce will add all numbers with the initial value and by default acc is 0


# Lambda Expression
print(list(map(lambda item: item*2, my_list)))  # we dont need the function to be called and just lambda
# it is just like a function without name which does some expression on that data
print(list(filter(lambda item:item %2 !=0,my_list)))

print(reduce(lambda acc,item: item + acc,my_list))

# Comprehension
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

my_list = [char for char in 'hello']  # it means add char for all char which are in hello
print(my_list)
my_list2 = [num for num in range(100)]
print(my_list2)
my_list3 = [num**2 for num in range(100)]  # we do some calculation on each number
print(my_list3)
my_list4 = [num for num in range(100) if num%3 != 0 and num%2 != 0 and num%5 !=0]
print(my_list4)

my_set = {num**2 for num in range(100) if num %5==0}
print(my_set)

my_dict = {k:v**2 for k,v in {'a':1,'b':2}.items() if v %2==0}
print(my_dict)

my_dict2 = {k:k*3 for k in [1,2,3]}
print(my_dict2)

