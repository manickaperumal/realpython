
class mobiles:
    def __init__(self,brand,price,offer):
        self.brand=brand
        self.price=price
        self.offer=offer

    def __lt__(self,other):
        return self.price<other.price

    def __add__(self,other):
        return self.offer + other.ccoffer

class creditcard:
    def __init__(self,brand,ccoffer):
        self.brand=brand
        self.ccoffer=ccoffer
        




m1=mobiles("vivo",10000,1000)
m2=mobiles("samsung",12000,1000)
cc=creditcard("vivo",500)

print(m1+cc)