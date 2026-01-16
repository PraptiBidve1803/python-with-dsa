
fruit_type="Mango"   #global scope 

def order_fruit():
    
    def update_order():
        global fruit_type
        fruit_type="Orange"
        
    update_order()


order_fruit()
print(f"Order the fruit : {fruit_type}")    
        