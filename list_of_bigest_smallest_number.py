l1=[3,6,4,2,7,1]
small =0
big =0
compar = l1[0]
for i in range(1,len(l1)):
    if compar <= l1[i] :
        big= l1[i]
    if compar >= l1[i]:
        small = l1[i]
    
print("Bigest number:",big)
print("smallest number:",small)
    