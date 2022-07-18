l=[3,6,8,2,7]
even_sum =0
odd_sum =0
for i in range(len(l)):
    if l[i]%2 == 0:
        even_sum += l[i]
    else:
        odd_sum += l[i]
print("even sum:",even_sum)
print("odd sum:",odd_sum)
    
    