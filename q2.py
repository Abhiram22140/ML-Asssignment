def mat_mult(A,B):
    
    if len(A[0])!=len(B):
        print("matrices arenot multipliable")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]    
              
    for i in range(len(A)):
      for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]+=A[i][k]*B[k][j]

    return result


A=[
    [2,3,4],
    [5,4,3]
]

B=[
    [1,5,6],
    [8,5,7],
    [5,12,3]
]

result=mat_mult(A,B)
print("the product is :",result)
                   
  