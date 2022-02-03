import json


class student:
    

    def __init__(self, name, age, medium):
        
        self.name = name
        self.age = age
        self.medium = medium
        with open("/home/manikam/111.json","a")as js:
         py=self.__dict__
         x= json.dumps(py)
         js.write(x)

    def a(self):
        with open("/home/manikam/111.json","r")as just:
            store=just.read()
            return store

obj=student("manic",21,"tamil")
obj1=student("aswin",22,"tamil")
obj2=student("perumal",22,"english")



