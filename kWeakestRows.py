def kWeakestRows(mat,k):
        temp =[]
        for i , m in enumerate(mat):
            cand = (sum(m),i)
            temp.append(cand)
        temp.sort()
        return [i[1] for i in temp[:k]]





rows = int(input("enter the number of rows"))
mat = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    mat.append(row)
print("enter the value of k")
k = int(input())
print(kWeakestRows(mat,k))
