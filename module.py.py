'''
Modules in python
What are module files in python:;
Files in python including functions,classes and variables.
extension is .py
importance:- code reuseable
2.Easy to manage

# SOME MODULE FILES IN PYTHON ARE SAVED AS .C EXTENSION

Types of modules in python
1. user defiine moule(.py),reuse with import statement
2. Predefined modules(already python setup)
build in
system library
third party modules(installed using PIP)


'''
help('modules')# list all the modules including the third party
#Q. How tto list modules installed in our system
# Q how to list all third party modules using pip dependency manager

#how to use build in modules in our program
import math
print("Square root of 25",math.sqrt(25))
import datetime
import os
import sys
print("Square root of 25",math.sqrt(25))
#a = len(help('modules'))
dir(sys)
# Q which command is used to check a module name of a function
# ans = dir
print()
print("hi\n")
# program to print list of build in modules only
print(sys.builtin_module_names)

# build in modules are developed in  c programming as well as python
# how to check the file or module type in python