
def chai_flavor(flavor="masala"):
    """It returns the flavor of the chai.
    It is the docstring"""
    
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)


def generate_bill(samosa=0,chai=0):
    """This function returns the total bill of the samosa and chai.
    Samosa-Each samosa having the price Rs.15
    Chai-Having price Rs.10
    Then it returns the total bill and Thank You msg
    """
    Total=samosa*15+chai*10
    return Total , "Thank you !"

print(generate_bill(samosa=5,chai=5))
