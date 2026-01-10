chai_cup=input("Enter the size of the cup (small/medium/large) : ").lower()
if chai_cup== "small":
    print(f"The price of your {chai_cup} size cup is Rs.10")
elif chai_cup=="medium":
    print(f"The price of your {chai_cup} size cup is Rs.15") 
elif chai_cup=="large":
    print(f"The price of your {chai_cup} size cup is Rs.20")
else :
    print(f"Your cup size is invalid")          
    