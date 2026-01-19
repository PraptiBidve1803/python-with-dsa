"""Types of functions :
1)Pure vs Impure
2)Recursive functions
3)Lambdas(Annonymous function)"""
  
  
def pure_chai(cups):  #pure function
    return cups*10

total_chai=0
# not recommended
def impure_chai(cups):
    global total_chai
    total_chai+=cups
    return total_chai
    
print(impure_chai(5)) 


# Recursive functions

def chai_cup(n):
    print(n)
    if n==0:
        return "All cups are poured" 
    return chai_cup(n-1)

print(chai_cup(8))   

# lambda function

chai_types=["Ginger","Kadak","Green","Light"]

strong_chai=list(filter(lambda chai:chai!="Kadak",chai_types))    
    
print(strong_chai)     
    
    

    
