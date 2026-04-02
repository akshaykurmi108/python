"""
# POLYMORPHISM      :   many forms
#ek hi cheej ke multiple meaning hona
# like + operator
print(2+4)
print("a"+"k")
#yaya + ek hi hai but dono place par differenr types se work kar raha hai
# ise hi operator overloading kaha jata hai jo ki polymorphism ka hi part hai


#Operator Overloading : when the same operator is allowed to have a different meaning according to contaxt

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i+",self.img,"j")

    def add(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)

num1=complex(7,8)
num1.shownumber()

num2=complex(9,4)
num2.shownumber()

num3=num1.add(num2)
# yaha par ham num1+num2 nahi kar sakte kyoki real ko real or img ko img se add karne koi add fn nhi hai isliye ham dunder fn ka use karemge
num3.shownumber()


class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self,num2):     #dunder fn
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)
    
    def __sub__(self,num2):     #dunder fn
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return complex(newreal,newimg)


num1=complex(6,8)
num1.shownumber()

num2=complex(9,4)
num2.shownumber()

num3=num1+num2          # ab ye work karega
num3.shownumber()

num4=num1-num2
num4.shownumber()
"""

# Q.1 : Define a circle class to create a circle with radious r using the cunstructor.
#define an area() method of the class which claculates the area of the circle.
# define a perimeter() method of the class which calculates the perimeter of the circle.

class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return(22/7)* self.radius *self.radius

    def perimeter(self):
        return(22/7)*2* self.radius
    
r=circle(5)
print(r.area())
print(r.perimeter())


#Q.2 : Define an employee class with an attribute role department and salary this class also has a show details method
# create an engineer class that inherit properties from employee and has additional attribute name and age.

class employee:
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal
    
    def showdetails(self):
        print( "role:",self.role)
        print("department:",self.dep)
        print("salary:",self.sal)

class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("DA","CS",100000)

    def showdetail(self):
        print("name:",self.name)
        print("age:",self.age)
    
e1=engineer("Akshay Kurmi",21)
e1.showdetails()
e1.showdetail()


# Q.3 : create a class called Order which stores item and its price.
#use under function __gt__() to convey that:
#     order1>order2 if price of order1>price of order 2

class Order:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __gt__(self,odr2):
        return self.price>odr2.price

odr1=Order("tea",15)
odr2=Order("coffie",45)
# print(odr1.name)
# print(odr1.price)
# print(odr2.name)
# print(odr2.price)

print(odr1>odr2)