
# A namespace is a mapping that stores names and their corresponding objects to avoid name conflicts.

class Chai:
    origin="India"   # attribute
    
print(Chai.origin)   
Chai.is_hot=True
print(Chai.is_hot)

# creating a objects from class chai

Ginger=Chai()
print(Ginger.origin)
print(Ginger.is_hot) 

Ginger.is_hot=False
print(f"Change object not effect on original class: {Chai.is_hot}")
print(f"After changing object:{Ginger.is_hot}")

Ginger.flavor="ginger chai"
print(Ginger.flavor)