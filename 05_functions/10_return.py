# def shop_glossary():
#     return "I shop for the glossary"

# shopping=shop_glossary()
# print(shopping)

def make_chai():
    print("I making the tea")
    
chai=make_chai()
print(chai)    #implicitaly return as none

def tea_seller():
    return 120    #one value
total=tea_seller()
print(total)


def chai_status(cups_left):   #early from a function
    if cups_left==0:
        return "Sorry,the chai is over"
    return "Chai is ready" 
    
print(chai_status(0))

print(chai_status(15))    


def chai_report():
    return 101,20,30    #multiple values

sold,remaining,unpaid=chai_report()
print("sold : ",sold)
print("remaining :",remaining)      