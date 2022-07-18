
mydict={'name':'Ramesha','age':'29','place':'Bangalore'}

print(mydict)

key=input("Enter the key to delete:")
if key in mydict:
    print("deleted key :",key,"and value:",mydict[key])
    del mydict[key]
    print("updated dictionery is:",mydict)
else:
    print("key does not exist")