l1=[3,6,8,2,7]
l2,l3=[],[]
for i in range(len(l1)):
    if l1[i]%2 !=0:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
print(l2)
print(l3)
    