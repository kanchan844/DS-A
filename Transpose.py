def Transpose(matrix):
    result =[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = result[i][j]
    return result
    

rows = int(input("enter the number of rows"))
matrix = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    matrix.append(row)
print(Transpose(matrix))
