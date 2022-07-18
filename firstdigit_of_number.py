a = int(input("Enter the number of a:"))
b = int(input("Enter the number of b:"))

i=1

while i <= a and i<=b:
    if a%i == 0 and b%i == 0:
        val= i
    i+=1
print("GCD of number {0} and {1} is : {2}".format(a,b,val))