def create_stack():
    stack=[]
    return stack

def push(stack,value):
    stack.append(value)
    return stack
def empty(stack):
    return len(stack)==0
def pop(stack):
    if empty(stack):
        print("stack is empty")
    else:
        print("popped element is:",stack.pop())
def display(stack):
    print(stack)
    
stack =create_stack()

while True:
    print("enter 1 to push an element:")
    print("enter 2 to pop an element:")
    print("enter 3 to display an element:")
    print("enter 4 to exit from stack:")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        value=int(input("Enter element to insert into stack:"))
        push(stack,value)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        display(stack)
    else:
        break;
    
