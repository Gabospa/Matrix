
import random


matrix = [ [1,0,0],[0,1,1],[1,1,0]]

def shoot(x, y):
    
    if check_range(x,y):

        if matrix [x][y] == 0:
            print ('Tiro con suerte')
        
        else:
            print ('BOOOM!!!!')
    else:
        print ('Caiste Fuera!')

def check_range(x,y):
    if x > 2 or y > 2:
        return False
    else:
        return True


if __name__ == '__main__':

    x = int(input('Seleciona valor X de 0 a 2: '))
    y = int(input('Seleciona valor Y de 0 a 2: '))
    shoot(x,y)
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])