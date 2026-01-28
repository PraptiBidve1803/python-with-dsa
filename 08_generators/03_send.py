
# send in geneartors

def chai_customer():
    print("Welcome to the chai stall !")
    order=yield #takes the value 
    while True:
        print(f"You order {order}")
        order=yield #wait for passing next chai value (if not using this then it run infinite times)
        
stall=chai_customer()
next(stall) #generator is start  
stall.send("Masala chai")  
stall.send("Lemon chai")
    