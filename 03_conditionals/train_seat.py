train_seat_type=input("Enter the seat type (sleeper/AC/general/luxury) : ").lower()

match train_seat_type:
    case "sleeper":
        print(f"Your seat type is {train_seat_type} - No AC,beds avialable ")
    case "ac":
        print(f"Your seat type is {train_seat_type} - Air conditioned , comfy ride ")
    case "general":
        print(f"Your seat type is {train_seat_type} - Cheapest option , no reservation ")
    case "luxury":
        print(f"Your seat type is {train_seat_type} - Premium seats with meals ")    
    case _:
        print("Invalid seat type")            
