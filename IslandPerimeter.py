def Island(grid):
    island = set((i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==1)
    perimeter =0
    for i,j in island:
        if((i-1,j) not in island):
            perimeter+=1
        if((i+1,j) not in island):
            perimeter+=1
        if((i,j-1) not in island):
            perimeter+=1
        if((i,j+1) not in island):
            perimeter+=1
    return perimeter

rows = int(input("enter the number of rows"))
grid = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    grid.append(row)
print(Island(grid))
