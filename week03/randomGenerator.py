# randomGenerator
# Author: Linda Grealish
# This program prints out a random number between 1 and 10
# week 3 lab 1

import random

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

number = random.randint(x,y)
print ("here is a random number {}". format(number))
