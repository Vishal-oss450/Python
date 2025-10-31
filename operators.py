#Operator = special symbols used to perform a specific task
#eg + is symbol and when appliied on operands
# perform concatenation or addition depends on the type of data
a= 1
b= 2
c= a+b
print(c)
s1="Hello"
s2="World"
s3 = s1+ " "+s2
print(s3)

# operands = on which we perform operation
#in programming opeerands are variables
# Types of operators:-
#1 on the basis on number of operands
#a Uninary operator Eg . Increment (EG. a = a+1,    a= a-1)
#a++
# b. Binary operator  
# number of operands 2
# #eg Addition subtraction etc
# c. Ternary operators 
# number of operands 3 eg. Logical operator (and,or,not)

#2. On the basis of behaviour
# a. Arithematic
''' addition , subtraction,*,/,%,**(exponent),  //(floor division)
'''
#eg. of arithmatic operator
a= 10
b = 2
print(a+b)
print(a-b)
print(a//b)
print(a**b)
print("a/b",a//b)

# Arithmetic assingnment operator
''' +=
-=
*=
/=
**=
//=
'''
a= 5
b=10
a+=b
print(a)
a*=b
print(a)
a**=b
print(a)
b//=a
print(b)

a= 10
b= 5
a**=b
print(a)

a=10
b=5
a%=b
print(a)


'''
Comparisin operators
> greater than
>= greater than equal to
<= less than equal  to
!= not eequal to
== check operator
'''
print(a==b)
print(a is b)

print("Logical operators")
#logical operators
#AND , OR, NOT
x=1
y=2
z=3
print(x>y and y>z and z>x) # and will return false if any of the condition is false
print (y>x and x<z and z>y)#and will return true if all the conditions are true
print(x>y and y>z and z<x)#and will return false if all the conditons are false
'''
in case of "or" falsse occour only when all conditions are false
in case of "and" true occour when all the cconditons are ture
in case of not opposite of or occur
'''

print(x>y or y>z or z>x)#or will return true is any of the condition is true
print(y>x or x<z or z>y)#or will return true if all the conditions are true
print(x>y or y>z or z<x)# or will return false if all the conditions are false

#NOT

print(not(x>y or y>z or z>x))

#conditional operators in python
'''
1 if
2 if else
3 elif ladder
4 match case
5 nested if else
'''
if x>y:
    print(x)

a = int(input("Enter first number"))
b = int(input("Enter second number"))
if a>b:
    print("First number is greater")
else : 
        print("second number is greater")
# write a program to accept string from a user
# also check wether it is upper case of lower case
s1 = input("Enter a string")
print("The string you entered is ", s1)
s2 = s1.upper()
print(s2)
if s1 == s2:
    print("The string you entered is in upper case")
else: print("The string you entered is in lower case")
