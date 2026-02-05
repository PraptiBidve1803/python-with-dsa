#Analysis of algorithm by time and space complexity

# e.g Sum of n natural numbers

lst=[1,2,3,4,5]

def sum_of_n_numbers(lst):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    return total


result=sum_of_n_numbers(lst)
print("The sum of first 5 natural numbers is:",result)   

# Using formula sum=n(n+1)/2
def sum_of_n_natural_no(lst):
    n=len(lst)
    sum=n*(n+1)/2
    return sum  
result2=sum_of_n_natural_no(lst)
print("The sum of 1st 5 natural numbers is:",result2)