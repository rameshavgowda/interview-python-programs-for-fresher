num = int(input("Enter the number:"))
print("the number is:",num)
sum=0
while num>0:
    rem = num%10
    sum += rem
    num //=10
    
print("the sum of all digites is:",sum)