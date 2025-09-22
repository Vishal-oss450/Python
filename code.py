# 1 Write a program to accept name from user and display tthe name with welcome message on screen. 
s1 = input("Enter your name")
print("Welcome",s1)

# Write a program to accept 3 numbers from a user can calculate their sum and average?
a = int(input("Enter a number"))
b= int(input("Enter second number"))
c = int(input("Enter third number"))
sum = a+b+c
average = (a+b+c) / 2
print("Sum = ",sum)
print("Average = ", average)

#Write a program to store a string literal and formatt the string using escape sequence and escape character
s1 = "welcome to python  \npython is good \n language  \n Learn this language" 
print(s1)


# Write a program to accept marks of 5 subbjects from user calculate total , calculate percentage, print result pass or fail on the basis of percentage
#percentage greater than or equal to 50 = pass otherwise fail
a = int(input("Enter marks of first subject"))
b = int(input("Enter marks of 2 subject"))
c = int(input("Enter marks of 3 subject"))
d = int(input("Enter marks of 4 subject"))
e = int(input("Enter marks of 5 subject"))
percentage = ((a+b+c+d+e)*100)/500
if percentage >= 50:
    print("Pass")
else: print("Fail")

# Program to accept price of 10 different items from user, calculate the total amount provide discount on the basis of total amount 
#if amount exceed 2000 apply discount 20%, display discount and final amount. Otherwise no discount

a = int(input("Enter price of item 1"))
b = int(input("Enter price of item 2"))
c = int(input("Enter price of item 3"))
d = int(input("Enter price of item 4"))
e = int(input("Enter price of item 5"))
f = int(input("Enter price of item 6"))
g = int(input("Enter price of item 7"))
h = int(input("Enter price of item 8"))
i = int(input("Enter price of item 9"))
j = int(input("Enter price of item 10"))
sum = a+b+c+d+e+f+g+h+i+j
discount = sum*0.20
if sum >= 2000:
    sum = sum - discount
    print("Total =", sum)
else: print("Total = ",sum)

