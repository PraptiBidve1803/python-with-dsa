
class Invalid_chai_Error(Exception):pass

def bill(flavor,cups):
    menu={"Masala":20,
          "Ginger":90}
    try:
        if flavor not in menu:     #Python checks ONLY the KEYS, not the values.
            raise ValueError("that chai is not available")
        if not isinstance(cups,int):  #“If cups is NOT an integer, raise an error”
            raise TypeError("The value of the cup must be in integer")
        total=menu[flavor]*cups
        print(f"Your bill for the {cups} cups of {flavor} flavor is Rs.{total}")
    except Exception as e: #Catch ANY error that happens inside try block” ,e:It stores the error message
        print(f"Error",e)
    finally:
        print("Thank you for visiting..") 
           
""" 
First value → goes into flavor
Second value → goes into cups
Python matches values by position, not by name.
"""           
bill("Elaichi",4)   
bill("Ginger","three")
bill("Masala",5)           