a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))

if a>b:
    maxval=a
else:
    maxval=b
    
while(True):
    if(maxval % a == 0 and maxval%b == 0):
        print("the LCM of %d and %d is : %d" %(a,b,maxval))
        break
    maxval += 1