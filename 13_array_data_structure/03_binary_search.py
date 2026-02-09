
# binary search


arr=[2,5,6,4,5,12,5,85,63]
arr.sort()
print(arr)
def binary_search(arr,i,j,x):
    while i<=j:
        mid=i+(j-i)//2   # No risk of overflow
        if arr[mid]==x:
            return mid
        elif x<arr[mid]:
            return binary_search(arr,i,mid-1,x)
        else: 
            x>mid
            return binary_search(arr,mid+1,j,x)
    return f"The index number of {x} is {arr.index(x)}"
        
result=binary_search(arr,0,len(arr)-1,12)   
print(result) 

"""
#arr = [2, 4, 5, 6]
len(arr) = 4
valid indexes = 0, 1, 2, 3
👉 arr[4] ❌ IndexError
***“Search from the first element to the last element”

"""

# Without recursion
def binary_search_without_recursion(arr,i,j,x):
    while i<=j:
        mid=i+(j-i)//2
        if x==arr[mid]:
            return f"The index number of {x} is {mid}"
        elif x>arr[mid]:
            i=mid+1
        else: 
            j=mid-1
    return f"The {x} number is not present"            

print(binary_search_without_recursion(arr,0,len(arr)-1,6))
print(binary_search_without_recursion(arr,0,len(arr)-1,89))
print(binary_search_without_recursion(arr,0,len(arr)-1,85))
