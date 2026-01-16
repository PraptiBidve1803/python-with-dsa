
def chai_order():
    chai_type="ginger"
    
    def kitchen():
        nonlocal chai_type
        chai_type="tulsi"
    kitchen()
    print(f"The chai type after updating by the kitchen is : {chai_type}")    

chai_order()