from collections import deque
def shift2DGrid(grid,k):
    dq = deque()
    for g in grid:
        for a in g:
            dq.append(a)
    for _ in range(k):
        dq.appendleft(dq.pop())
    for g in grid:
        for i in range(len(g)):
            g[i] = dq.popleft()
    return grid

rows = int(input("enter the number of rows"))
grid = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    grid.append(row)
print("How many times you want to move the grid")
k = int(input())
print(shift2DGrid(grid,k))
