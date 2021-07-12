def FlipImage(image):
    for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[0])):
                if(image[i][j]==0):
                    image[i][j]=1
                else:
                    image[i][j]=0
    return image




rows = int(input("enter the number of rows"))
image = []
print("Enter the elements of the grid row wise")
for i in range(rows):
    row= list(map(int, input().split()))
    image.append(row)
print(FlipImage(image))
