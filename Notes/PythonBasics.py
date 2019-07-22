
###################################################
# 1. Python passing parameters through function
###################################################
a = 1
def fun_assignValue(a):
    a = 2
fun_assignValue(a)
print(a)

a = []
def fun_appendElement(a):
    a.append(1)
fun_appendElement(a)
print(a)
'''
mutable object vs immutable object
String, tuples and numbers are immutable
list, dict and set are mutable 

****** KEY NOTE  ******
Python is passing by object reference 
1.THE VARIABLE IS NOT THE OBJECT 
    e.g.  x=[]  --->>  [] is a empty list, x is a variable that points to the empty list, 
    but x itself is not the empty list, the empty list is the object sitting in the RAM
2. Object references are passed by value

'''
# For mutable object like list, the parameter passed in is a reference to outer_list.
# The mutating list method can change the list and have the reflected in the outer scope
print("Tthe mutating list method can change the list and have the reflected in the outer scope")
def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)
# the outer_list and the_list are pointing to same object(list)
outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)

# For mutable object like list, assigning a new list to it had no effect outside scope of the method
print(' ')
print("For mutable object like list, assigning a new list to it had no effect outside scope of the method")

def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)

###################################################
# 2. @staticmethod and @ class
###################################################
print('  ')


def foo(x):
    print("executing foo(%s)"%(x))

class A(object):
    # the object instance is implicitly passed as the first argument
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod # use decorator to define it
    # the class of the object instance is implicitly passed as the first argument instead of 'self'
    def class_foo(cls,x):
        # always receive 'cls' as the first argument
        print("executing class_foo(%s,%s)"%(cls,x))
    # you intend to call it from the class rather than from a class instance


    @staticmethod
    # neither self nor cls is implicitly passed as the first argument
    def static_foo(x):
        print("executing static_foo(%s)"%x)


a=A()
a2=A()

a.foo(1)
a.class_foo(1)
A.class_foo(1)
a.static_foo(1)
A.static_foo(1)

###################################################
# 3. Iterator Generator and Yield
###################################################

# Everything you can use "for... in..." on is an iterable;

'''
Generators are iterators, a kind of iterable you can only iterate over once. 
Generators do not store all the values in memory, they generate the values on the fly
'''
print("  ")
print("3.1 Generator")
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

'''
It is just the same except you used () instead of []. 
BUT, you cannot perform for i in mygenerator a second time since generators can only be used once: 
they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
'''

'''
yield is a keyword that is used like return, except the function will return a generator.
To master yield, you must understand that when you call the function, 
the code you have written in the function body does not run. The function only returns the generator object

The first time the for calls the generator object created from your function, 
it will run the code in your function from the beginning until it hits yield, 
then it'll return the first value of the loop. 
Then, each other call will run the loop you have written in the function one more time, 
and return the next value, until there is no value to return
The generator is considered empty once the function runs, 
but does not hit yield anymore. It can be because the loop had come to an end, 
or because you do not satisfy an "if/else" anymore
'''
print("3.2 Yield")
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
    print(i)



 ### Controlling a generator exhausion
print("3.3 Generator Bank example")
class Bank():  # Let's create a bank, building ATMs
    crisis = False
    @property
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()  # When everything's ok the ATM gives you as much as you want
corner_street_atm = hsbc.create_atm
print(next(corner_street_atm))
print(next(corner_street_atm))
print([next(corner_street_atm) for cash in range(5)])
hsbc.crisis = True
print(next(corner_street_atm))
wall_street_atm = hsbc.create_atm()
print(next(wall_street_atm))
hsbc.crisis = False
print(next(wall_street_atm))
brand_new_atm = hsbc.create_atm()
for cash in brand_new_atm:
    print(cash)

###################################################
# 4. *arg and **kwag
###################################################




###################################################
# 5.
###################################################



class A():
    def foo1(self):
        print("A")
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print("C")
class D(B, C):
    pass

d = D()
d.foo1()


###################################################
# 6.  __new__  vs  __init__
###################################################










