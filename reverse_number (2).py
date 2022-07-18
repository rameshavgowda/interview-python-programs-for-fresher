num = int(input("Enter the number:"))
print("the number is:",num)
rev=0
while num>0:
    rem = num%10
    rev = (rev*10) +rem
    num //=10
    
print("the reverse number is:",rev)