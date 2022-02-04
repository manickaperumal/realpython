import json
l=[]
class student:
    def __init__(self,name,age,degree,district):
        self.name=name
        self.age=age
        self.degree=degree                         #for to store a object specific information
        self.district=district
        with open("/home/manikam/data.json","w")as js:
           global l
           dic=self.__dict__                       
           l.append(dic)                           #all object details will be stored in a list called 'l'(list name)
           json.dump(l,js)                         #list convert into json file 
                                         

    @staticmethod
    def namesorder():
        nameslist=[]                                #to store a names in nameslist
        for i in global_list:
        # print (i)
            dict=i
            nameslist.append(dict["name"])
            nameslist.sort()
        for j in nameslist:
          print(j)
    @staticmethod            
    def ageorder():
        
        age=[]
        for i in global_list:
            dict=i
           
            age.append(dict["age"])
            age.sort(reverse=True)
        for j in age:    
          print(j,end=" ")



    
                
stud1=student("manic",21,"Bsc","tuty")
stud2=student("perumal",22,"Bcom","trichy")
stud3=student("hari",24,"Msc","kovilpatti")
with open("/home/manikam/data.json","r")as js:   
    global_list=[]
    global_list=json.load(js)   
    # print(global_list)                    #create a global to be used by any function     

stud1.namesorder()
stud1.ageorder()

