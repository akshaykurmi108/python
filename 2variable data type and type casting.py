name ="akshay \"kurmi\""
age = 19
DOB ="8/10/2006"
place = "sagar"
namewithfathername = name,"indrakumar kurmi" 
print("my name is : ",name,"\n","i am ",age,
      "year old","\n","DOB = ",DOB,"\n",
      "birth place = ",place)
print("ak")
print(namewithfathername)
print(type(name))
print(type(age))
print(type(DOB))
print(type(place))




#### DATA TYPE

name ="akshay \"kurmi\""
age = 19
DOB =8.10
a= False
b= None 
print(type(name))
print(type(age))
print(type(DOB))
print(type(a))
print(type(b))





###TYPE CONVERSING
A=12
B=8.3
print(A+B) 
# yaha par int ko automaticully float me convert kar diya
#lekin agar iski jagah par string(c="12" or "abcd") hoti to ye convert nahi kar pata 
#iske liye hum TYPE CASTING use karte hai


### TYPE CASTING

a="12"
b=45
print(int(a)+b)

c=int(12.9)
d=int("10")
print(c+d)

e=24454
e=str(e)
print(type(e))# ye string print karega
