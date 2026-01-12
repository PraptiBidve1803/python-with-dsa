flavours=["Tulsi","Out of stock","Ginger","Discontinued","spice"]
for flavour in flavours:
    if flavour=="Out of stock":
        continue
    if flavour=="Discontinued":
        break
    print(f"{flavour} flavour is found ")
print("Loop is ended")    
    