input1="rajesh"
input2="ganesh"
output=[]
for i in input1:
    if(i in input2):
        pass
    else:
        output.append(i)

for i in input2:
    if(i in input1):
        pass
    else:
        output.append(i)
print(*output)
