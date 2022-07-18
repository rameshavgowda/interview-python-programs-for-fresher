num = int(input("Enter the number:"))
sum=0
for i in range(1,num):
    if num%i == 0:
        sum +=i
print(sum)
if num==sum:
    print("no is perfect")
else:
    print("no is not perfect")
        