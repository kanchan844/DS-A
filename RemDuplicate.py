print("enter the size of the array")
n = int(input())
print("enter the elements of the array")
nums = list(map(int,input().strip().split()))[:n]
i=0
for j in range(1,n):
    if(nums[j] != nums[i]):
        nums[i+1] = nums[j]
        i+=1
print(i+1)
    
