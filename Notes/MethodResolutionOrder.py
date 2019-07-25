
#https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/

class A:
    def rk(self):
        print(" In class A")


class B(A):
    def rk(self):
        print(" In class B")


class C(A):
    def rk(self):
        print("In class C")

    # classes ordering


class D(B, C):
    pass

class E(C, B):
    pass

print("instance in B")
r = B()
r.rk()

print("instance in D")
r = D()
r.rk()

print("instance in E")
r = E()
r.rk()

'''
In the above Example algorithm first looks into the instance class for the invoked method. 
If not present, then it looks into the first parent, if that too is not present then-parent of the parent 
is looked into. This continues till the end of the depth of class and finally, till the end of inherited classes. 
So, the resolution order in our last example will be D, B, A, C, A. But, A cannot be twice present thus, 
the order will be D, B, A, C. But this algorithm varying in different ways and showing different behaviours 
at different times .

'''


# Old style class
class OldStyleClass:
	pass

# New style class
class NewStyleClass(object):
	pass


'''
Method resolution order(MRO) in both the declaration style is different. 
Old style classes use DLR or depth-first left to right algorithm whereas new style classes use C3 Linearization 
algorithm for method resolution while doing multiple inheritances.
'''