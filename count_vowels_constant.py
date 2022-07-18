ch=input("Enter the string:")
vowel =0
constant =0
count =0
for i in ch:
    count +=1
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel += 1
    else:
        constant +=1
        
print("total chars:",count)
print("vowels :",vowel)
print("constant :",constant)