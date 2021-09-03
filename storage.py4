def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
string="All is well"
finale=""
count=0
a=list(string.split(" "))
for i in a:
    temp=unique(str(i))
    for j in temp:
        count=0
        for k in i:
            if(j==k):
                count=count+1
        if(count!=1):
            finale=finale+str(j)+str(count)
        else:
            finale=finale+str(j)
            
print(finale)
