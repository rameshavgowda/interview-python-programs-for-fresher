ch=input("Enter the string:")
ch1 =''
for i in range(1,len(ch)+1):
    if (i %2 != 0):
        ch1 += ch[i-1]
print("original string:", ch)
print("odd numbered string:", ch1)