# Matrix Vector Dot Product
def matrix_vector_dot_product(matrix,vector):
    if not matrix or not vector:
        return -1

    rows=len(matrix)
    cols=len(matrix[0])
    vector_len=len(vector)

    for row in matrix:
        if len(row)!=cols:
            return -1
    
    if cols!=vector_len:
        return -1
    
    result=[]
    for i in range(rows):
        row_sum=0
        for j in range(cols):
            row_sum+=matrix[i][j]*vector[j]
        result.append(row_sum)

    return result

if __name__=="__main__":
    a=[[1,2],[2,4]]
    b=[1,2]
    print("Matrix : ",a)
    print("Vector : ",b)

    result1=matrix_vector_dot_product(a,b)
    print(result1)