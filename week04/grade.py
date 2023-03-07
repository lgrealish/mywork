# grade.py
# Author: Linda Grealish
# This program reads in a students percentage mark
# and prints out the corresponding grade
# week 4 lab 1

percentage = float (input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")

elif (percentage) < 39.5:
    print ("Fail")

elif (percentage) < 49.5:
    print ("Pass")

elif (percentage) < 59.5:
    print ("Merit 2")

elif (percentage) < 69.5:
    print ("Merit 2")

else: print("Distinction")