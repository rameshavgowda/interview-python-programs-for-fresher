num= int(input("enter the number:"))

count=0
temp=0
sum=0

temp= num
while temp>0 :
    count +=1
    temp //= 10
    
print(count)

temp=num
while temp>0:
    rem= temp%10
    sum +=(rem**count)
    temp //=10
 
print(sum)
if sum == num:
    print("the number {0} is amstrong number".format(num))
    
else:
    print("not a amstorng number")