# Array ===> list in python
# Random access
array=[20,56,1,2,3,45,20,88,5,6]
print(array[7]) #passing the index inside the array
print(len(array))  #printing the length of the array

# search for an element 56 and return its index ,if not present then return -1

def linear_search(array,x):
    for i in range(len(array)):
        if array[i]==x:
            return i
    return -1
print(linear_search(array,56))  
print(linear_search(array,5))   
print(linear_search(array,6))
print(linear_search(array,78))  
# insert an element into the array
array.insert(3,45)
print(array)
print(len(array))

# remove the element from the array
num=[2,5,9,6,4,5]
num.remove(9)
print(num)
# count the number of the times an element present in the array
print(num.count(5))

# delete the particuler element from the array
num_1=[5,56,14,11,23]
num_1.pop(1)
print(num_1)

# sorting the element by the increasing order
num_1.sort()
print(num_1)

# extract the elementfrom array
print(num_1.index(23))

#extend the original array
print(num_1.extend([5,89,7,4,32,15]))
print(num_1)

# reverse the array
num_1.reverse()
print(num_1) 





# ****Practice******

number=[4,8,9,3,4,5,6]
print(number[2])

def linear_search(number,y):
    for i in range(len(number)):
        if number[i]==y:
            return f"The {y} is present at position {i}"
    return "Number is not present" 
print(linear_search(number,9))  
print(linear_search(number,18)) 
# remember at function insert(index,element) is used
number.insert(2,18) 
print(number)
number.remove(5)
print(number)
print(number.count(4))
print(number.count(5))
print(len(number))
print(number.pop(1)) #it takes the index 
print(number)
number.sort()
print(number)

print(number.index(4))
print(number)
number.extend([7,8,2,36,18])
print(number)

number.reverse()
print(number)


