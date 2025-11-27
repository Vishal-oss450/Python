import sys
print(sys.builtin_module_names)
print(len(sys.builtin_module_names))
# how to check or list build in modules name
print(sys.prefix)
# sys.prefix command is used to  retrieve file location of the module 
#Command to check physical condition of module


# not but here we can list only .py
import os
print(os.__file__)
import math
print(math.__file__)# developed in c not supported by __file__command   

'''
write a program to impement build in math module
and use predefine function of math modules in program
'''
import math
res = math.factorial(5)
print("Factorial of 5 is = ",res)
res = math.pow(2,5)
print("2 power 5 is",res)