# Error Handling
# if we get error we can handle and let the python continue if it has error even
# some error
# print('add'+1)  # type error: two different data type
# def hooohoo()  # Syntax Error: when forget some thing like : in the end
# print('ali')  # name error, undefined name
# li[5]  # Index Error: list index out of range
# di{'b]  # key error: key not found

while True:
    try:  # do this part of code and any thing happens can be handle by except
        num = int(input('give a number'))
        10/num
        #raise ArithmeticError('stopped')  # if we want to stop the program, we should delete except part or use raise to bring an error
    except ValueError:  # It handle ValueError
        print('give a numberrrrrr')
    except ZeroDivisionError:  # it handle Zero division error
        print('more than 1')
    else:
        print('thanks')
        break
    finally:  # no matter what is result, we have to do this part
        print('finally done')

def summ(n1,n2):
    try:
        return n1+n2
    except TypeError as err:  # we use error message in print function
        print(f'num please {err}')
print(summ(1,'2'))

def summ2(n1,n2):
    try:
        return n1/n2
    except (TypeError,ZeroDivisionError) as err:  # we use two error message in one
        print(f'not zero {err}')
print(summ2(1,0))
