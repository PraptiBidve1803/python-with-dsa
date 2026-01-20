""" comprehension are a concise way to create
lists,sets,dictionaries or generators in 
Python using a single line of code
  where are they used in real life ?
  filter item
  transform item  
  create a new collection
  flatten nested structure
  what purpose do they serve?
  cleaner code
  faster execution
  
  types of comprehensions
  List,set,dictionary,generators  
"""
# List Comprehension 
# Syntax: [expression for item in itearable if condition]

menu=["Ginger tea","cardmom tea","milk tea","Iced lemon tea",
      "Black tea","Iced peach tea"]
iced_tea=[tea for tea in menu if "Iced" in tea]
print(iced_tea)