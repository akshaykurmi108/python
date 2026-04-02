print("Hi Akshay Kurmi")
# Q.1:
# 4
# 4 3
# 4 3 2
# 4 3 2 1

for i in range(4, 0, -1): 
    for j in range(4, i-1, -1):
        print(j, end=" ")
    print()  


#Q.2:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

num=1
for i in range(1,5,1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()


#Q.3:
#    1
#   12
#  123
# 1234
#12345

for i in range(1,7,1): 
    for j in range(5, i-1, -1):
        print(" ", end=" ")
    for k in range(1,i,1):
        print(k,end=" ")
    print()  


#Q.4:

#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5


for i in range(1,7,1): 
    for j in range(5, i-1, -1):
        print("", end=" ")
    for k in range(1,i,1):
        print(k,end=" ")
    print()  

# star pattern
for i in range(1,7,1): 
    for j in range(5, i-1, -1):
        print("", end=" ")
    for k in range(1,i,1):
        print("*",end=" ")
    print()  


# Q:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,7,1): 
    for j in range(5, i-1, -1):
        print("", end="")
    for k in range(1,i,1):
        print(k,end=" ")
    print()  


a= input("choose figure\nc for circle,r for ractangle")
if a=="c":
    r=float(input("radius:"))
    area=2*3.14*r
    print(area)

elif  a=="r":
    l=float(input("length:"))
    w=float(input("wridth:"))
    area_of_ract=l*w
    print(area_of_ract)
else :print("wrong input")