'''
1. else statement with for loop
2. eelse statement with while loop
'''
'''
When we place else with for loop and while loop, on successful execution of the loop and while, the statement placed inside the else
will execute
on any interupt of the for and while loop,else will not execute
'''
sum = 0
for i in range(1,10):
    print(i,end =" ")
    sum = sum+i
else:
    print("Loop executed successfully")
    print("sum = ",sum)

# 2nd example
for i in range(1,10):
    print(i)
    if i==5:
        break 
else:
    print("Loop executed successfully")

'''
Write a program to accept a range from user and print  table of all the numbers multiple of 5 in the  range in a proper format of eg. 2*1=2
and print "this program will help to understand f or format function used with print function
'''

print("from while loop")
a = int(input("Enter starting range"))
b = int(input("Enter the ending range"))
while a<=b:
    if a%5 == 0:
        t =a
        print()
        print()
        i=1
        while i<=10:
            print(f"{a}*{i}={a*i}")
            i=i+1
    a=a+1
        

'''
a = int(input("Enter starting range"))
b = int(input("Enter the ending range"))

for a in range(a,b):
    if a%5 == 0:
        t =a
        print()
        print()
        for i in range(1,10):
            print(f"{t} * {i} = {t*i}")
'''
'''
Character data type holds 1 character at a time.
string data type stores squences of data


here a variable with 1 character is a string with length 1
'''
ch1 = 'a'
ch2 = "a"
ch3 = """a"""
ch4='''a'''
ch5=r'c'
print(type(ch1))
print(type(ch2))
print(type(ch3))
print(type(ch4))
print(type(ch5))
print(ch5)

# string operators / string slicing
# string predefine functions
#string operator
#1. +(for concatenation(used to combine multiple strings))
#2. * (for string replication)

str1 = "python"
str2 = "programming"
str3= str1+str2

'''
how string is formed in memory
In python each character store in a string is first interpreteed with its unicode value and then stored in memory using hash method
'''
import sys
a = 65
print(a.char())