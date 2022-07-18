ch=input("Enter the string:")
ch1=''
for i in range(len(ch)):
    if(ch[i] >= 'a' and ch[i] <='z'):
        ch1 += chr(ord(ch[i])-32)
    else:
        ch1 += ch[i]
    
print(ch)
print("using inbuilt function :",ch.upper())
print(ch1)