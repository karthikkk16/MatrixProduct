def MatrixProduct(arr,rows,columns,numberToMultiply):
    for i in range(rows):
        for j in range(columns):
            arr[i][j]= numberToMultiply * arr[i][j]

    return arr
rows=int(input("rows:"))
columns=int(input("columns:"))
numberToMultiply=int(input("num to multiply:"))
matrix=[]
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print(MatrixProduct(matrix,rows,columns,numberToMultiply))