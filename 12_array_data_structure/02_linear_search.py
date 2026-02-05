
# linear search 
num=[2,6,8,5,9,4]
def linear_search(num,x):
    for i in range(len(num)):
        if num[i]==x:
            return f"The searching element {x} having index {i}"
    return f"Number {x} is not present in the given array"

result=linear_search(num,9)
print(result)    
print(linear_search(num,18))