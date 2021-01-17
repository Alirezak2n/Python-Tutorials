# Generators
range(100)  # it is a generator too
# all generators like range are iterables but not are iterables like list are generator

def generator_func(num):
    for i in range(num):
        yield i  # it pause function and comes back later, if we use return it is not a generator

for item in generator_func(1000):
    print(item)  # here it print only one number each time
print(generator_func(10))

ge=generator_func(10)
next(ge)  # with next it goes to next number
print(next(ge))

def our_for(iterable):  # how for loops work
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

our_for([1,2,3])


class MyGen():  # how range work
    current = 0
    def __init__(self,first,last):  # a class with the option of first and last
        self.first = first
        self.last = last

    def __iter__(self):  # make the class iterable
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current +=1
            return num
        raise StopIteration


gen = MyGen(0,100)
for i in gen:
    print(i)
