
# classmethod
class Chai_order:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type=tea_type
        self.sweetness=sweetness
        self.size=size
        # A class method is a method that creates an object using the class itself, not an existing object.
    @classmethod
    def from_dict(cls,chai_data):
        return cls(
            chai_data["chai_type"],
            chai_data["sweetness"],                
            chai_data["size"])
        
    @classmethod
    def from_string(cls,string_data):
        chai_type,sweetness,size=string_data.split(",")
        return cls(chai_type,sweetness,size )   
class Chai_utils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Medium","Large","Low"]
print(Chai_utils.is_valid_size("200ml"))
print(Chai_utils.is_valid_size("Low"))        
            
order1=Chai_order.from_dict({"chai_type":"Masala","sweetness":"medium","size":200})   
       
print(order1.__dict__) 
order_2=Chai_order.from_string("Ginger,low,300") 
print(order_2)
print(order_2.__dict__)         
            