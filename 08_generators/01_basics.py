"""
Generators
you saved memory
you dont want the results immediately
lazy evaluation

    """
 # normal function => gives everything at once
#  Generator=>gives  one value at a time 
    
    
def get_chai():
    return ["Masala chai","Ginger chai","Elaichi chai",]


print(get_chai()) 

# def serve_chai():
#     yield "Masala chai"
#     yield "Ginger chai"
#     yield "Elaichi chai"
#     yield"spicy chai"
    
# stall=serve_chai()    

# print(stall)
# print(next(stall))
# print(stall)

def get_fruit():
    yield "Mango"
    yield "Bananna"
    yield "Orange"
    yield"Apple"
    return
    
    
for fruit in get_fruit():
    print(fruit)    