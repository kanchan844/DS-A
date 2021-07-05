def subsetXORSum(nums):
    ans =0
    for i in range(2**len(nums)):
        temp =[]
        for j in range(len(nums)):
            if i&1<<j>0:
                temp.append(nums[j])
        s =0
        for i in temp:
            s^=i
        ans+=s
    return ans
n = int(input("enter the size of the array"))
nums =[]
for i in range(n):
    ele=int(input("enter the elements"))
    nums.append(ele)

print(subsetXORSum(nums))
