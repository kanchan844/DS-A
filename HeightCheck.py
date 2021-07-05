def HeightChecker(heights):
    expected = sorted(heights)
    count =0
    for i in range(len(heights)):
        if(heights[i]!= expected[i]):
            count+=1
    return count
n1 = int(input("enter the size of the array heights"))
heights =[]
for i in range(n1):
    ele=int(input("enter the elements"))
    heights.append(ele)


print(HeightChecker(heights))
