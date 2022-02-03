import json
class student:
    def __init__(self,name,age,medium):
        self.name=name
        self.age=age
        self.medium=medium



    def a(self):
       store=self.__dict__
       json1=json.dumps(store)
       
       print(type(json1))
       return json1

    def b (self):
        print(self.age)


stud1=student("manic",21,"tamil")
print(stud1.a())
stud1.b()

output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/a.py
<class 'str'>
{"name": "manic", "age": 21, "medium": "tamil"}
21
manikam@manikam:~$ 


        
     











