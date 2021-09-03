alpha="abcdefghijklmnopqrstuvwxyz"
list=[]
list=list(map(int,input().split(",")))
output = []
for i in list:
    a = alpha[i-1]
    output.append(a)
print(*output)
