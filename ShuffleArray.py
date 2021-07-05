print("Enter the size of the array")
x= int(input())
nums=[]
print("enter the elements of the array")
for i in range(x):
    ele=int(input())
    nums.append(ele)
n=x//2
l=[]
for i in range(n):
    l.append(nums[i])
    l.append(nums[i+n])
    
print(l)
