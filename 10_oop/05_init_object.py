# init <===> constructor
"""A constructor is a special function that runs automatically
when you create an object from a class.
    """
    
    
class Chai_order:
    def __init__(self,type_,size):   #constructor
        # 1)Python calls it automatically 2)self connects data to that specific object
        # Create a variable called type inside the object
        self.type=type_ 
        self.size=size  #e.g order_1.size=200
        
    def chai_summary(self):
        return f"The cup size of the {self.type} chai is {self.size}ml"
    
order_1=Chai_order("Ginger",200)    # behind the scene ==>Chai_order.__init__(order_1,"Ginger",200)
print(Chai_order.chai_summary(order_1))  

order_2=Chai_order("Masala",150)
print(order_2.chai_summary())

        
        
            
   