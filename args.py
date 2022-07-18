def multiply(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul
print(multiply(1,2,3,4,5))
