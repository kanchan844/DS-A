def longestCommonPrefix(strs):
    cur = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < len(strs[i]) and j < len(cur):
            if cur[j] != strs[i][j]:
                break
            j += 1
        cur = cur[:j]
    return cur

strs=[]
print("Enter the length")
n=int(input())
print("enter the elements")
for i in range(n):
    ele =input()
    strs.append(ele)
print(longestCommonPrefix(strs))



''' strs = sorted(strs, key=len)  # sort the strings shorted to longest

        if not strs: 
            return '' 
        string1 = min(strs)  # get shortest string in list
        string2 = max(strs) # get longest string in list
        for i, c in enumerate(string1):
            if c != string2[i]:
                return string1[:i]
        return string1'''



        
