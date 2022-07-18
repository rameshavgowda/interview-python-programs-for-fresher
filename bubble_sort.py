elements=[]
number=int(input("Enter the number of elements to insert into list:"))
for i in range(number):
    value=int(input("Enter the [%d] element :"%i))
    elements.append(value)
print(elements)
for i in range(number-1):
    for j in range(number-i-1):
        if elements[j]> elements[j+1]:
            temp = elements[j]
            elements[j] = elements[j+1]
            elements[j+1] = temp
            
print(elements)
            
