
class Out_of_ingredients_Error(Exception):
    pass
def chai_ingredirnts(milk,sugar):
    if milk==0 or sugar==0:
        raise Out_of_ingredients_Error("Missing milk or sugar")
    print("Chai is ready")
chai_ingredirnts(0,5) 
chai_ingredirnts(2,5)   
        