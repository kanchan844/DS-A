def mostCommonWord(paragraph,banned):
    paragraph = paragraph.lower()
    for i in "!'.?,:;-":
        paragraph = paragraph.replace(i,' ')
    paragraph=paragraph.split()
    dict={}
    for word in set(paragraph):
        if word not in banned:
            dict[word] = paragraph.count(word)
    m = max(dict.values())
    for key in dict:
        if(dict[key]==m):
            return(key)
paragraph = input()
banned = input()
print(mostCommonWord(paragraph,banned))

        
