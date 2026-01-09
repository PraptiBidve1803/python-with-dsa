
#Boolean

is_boiling=True  #upcasting
total_stir=4
total_actions=is_boiling+total_stir
print(f"total_actions needed {total_actions}")

tea_ready=0
print(f"tea is ready ? : {bool(tea_ready)}")


water_hot=1
tea_added=1
milk_added = False
teaIS_ready= water_hot and tea_added
print(f"tea is ready ?: {teaIS_ready}")

milk_tea=water_hot and tea_added or milk_added
print(f"milk tea is ready ? : {bool(milk_tea)}")

