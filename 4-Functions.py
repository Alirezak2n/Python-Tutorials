# Functions
def hello(name='Elham',emoji=':*'):  # name and emoji are two parameters, two name are its default if we didnt have argument
    print(f'hi {name},{emoji}')
# difference between parameter and arguments is that first one use when define functions while arguments are use
# when calling or invoke function
hello('ali',':)')  # ali and :) are two arguments we give
hello(name='ali',emoji=':)')  # this called as keyword argument
hello()

# def sum(num1,num2):  # we only def another function and not calling it and we cant call
#     def another_func(num1,num2):
#         return num1+num2  # return automatically exit the function and doesnt continue after return
#     return another_func(num1,num2)
# print(sum(4,6))
def test(a):  # its called doc string, it add info when using function
    '''
    comment: great feature that shows information
    '''
    print(a)
test('!')

def is_even(num):
    return num % 2==0  # it returns in front of that so give a true or false
print(is_even(5))

def super_func(*args, **kwargs):  # when we have different args or dont know the exact number of them and store them as
    # int but **kwargs are for keywords which are argument and will store them in dicts

    print(args,kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1,2,3,4,5,num1=12,num2=34))
  # Rule order: Params, *args, default params, **kwargs
  # example : def super_func(name, *args,i='hi', **kwargs)

# Scope Rules in functions
# 1-Locals(in function), 2-Parent Local(in parent function), 3-Global, 4-built-in python functions(like sum)
total=0
def count():
    global total  # we use global which tell function to use global variable
    total+= 1  # we first say use global variable and then modify it
    return total

# second way: def count(total): total+=1 return total and then  print count(count(count(total)))
count()
count()
print(count())
def out():
    x='local'
    def inn():
       nonlocal x  # it is used for accessing parent local which we can modify nonlocal variable
       x='nonlocal'  # if we comment upper line, we would have two x in result
       print('inner:',x)

    inn()
    print('out:',x)
out()
