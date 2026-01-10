device_status= input("Enter the status of the device(active/offline) : ").lower()
temperature=int(input("Enter the temperature : "))

if device_status== "active":
    if temperature>35:
        print("High temperature alert!")
    else:
        print("Normal temperature")
else:
    print("The device is offline")            

