# A decorator is a function that takes another function and adds extra work to it.
from functools import wraps
def my_decorator(func):   #takes another function as input/receives function
    @wraps(func)        #It keeps the original function’s name and details safe.
    def wrapper():     # it runs greet()
        
        # my_decorator() runs ONLY ONCE (when decorating)
        # # wrapper() runs EVERY TIME you call greet()
        
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper    
        
@my_decorator
def greet():
    print("Hello from Prapti to decorators !")
    
greet()
print(greet.__name__)    