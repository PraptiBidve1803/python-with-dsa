
# static method
class ChaiUtils:
    @staticmethod   # @staticmethod is used when a method does NOT need object data (self) and acts as a helper function.
    def clean_ingredients(text):
        return[item.strip() for item in text.split(",")]  #strip() does:Removes extra spaces From left and right side


raw= "  Water,  milk  , ginger, honey"   
cleaned=ChaiUtils.clean_ingredients(raw)
print(cleaned)     
    
