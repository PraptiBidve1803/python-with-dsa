staff=[("Amit",15),("Sonali",17),("Raj",18),("Sita",19)]
for name,age in staff:
    if age>=18:
        print(f"{name} you are eligible for the staff member")
        break
        
else:
    print("You are not eligible")        