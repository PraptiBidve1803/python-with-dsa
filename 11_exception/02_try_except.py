
# try-except in python
orders={"Masala":30,
        "Ginger":40}
try:
    orders={"Elaichi"}
except KeyError:
    print("The key that you trying to access is not exist")    
print("Hello chai coders")