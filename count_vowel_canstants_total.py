ch=input("Enter the string:")
st =set(ch)
for j in st:
    count =0
    for i in range(len(ch)):
        if (ch[i] == j):
            count += 1
            
    print(j,":",count)
