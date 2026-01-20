
# Dictionary : {expression for item in iterable if condition}
#                  |-- key:value 
chai_prices_inr={
    "Masala_chai":50,
    "Ginger_chai":70,
    "Elaichi_chai":80
}

chai_prices_usd={ tea:price/80 for tea,price in chai_prices_inr.items()}

print(chai_prices_usd)