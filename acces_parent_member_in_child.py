class parent(object):
    def __int__(self,name):
        self.name=name
    

class child(parent):
    def __init__(self,name,age):
       # super(child,self).__init__(name)
        parent.name=name
        self.age=age
        
    def diplay(self):
        print("name=",parent.name)
        print("age=",self.age)
        
c1=child("Ramesha",29)
c1.display()