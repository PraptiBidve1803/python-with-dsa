# self = the object that is calling the method
# self is not a keyword
# It is a reference to the current object
# Without self, object methods cannot work

class Chaicup:
    size="150ml"
    
    def describe(self):     #method
        return f"The chaicup size is: {self.size}"
    
cup1=Chaicup()
print(Chaicup.describe(cup1)) 

cup2=Chaicup()
cup2.size="100ml"

print(Chaicup.describe(cup2))   
