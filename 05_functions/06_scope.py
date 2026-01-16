#   scope of the function

def chai_type():    #local scope
    chai="Tulsi"
    print(f"Inner :The chai type is {chai}")
    
chai="Lemon"  #global scope  
chai_type() 
print(f"Outer :The chai type is {chai} ") 



# Enclosing scope

def chai_counter ():
    chai_order ="ginger"
     
    def print_order():
        chai_order="masala"
        print(f"Inner : Serve the {chai_order} chai")
    print_order()
    print(f"Outer : Serve the {chai_order} chai")    
        
        

chai_counter()
chai_order="Tulsi"  #global scope

print(f"Global : Serve the {chai_order} chai ")

  
    
