# length.py
# Author: Linda Grealish
# This program reads in a string
# and strips any leading or trailing spaces
# week 3 lab 3

rawstring = input('Please enter a string:')
normalisedstring = rawstring.strip().lower() # this changes to all lower case

lengthofrawstring = len(rawstring)
lengthofnormalised = len(normalisedstring)

print(f"That String normalised is :{normalisedstring}")
print(f"we reduced the input string from {lenghtofrawstring} to {lenghtofnormalised} characters")