#List

stationary=["pencil","pen","eraser","scale"]
print(f"The stationary is {stationary}")

stationary.append("set_squares")
print(f"The stationary is {stationary}")

stationary.remove("pen")
print(f"The stationary is {stationary}")

stationary.sort()
print(f"The stationary is {stationary}")
stationary.insert(2,"sharpner")
print(f"The stationary is {stationary}")

fruits=["Mango","Apple","Bananna","Orange"]
vegetables=["Lady_finger","Spinach","Cabbage","Pumpkin"]
fruits.extend(vegetables)
print(f"The fruits and vegetables are{fruits}")

Sugar_level=[1,8,5,3,4]
print(f"Maximum sugar level is {max(Sugar_level)}")
print(f"Minimum sugar level is {min(Sugar_level)}")
new_sugarLevel=Sugar_level.pop()
print(f"Sugar levels are {Sugar_level}")
Sugar_level.reverse()
print(Sugar_level)

drink=["milk","Water"]
spices=["Cardamom","Ginger"]
mix_spice=drink+spices
print(f"The mix spices drink is {mix_spice}")

# operator overloading
strong_brew=["black_tea","ginger"]*3
print(strong_brew)

#bytearray
raw_spice_data=bytearray(b"cinnamon")
raw_spice_data=raw_spice_data.replace(b"cinna",b"carda")
print(raw_spice_data)
