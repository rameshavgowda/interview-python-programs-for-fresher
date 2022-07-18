def create_queue():
    queue=[]
    return queue

def insert(queue,value):
    queue.append(value)
    return queue
def empty(queue):
    return len(queue)==0
def pop(queue):
    if empty(queue):
        print("queue is empty")
    else:
        print("popped element is:",queue.pop(0))
def display(queue):
    if empty(queue):
        print("queue is empty")
    else:
        print(queue)
    
queue =create_queue()

while True:
    print("enter 1 to insert an element:")
    print("enter 2 to pop an element:")
    print("enter 3 to display an element:")
    print("enter 4 to exit from queue:")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        value=int(input("Enter element to insert into queue:"))
        insert(queue,value)
    elif choice == 2:
        pop(queue)
    elif choice == 3:
        display(queue)
    elif choice== 4:
        break;
    else:
        print("Invalid input")
    
