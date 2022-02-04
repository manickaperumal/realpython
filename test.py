import json
l=[]
class student:
    def __init__(self,name,age,degree,medium,district):
        self.name=name
        self.age=age
        self.degree=degree 
        self.medium=medium                        #for to store a object specific information
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
         agelist=[]                                #to store a names in nameslist
         for i in global_list:
            # print (i)
                dict=i
                if dict["age"]>15 and dict["age"]<20:
                    print(dict["name"],"age is",dict["age"])
              

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

    def vowel(self):
        # print(global_list)
        for i in global_list:
            dict=i
            if dict["medium"]=="tamil":
                if dict["age"]<=20:

                    for names in dict["name"]:

                      


                       if names=="a" or names=="e" or names=="i" or names=="o" or names=="u":
                           print(dict["name"],"age is",dict["age"],"studying",dict["medium"],"medium")
                           break
    def namebased(self,name):
        nameslist=[]
        for i in global_list:
            dict=i
            # print(dict)
            
            for k in dict.values():
               if k==name:
                  print(dict)

        #     nameslist.append(dict["name"])
        # for names in nameslist:
        #     if name==names:
        #         print(self.__dict__)
                    
                
stud1=student("manic",21,"Bsc","english","tuty")
stud2=student("perumal",22,"Bcom","english","trichy")
stud3=student("hari",24,"Msc","english","kovilpatti")
stud4=student("aathavan",17,"12th","tamil","coiambatore")
stud5=student("amaran",17,"12th","tamil","chennai")
stud6=student("ganesh",16,"11th","tamil","tirunelveli")
stud7=student("zzz",17,"12th","tamil","chennai")
stud8=student("mari",21,"bcom","english","tuty")
stud9=student("aswin",19,"12th","tamil","bangalore")
stud10=student("kannan",13,"8th","tamil","tuty")
with open("/home/manikam/data.json","r")as js:   
    global_list=[]
    global_list=json.load(js)   
                                                #create a global to be used by any function     
#stud1.namesorder()
#stud1.ageorder()

#stud1.agelimit()
#stud1.namecheck()
stud1.vowel()
stud1.namebased("manic")
stud5.namebased("amaran")
stud1.namebased("ganesh")

