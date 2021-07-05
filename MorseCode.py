def uniqueMorse(words):
    morse_code =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    res =[]
    for word in words:
        morse =""
        for char in word:
            morse+=morse_code[ord(char)-97]
        if morse not in res:
            res.append(morse)
    return len(res)

words =[]
n = int(input("enter the length of the words"))
print("enter the elements")
for i in range(n):
    ele = input()
    words.append(ele)
print(uniqueMorse(words))
