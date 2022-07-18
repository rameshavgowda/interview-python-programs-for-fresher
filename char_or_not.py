ch=input("Enter the string:")

if (ch >='a' and ch <='z') or (ch >='A' and ch <='Z'):
    print("is a charrecter")
elif (ch >='0' and ch <='9'):
    print("is a digit")
else:
    print("special symbol")
    
    '''even we can use the isalpha() and isdigit() function as well'''