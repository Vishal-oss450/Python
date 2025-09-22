'''
programms on decision making
1. write a program to accept choicce from user and print result
S print sunday
M print monday
T print tuesday
W print wednesday
Th prints thursday
F prints Friday
Sa print saturdayy
'''
s1 = input("Enter a choice")
if s1== "S":
    print("sunday")
elif s1== "M":
    print("monday")
elif s1== "T":
    print("tuesday")
elif s1== "W":
    print("Wednesday")
elif s1== "Th":
    print("thursday")
elif s1== "F":
    print("Friday")
elif s1== "Sa":
    print("saturday")
else: print("Enter a valid choice")



'''
2. Write a program to accept choices from a user and print result
1. print hi
2 . print welcome
3. print bye
'''
h = int(input("Enter your choice"))
if h==1:
    print("Hi")
elif h==2:
    print("welcome")
elif h==3:
    print("Bye")
else: print("Enter a valid choice")




'''
3. write a program to accept characters from user and print characters in capital or small letter

'''
s1= input("Enter a string")
s2 = s1.lower()
s3 = s1.upper()
print("Your string in capital is ",s3)
print("Your string in small letter is",s2)




'''
4. design a app for movie ticket booking
a first accept choice of seat(classic @ 100 /premium @300/recliner @r500)
b accept the number of seats
c now according to amoount provide offers
i amount between 500 to 1500
offer include(choice of a meal worth R200 or discount 2%)
ii amount more than 1500
offer iinclude (choice of a meal worth R500 or discount of 4%)
'''
print("Enter 1 for classic seat \nEnter 2 for premium seat \nEnter 3 for recliner seats")
a = int(input("Enter your choice"))
b = int(input("Enter the number of seats"))
c=0
d=0
discount = 0
famount=0
amount=0
if a==1:
    amount= 100*b
elif a==2:
    amount = 300*b
elif a==3:
    amount = 500*b
else: print("enter a valid choice")
if 500<= amount <=1500:
    print("congrachulations you can either win 2% discount or grab a meal of worth 200")
    print("Enter 1 for discount\nEnter 2 for a meal")
    c= int(input("Enter your choice"))
    if c==1:
        discount = 0.02*amount
        famount = amount-discount
        print("Your amount is ",famount)
    else:
        print("YOu can have your meal of 200 and your amount is",amount)
elif amount>1500:
    print("congrachulations you can either win 4% discount or grab a meal of worth 500")
    print("Enter 1 for discount\nEnter 2 for a meal")
    d= int(input("Enter your choice"))
    if d==1:
        discount = 0.04*amount
        famount = amount-discount
        print("Your amount is ",famount)
    else:
        print("YOu can have your meal of 500 and your amount is",amount)
else:
    print("Your amount is",amount)








'''
5 write a program to design a app for retail store , calculate final bill and discount on multiple brands according to the given choice
woodland = 20 %discount
levis= 30% discount
veroModa= 35%discount
US polo = 40% discount
User can shop from multiple brands, also with amounnt exceeding 5000, offer a gift vocher of rs 500
'''
a = int(input("Enter the amount of shopping from woodland, if no product sold enter amount = 0"))
b = int(input("Enter the amount of shopping from levis,if no product sold enter amount = 0"))
c = int(input("Enter the amount of shopping from veroModa,if no product sold enter amount = 0"))
d = int(input("Enter the amount of shopping from US POLO,if no product sold enter amount = 0"))
adiscount = a*20/100
bdiscount = b*30/100
cdiscount = c*35/100
ddiscount = d*40/100
e = int(input("Enter the total bill made in the store"))
totaldiscount = adiscount+bdiscount+cdiscount+ddiscount
finalbill = e-totaldiscount
if finalbill >5000:
    print(f"Your bill is {finalbill}, including a R500 vorchure" )
else:
    print("Your bill is",finalbill)





'''
Q6 TO qualify a scholarship student have to go through three screening tests
1.Aptutute test( marks out of 100)
2. coding tesrt(marks out of 100)
3 vivia test(marks out of 100)
Eligibility depends on the given criterias 
Student have to secure more than 95 marks in coding test,
total of apitite and vivia should me more than 130,
average marks are more than 180
'''
a = int(input("Enter the marks of apitute test"))
b = int(input("Enter the marks of coding test"))
c = int(input("Enter the marks of viva test"))
sum = a+c
average = (a+b+c)/3
if b>95 and sum>130 and average>180:
    print("You are eligible for scholarship")
else: print("NOT ELIGIBLE FOR SCHOLARSHIP")


