import json
l=[]
class student:
    def __init__(self,name,age,degree,district):
        self.name=name
        self.age=age
        self.degree=degree
        self.district=district
        with open("/home/manikam/data.json","w")as js:
           global l
           dic=self.__dict__
           l.append(dic)
           json.dump(l,js)
    @staticmethod
    def dict():
       with open("/home/manikam/data.json","r")as js:
            list=json.load(js)
            nameslist=[]
            for i in list:
                # print (i)
                dict=i
                nameslist.append(dict["name"])
                nameslist.sort()
            for j in nameslist:
                print(j)
                
stud1=student("manic",21,"Bsc","tuty")
stud2=student("perumal",22,"Bcom","trichy")
stud3=student("hari",24,"Msc","kovilpatti")
stud1.dict()

