"""
### Defining a Function
def function_name ( parameter 1, parameter 2, parameter 3, …………, parameter n)
# work of function
Return value

## calling a Function
Function_name(argument 1, argument 2, argument 3, …………, argument n)

## parameters : koi value jo ham dete hai uska name
## Argument : value jo ham dete hai or value jis ppar ham function ko perform karna chahte hai.
"""

# create a function to perform addition of two no.
def sum(a,b):
    add = a+b
    print(add)
    return sum
sum(3,8)
sum(56468451.515156165,57435468.78454646)

# create a function to perform multiplication of two no.
def mul(a,b):
    multiplication = a*b
    print(multiplication)
    return mul
mul(12,16)
mul(2.211,21.16465411)

# create a function to perform division of two no. (a/b)
def div(a,b):
    division = a/b
    print(division)
    return div
div(12,6)
div(12354.231498,132.542145454)

# create a function to perform subtraction of two no. (a-b)
def sub(a,b):
    subtraction = a-b
    print(subtraction)
    return sub
sub(12,6)
sub(123.231498,1325.542145454)

# create a function to perform average of three no.
def avg(a,b,c):
    print((a+b+c)/3)
    return avg
avg(15,17,58)
avg(48.4564,545.64,6441.45)

## default perameter
# sum(a,b) # yaha par ham a or b ki default value or kisi 1 ki default value de sakte hai ,
# 1 default value dene par ham sirf bad bali value ko default value de sakte hai,pahle bali ko nhi.
# sum(a,b) : default value set nhi hai,
# sum(a=1,b=1) : dono default value set hai,
# sum(a,b=1) : ek default value set ha, ## sum(a=1,b) : ye galat hogsum
def add(a=1,b=1):
    print(a+b)
    return add
add(56,64)

def add(a,b=1):
    print(a+b)
    return add
add(56)

'''def add(a=1,b):
    print(a+b)
    return add
add(56)
# error aayega'''

# write a function :WAF
#waf to print length of a list.
list=["a","b","c","d","e","f","g","h","i","j","k"]
def length(a):
    print(len(a))
    return length
    
length(list)
# yaha length function ko alag tarah use kiya gaya hai.

#waf to print element of list in a single line.
list=["a","b","c","d","e","f","g","h","i","j","k"]
def printa(a):
    for i in a:
        print(i, end=" ")

printa(list)

# waf to find the factorial of n no.
def fect(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i # fact*=i
    print(fact)
    return fect

fect(int(input("enter no. : ")))

# waf to convert usd to inr.
def cnv(a):
    print("amount in INDIAN rupies : ",a*85)

cnv(float(input("enter ammount in USD :  ")))

# waf to print no. is even or odd.
def OE(n):
    if(n%2==0):
        print(a,"No. is even")
    else:print("No. is odd")
a= int(input("Enter a No. : "))
OE(a)



# RECURSION : FUNCTION KA RAPETE HONA  RECURSION KAHLATA HAI
# print no 1 to 5 using recursion
def show(n):
    if (n==6):
        return
    print(n)
    show(n+1)
    # print("a")  : agr ham ye chahte hai ki ek bar fn end hone ke bad me kuch print ho to ham iska use kar sakte hai 
show(1)

# wap to print factorial
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1)*n
print(fact(5))

# wap to print sum of first n no.
def sum(n):
    if (n==0):
        return 0
    return sum(n-1) + n
print(sum(10))

# wap to print all elements in the list
def show(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    show(list,idx+1)

a= ["a","b","c","d","e"]
show(a)
