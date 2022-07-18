num= int(input("Enter the number:"))
fact =1
for i in range(1,num+1):
    fact *= i
    
print("factorial of {0} is : {1} ".format(num,fact))
