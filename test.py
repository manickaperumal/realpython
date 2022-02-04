import json
l=[]
class student:
    def __init__(self,name,age,degree,district):
        self.name=name
        self.age=age
        self.degree=degree
        self.district=district
        with open("/home/manikam/888.json","w")as js:
           global l
           dic=self.__dict__
           l.append(dic)
           json.dump(l,js)



            
stud1=student("manic",21,"Bsc","tuty")
stud2=student("perumal",22,"Bcom","trichy")
stud3=student("hari",24,"Msc","kovilpatti")