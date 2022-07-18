ch=input("Enter the string:")
sc=input("Enter the search char:")

flag=0

for i in range(len(ch)):
    if ch[i] == sc :
        flag=1
        break;
    
if(flag == 0):
    print("search not found")
else:
    print("the search char {0} is found at position {1}".format(sc,i+1))
