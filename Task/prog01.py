class Student:
    #     def __init__(self):
    #         print("Student instance created")

    #     def show(self,x,y):
    #         print(x,y)
    # s1 = Student()
    # s1.x = 10
    # s1.y = 20
    # s1.show(s1.x,s1.y)

    # semester = "2nd"
    # descipline = "BSCS"

    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def show(self):
        print(self.name, self.reg_no)


s1 = Student("Nawaz", "2020-2021-00001")
s2 = Student("Ahmed", "2020-2021-00002")
s1.show()
s2.show()
