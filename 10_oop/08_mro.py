
# Method resolution order(mro)

class A:
    label="A:Base class"

class B(A):
    label="B:Masala blend"
class C(A):
    label="C:Herbal blend"  
    
class D(B,C):  #order of inhereting class is matter....
    pass         

cup=D()
print(cup.label)
print(D.__mro__)


