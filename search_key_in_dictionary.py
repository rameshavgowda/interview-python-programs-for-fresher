
mydict={'name':'Ramesha','age':'29','place':'Bangalore'}

print(mydict)

key=input("Enter the key to search:")
if key in mydict.keys():
    print("key :",key,"and value:",mydict[key])
else:
    print("key does not exist")