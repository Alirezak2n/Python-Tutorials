# OOP
# 1-encapsulation all attributes and functions and method
# 2-Abstraction means hide every thing which is not necessary or used
# 3-Inheritance attributes and methods can be shared by a class to others and we will have subclass or derived class
# 4-Polymorphism means many form, object classes share method name but they can act differently, two class but one func which act different in each
class PlayerCharacter:  # there is a standard to every word has capitalize letter
    membership = True  # it is class object attribute is different than attributes because they are not dynamic
    def __init__(self, name,age):  # init is dunder or magic method, self refer to what is left of . to have name like .add
        if self.membership:  # it is possible to use PlayerCharacter.membership instead
            self._name = name  # these two line are init or constructor method
            self._age = age  # these are different attributes, when we use _ before name it means variable is private

    def shout(self):  # it is a method
        print(f'my name is {self._name}')
        return self

    @classmethod  # it is a decorator and we can use it without instantiate a class
    def adding_things(cls,num1,num2):  # we should use cls which is standard for class method
        return cls('teddy',num1+num2)  # this way we use it as name and age

    @staticmethod
    def adding_things2(num1,num2):  # the only difference is that we dont have access to cls so cant access class attributes
        return num1+num2


class Test(PlayerCharacter):  # when we have another class in () it means we used inheritance
    pass

player1 = PlayerCharacter('Ali', 22)  # instantiate of class
print(player1._name,player1._age,player1.shout(),player1.membership)
player3 = PlayerCharacter.adding_things(2,8)
print(player3._name,player3._age)
print(PlayerCharacter.adding_things2(5,9))  # we didnt instantiate class of player
print(isinstance(player1,PlayerCharacter))
print(isinstance(player1,object))  # every thing in python is object, object class




class User(object):  # automatically every class gets every method from object class and we can dont write it
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email)  # we need to have email from User class so we add this line which is init of user
        super().__init__(email)  # it is the second way to add email which call super class or class above wizard and is better because we dont have self
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1=Wizard('Merlin',60,'@gmail')
print(wizard1.attack())
print(wizard1.sign_in())
print(wizard1.email)  # although it inherit sign in, wizard has its own __init__ function so we should modify wizard

# Introspection  means the ability to determine the type of a object at runtime and gives all abilities when type .
print(dir(wizard1))

class Multi(Wizard,User):  # we can have a class which inherit from multiple classes but we should be careful about arguments
    # def __init__(self,name,power,arrows ):  # when using multiple inherit, we should give the format of input
        # FirstClass.__init__(self,name,arrows)  # also we should define both of inherit classes
        # SecondClass.__init__(self, name, power)
    pass

hb1 = Multi('new',22,'wowo')
print(hb1.attack())

# Dunder are special methods

class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'YOYO',
            'pets':  False
        }


    def __str__(self):
        return f'{self.color}'  # some times we want our class to behave especial just like lists or dicts but usually we shouldn't change them

    def __len__(self):  # changed the function of len
        return 5

    def __call__(self):  # we changed the function of being called
        return 'Yess??'

    def __getitem__(self, index):  # changed the function of get item or []
        return self.my_dict[index]



action_figure = Toy('red',0)
print(action_figure.__str__())  # example of a special method
print(str(action_figure))  # second way of print
print(str('action_figure'))  # it can be seen that str only behave especial when it is given action_figure object not string
print(len('action_figure'))
print(len(action_figure))
print(action_figure())  # we used call our function and get our desired output
print(action_figure['name'])

# MRO - Method Resolution Order

class A:
    num=10
class B(A):
    pass
class C(A):
    num=1
class D(B,C):  # we have multiple inheritance it doesnt go d-b-a it goes d-b-c-a
    pass

print(D.num)  # the number is by the last inheritance
print(D.mro())
