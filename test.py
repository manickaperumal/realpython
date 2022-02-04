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

        
    def agelimit(self):
         nameslist=[]                                #to store a names in nameslist
         for i in global_list:
            # print (i)
                dict=i
                nameslist.append(dict["age"])
                for j in nameslist:
                    if j>=15 and j<=20:
                        print(dict["name"])
                

    def namecheck (self):
        nameslist=[]
        for i in global_list:
            dict=i
            nameslist.append(dict["name"])
        print(nameslist)
        for j in nameslist:
            # print(j)
            if j[0]=='a' and j[-1]=='n':
                print(j)


    
                
stud1=student("manic",21,"Bsc","tuty")
stud2=student("perumal",22,"Bcom","trichy")
stud3=student("hari",24,"Msc","kovilpatti")
stud4=student("aathavan",17,"12th","coiambatore")
stud5=student("amaran",17,"12th","chennai")
with open("/home/manikam/data.json","r")as js:   
    global_list=[]
    global_list=json.load(js)   
                                                #create a global to be used by any function     
# stud1.namesorder()
# stud1.ageorder()

# stud1.agelimit()
stud1.namecheck()