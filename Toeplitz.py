def Toeplitz(matrix):
    row,col=len(matrix),len(matrix[0])
    for i in range(1,row):
        for j in range(1,col):
            if(matrix[i][j]!=matrix[i-1] [j-1]):
               return("False")
    return("True")

rows = int(input("enter the number of rows"))
matrix = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    matrix.append(row)
print(Toeplitz(matrix))
