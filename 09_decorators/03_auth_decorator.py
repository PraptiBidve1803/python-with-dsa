
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(role_type):
        if role_type!="Admin":
            print("Access is denied")
            return None
        else:
            return func(role_type)    
        
    return wrapper


@require_admin

def tea_inventory(role_type):
    print("Access is granted")
    
    
tea_inventory("user")        
    
tea_inventory("Admin")    
        
            