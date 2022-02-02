class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def fun(self):
        print(self.__dict__)

a=test("manic",21)
b=test("aswin",21)

a.fun()
b.fun()


# output:

# {'name': 'manic', 'age': 21}
# {'name': 'aswin', 'age': 21}