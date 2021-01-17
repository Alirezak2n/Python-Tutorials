a=100   #age a tu yki az function ha bashe dg global nis va local hast
#pas f2 nmitune bbinatesh
def f1():
    print(a)
def f2():
    print(a)

a=250
def f3():
    a=100 #vaghti ejra beshe az memory pak mikone
    print(a)
    
def f4():#tarkibi az global o local
    b=a+50
    print(b)


print(a) #a global avaz nashode
print(f3())
print(f4())

def f1():
    global a # migim k mikhaym az global a estefade konim o taghyiresh bedim
    a = 100 #bayad hatman dar 2 khat bashe
    print(a)
def f2():
    a= 50
    print(a)

print(a)
print(f1())
print (f2())

a=[1,2,3]
def f1():
    a[0] = 100 #bdune estefade az global mishe yek index list ro avaz kard
    a[1] = 23
    print(a)
def f2():
    a= 50
    print(a)

print(a)
print(f1())
print (f2())
print(a)

