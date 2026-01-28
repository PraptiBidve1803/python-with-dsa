"""Studied in generators :
=>yield
=>next   
=>send 
=>yield from 
=>close"""

# yielf from in generators

def local_chai():
    yield "Masala chai"
    yield "Elaichi chai"
    yield "Ginger chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
for chai in full_menu():
    print(chai)            
    
    
 
# close in generators

def chai_customer():
    try:
        while True:
            order=yield "Waiting for the order"
            
    except:
        print("Stall closed, no more chai")   
        
stall=chai_customer()
print(next(stall)) 
stall.close()  #cleanup or generator is closed            



