from random import randint
rows = int(input('Введите кол-во рядов матрицы: '))
cols = int(input('Введите кол-во столбцов матрицы: '))
res1=0
res2=[0]*rows
matrix=[[randint(1,99) for _ in range (rows)] for _ in range (cols )]
for i in range (cols):

    for j in range (rows):
        res1=res1+matrix[i][j]
        print('{:>5}'.format(matrix[i][j]), end=' ')
        res2[j]=res2[j]+matrix[i][j]
    print('{:>7}'.format(res1))
    res1=0
for j in range (rows):

    print(' ',res2[j], end=' ')

