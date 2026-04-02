set={95,7,10,45,18,74,63,18,10,"hello","akshay"}
set1={15,72,"ram",95,68.04,7,10,74,63,"akshay"}
print(set)
print(set1)

print(type(set))
print(len(set))
print(type(set1))
print(len(set1))

#print null set  :  seta=set() ,
# to chack null set  :     print(type(seta)).

### SET METHOD

#set.add(element)  :  to add element on a set
set.add(52)
set.add((45.18,63.74))
set.add(963.1452)
print(set)
# print(set.add(65))# is tarah se element ko add nhi kar sakte 

#set.remove(element) : to remove element from the set
set.remove(18)
print(set)

"""#set.pop() : to remove a random element
set.pop()
print(set.pop())  # print karta hai kin sa element pop hoga 
print(set)

#set.clear() : set ko clear karta hai
set.clear()
print(set)
print(len(set))
"""

## UNION of SET  :  set1.union(set2)  : combine karke new set return karta hai.
print(set.union(set1))
print(set) #purana set i print hoga
print(set1) # purana set1 hi print hoga
## INTERSECTION of SET  :  set1.intersection(set2)  : common values ko print kareta hai.
print(set.intersection(set1))
print(set) #purana set i print hoga
print(set1) # purana set1 hi print hoga


## store "9 & 9.0 in set"
# 1
setb={9,"9.0"} #{'9",9.0}
print(setb)
#2
setc={(int,9),(float,9.0)}
print(setc)