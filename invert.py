

def get_determinant(A):
    if len(A) == 2:
        det = (A[0][0]*A[1][1])-(A[0][1]*A[1][0])
    
    if len(A) == 3:
        det = ((A[0][0]*A[1][1]*A[2][2])+(A[1][0]*A[2][1]*A[0][2])+(A[2][0]*A[0][1]*A[1][2])
        -(A[0][2]*A[1][1]*A[2][0])-(A[1][2]*A[2][1]*A[0][0])-(A[2][2]*A[0][1]*A[1][0]))
    return det


def get_inverse(A):
    if len(A) == 2:
        inv_A = [[A[1][1]/(get_determinant(A)),-1*A[0][1]/(get_determinant(A))],
        [-1*A[1][0]/(get_determinant(A)),A[0][0]/(get_determinant(A))]]
    
    if len(A) == 3:
        inv_A = [[((A[1][1]*A[2][2])-(A[1][2]*A[2][1]))/get_determinant(A), ((A[0][2]*A[2][1])-(A[0][1]*A[2][2]))/get_determinant(A), ((A[0][1]*A[1][2])-(A[0][2]*A[1][1]))/get_determinant(A)],
        [((A[1][2]*A[2][0])-(A[1][0]*A[2][2]))/get_determinant(A), ((A[0][0]*A[2][2])-(A[0][2]*A[2][0]))/get_determinant(A), ((A[0][2]*A[1][0])-(A[0][0]*A[1][2]))/get_determinant(A)],
        [((A[1][0]*A[2][1])-(A[1][1]*A[2][0]))/get_determinant(A), ((A[0][1]*A[2][0])-(A[0][0]*A[2][1]))/get_determinant(A), ((A[0][0]*A[1][1])-(A[0][1]*A[1][0]))/get_determinant(A)]]
    
    return inv_A


def transpose(A):
    return [list(i) for i in zip(*A)]


def get_complement(A):
    i= len(A)
    return [row[:i]+row[i+1:] for row in (A[:i]+A[i+1:])]

def build_matrix (num):
    if num == 2 or num == 3:
        A = [[0 for row in range(num)] for columns in range(num)]
        for i in range(num):
            for j in range(num):
                A[i][j] = int(input('Enter matrix 2x2 or 3x3 numbers: '))
    else:
        print ('Select a valid number')

    return A


if __name__ == '__main__':
    matrix_size = int(input('Select matrix size between 2 or 3: '))
    matrix_A = build_matrix(matrix_size)
    print(matrix_A)
    # print(transpose(matrix_A))
    print(get_determinant(matrix_A))
    print(get_inverse(matrix_A))
    # print(get_complement(matrix_A))