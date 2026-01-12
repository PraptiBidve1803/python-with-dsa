#zip : iterate over a several iterables in parallel,producing a tupes with an item from each one

names=["Prapti","Abhi","Akki","Raj"]
bill=[50,70,82,96]

for name,amount in zip(names,bill):
    print(f"{name} paid Rs.{amount}")