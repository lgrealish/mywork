# convert.py
# Author: Linda Grealish
# This program takes in a float amount of dollars
# and returns than absolute amount in cent
# week 3 lab 2

number = float(input("Please enter an amount:"))

absolutevalue = abs(number)

# the code below was returning a .0 at the end of the result until I added the str() function
string2 = "The amount in cent is : "+ str(int(absolutevalue * 100))

print (string2)

