
class Chai:
    temperature="hot"
    strength="strong"
    
print(Chai.temperature)
print(Chai.strength) 

masala=Chai()   #creating object   
print(masala.temperature)

masala.cup_size="small"
print(masala.cup_size)

masala.strength="mild"
print("changing the object :",masala.strength)
print("not affecting the class: ",Chai.strength)    

del masala.strength
print("deleting the attribute temperature from object :",masala.strength)