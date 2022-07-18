ch=input("Enter the string:")

ch1= ch
print(ch1)

ch2= ch[0:6]
print(ch2)

ch3=''
for i in range(len(ch)):
    ch3 += ch[i]
    
print(ch3)