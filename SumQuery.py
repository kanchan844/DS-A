def RangeSum(nums,left,right):
    n=len(nums)
    for i in range(1,n):
        nums[i] = nums[i-1] +nums[i]
    if(left == 0):
        return(nums[right])
    else:
        return(nums[right]-nums[left-1])
n = int(input("enter the size of the array "))
nums =[]
for i in range(n):
    ele=int(input("enter the elements"))
    nums.append(ele)
left=int(input("enter integer left"))
right=int(input("enter right"))
print(RangeSum(nums,left,right))
