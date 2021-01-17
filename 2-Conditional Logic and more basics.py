# If Operator
if "Hello" and 5 :
    print("Alireza Is Smart ")
elif 2 == 3:
    print("ZOOOOOO")
else:
    print("WOW")

# Ternary Operator or Conditional expression
#condition_if_true if condition else condition_if_false
fact="alireza will be successfull" if 5 else "Whatever"
print(fact)
print("aaa") if 2==3 else print("sss")
# Short Circuiting
if True or False:
    print("second part does n't matter due to short circuiting")
# logical operator
print(4<3)
print(4==5)
print('a'<'b')
print('c'<'b')
print(1<=1)
print(1!=2)
print(not (True))
print(10 == 10.0) # should have same value
print(10 is 10.0) # should be exactly the same
a = [1,2,3]
b = [1,2,3]
print(a is b)  # false because they are in different memory space
print([] is [])  # two list in two different space
# Truthy and Falsy
print(bool("Hello"))
print(bool(5))
print(bool(""))
print(bool(0))
# For Operator
for item in [1,2]:  # item can be anything its just a variable
    for x in {'name': 'Alireza', 'age': 25,
              'can_do it': True}.items():  # as a dictionary we can use .keys or .values too
        print(item, x)
        key, value = x
        print(key, value)
    for key,value in {'name':'Alireza','age':25,'can_do it':True}.items():  # another way which we use without having to write another line
        print(key,value)  # only list,dict,tuple,set,string that are collection of items are iterable not int or...
print(item)
print(range(100))
print(range(0,100))  # both of them are same
for _ in range(10,0,-2):  # if we want to do reverse we should take care of our range to start from big to small
    print(_)
    print(list(range(10)))
# Enumerate
for i,j in enumerate("Alireza"):  # its like range but gives the index too
    print(i,j)
    if j=='r':
        print(f'the index of r is {i}')
for i in enumerate([1,2,3]):
    print(i)
# While
i = 0
while i < 1:
    print(i)
    i+=1
else:
    print('DOne')
# Break,Pass,Continue
for item in [1,2,3]:
    print(item)
    break  # it will come out of the loop completely
for item in [1,2,3]:
    continue  # it will come out of current loop and start again at loop
    print(item)
for item in [1,2,3]:
    pass  # it does nothing, just pass it to next line and when we have nothing in loop it doesnt bring error 

# Variable and Constant and dunder
PI = 3.14  # Constant, it means it should not be changed
pi = 3.14  # a variable
a, b, c = 1, 2, 3
print(c, a, b)
__pi__ = 3.14  # a dunder, it is better not to do
# Expressions and Statements
iq = 100 / 20  # 100/20 is an expression but the whole line is a statement
# Augmented Assignment Operator
some_value = 5
# some_value = some_value + 2
print(some_value)
some_value += 2  # operator comes in the left of the equation
print(some_value)
some_value -= 2
print(some_value)
# Math Functions
print(round(3.4))
print(round(3.6))
print(abs(-16))
# Complex

# Binary
print(bin(5))
print((int('0b101', 2)))




