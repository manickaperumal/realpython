import json


class student:
    

    def __init__(self, name, age, medium):
        
        self.name = name
        self.age = age
        self.medium = medium
        with open("/home/manikam/data.json","a")as js:
          js.write(self.__dict__)

    def a(self):
        store = self.__dict__
        json1 = json.dumps(store)
        print(type(json1))
        return json1

    def b(self):
        print(self.age)

    def c(self):
        store = stud1.__dict__
        json1 = json.dumps(store, sort_keys=True)
        return json1
with open("/home/manikam/data.json","w"):


    stud1 = student("manic", 21, "tamil")
    print(stud1.a())
    stud1.b()
    json1 = stud1.c()
    print(json1)
    print(json1)