'''
placing one conditional construct inside another
TYPES OF NESTING


1.if condition:
    if condition:
        statement

2. if inside if else
if condition:
    if condition:
        statement
    else:
        statement

3. if else inside if else
syntax: 
'''
# Example to check different types of nesting
# program to check wether a number is positive or even or odd or negative even or odd
a = int(input("enter a number"))
if a>0:
    if a%2==0:
        print("The number is positive and even")
    else : print("The number is positive and odd")
if a<0:
    if a%2 == 0:
        print("The number is negative and even")
    else : print("The number is negative and odd")

