
#sets
outside_Sports={"Cricket","Football","kabbadi","Volyball","table_tennis"}
inside_Sports={"Chess","Caram","snake_ladder","table_tenis"}

#union of sets
all_Sports=outside_Sports | inside_Sports
print(f"All sports are: {all_Sports}")

outside_sports_Only=outside_Sports-inside_Sports

print(f"Only outside sports are : {outside_sports_Only}")

common_Sports=outside_Sports & inside_Sports
print(f"common sports are:{common_Sports}")

