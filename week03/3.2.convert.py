# convert.py
# Author: Linda Grealish
# This program takes in a float amount of dollars
# and returns than absolute amount in cent
# week 3 lab 2

number = float(input("Please enter an amount:"))
absolutevalue = abs(number)
string2 = "The amount in cent is : "+str(absolutevalue * 100)

print (string2)

