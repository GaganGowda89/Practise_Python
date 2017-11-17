#!/usr/bin/env python
#Program to List odd numbers in the given Range 

import sys

#Method to find odd number and add to the list
def  odd(x):
     if (x % 2 != 0):
     	odd_LIST.append(x)

#user input 
l, r =  input(" Enter the range, i.e left and right numbers (Note: Give a comma to enter the next no) :   ").split(',')
#To use them as interger
l, r = int (l), int(r)
odd_LIST = []
for i in range(l,r):
    odd(i)
for j in odd_LIST:
	print (j)    
