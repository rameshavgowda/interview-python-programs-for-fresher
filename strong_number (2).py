num = int(input("Enter the number:"))
temp= num
sum =0
while temp >0 :
    fact=1
    i=1
    rem = temp%10
    while i <=rem:
        fact *=i
        i +=1
        
    print("the factorial of %d is: %d"%(rem,fact))
    sum +=fact
    temp //=10
    
print(" the sum of all the factorials is:",sum)

if num == sum:
    print("the number %d is strong number"%num)
else:
    print("the number %d is not strong number"%num) 