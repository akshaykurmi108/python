dict={"name":"akhay",
      "list":["akshay",74,63.7],
      "tuple":("ram",345,876.65),
      "a":3455,
      "b":6567.75,
      7676:677,
      45679.6545:"raja",
      "c":True
}

print(dict)

## EMPTY DICTIONARY : dict={}   : ye ek empty dictionary

print(type(dict))
# ise list ya tuple ke form nhee print kara sakte hai , type casting ke through
# print(list(dict.keys()))

print(list(dict))
print(type(list(dict)))

#print(tuple(dict.keys()))
print(tuple(dict))
print(type(tuple(dict)))

# to find the length of the dictionary
#print(len(dict))
print(len(dict))

## Dictionary ke andar ham kay element ko access kar sakte hai,
# dict["kay_name"]
print(dict["name"])
print(dict["list"])
print(dict["a"])
print(dict[7676])
print(dict["tuple"])

## kisi kay ki new valuechangekarna
# dict["kay_name"]="new_value"
dict["name"]="akshay kurmi"
print(dict)

## Dictionary me new kay ko add karna ,
# dict["new_kay"]="ney_value"
dict["ram"]=19
print(dict)

## we also can create an emoty sictionary
#dict={}
null_dict={}
print(null_dict)

## we also can assige a new value or can change it
null_dict["name"]="akshay kurmi"
null_dict["ram"]=19
print(null_dict)
null_dict["name"]="kurmi"
print(null_dict)
## we can perform all the operation same as dictionary on null dictionary



### NESTED DICTIONARY
# dictionary ke andar dictionary  : same as conditional statement
dict1={"name":"akhay",
       "z":{"list":["akshay",74,63.7],
      "tuple":("ram",345,876.65),
      "q":{"a":3455,
      "b":6567.75,
      7676:677,
      45679.6545:"raja",
      "c":True}
      },
      "nested_dict":{"TOC":98,
                  "dbms":99,
                  "cy":98,
                  "iwt":99,
                  },
      "percentage":98.5,
}

print(dict1)

## iske andar ham kisi sub dictionary or unke andar ke keys ko bhee print kara sakte hai print kara sakte hai
print(dict1["nested_dict"])
print(dict1["nested_dict"]["TOC"])
print(len(dict1))





### DICTIONARY METHODS


## dict.keys() : sari keys ko print karta hai (keys ke name) , (keys ki andar ki value ko nhi)

print(dict1.keys())
print(type(dict1.keys()))

# ise list ya tuple ke form nhee print kara sakte hai , type casting ke through
# print(list(dict.keys()))
print(list(dict1.keys()))
print(type(list(dict1.keys())))

#print(tuple(dict.keys()))
print(tuple(dict1.keys()))
print(type(tuple(dict1.keys())))


#dict.values() : sari keys ki value ko print karta hai (keys ko nhi) ,(sub dictionary ki kay_values ko bhee print karta hai)

print(dict1.values())
print(type(dict1.values()))

# ise list ya tuple ke form nhee print kara sakte hai , type casting ke through

print(list(dict1.values()))
print(type(list(dict1.values())))

print(tuple(dict1.values()))
print(type(tuple(dict1.values())))


# dict.item : key or value ke pairs ko return karta hai as a tuple
print(dict1.items())

# ise list yake form nhee print kara sakte hai , type casting ke through

print(list(dict1.items()))
print(type(list(dict1.items())))

# kisi pair ko alag se bhee access kar sakte hai.
pairs=list(dict1.items())
print(pairs[2])
print(type(pairs[2]))


# dict.get(kay) : kisi key ki value print karne ke liye

# print(dict1["z"])# iska use bhee hum value ko print karne ke liye karte hai 
# but agar yaha par "z" ki jagah par han "z1" ya "or kuch ji dictionary me nhi hai "
#use print karane par ye "error" deta hai 
#lekin dict.get("z1") karne per ye error nhi dega uske bajah ye ""none"" print karega,
print(dict1.get("name"))
print(dict1.get("asdfghjkl")) # print karega : ""none""


# dict.update(new_dict) : dictionary ke andar koi bhee kay or uski value ka pair pass kar sakte hai
dict1.update({"city":"indore"})
print(dict1)
print(dict1.update({"city":"indore"})) # none print karega 
# ham new dictionary banakar bhee aadd kar sakte hai
dict2={"dob":8.10}
dict1.update(dict2)
print(dict1)



### PRACTICE QUESTIONS
## Q.  store word meaning in python dictionary

dicta={"table":[input("enter meaning : "),input("enter another meaning : ")],
       input("enter 2nd word : "):[input("enter meaning :"),input("enter another meaning : ")]
       }
print(dicta)
print(type(dicta))


## Q. how many classes are required for thr sybjects
#1
dictb={"subject":["python","java","Cpp","javascript","C"]}
h =(len(dictb.get("subject")))
print("no. of classroom required : ",h)
# also  :  print("no. of classroom required : ",(len(dictb.get("subject"))))
#2
dictc={"python","java","cpp","java","python","c","javascript","java","python"}
print("no. of classroom required : " , len(dictc))

a={}
print(a)
a.update({"subject1":98})
a.update({"subject2":89})
a.update({"subject3":88})
print(a)