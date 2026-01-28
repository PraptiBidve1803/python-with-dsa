
from functools import wraps
def my_logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"🚀Calling: {func.__name__} ")
        result=func(*args,**kwargs)
        print(f"✅Complete: {func.__name__}")
        return result
    
    return wrapper
        
@my_logger
def making_tea(type,milk="no"):
    print(f"The {type} tea is ready and {milk} milk")  
    
making_tea("Ginger chai")          