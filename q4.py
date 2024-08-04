def transpose(A):
    rows=len(A)
    cols=len(A[0])

    transpose_matrix=[[0 for _ in range (rows)] for _ in range (cols) ]

    for i in range(rows):
        for j in range(cols):
            transpose_matrix[j][i] = A[i][j]

    return transpose_matrix

A=[
    [1,4,6],
    [9,6,2],
    [5,2,6]
]

transpose_matrix = transpose(A)
print("the transposed matrix is:")
for row in transpose_matrix:
 print(row)

