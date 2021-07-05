print("Enter the size of the array")
n= int(input())
nums=[]
print("enter the elements of the array")
for i in range(n):
    ele=int(input())
    nums.append(ele)
print("enter the element to delete")
val=int(input())

s=0
if(n==0):
    print(0)
for i in range(n):
    if(nums[i]!=val):
        nums[s] = nums[i]
        s+=1
print(s)
    
