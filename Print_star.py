#!/usr/bin/env python
#Program to List odd numbers in the given Range 

import sys

#Method to find odd number and add to the list
def  print_odd(x):
     if (x % 2 != 0):
     	print("*")

#user input 
l, r =  input(" Enter the range, i.e left and right numbers (Note: Give a comma to enter the next no) :   ").split(',')
#To use them as interger
l, r = int (l), int(r)
for i in range(l,r):
    print_odd(i)
 