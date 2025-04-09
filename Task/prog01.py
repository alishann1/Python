class Student: 
    def __init__(self): 
        print("Student instance created")
        
    def show(self,x,y):
        print(x,y)
s1 = Student()
s1.x = 10
s1.y = 20
s1.show(s1.x,s1.y)