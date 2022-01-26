class mobiles:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def __gt__(self,other):
        return self.price>other.price

m1=mobiles("vivo",10000)
m2=mobiles("redmi",12000)
print(m1>m2)
