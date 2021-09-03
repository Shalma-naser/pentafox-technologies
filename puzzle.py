def findPairs(lst, i): 
    res = []
    while lst:
        num = lst.pop()
        diff = i - num
        if diff in lst:
            res.append((diff, num))
    if res == []:
        print("No Pairs found")
    return res
lst = list(map(int,input("\nEnter the list : ").strip().split()))
i = int(input("Enter the sum : "))
print(findPairs(lst, i))
