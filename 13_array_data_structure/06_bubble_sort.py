
# Bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                # swap of the elements
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[2,50,89,69,45,63,21]
result=bubble_sort(arr)
print(result)            
