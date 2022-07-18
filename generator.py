def my_gen():
    
    n=1
    print("first time print")
    yield n
    
    n +=1
    print("second time print")
    yield n
    
    n +=1
    print("thired time print")
    yield n
    
a=my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))