def SumMax(nums):
    nums = sorted(nums)
    s=0
    for i in range(0,len(nums),2):
        s+=nums[i]
    return s
n = int(input("enter the size of the array"))
nums =[]
for i in range(n):
    ele=int(input("enter the elements"))
    nums.append(ele)
print(SumMax(nums))
