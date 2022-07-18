num= int(input("Enter the number:"))

print("the factors of {0} is given below:".format(num))

for i in range(1,num+1):
    if num%i == 0:
        print(i)