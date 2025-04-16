# i = len("Anaconda")
# print(i)
# i = len([1,2,3,4])
# print(i)


# def add (a,b,c=0):
#     return a + b + c
# print(add(3,4))
# print(add(3,4,6))
# print(add(3,4,8))

class A:
    def f(self, i = None):
        if i == None:
            print("Sequence 01")
        else:
            print("Sequence 02")
            

def main():
    a = A()
    a.f()
    a.f(3)
    
if __name__ == "__main__":
    main()    
    
