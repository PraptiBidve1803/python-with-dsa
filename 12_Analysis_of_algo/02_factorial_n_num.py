#factorial of n numbers :
"""
n=5     5!=5*4*3*2*1
while(n>0)
fact(n)=n*(n-1)

"""

def fact_n_num(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return fact
print(fact_n_num(5))    


    
    
    
