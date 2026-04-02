###   WHILE LOOP

# while_condition :  # syntex

# print hello 5 time 

a=1
while a<=5:
    print("helo",a)
    a+=1

''' nakam pryash
a=1
b=1
while a<=5:
    while b<=5:
        print(b)
        b+=1
    print(a)
    a+=1
    '''


#print no. from 1 to 5
a=1
while a<=5:
    print(a)
    a+=1
    
#print no. from 5 to 1
a=5
while a>=1:
    print(a)
    a-=1

#print no. from n to m # increasing
a=int(input("enter no. from : "))
b=int(input("enter no. to"))
while a<=b:
    print(a)
    a+=1

# print no. from n to m #decreasing
a=int(input("enter no. from : "))
b=int(input("enter no. to"))
while a>=b:
    print(a)
    a-=1

# print a multiplication table of no. n.
a=int(input("enter a no. : "))
b=1
while b<11:
    print(a,"*",b,"=",a*b)
    b+=1
    
# print an squre of no. from n to m
a=int(input("enter from no."))
b=int(input("enter to no."))
while a<=b:
    print(a*a)
    a+=1
   
# print an squre of no. from n to m in a list
list=[]
a=int(input("enter from no."))
b=int(input("enter to no."))
while a<=b:
    list.append(a*a)
    a+=1
print(list)

# print all the element from the list using whilw loop
a=["a","b","c","d","e","f"]
b=0
while b<+len(a):
    print(a[b])
    b+=1

# # print numbers from n to m with th diffrence of k
n=int(input("start : "))
m=int(input("ending :"))
k=int(input("step : "))
while(n<m):
    print(n)
    n+=k
# print odd no. from n to m 
n=int(input("start : "))
m=int(input("ending :"))
while(n<m):
    if(n%2!=0):
         print(n)
    n+=1
# print even no. from n to m 
n=int(input("start : "))
m=int(input("ending :"))
while(n<m):
    if(n%2==0):
         print(n)
    n+=1
'''
#print no. from n to m and in every line also havs printed n to that line no.

1
12
123
1234
12345
......
..............
# kuch is tarah se

a=int(input("enter from no."))
b=int(input("enter to no."))
while a<=b:
    print(a)
    a+=1
    print(a)
    '''

# searching using loop, in tuple
a=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 25)
b=0
c=int(input("enter a no. : "))
while b<len(a):
    if(c==a[b]):
        print(c,"found at index",b)
    else:print("finding")
    b+=1
     
    

## BREAK in loop

a=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 25)
b=0
c=int(input("enter a no. : "))
while b<len(a):
    if(c==a[b]):
        print(c,"found at index",b)
        break
    b+=1

# another one example
# print no. from 1 to 5
a=1
while a<=99:
    print(a)
    if(a==15): # 15 par jakar ruk jayega
        break
    a+=1


    
# CONTINUE in loops : loop jis point par chal raha hota hai use skip karke uske aage continue karta hai,
a= 0
while a<6:
    if(a==4):
        a+=1
        continue # yaha par ye 4 ko print nhi karega lekin uske aage "continoue" kar dega,
    print(a)
    a+=1

#print 1 to 10 odd value using "continoue"
a=0
while a<11:
    if(a%2==0):
        a+=1
        continue
    print(a)
    a+=1

# sum of first n no. 
a=int(input("from "))
b=int(input("to "))
sum=0
while(a<=b):
    sum+=a
    a+=1
print(sum)

# fectorial of first n no. 
# a=int(input("start : "))  # hame factorial ko 1 se start karne padta hai isliye ham ise nhi lenge
a=1
b=int(input("ending :"))
fact=1
while(a<=b):
    fact=fact*a
    a+=1
    print("fact. of ",a,"=",fact)


###   FOR LOOP  ###

# SYNTEX :  for _ in range():

# print no. from 0 to 10 
for a in range(11):
    print(a)

# print no. from 0 to n
for a in range(int(input("enter a no."))):
    print(a)

# for loop in list
list= [55,2,8,6,7,5,89,32,77,48,1,98,45,2,42,86]
for a in list:
    print(a)

# for loop in tuple
tuple = (77,48,1,98,45,2,42,55,2,8,6,7,5,89,32)
for a in tuple:
    print(a)
   
# For loop in string
str="akshay _ kurmi"
for a in str:
    print(a)
 
## else in loop
str="akshay _ kurmi"
for a in str:
    if(a=="_"):
        print("_ mil gaya")
        break
    print(a)
else:print("end")

## print squre of no. from 1 to n-1
for i in range(int(input("enter a no. : "))):
    print(i*i)
    
## print squre of no. from 1 to n-1 in a list
list=[]
for i in range(int(input("enter a no. : "))):
    list.append(i*i)
print(list)

# searching using for loop
a=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 25)
b=int(input("no. : "))
idx=0  # ismeham directly index ko print nhi kara sakte isi liye idx name ka ek variable banate hai
for i in a:
    if(i==b):
        print("element", b ,"found at index : " , idx)
    idx+=1
else:print("element not found")


## RANGE Fnction

# range(start**,stop,step**)
for i in range(15):     # stop condition only
    print(i)


for i in range(5,15):    # start & stop condition
    print(i)


# for i in range(15,2): # stop & step condition apply nhi kar sakte
    # print(i)

for i in range(4,26,3):   #start , stop , step condition
    print(i) 

# print numbers from n to m with th diffrence of k
for i in range(int(input("start : ")),int(input("ending :")),int(input("step : "))):
    print(i)

# print odd no. from n to m 
for i in range(int(input("start : ")),int(input("ending :"))):
    if(i%2!=0):
        print(i)

# print even no. from n to m 
for i in range(int(input("start : ")),int(input("ending :"))):
    if(i%2==0):
        print(i)
'''
# list ke sath upper wala
list=[]
for i in range(int(input("start : ")),int(input("ending :")),int(input("step : "))):
    list.append(i)
    print(list)
    if(i%2!=0):
        print(i)
        '''

# print no. from n to m and m to n
for i in range(int(input("from :")),int(input("to : "))):
    print(i) 

# m to n
for i in range(int(input("from :")),int(input("to : ")),int(input("step"))):
    print(i) 

# table of multiplication of a no.
a=int(input("no. : "))
for i in range(1,11):
    print(a,"*",i,"=",a *i)
    
## PASS  statement : iska use ham tab karte hai jab hame lagta hai ki loop ka use hame bad me hoga 
for i in range (10):
    pass
    
# sum of first n no.
sum=0
a=int(input("start : "))
b=int(input("ending :"))
for a in range(a,b+1):
    sum+=a
print(sum)

# fectorial of first n no. 
# a=int(input("start : "))  # hame factorial ko 1 se start karne padta hai isliye ham ise nhi lenge
b=int(input("ending :"))
fact=1
for a in range(1,b+1):
    fact=fact*a
    print("fact. of ",a,"=",fact)


#WAP to print the digit of the no.
n=int(input("enter a no. : "))
i=10
while(n>0):
    n=n//i
    print(n)
