import json


class student:
    

    def __init__(self, name, age, medium):
        
        self.name = name
        self.age = age
        self.medium = medium
        with open("/home/manikam/111.json","w")as js:
            j1=json.dumps(self.__dict__)
            js.write(j1)
    @staticmethod
    def dict():
      with open("/home/manikam/111.json","r")as f:
            dict=json.load(f)
            print(type(dict))
            print(dict)
            print(dict["name"])
   



obj=student("manic",21,"tamil")
obj.dict()


