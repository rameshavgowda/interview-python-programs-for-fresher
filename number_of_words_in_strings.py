ch=input("Enter the string:")
count = 1
for i in range(len(ch)):
    if(ch[i] == ' ' or ch[i] == '\n' or ch[i] == '\t'):
        count += 1
        
print("the number of words are:",count)