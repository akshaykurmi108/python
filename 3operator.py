####  ARITHMATIC OPERATOR
a=7
b=2
#addition operator (+) ; used for finding addition
print(a+b)
#substraction operator(-) ; used for finding substraction
print(a-b)
#multiplication operator (*); used for finding multiplication
print(a*b)
#division operator(/) ; used for finding division
print(a/b)
#module operator(%) ; used for finding rmainder
print(a%b)
#Exponential operator(**) ; used for finding power( a ki power b)
print(a**b)
#floor division operator(//) ; devide larne ke bad desimal ki floor value print karta hai
#example :kisi bi no ke desimal ko hatakar uski int. value ko print karega (3.5 ya 3.9 ya 3.1 ke liye "3" ko print karega)
print(a//b)



#### RELATIONAL OPRATOR
a= 30
b= 130
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)




### ASSIGNMENT OPERATOR
#isme hum ko value assign karte hai
a=8
a=a+2 #  or  a+=2
print(a)
b=4
b-=1
print(b)
c=7
c*=2
print(c)
d=9
d/=4.5
print(d)
e=24
e%=5
print(e)
f=11
f**=3
print(f)



###LOGICAL OPERATOR
print(not False)
print(not True)

a=True
b=False
print("and operator : ",a and b)
print("or operator : ",a or b)

a=2
b=3
print("and operator : ",a and b) #bad vala print karta hai
print("or operator : ",a or b) #pahle vala print karta hai
print("and operator : ",(a==b) and (b>=a))
print("or operator : ",(a>b) or (a<b))





#  SOME QUESTIONS
# Q.1 . WAP to print 2 No. and sum, and also with user input
# code
a=29
b=56
c=a+b
print("a=",a,"\n b=",b,"\n c=",c)
#with user input
q=int(input("enter 1st no."))
w=int(input("enter 2nd no."))
print(q,"\n",w)
sum=q+w
print(sum)
# or print("sum = ", q+w)

# Q.2 . WAP to input side of a spure and print its area.
a=float(input("enter a = "))
print("area of square = ",a**2)

# Q.3 .  WAP to input 2 floating point numbers and print thair average
r=float(input("enter 1st no."))
t=float(input("enter 2nd no."))
y=(r+t)/2
print("avg. is :",y)

# Q.4 .  WAP to input 2 int no. . print true if s is greater then or equal to d, if not print false.
s=int(input("enter no. 1: "))
d=int(input("enter no. 2: "))
print(s>=d)


 #### CALCULATOR
a=int(input("enter a no. : "))
b=int(input("enter a no. : "))
add=a+b
sub=a-b
mul=a*b
div=a/b
c=a//b
power=a**b
mod=a%b
print("addition : ",add)
print("subtraction : ",sub)
print("multi[lication]",mul)
print("division",div)
print("flore division",c)
print("power",power)
print("reminder", mod)