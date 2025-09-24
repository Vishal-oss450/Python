'''
Q1. Employee Salary Slip Generator
Write a program that accepts basic salary of an employee and calculate the following:
•	HRA = 20% of basic
•	DA = 10% of basic
•	PF = 12% of basic
•	Gross Salary = Basic + HRA + DA
•	Net Salary = Gross - PF
Decision Rules:
•	If Net Salary ≥ 80,000 → Category = "High Earner"
•	If 50,000 ≤ Net Salary < 80,000 → "Mid Earner"
•	Else → "Low Earner"
'''
a = int(input("Enter your basic salary"))
b = 0.2*a
c = 0.1*a
pf = 0.12*a
gross = a+b+c
net = gross-pf
if net>=80000:
    print("You are a high earner and your salary is",net)
elif net>=50000 and net <80000:
    print("You are a mid earner and your salary is ",net)
else: print("You are a low earner and your salary is",net)




'''
Q2. Loan Eligibility System
Create a program that checks loan eligibility.
Inputs: age, monthly_income, existing_loan, CIBIL_score.
Conditions:
•	Age must be between 21-60
•	Income must be ≥ 25,000
•	Existing loan must be ≤ 50% of income
•	CIBIL score ≥ 700
If all conditions are satisfied → "Eligible for Loan"
Else, display reason for rejection (e.g., "Rejected due to low CIBIL score").
'''
age = int(input("Enter your age"))
income = int(input("Enter your income"))
exloan = int(input("Enter your existing loan"))
cibi = int(input("Enter your CIBIL score"))
a = income/2
if 21<=age<=60 and income>=25000 and exloan<=a and cibi>= 700:
    print("You are eligible for loan")
else: print("Not eligible")




'''
Q3. Smart Traffic Fine System
A city wants to implement a traffic fine system.
Inputs: speed, vehicle_type (car/bike/truck), seat_belt (Yes/No), helmet (Yes/No if bike).
Rules:
•	Speed > 80 → Fine ₹2000
•	Car without seat belt → +₹1000 fine
•	Bike without helmet → +₹1500 fine
•	Truck speed > 60 → +₹3000 fine
Display: "Total Fine = …"
If no rules violated → "No Fine. Drive Safe"
'''
print("Enter 1 for car")
print("Enter 2 for bike")
print("Enter 3 for truck")
a = int(input("Enter your choice"))
fine =0
speed = int(input("Enter the speed"))
if speed>80:
            fine = fine+2000
match a:
    case 1:
        s1 = input("Enter wether you entered seat belt or not")
        if s1 =="no":
            fine = fine+1000
            print("Your fine is ",fine)
        else: print("No fine.Drive safe")
    case 2:
        s2 = input("Enter wether you entered helmet or not")
        if s2 =="no":
            fine = fine+1500
            print("Your fine is ",fine)
        else: print("No fine,drive safe")
    case 3:
        if speed>60:
            fine = fine+3000
            print("Your fine is ",fine)
        else: print("No fine.Drive safe")



'''
Q4. E-Commerce Discount Calculator
Write a program that asks for product price and user type (Regular, Premium, VIP).
Discount Rules:
Regular:
< 500 → 5%
≥ 500 → 10%
Premium:
< 1000 → 15%
≥ 1000 → 20%
VIP: Flat 25% discount always
Also apply extra 5% discount if payment mode = "Online".
Finally display the discounted price.
'''
print("Enter 1 for regular user")
print("Enter 2 for premium user")
print("Enter 3 for VIP user")
a = int(input("Enter your choice"))
amount = int(input("Enter the amount of shopping"))
match a:
    case 1:
        if amount<500:
            discount = 0.05*amount
            s3 = input("IS ONLINE MODE OF PAYMENT USED (yes or no)")
            if s3=="yes":
                odiscount = 0.05*amount
                famount = amount-discount - odiscount
            else:
                famount = amount-discount
            print("your final amount is ",famount)
        elif amount>=500:
            discount = 0.1*amount
            s3 = input("IS ONLINE MODE OF PAYMENT USED (yes or no)")
            if s3=="yes":
                odiscount = 0.05*amount
                famount = amount-discount - odiscount
            else: famount = amount-discount
            print("your final amount is ",famount)
    case 2:
        if amount<1000:
            discount = 0.15*amount
            s3 = input("IS ONLINE MODE OF PAYMENT USED (yes or no)")
            if s3=="yes":
                odiscount = 0.05*amount
                famount = amount-discount - odiscount
            else:
                famount = amount-discount
            print("your final amount is ",famount)
        elif amount>=1000:
            discount = 0.2*amount
            s3 = input("IS ONLINE MODE OF PAYMENT USED (yes or no)")
            if s3=="yes":
                odiscount = 0.05*amount
                famount = amount-discount - odiscount
            else: famount = amount-discount
            print("your final amount is ",famount)
    case 3: 
        s3 = input("IS ONLINE MODE OF PAYMENT USED (yes or no)")
        if s3=="yes":
            odiscount = 0.05*amount
            discount = 0.25*amount
            famount = amount - odiscount-discount
            print("Your final amount is",famount)
        else:
            discount = 0.25*amount
            famount = amount -discount
            print("Your final amount is",famount)




'''
Q5. University Admission System
Write a program that takes marks in Physics, Chemistry, and Math.
•	Calculate total and average.
Admission Criteria:
•	Average ≥ 70 and each subject ≥ 60 → "Eligible for Admission"
•	Else if Math ≥ 90 → "Eligible under Math Special Quota"
•	Else → "Not Eligible".
'''

p = int(input("Enter the marks of physics"))
c = int(input("Enter the marks of chemistery"))
m = int(input("Enter the marks of math"))
total = p+c+m
average = total/3
if average>=70:
    if p>=60 and c>=60 and m>=60:
        print("Eligible for admission")
elif m>=90:
    print("Eligible for math quotta")
else:
    print("Not eligible")




'''
Q6. Movie Ticket Pricing System
Inputs: age, movie_type (2D/3D), day (weekday/weekend).
Rules:
•	Base price = ₹200
•	If 3D → +₹100
•	Weekend → +₹50
•	Age < 12 → 50% discount
•	Age > 60 → 30% discount
Calculate and display final ticket price.
'''
age= int(input("Enter your age"))
print("Enter 1 for 2d movie\nEnter 2 for 3d movie")
mt = int(input("Enter movie type"))
print("Enter 1 for weekday\nEnter 2 for weekend")
day = int(input("Enter the day"))
if age<12:
    if mt==1:
        if day == 1:
            discount = 0.5*200
            price = 200-discount
        else:
            discount = 0.5*250
            price = 250-discount
    elif mt==2:
        if day == 1:
            discount = 0.5*200
            price = 200-discount+100
        else:
            discount = 0.5*250
            price = 250-discount+100
elif age>60:
    if mt==1:
        if day == 1:
            discount = 0.3*200
            price = 200-discount
        else:
            discount = 0.3*250
            price = 250-discount
    elif mt==2:
        if day == 1:
            discount = 0.3*200
            price = 200-discount+100
        else:
            discount = 0.3*250
            price = 250-discount+100

print("Final price = ",price)




'''
Q7. Online Examination Result
Inputs: Correct answers, Wrong answers, Unattempted.
Marking scheme: +4 for correct, -1 for wrong, 0 for unattempted.
Rules:
•	Score ≥ 180 → "Excellent"
•	120-179 → "Good"
•	60-119 → "Average"
•	Below 60 → "Fail"
Also, if Wrong answers > Correct answers, show: "Improve accuracy!"
'''
cans = int(input("Enter the correct answers"))
wans = int(input("Enter the wrong answers"))
uans = int(input("Enter the unattempted answer"))
totalc = cans * 4
totalw = wans * -1
totalu = 0*uans
total = totalc+totalw+totalu
if total>=180:
    print("Excellent")
elif 120<=total<=179:
    print("Good")
elif 60<=total<=119:
    print("Average")
elif total<60:
    print("Fail")




'''
Q8. ATM Transaction Simulation
Inputs: account_balance, amount_to_withdraw, account_type (Saving/Current), day (weekday/weekend).
Rules:
•	Withdrawal allowed only if balance ≥ withdrawal + 1000 (minimum balance).
•	Weekend transactions charge extra ₹50 fee.
•	Saving account daily limit = 25,000; Current account = 50,000.
Output: Success/Failure with reason and updated balance.
'''

balance = int(input("Enter your balance"))
awithdraw = int(input("Enter the amount to withdraw"))
t = int(input("Enter 1 for savings account\nEnter 2 for current account"))
d = int(input("Enter 1 for weekday\nEnter 2 for weekend"))
a = awithdraw+1000

if balance>=a:
    if t==1:
        if awithdraw<=25000:
            if d==1:
                v = balance-awithdraw
                print("Transaction successful and now your balance is ",v)
            elif d==2:
                v = balance-awithdraw-50
                print("Transaction successful and now your balance is ",v)
            else:
                print("Savings account allows daily limit of only 25,000")
    elif t==2:
        if awithdraw<=50000:
            if d==1:
                v = balance-awithdraw
                print("Transaction successful and now your balance is ",v)
            elif d==2:
                v = balance-awithdraw-50
                print("Transaction successful and now your balance is ",v)
            else:
                print("Current account allows daily limit of onlt 50,000")
else: print("Insufficient balance")


'''
Q9. Online Food Delivery Charges
Inputs: distance, order_amount, user_type (Normal, Gold, Platinum).
Rules:
•	Base delivery = ₹50
•	If distance > 5 km → +₹10/km extra
•	Free delivery if order_amount ≥ 1000
•	Membership benefits:
o	Gold → 20% discount on order
o	Platinum → 30% discount on order
o	Normal → No discount
Display final bill amount including delivery.
'''
distance = int(input("Enter delivery distance (km) "))
orderamount = int(input("Enter order amount  "))
usertype = input("Enter user type (Normal, Gold, Platinum): ")
if usertype == "Gold":
    orderamount = orderamount * 0.80 
elif usertype == "Platinum":
    orderamount = orderamount * 0.70 
if orderamount >= 1000:
    deliverycharge = 0
else:
    deliverycharge = 50
    if distance > 5:
        deliverycharge += (distance - 5) * 10
finalbill = orderamount + deliverycharge

# Output
print("Discounted Order Amount : ₹",orderamount)
print("Delivery Charge  : ₹",deliverycharge)
print("Final Bill Amoun : ₹", finalbill)