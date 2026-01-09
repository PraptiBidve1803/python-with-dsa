# dictionary 

tea_order=dict(type="masala_chai",size="1cup",sugar="1tspoon")
print(f"tea order is {tea_order}")

chai_recipe={}
chai_recipe["base"]="black_tea"
chai_recipe["liquid"]="milk"
chai_recipe["flavour"]="ginger"
print(f"The chai recipe is {chai_recipe}")
print(f"chai recipe having a base is {chai_recipe["base"]}")
del chai_recipe["liquid"]
print(f"chai recipe is {chai_recipe}")
print(f"is sugar in tea order ? {"sugar" in tea_order}")
tea_order={"type": "ginger_chai","sugar" :1,"size" : "large"}
print(f"print the keys only : {tea_order.keys()}")
print(f"print the values only : {tea_order.values()}")
print(f"print the item: {tea_order.items()}")
last_item=tea_order.popitem()
print(tea_order)
extra_spices={"cardamom":"crushed","ginger":"slice"}
chai_recipe.update(extra_spices)
print(f"updated chai recipe is : {chai_recipe}")
customer_note= tea_order.get("size","no note")
print(f"customer note is : {customer_note}")





