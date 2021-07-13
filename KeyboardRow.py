def findWords(words):
    set1 = {'q','w','e','r','t','y','u','i','o','p'}
    set2 = {'a','s','d','f','g','h','j','k','l'}
    set3 = {'z','x','c','v','b','n','m'}
        
    res = []
    for i in words:
        wordset = set(i.lower())
        if (wordset&set1 == wordset) or (wordset&set2 == wordset) or (wordset&set3 == wordset):
            res.append(i)
    return res
n= int(input("enter length of array string"))
words=[]
print("enter elements")
for i in range(n):
    ele=input()
    words.append(ele)
print(findWords(words))
        
