l=[2,5,4,8,96,12,45,86]

for i in range(len(l)):
    for j in range(len(l)-1):
        if(l[i]<l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l[i])




