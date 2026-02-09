
# fuction definition
def binary_searchSorted2D_Array(matrix_2D,target):
    # number of rows
    m=len(matrix_2D)
    if m==0:
        return False
    # No.of columns
    n=len(matrix_2D[0])
    left=0
    right=(m*n)-1
    while left<=right:
        mid=left+(right-left)//2
        mid_element=matrix_2D[mid//n][mid%n]
        if target==mid_element:
            return f"True : matrix_2D[{mid//n}][{mid%n}]={target}"
        elif target>mid_element:
            left=mid+1
        else:
            right=mid-1
    return False            
    
# function calling
matrix_2D = [[2,4,6,7],
             [9,11,13,15],
             [18,25,80,85]]
result= binary_searchSorted2D_Array(matrix_2D,25)
result_2= binary_searchSorted2D_Array(matrix_2D,90)
print(result)
print(result_2)
