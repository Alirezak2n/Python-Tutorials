# Decorators
# Higher order function (HOF) means accept or return a function in another function like map


def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('//////////')
    return wrap_func()

@my_decorator
def hello():
    print('Helloo')

@my_decorator
def bye():
    print('see ya')

# hello()  # all we done is calling function hello and wrap it in decorator just like hello2 or below that
# bye()


# hello2=my_decorator(hello)
# hello2()
#
# my_decorator(hello)()

 #  we have seen some examples of decorators such as staticmethod and classmethod and now we see another use of them

from time import time  # use modules
def performance(func):
    def wrapper(*args, **kwargs):  # we dont know our functions how many params have and want to use it on every function
        t1 = time()
        result = func(*args, **kwargs)  # we wrapped our function with time and then print how long it took
        t2 = time()
        print(f'it took {t2 - t1} s')
        return result
    return wrapper

@performance  # we call the function
def long_time():
    for i in range(10000000):
        i*5

long_time()
