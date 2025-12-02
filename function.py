'''
Functions in python:-
If we write multipe,lenthy lines of code in a single program,it is difficult to directly find the point 
where qw are getting errors or may be we loose readable quality
to increase readable quality of our program,we divide our length and complex code into smaller chunks 
known as functions,

this approach makes our code more readable,modularr,simpler,easy to understand ,easy to find errors
In functions, we combine statements to perform specific task.

types:-
1. predefined functions:-
2. user defined functions
function defination:- wworking
function calling:- execute

Syntax
directly called by user name()
eg. print()
input(),upper(),lower(),sort()etc

def functionname(parameters optional):
    statement
    or
    statements
functionname(arguments)  #function calling

'''
#Example of function with no return type and no parameter
def fun1():               #function defination
    print("Hello")
fun1() #function calling
print(fun1()) #by default every function in python returns none object
#we specify a return value
#none object(Sent by python interpreter in absence of a object)

#Example(Function with return type and no parenthesis)
def fun1():
    return"Hello"
print(fun1())#or
res=fun1()
print(res)


#Function with Parameters and no return type
def fun1(x,y): #Here x and y are parameters
    print(x*y)

fun1(2,3) # here 2 and 3 are arguments

#Function With Parameters and Return Type
def fun1(x,y):
    return x*y
res = fun1(2,3)
print(res)

#keyword arguments
def fun1(x,y):
    return x*y
res = fun1(x=2,y=3)
print(res)

#Default Parameters
#1. Required Parameters
#2. Optional parameters

def fun1(x,y=1):#required parameter
    return x*y
res = fun1(2,y=22)# Optional Parameter
print(res)

# we can not place required parameter after optional parameters
#we can only place optional parameters after required parameters


# Example program *arg

def fun1(*num):
    print(num)
fun1(1,2,3,4,5,6,7)
#in this example the arguments are packed inside a tuple
#now tuple are iterable and we can perform any further task

def fun1(*num):
    res = 1
    for i in num:
        res = res*i
    print(res)
fun1(1,2,3,3,44,5,56,6,6,7,77,5)
    
def fun1(*num):
    sq = 0
    for i in num:
        sq += i*i
    print(sq)
fun1(5,5)