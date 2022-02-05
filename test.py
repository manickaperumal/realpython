import json
l = []


class student:
    def __init__(self, name, age, degree, medium, district):
        self.name = name
        self.age = age
        self.degree = degree
        self.medium = medium  # for to store a object specific information
        self.district = district
        with open("/home/manikam/data.json", "w")as js:
            global l
            dic = self.__dict__
            # all object details will be stored in a list called 'l'(list name)
            l.append(dic)
            json.dump(l, js)  # list convert into json file

    @staticmethod
    def namesorder():
       sorted_list=sorted(global_list,key=lambda x:x["name"])
       for i in sorted_list:
           print(i)

    @staticmethod
    def ageorder():

         sorted_list=sorted(global_list,key=lambda x:x["age"],reverse=True)
         for i in sorted_list:
           print(i)

  
        

    def agelimit(self):
        agelist = []  # to store a names in nameslist
        for i in global_list:
            # print (i)
            dict = i
            if dict["age"] > 15 and dict["age"] < 20:
                print(dict["name"], "age is", dict["age"])

    def namecheck(self):
        nameslist = []
        for i in global_list:
            dict = i
            nameslist.append(dict["name"])
        print(nameslist)
        for j in nameslist:
            # print(j)
            if j[0] == 'a' and j[-1] == 'n':
                print(j)

    def vowel(self):

        for i in global_list:
            if i["medium"] == "tamil" and i["age"] <= 20 and  set(["a", "e", "i", "o", "u"]).intersection(set(list(i["name"]))):
                    print(i["name"], "age is", i["age"],"studying", i["medium"], "medium")


    def namebased(self, name):
        nameslist = []
        for i in global_list:
            dict = i
            # print(dict)

            for k in dict.values():
                if k == name:
                    print(dict)


stud1 = student("manic", 21, "Bsc", "english", "tuty")
stud2 = student("perumal", 22, "Bcom", "english", "trichy")
stud3 = student("hari", 24, "Msc", "english", "kovilpatti")
stud4 = student("aathavan", 17, "12th", "tamil", "coiambatore")
stud5 = student("amaran", 17, "12th", "tamil", "chennai")
stud6 = student("ganesh", 16, "11th", "tamil", "tirunelveli")
stud7 = student("zzz", 17, "12th", "tamil", "chennai")
stud8 = student("mari", 21, "bcom", "english", "tuty")
stud9 = student("aswin", 19, "12th", "tamil", "bangalore")
stud10 = student("kannan", 13, "8th", "tamil", "tuty")
with open("/home/manikam/data.json", "r")as js:
    global_list = []
    global_list = json.load(js)
    # create a global to be used by any function
# stud1.namesorder()
stud1.ageorder()

# stud1.agelimit()
# stud1.namecheck()
# stud1.vowel()
# stud1.namebased("manic")
# stud5.namebased("amaran")
# stud1.namebased("ganesh")
