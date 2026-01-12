
users=[
    
    {"id":1,"total":100,"coupon":"P10"},
    {"id":2,"total":150,"coupon":"F20"},
    {"id":3,"total":200,"coupon":"D30"}
    
     ]

discounts = {
    "P10" : [0.2 , 0],
    "F20" : [0.5 , 0],
    "D30" : [0 , 30],
    "E60" : [0,10]
} 

for user in users :
    percent,fixed = discounts.get(user["coupon"],[0,0])
    discount= user["total"]*percent+fixed
    print(f" {user["id"]} paid Rs.{user['total']} and got discount of Rs.{discount} for the next order ")
    