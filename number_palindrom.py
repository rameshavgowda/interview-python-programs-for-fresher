num = int(input("Enter the number:"))
rev=0
temp=num

while temp>0:
    rem = temp%10
    rev = (rev*10) + rem
    temp = temp//10
    
print("reverse number is :",rev)

if(num == rev):
    print(" no is palindrome")
else:
    print("no is not palindrome")