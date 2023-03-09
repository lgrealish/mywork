# average.py
# Author: Linda Grealish
# Keeps reading numbers until a 0 is entered.  Then prints out an average of them.
# week 4 lab 2

numbers = []

number = (int(input("enter number(0 to quit) : ")))

while number != 0:
    numbers.append (number)
    number = (int(input("enter number(0 to quit) : ")))

for value in numbers:
    print (value)

average = float(sum(numbers) / len(numbers))
print (f"The average is {average}")