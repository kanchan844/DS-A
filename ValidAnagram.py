def isAnagram(s,t):
        if(sorted(s)==sorted(t)):
		return True
	else:
		return False
s=input("enter first string")
t=input("enter second string")
print(isAnagram(s,t))