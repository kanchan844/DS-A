def Count(nums):
    n = len(nums)
    l =[]
    for i in range(n):
        c =0
        for j in range(n):
            if(nums[i]>nums[j] and i!=j):
                c = c+1
        l.append(c)
    return l

n = int(input("enter the size"))
nums =[]
for i in range(n):
    ele = int(input("enter the elements"))
    nums.append(ele)

print(Count(nums))
