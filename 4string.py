str="aKSHAY _ kurmi"
str1='this is ak'
str2="""\n thats me akshaykurmi"""
print(str,"\n",str1,"\n",str2)


# 1 # Concatenation : used to add two or more strings  .

print(str1+str2)

#hum dono string ko teesri string me bhee add kara sakte hai  .
#strc=stra+strb   ....   print(strc)  .

# 2 # len : used to find the length of string  .
#len (length) ke ander sare charscter count hote hai , space bhee .

print(len(str))
print(len(str1)+len(str2))

# 3 # INDEXING : used to access the specific charecter present at any specific index or position.
# indexing start with "0",not from "1".
#indexing ki help se hum index ki value ko change nhi kar sakte.

print(str[0],str[7])
print(str[6])

#ise teesre variavle ke through bhee access kar sakte hai.
# a= str[5]  ...  print(a)   o/p :  y  .
 
# 4 # SLICING : use to access an part of string .
# str[strating index : ending index] isme ending character print nhi hoga.
#agar hame ending element bhee print karna hai to hame us index ke aagevale index ki value leni hogi.

print(str[0:2])
print(str[7:])# also can use len() ...  [7: len(stre)]
print(str[:6])
print(str[-7:-3]) #for nagetive indexing



##  FUNCTION OF STRING ##

# str.startswith("aK") : s function me bracks ke ander ki value string ke starting me hogi to ye true print karega otherwise false frint karega.
print(str.startswith("aK"))
print(str.startswith("SH",2,7))

# str.endswith() : is function me bracks ke ander ki value string ke last me hogi to ye true print karega otherwise false frint karega.

print(str.endswith("ak"))
print(str.endswith("mi"))
print(str.endswith("ay",0,10))
print(str.endswith("AY",0,6))

'''# str.capitalize() :string ke pahle character k capital letter me convet kar deta hai.

print(str.capitalize())# yaha par ek new string bankar print hogi
print(str)#isse pureni string print hogi   ###agar ham purami string ko hatakar new string ko lana chahte hai to 

str=str.capitalize() #iska ues karenge # orignal string ko modify kar dega
print(str)#purani string ko capitalize karke print karega
'''
#str,replace(old string , new string) : poori string me kisi word ya kisi letter ko replace kar sakte hai kisi or word ya letter se . .

print(str.replace("_"," indrakumar "))
print(str.replace("a","A"))

# str.find(word) : string me koi word ya letter jaha kahi bhee aata hai to ye uska starting index print karta hai.

stra="my name is akshay kurmi "
print(stra.find("is"))
print(stra.find("k"))
print(stra.find("a"))
print(stra.find("b")) # b string me nh hai isliye ye "-1" print karega.

# str.count("ak") : count karta hai ki koi letter ya word kitni bar string me aaya hai.

strb="my name is akshay  and my sername is kurmi"
print(strb.count("is"))
print(strb.count("a"))
print(strb.count("z"))   

# str.upper() : string ke andar sare lettres ko upper case me convert kar dete hai,
print(str.upper())

# str.lower() : string ke andar sare lettres ko lower case me convert kar dete hai,
print(str.lower())

# str.split() : string ko list ke form me convert kar deta hai,
print(str.split())

# str.center() : iske brackes me ham jitni value/length dete hai,uske ending me 
#jo bhee ham print karana chahte hai vo pirnt hota hai,or vaki pale ki space khali rahti hai,
print(str.center(50))
print(len(str.center(50)))
print(len(str))

#str.index(value) index find karne ke liye ; agar element present na ho to error aa jati hai
print(str.index("Y"))

#str.isalnum() : to chack all the letters present in the string are numbers or not,
print(str.isalnum())

# str.isalpha() : to chack all the letters present in the string are characters or not,
print(str.isalpha())

# str.islower() : to chack all the letters present in the string are lowercase or not,
print(str.islower())

# str.isupper() : to chack all the letters present in the string are uppercase or not,
print(str.isupper())

# str.istitle() : to chack given string is title or not(first letter capital hai ya nhi)
print(str.istitle())

# str.isprintable() : to chack all the letters present in the string are printable or not,
print(str.isprintable())

# str.isspace() : to chack given string me space hai ya nhi
print(str.isspace())

# str.swapcase() : to conver lowercase to uppercase and wisevarsa
print(str.swapcase())

# str.title() : convert string to title string
print(str.title())