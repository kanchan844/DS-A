def luckyNumber(matrix):
    row ,col =[],[]
    for i in matrix:
        row.append(min(i))
    for j in zip(*matrix):
        col.append(max(j))
    for i in row:
        if i in col:
            return[i]



rows = int(input("enter the number of rows"))
matrix = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    matrix.append(row)
print(luckyNumber(matrix))
