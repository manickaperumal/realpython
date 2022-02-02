class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def fun(self):
        print(self.__dict__)

    def __str__(self):
      return self

a=test("manic",21)
b=test("aswin",21)
print(a)



