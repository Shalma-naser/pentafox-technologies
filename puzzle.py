def findPairs(lst, i): 
    out = []
    while lst:
        num = lst.pop()
        diff = i - num
        if diff in lst:
            out.append((diff, num))
    if out == []:
        print("No Pairs found")
    return out
lst = list(map(int,input("\nEnter the list : ").strip().split()))
i = int(input("Enter the sum : "))
print(findPairs(lst, i))
