#a.	Program to print the type of variable (int, float, str, etc.)
a = input("Enter a variable")
if a.isdigit():
    print("You hsve entered a integer")
elif a.startswith('-') and a[1:].isdigit():
    print("negative integer")
elif '.' in a:
    print("You have entered float value")
else:
    print("You entered a string")

#b.	Program to swap two variables using a third variable
a = int(input("Enter variable 1")) #1
b = int(input("entter variable 2"))#2
c = 0
print(f"variables you entered are {a} ,{b}")
c = b #c = 2
b = a  #b = 1
a = c # a = 2
print(f"i swapped variables {a},{b}")


#c.	Program to add two numbers
#d.	Program to check if a number is positive
a = int(input("Enter a  number"))
b = int(input("Enter second number"))
c = a+b
print(f"Sum is : {c}")
if a>=0:
    print("a is positive")

#.	Program to check the largest of two numbers
a = int(input("Enter aa number"))
b = int(input("Enter another number"))
if a>b:
    print("First no. is greater")
else: print("Second no. is greater")



#j.	Program to print numbers from 1 to 10
for i in range (1,10):
    print(i)

print()
print()

#k.	Program to print even numbers between 1 to 20
for i in range(2,20,2):
    print(i)

print()
print()
print()

#l.	Program to calculate the sum of first 10 natural numbers
sum = 0
for  i in range(1,10):
    sum +=i
print (sum)



#m.	Program to find the factorial of a number
a = int(input("Enter a number"))
f = 1
for i in range(a,0,-1):
    f = f*i
print("factorial = ",f)


#n.	Program to print a square pattern using *
s = int(input("Enter the size of the square"))
for i in range (1,s+1):
    for j in range(1,s+1):
        print("*", end = " ")
    print()



#o.	Program to print multiplication table of a number
a = int(input("Enter a number"))
t = 0
for i in range(1,11):
    t = a*i  
    print(t)
   



#p.	Program to find the length of a list
l1 = (input("Enter the list")).split()
length = len(l1)
print("length is ",length)


#q.	Program to append a value to a list

l1 = input("Enter the list").split()
l1.append(20)
print("After append list = ",l1)


#r.	Program to sort a list in ascending order
l1 = [1,2,32,43,4,5,5,5]
l1.sort()
print("Sorted list is ",l1)


#s.	Program to generate a list of numbers from 0 to 10
l1 = list(range(1,11))
print(l1)



#	Program to generate a list of even numbers from 2 to 20
l1 = list(range(2,21,2))
print(l1)


#u.	Program to calculate the average of a list of numbers
l1 = input("Enter the list").split()
count = len(l1)
sum = 0
for i in range(0,count):
    sum +=int(l1[i])
if count>0:
    average = sum/count
    print(Average)
else: print("List is empty")



#v.	Program to check if two variables refer to the same object (memory location)
a = (input("Enter a number"))
b = (input("Enter another number"))
c= a is b
if c==True:
    print("Same memory location")
else: print("different")



#w.	Program to check if a year is a leap year
a = int(input("Ennter a year"))
if a%400==0:
    print("Leap year")
else: print("Normal year")


#x.	Program to check if a number is prime
#x.	Program to check if a number is prime
a = int(input("Enter a number"))
c = 0
for i in range(1,a+1):
    if a%i==0:
        c +=1
if c==2:
    print("prime")
else: print("not prime")


#y.	Program to find the largest of three numbers
#y.	Program to find the largest of three numbers
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if a>b and  a>c:
    print("First number you entered is greater")
elif b>a and b>c:
    print("Second number is greater")
else: print("Third is greater")


#aa.	Program to find the sum of all elements in a list
l1 = input("Enter the elements of list").split()
sum = 0
l = len(l1)
for i in range(0,l):
    sum += int(l1[i])
print("Sum of all elements is ",sum)


#dd.	Program to print a pyramid pattern using *
a = int(input("Enter the length of the pyramid"))
for i in range(1,a+1):
    for j in range(i):
        print("*",end =" ")
    print()



#ff.	Program to generate a list of square numbers using range()
a = int(input("Enter the range wherere you want the squares"))
l1 = []
s = 0
for i in range(1,a+1):
    s = i**2
    l1.append(s)
print("Your list is ",l1)


#hh.	Program to print a list of prime numbers within a range
