class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_info(self):
        print({self.name, self.age, self.employee_id})


e = Employee("Ali", 19, 101)
e.show_info()
