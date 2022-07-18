def smart_divide(func):
    def inner(a, b):
        print("I am inside decoretor")
        print("I am going to divide", a, "with", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print("I am inside function")
    return (a/b)

a,b=4,0
print(divide(a,b))