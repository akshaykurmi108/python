#1
print("hello world",)
#2
print("akshay kurmi")
#3
print("hello world","akshay kurmi")
#4
print("hello world\nakshay kurmi")
#5
print(12345)
#6 
print(34567)
#7
print(12+3)
#8
print(12-3)
#9
print(12*3)
#10
print(12/3)



####
#TAKE INPUT FROM USER 
####
a= input("input from user")
print(a)

b=input("input : ")
print(b)
print(type(b)) #ye hamesha string hi aayegi #ye pahle se fix rahta hai means default hai
# yadi hame int ya float me input lena hai to hum int() ya float() ka ue karenge 
aa=int(input("enter a no."))
bb=float(input("enter something"))
print(aa,bb)
#print multiple value
print("akshay",7,12.6)
# print seperation (multiple cheejo ke beech me kuch or print karna)
print("akshay",7,12.6,sep="~_~") # ~_~ ki jagah par kuch bhee le sakte hai
# value vprint karane ke bad me hum end me kuch beee print kara sakte hai
print("akshay",7,12.6,sep="~_~",end="kuch bhee ")