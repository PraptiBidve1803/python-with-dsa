
def chai_orders(flavor):
    if flavor not in ["Masala","Elaichi"]:
        raise ValueError("Unsupported chai flavor")
    print(f"Brewing the {flavor} chai")

chai_orders("Masala")
chai_orders("Ginger")    
         
    