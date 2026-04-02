a= "akshay"
if(a=="ram"):
    print("a is ram")#if ki condition true hui to ye print hoga.
elif(a=="syam"):
    print("a is syam")#elif ki condition true hui to ye print hoga.
else:
    print("a is akshay") #pahle  ki sari condition true nahi hui to ye print hoga.


#####
M=marks=float(input("enter marks of an studetn out of 100 : "))
if(M>100):
    print("invailed marks")
elif(M>=95):
    print("grade = A+")
elif(95>M>=90):
    print("grade = A")
elif(90>M>=80):
    print("grade = B")
elif(80>M>=70):
    print("grade = C")
elif(70>M>=60):
    print("grade = D ")
else:
    print("fail")


### NESTING.
age=int(input("enter age :  "))
if(age>=18):
    if(age>=25):
        if(age>=50):
            print("more then 50")
        elif(50>age>=40):
            print("more hen 40")
        else:print("more then 25")
    elif(25>age>=20):
        print("more them 20")
    else:print("more then 18")
elif(18>age>=15):
    print("more then 15")
else:print("less then 15")


# chack the given no is even or odd,
n= int(input("enter a no. : "))
if(n%2==0):
    print("no. is even")
else:print("no. is odd")


# WAT to find the greatest no of 3 no. entered by the user.
a= int(input("enter a no. a : "))
b= int(input("enter a no. b : "))
c= int(input("enter a no. c : "))
if(a>=b):
    if(a>=c):
        print("a is greater")
    elif(c>=b):
        print("c is greater")
elif(b>=c):
    print("b is greater")
else:print("c is greater")

# or 
if(a>=b and a>=c):
    print("a is greater")
elif(b>=a and b>=c):
    print("b is greater")
else:print("c is greater")


# WAP to chack the no. is multiple of seven or not
z= int(input("enter a no. : "))
if(z%7==0):
    print("no. is multiple of 7")
else:print("no. is not a multiple of 7")

# WAP to calculate total percentage and division of 6 subject.

s1=int(input("enter a no. of subject 1 : "))
s2=int(input("enter a no. of subject 2 : "))
s3=int(input("enter a no. of subject 3 : "))
s4=int(input("enter a no. of subject 4 : "))
s5=int(input("enter a no. of subject 5 : "))
s6=int(input("enter a no. of subject 6 : "))
total=s1+s2+s3+s4+s5+s6
print(f"/n total marks:{total}out of 600")  # ' f ' ka use karke ham total ko print na karakar uski value ko print karayenge
# print(f"/n total marks:{s1+s2+s3+s4+s5+s6}out of 600")   :  is tarah se bhee likh sakte hai
percentage=total/6  #  (s1+s2+s3+s4+s5+s6)/6   
print(percentage)

if(percentage>100):
    print("invailed marks")
elif(percentage>=95):
    print("grade = A+")
elif(95>percentage>=90):
    print("grade = A")
elif(90>percentage>=80):
    print("grade = B")
elif(80>percentage>=70):
    print("grade = C")
elif(70>percentage>=60):
    print("grade = D ")
else:
    print("fail")
    