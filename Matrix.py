from random import randint
m, n = 5, 5

Matrix = [[randint(-10, 10) for j in range(n)] for i in range(m)]
for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        print(Matrix[i][j], end=' ')
    print()
Matrix = [[0 if i<j else Matrix[i][j] for j in range(n)] for i in range(m)]
for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        print(Matrix[i][j], end=' ')
    print()





