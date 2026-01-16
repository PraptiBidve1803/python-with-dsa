def add_vat(price,vat_rate):
    return price+(price*(vat_rate/100))

order=[100,150,200]
for price in order :
    final_price=add_vat(price,10)
    print(f"The original_price is {price} and the final price with vat is {final_price}")    