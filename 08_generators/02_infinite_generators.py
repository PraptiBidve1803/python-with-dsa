# Infinite generator = a generator that keeps giving values forever, one at a time, until you stop asking

def infinte_generator():
    count=1
    while True:
        yield f"Refill #{count}"
        count+=1
        
        
Refill=infinte_generator() 
user2=infinte_generator()
for _ in range (6):
    print(next(Refill))    
    
for _ in range(7):
    print(next(user2))       
        
                
    
    
    


