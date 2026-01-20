favourite_chai=["Green tea","Lemon tea","Green tea","masala chai",
                "Elaichi chai"]

unique_chai={tea for tea in favourite_chai}
print(unique_chai)

recipes={
    "Elaichi chai":["Cardamom","milk"],
    "Masala chai":["Ginger","black pepper","cloves"],
    "Ginger chai":["Ginger","milk"]
    
}

unique_spices={ spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
