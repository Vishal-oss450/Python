#loops in python   (In python there is no data type og character , even with any data with only 1 character there is  string of length 1)
#Interative programming/repetitive(using loop)
'''
1. for loop
2.while loop
For syntax
for variable in sequence
 statement

'''
#example program "for": with sequence
st = "Hello world"
for i in st:
    print(i)

'''
1. object(can print object or objects at same time)
2. Seperator(What to be placed between objects , default iis "  ")
3. end(what to place at the end of print function,default is \n)
'''
st = "Hello world"
for i in st:
    print(i,end=" ")

#program to check parameters of print function
st1 = "Hello world"
d = "12"
m = '1'
y = "2024"
print(d,m,y,sep="-",end="")
print()

#Example prograam with range function with different overload
'''
range function wiith for loop provides sequential width to follow in ascending or descending order
Overloads of range function
1. range(stop) starts with 0 to stop-1
2.range (start,stop)start with start variable to stop-1
3.range(start,stop,step) start with value of start to stop -1 with number of steps to skip in ascending order or descending order 
'''
for i in range(10): #with stop only
    print(i,end=" ")
print()
for i in range(100,110): #range with start and stop
    print(i,end=" ")
print()
for i in range(20,10,-2):
    print(i,end=" ")
print()

# print table of 3
for i in range(1,11):
    print(f"{i}*3 = {i*3}")
print(" 2nd time")
for i in range(11):
    print(i*3,sep="*",end = " ")

print()


'''
2 while loop
syntax
initialisation
while condition:
statement
invrement or decrement statement
'''
#example program on while loop
# program to print all natural number in range
a =1
while a<=10:
    print(a,end =" ")
    a+=1
a= int(input("Enter the number"))
b = 1
while b<=10:
    print(f"{a}*{b}={a*b}",end=" ")
    b = b+1

print()

# program to acceppt input from user and print multiples of 3 and 5
a = 4
b = 400
for a in range(a,b):
    if a%3 == 0 and a%5==0:
        print(a,end=" , ")


'''
Jumping Statements
These are the statements which are used when our program is in continous motion to interrupt that motion, we use jumping statemts 
when compiler reads jumping statement its execution path interrepts and change
1. Break
2.continue:- skip statement place after it
3. Pass: do nothing

'''
#Example program on break, continue and pass
i = 1
while i<=20:
    print(i,end="")
    if i==3:
        continue
    i=i+1
# Write a program to accept a range from a user
'''
if 5 is in the range ,print element 5 found in the range,
if a number multiple of 7 is found in the range, exit the loop
if a number O is in the range do nothing
'''
