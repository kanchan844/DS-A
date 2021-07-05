def GoodPairs(nums):
    len1 = len(nums)
    count =0
    for i in range(len1):
        for j in range(i+1,len1):
            if(nums[i]==nums[j]):
                count+=1
    return count

n = int(input("enter the size"))
nums =[]
for i in range(n):
    ele = int(input("enter the elements"))
    nums.append(ele)

print(GoodPairs(nums))
        
