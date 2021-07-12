def reverseVowels(s):
    vowls = {'a', 'e', 'i', 'o', 'u'}
    s = list(s)
    slow, fast = 0, len(s)-1
    while slow < fast:
        if s[slow].lower() in vowls:
            while not s[fast].lower() in vowls:
                fast -= 1 
                if fast < slow:
                    return ''.join(s)
            s[slow], s[fast] = s[fast], s[slow]
            fast -= 1
        slow += 1
    return ''.join(s)

str = input("enter the string")
print(reverseVowels(str))
