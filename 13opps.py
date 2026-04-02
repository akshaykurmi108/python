# creation of class
# class classname:
class a:
    name="akshay kurmi"

#creating an object
#objectname = classname()
s1=a()
print(s1.name) # for printing name
s2=a()
print(s2.name)

#for printing addresh of object
o1=a()
print(o1)



#class of car
class car:
    brand="Audi"
    color="black"
    model="17 a"

c1=car()
c2=car()
c3=car()

print(c1.brand)
print(c2.color)
print(c2.model)
print(c3.model)




# Constructor 
class student:
    name="akshay"
    def __init__(slef):    # self parameter hame pass karna hi padta hai nahi to error aayegi,self ka name badalkar or kuch bhee rakh sakte hai
        print("creating new student")
s1= student()
print(s1.name)


class student:
    name="akshay"
    def __init__(self):
        print(self)
        print("creating new student")
s1= student()
print(s1.name)


class student:
    def __init__(self,fullname,marks):
        self.name=fullname    # generlybih side same name ka use karte hai
        self.marks=marks
        print("creating new student")
s1=student("akshay",98)
print(s1.name)
print(s1.marks)
s2=student("ram",99)
print(s2.name,"=",s2.marks)



#Default contructer : jisme sirf ek hi parameter hota hai ; agr ise hum create nahi bhee karenge to ye autometuclly create ho jata hai

class a:
    b=12
    def __init__(self):
        print("a")
q=a()
print(q.b)


# parameterized constructor : jisme default ke alava bhee other parameter ho vo parameterized constrictor hota hai.
class akshay:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        print("new")
s1=akshay("ak",14)
print(s1.name,":",s1.roll)




#class and instance attributes
#class attr : poori class ka ek  : common things ke liye use hota hai
#object attr har object ke liye diffrent hoga 
# yesa data jo har obj ke liye alag hota hai use hamm (self.) se define karte hai.
# hum data ko class attr me store karte hai taki kam storage cover ho ya bhare
class student:
    collage="MIT"
    def __init__(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
        print("new student added")

s1=student("a",1,"q")
print(s1.name,":",s1.roll,"\nbranch:",s1.branch,"\ncollage name:",s1.collage)
s2=student("b",2,"w")
print(s2.name,":",s2.roll,"\nbranch:",s2.branch,"\ncollage name:",s2.collage)
# also we can do
print(student.collage)

# agar hamare pass same name ke class attr hai or same name ko obj attr hai to obj ke attr ki value higher hoti hai
# obj attr > class attr


# METHODS

class student:
    def __init__(self,name):
        self.name=name
    def met(self):
        print("hi this is :",self.name)

s1= student("himanshu")
s1.met()



# Que.create student class that takes name & marks of 3 subject as arguments in constructor.then create a method to print an avg
class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        print((self.m1+self.m2+self.m3)/3)
s1=student("raj",9,8,9)
print(s1.name,"\ns1=",s1.m1,"\ns2=",s1.m2,"\ns3=",s1.m3)
s1.avg()

# hum iselist method se bhee kar sakte hai
# markse ko ek list me lekar 
# hum attribute ki value ko directly bhee change kar sakte hai
s1.name="akshay"
print(s1.name)





# static method
# which dont have self parameter
# they work at class level
# not for object
# create an static method: 
            # @static method
            # def college():
            # print("something")


class student:
    def __init__(self,name):
        self.name=name

    
    def met(self):
        print("hi this is :",self.name)
    @staticmethod  #decorator
    def collage():
        print("MIT")

s1= student("himanshu")
s1.met()
s1.collage()

    


# abstraction:
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clt=False

    def start(self):
        self.clt=True
        self.acc=True
        print("car started")

a1=car()
a1.start()

# hare user ko directly car start hote dikh rahi hai uske peeche ki kahani nahi(true false nahi)



# QUE.
# create account class with two attributes balance and account No. 
# create method to credit debit and printing the balance
class account:
    def __init__(self,acno,balance):
        self.acno=acno
        self.balance=balance
        print("Account Details")

    def credit(self,amount):
        self.balance+=amount
        print("amount added",amount)
        print("totel balance:",self.balance)

    def debit(self,amount):
            self.balance-=amount
            print("amount debited:",amount)
            print("totel balance:",self.balance)

    def bal(self):
        print("Balance:",self.balance)


a1=account(12345678910,87984)
print("ac No.:",a1.acno,"\nBalance:",a1.balance)
a1.credit(1000)
a1.debit(8984)
a1.bal()
