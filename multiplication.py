
matrix_A = [ [2,0], [3,0]]
matrix_B = [ [1,0], [1,2]]

rows_A = len(matrix_A)
columns_A = len(matrix_A[0])
rows_B = len (matrix_B)
columns_B = len(matrix_B[0])

print(f' m: {rows_A}')
print(f' n: {columns_A}')
print(f' r: {columns_B}')


matrix_C = [[0 for row in range(rows_A)] for columns in range(columns_B)]
print(matrix_C)

if __name__ == '__main__':

    aux = 0
    if columns_A == rows_B:
        for i in range(columns_B):
            for j in range(rows_A):
                for k in range(columns_A):
                    matrix_C[i][j] += (matrix_A[i][k] * matrix_B[k][j])
            
        print(matrix_C)        
         
    else:
        print('No se puede muliplicar')