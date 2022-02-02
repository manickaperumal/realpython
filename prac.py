#we can acess the class level variable through class name.we can access also through obj name.we can modify .

class supermarket:
    
    discount=20

    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.discount=supermarket.discount

    def objdetails(self):
        print(self.__dict__)

rice=supermarket("abc",300)
rice.objdetails()

shoe=supermarket("nike",500)
shoe.discount=30

shoe.objdetails()

#learn--> if we want to change the class value for particular obj ,we can change through the obj name 
#output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/prac.py
{'brand': 'abc', 'price': 300, 'discount': 20}
{'brand': 'nike', 'price': 500, 'discount': 30}
manikam@manikam:~$ 










