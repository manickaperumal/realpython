class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def fun(obj):
        print(obj.__dict__)

a=test("manic",21)
b=test("aswin",21)

a.fun(a)
b.fun(b)


# output:

# {'name': 'manic', 'age': 21}
# {'name': 'aswin', 'age': 21}