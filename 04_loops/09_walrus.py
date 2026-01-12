
# walrus opeartor in python
# value=19
# remainder=value%5
# if remainder:
#     print(f"not divisible,remainder is {remainder}")

# value=16
# if(remainder:= value%5):
#     print(f"not divisible,remainder is {remainder}")
    
# tea_cup_size=["small","large","medium"]

# if (size:= input("Enter the tea cup size : ").lower())  in tea_cup_size:
#     print(f"Wait serving your tea having a cup size : {size}")
# else:
#     print(f" {size} size is not available")        


flavors=["spice","ginger","tulsi","mint"]
print(f"Available flavors are : {flavors}")

while(flavor:=input("choose your tea flavor : ")) not in flavors:
    print (f"Sorry , {flavor} flavor is not available")
print (f"You choose {flavor} chai")    
