def KidWithCandies(candies , extracandies):
    curr_max = max(candies)
    result =[]
    for candy in candies:
        if candy +extracandies >= curr_max:
            result.append(True)
        else:
            result.append(False)
    return result
candies =[]
n = int(input("enter the size of the array"))
for i in range(n):
    ele= int(input("enter the elements"))
    candies.append(ele)
extraCandies = int(input("enter extra candy"))
print(KidWithCandies(candies,extraCandies))
