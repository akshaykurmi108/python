#del kayword
class student:
    def __init__(self,name):
        self.name=name

s1=student("akshay")
print(s1.name)

# del s1 # to delet s1
print(s1)
print(s1.name)

# Private attribute and Methods
# class ke andar se hi access kar sakte hai bahar se nahi

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        # self.acc_pass=acc_pass    # abhi ye public hai 
        # private karne ke liye "self." ke bad me "__"lagate hai
        self.__acc_pass=acc_pass    # ab ye private hai
        # ise class ke andar se access kar sakte but bahar se nahi
    
a1=account(12345,"qwertyuiop")
print(a1.acc_no)
# print(a1.__acc_pass)            # account no to print hoga but pass print nahi hoga kyoki vo class ke bahar se print kara rahe hai 
#agar hum class ke andar se passeord ko print karate to vo print ho jata hai

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  

    def show(self):
        print(self.__acc_pass)


a1=account(12345,"qwertyuiop")
print(a1.acc_no)
print(a1.show())


# private method

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  

    def __show(self):
        print(self.__acc_pass)
        # ham private method ka use karte hai taki agar kisi or method ko us method ki jarurat ho class ke andar , but bahar se koi use access na kar paye to uske liye ham iska use karte hai
    def hi(self):
        self.__show()

a1=account(12345,"qwertyuiop")
print(a1.acc_no)
print(a1.hi())



# INHERITANCE
#PARENT CLASS KI PROPERTIES child class access kar sakti hai

class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clt=False

    def start(self):
        self.clt=True
        self.acc=True
        print("car started")

    def stop(self):
        self.brk=True
        print("car stoped")

class BMW(car):
    def __init__(self,name):
        self.name=name

car1=BMW("black")
car2=BMW("white")
print(car1.start())
print(car2.start())

print(car1.stop())


# single inheritance me 1 base class hoti hai or 1 derived class hoti hai
#multi level inheritance me base class ki derived class to hoti hi hai also us derived class ki bhee derived slass hoti hai or iske or bhee levels ho sakte hai
# multiple inheritance me multiple base class ki 1 derived class hoti hai


# multilevel inheritance
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clt=False

    def start(self):
        self.clt=True
        self.acc=True
        print("car started")

    def stop(self):
        self.brk=True
        print("car stoped")

class cars(car):
    color="black"

class BMW(cars):
    def __init__(self,name):
        self.name=name

car1=BMW("model1")
car2=BMW("model2")
print(car1.start())
print(car2.start())

print(car1.color)


#multiple inheritance

class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clt=False

    def start(self):
        self.clt=True
        self.acc=True
        print("car started")

    def stop(self):
        self.brk=True
        print("car stoped")

class cars:
    color="black"

class BMW(car,cars):
    def __init__(self,name):
        self.name=name

car1=BMW("model1")
car2=BMW("model2")
print(car1.start())
print(car2.start())

print(car1.color)


# SUPER METHOD
# super() method is used to access method of parent class

class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")


class BMW(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1=BMW("black","petrol")
# print(car1.start)
print(car1.type)



# CLASS METHOD
class person:
    name="anonymous"

    def changename(self,name):
        self.name=name

p1=person()
p1.changename("akshay")
print(p1.name)
print(person.name)
# yaha par specific person ka name to change ho raha hai but person class me jo name diya hai vo change nahi ho raha hai
# iske liye ham class method ka use karte hai 
 

class person:
    name="anonymous"

    def changename(self,name):
        self.__class__.name=name        # __class__ ka use karke
        # person.name=name              # classname ka use karke 

p1=person()
p1.changename("akshay")
print(p1.name)
print(person.name)


class person:
    name="anonymous"

    @classmethod                    # defining class method
    def changename(cls,name):           #   cls    ,  self ki tara hi hota hai
        cls.name=name

p1=person()
p1.changename("akshay")
print(p1.name)
print(person.name)


# PROPERTY DECORATOR
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    def percent(self):
        self.percentage=(self.phy + self.chem + self.math)/3

s1=student(99,98,98)
s1.percent()
print(s1.percentage)

s1.phy=97
print(s1.phy)
s1.percent()
print(s1.percentage)

# isi kam ko karne ka or simple tarika hota hota hao property decorator

class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return (self.phy + self.chem + self.math)/3

s1=student(99,98,98)
print(s1.percentage)

s1.phy=97
print(s1.phy)
print(s1.percentage)
