

def order_process(item,quantity):
    try:
        price={"Masala":20}[item]
        cost=price*quantity
        print(f"Total cost is",cost)
    except KeyError:
        print("Sorry that chai is not in the menu")
    except TypeError:
        print("Quantity must be in number")

# order_process("Masala","two")
order_process("Ginger",20)                
    
    
    
    
    