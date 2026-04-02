"""f= open("file.txt", "r") # to open file
# data = f.read() # data read karne ke liye 
# print(data)

# print(type(data)) # to print data type of data

print(f.read(6))  #first n letters ko print karne ke liye # first n words ko read karta hai

print(f.readline()) # read line by line # read line 1
###line change hone par \n default hota hai
print(f.readline())  #read line 2
print(f.readline())  #read line 3
f.close  # close the file 

### write in file : file ka purana data delete kar deta hai or new data add karta hai
f=open("file.txt" , "w")
f.write("this is i am performing write operation in file \n")
f.write("this is i am performing write operation in file \n")
f.write("this is i am performing write operation in file\n")
f.write("is that....\n")
f.close

###append in file : add data at the end of file 
f=open("file.txt" , "a")
f.write("\nthis is i am performing append operation in file \n")
f.write("this is i am performing append operation in file \n")
f.write("this is i am performing append operation in file\n")
f.write("is that ....\n")
f.close

### r+ :file me starting se overwrite karna ke liye usefull hoti hai
f=open("file.txt" , "r+")
f.write("\nthis is r+ in file \n")
f.write("purane data me satrtin se change karta hai \n")
f.write("purane data ko hatakar new data put karta hai\n")
f.write("isme poora data delete nhi hota")
f.write("is taht ....\n")
print(f.read())
f.close

### w+ : file ko write ke sath me read bhee kar sakte hai
f=open("file.txt","w+")
f.write("this is i am performing write+ operation in file \n")
f.write("this is i am performing write+ operation in file \n")
f.write("this is i am performing write+ operation in file\n")
print(f.read())
f.close

### with syntext : with open("file name","operation")cs f:
##### jo kam ham normallykarte hai vo
with open("file.txt","r") as f:
    print(f.read())

### deletind a file : iske liye hame import os use karna padta hai
import os
os.remove("file.txt")
""" 

### 1. 
with open("practice.txt","w") as f:
    f.write("I everypne\ni am learning file I/O\nusing python.\ni like it")

###2
f= open("practice.txt","r")
a=f.read()
data=a.replace("using","in")
print(data)
f.close

q= open("practice.txt","w")
q.write(data)