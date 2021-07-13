def shortestToChar(s,c):
        N = len(s)
        left,right,output = [None]*N , [None]*N , [None]*N
        temp = float("inf")
        for i in range(N):
            if(s[i]==c):
                temp =0
            left[i]=temp
            temp+=1
        for i in range(N-1,-1,-1):
            if(s[i]==c):
                temp =0
            right[i] = temp
            temp+=1
        for i in range(N):
            output[i] = min(right[i],left[i])
        return output
s = input("enter the string")
c =input("enter the character")
print(shortestToChar(s,c))
