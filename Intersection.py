def Intersection(nums1,nums2):
    a = set(nums1)
    b = set(nums2)
    arr =[]
    for num in a:
        if num in b:
            arr.append(num)
    return arr

nums1=[]
nums2=[]

n1 = int(input("Enter the size of first array"))
for i in range(n1):
    ele = int(input("enter element"))
    nums1.append(ele)
n2 = int(input("enter the size of the second array"))
for i in range(n2):
    ele = int(input("enter elements"))
    nums2.append(ele)

print(Intersection(nums1,nums2))
