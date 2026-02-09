"""  
try = “Try to run this code”
except = “If an error happens, handle it”
"""



def serve_chai(flavor):
    try:
        print(f"Preparing flavor chai....")
        if flavor=="Unknown":
            raise ValueError("we don't know that flavor ")
    except ValueError as e:
        print("Error",e)
    else:
        print(f"Served {flavor} chai")
    finally:
        print("Next customer please")
serve_chai("Masala")  
serve_chai("Unknown") 
             
            