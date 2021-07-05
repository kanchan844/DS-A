def decompress(nums):
    x =[]
    i=1
    while(i<len(nums)):
        j =i-1
        for j in range(0,nums[j]):
            x.append(nums[i])
        i =i+2
    return x
n = int(input("enter the size of the array"))
nums =[]
for i in range(n):
    ele=int(input("enter the elements"))
    nums.append(ele)

print(decompress(nums))
