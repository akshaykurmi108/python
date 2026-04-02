list=[12,42,84,65,36,53,"ram","syam","sita",9,7,1,9,1,7]
print("list = ",list)
print(type(list))

#access the value of specific index ; list[index No.]
print(list[10])
print(list[0],list[7])

#len() : to print the lenth of list
print(len(list))

#list ko update karna
list[1]=71
list[6]="ak"
print(list) #updated list print hogi


# LIST SLICING

print(list[1:5]) # index 1,2,3,4 ki value print hogi index 5 ki nhi
print(list[:4])#same as list[0:4]
print(list[8:])#same as list[8:len(list)]
print(list[-9:-2]) # for nagetive indexing




# LIST METHODS
list1=[12,42,84,65,36,53]

# list.append(value) : to add element at the end of the list
list1.append(100)
print(list1)

list.append(100)
print(list)

#list.sort() : to sort the list (assending order)
list1.sort()
print(list1)

list2=['z','s','h','t','i','k','e','b','j','t']
list2.sort()
print(list2)

# list.sort(reverse=True) : sort the list in desending order
list1.sort(reverse=True)
print(list1)

list2.sort(reverse=True)
print(list2)

# list.reverse() : to print reverse list.
list1.reverse()
print(list1)

# list.insert(index,element) : to insert the element at any specific index / position
list1.insert(4,97)
print(list1)

list.insert(4,"akshay")
print(list)

#list.remove(index,element) : to remove an first occurence of element
list.remove(9)
print(list)

# list.pop(index) : to remove element at specific index.
list.pop(6)
print(list)



# WAP to ask the user to enter name of their three favorite mivies & store them in a List.
a=input("enter first movie name : ")
b=input("enter second movie name : ")
c=input("enter third movie name : ")
lista=[a,b,c]
print(lista)
print(type(lista))

# # WAP to chack if a list a palindrone of element
lista=["ram",1,9.7,9.7,1,"ram"]
listb=lista.copy()
listb.reverse()
print(lista)
print(listb)
if(lista==listb):
    print("list is palindrone")
else:("not palindrone")


''' mere galat prayas 
list=[12,42,84,65,36,53,"ram","syam","sita",9,7,1,9,1,7]
if(list == list.reverse()):
    print("list is palindrone")
else:print("not palindrone")

listp=["ram",1,9.7,9.7,1,"ram"]
print(listp)
listp.reverse()
print(listp)
listp=[1,2,1]
listq=listp.reverse()
if(listp == listq):
    print("list is palindrone")
else:print("not palindrone")'''