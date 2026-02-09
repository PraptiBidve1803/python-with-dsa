# Implementation of the ternary search

arr=[2,8,9,56,78,99,100,101,102]
l=0
r=len(arr)-1

def ternary_search(arr,l,r,x):
    while(l<=r):
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if x==arr[mid1]:
            return mid1
        elif x==arr[mid2]:
            return mid2
        elif x<arr[mid1]:
            return ternary_search(arr,l,mid1-1,x)
        elif x>arr[mid2]:
            return ternary_search(arr,mid2+1,r,x)
        else:
            return ternary_search(arr,mid1+1,mid2-1,x)
    return f"{x} is not present in the given array"
result1=ternary_search(arr,l,r,34)    
print(result1)   
result2=ternary_search(arr,l,r,100)    
print(f"100 is prsent at index {result2}")  