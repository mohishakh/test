class Ketab :
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def  full_name(self):
       return f'{self.name}\n{self.price}'
class Bache(Ketab):
    def __init__(self,name,price,title):
        Ketab.__init__(self,name,price)
        self.title=title
    def full_name(self):
         return f'{self.name}\n{self.price}\n{self.title}'
class Bozorgsal(Ketab):
    def __init__(self,name,price,title2):
        Ketab.__init__(self,name,price)
        self.title2=title2
    def full_name(self):
         return f'{self.name}\n{self.price}\n{self.title2}'           
Bache= Bache("test1",4500,"ketab Bache") 
Bozorgsal= Bozorgsal("test 2",7000,"ketab Bozorgsal") 
print(Bache.full_name())
print(f'name:{Bache.name}price:{Bache.price}')
print(Bozorgsal.full_name())
print(f'name:{Bozorgsal.name}price:{Bozorgsal.price}')