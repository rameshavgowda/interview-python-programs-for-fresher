l=[3,6,8,2,7]
big =0
for i in range(len(l)):
    for j in range(2,len(l)):
        if l[i] < l[j]:
            big = l[j]
print(big)
    