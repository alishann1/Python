# i = len("Anaconda")
# print(i)
# i = len([1,2,3,4])
# print(i)


# def add (a,b,c=0):
#     return a + b + c
# print(add(3,4))
# print(add(3,4,6))
# print(add(3,4,8))

# class A:
#     def f(self, i = None):
#         if i == None:
#             print("Sequence 01")
#         else:
#             print("Sequence 02")
            

# class B(A):
#     def f(self, i= None):
#         if i == None:
#             print("Sequence 01 in child class")
#         else: 
#             print("Sequence 02 in the child")

# def main():
#     a = B()
#     a = A()
#     a.f()
#     a.f(3)
    
# if __name__ == "__main__":
#     main()    \
    
class Pet:
    def __init__(self, name1, age1):
        self.name1 = name1
        self.age1 = age1
    def __str__(self):
        return self.name1 + " " + str(self.age1)
class Dog(Pet):
    def __init__(self, name1, age1, breed1):
        super().__init__(name1, age1)
        self.breed1 = breed1
    def __str__(self):
        return super().__str__() + self.breed1
        
    def bark(self):
        print("bark bark")
        
class Cat(Pet):
    def purr(self):
        print("purr purr")
        
spotty = Dog("Spotty", 5 ," Golden Retriever")
cutie = Cat("Cutie ", 4)
print(spotty)
print(cutie)
# spotty.bark()
# cutie.purr()