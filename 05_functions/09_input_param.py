# chai="Ginger chai"
# def preparing_chai(order):
#      print("Praparing" , order)
    
    
# preparing_chai(chai)
# print(chai)    
    
    
chai=[1,2,3]
def edit_chai(cup):
    cup[1]=42
    
    
edit_chai(chai)
print(chai)  



# two types of argument : args , *kwargs

def make_chai(tea,sugar,milk):
    print(tea,sugar,milk)
    
make_chai("Aasam","no","no")   #positional
make_chai(tea="Green",milk="No",sugar="medium")  #keywords


def special_chai(*ingredients,**extras):
    print("Ingredientd",ingredients)
    print("Extras",extras)
    
special_chai("Cinnamon","Cardmom",sweetner="Honey",flavor="Ginger", milk="No")  #args and keyargs  
    
def fruit_order(order =[]):
    order.append("Mango")
    print(order)
    
fruit_order() 
fruit_order()  


def vegetable_order(order=None):
    if order is None:
        order=[]
        print(order)    
        
vegetable_order()
vegetable_order()        
       