<<<<<<< HEAD
# week06-functions.py.py
# Author: Linda Grealish
# Program that allows a user to create new students and to view students
# week 06 lab

def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice

def doAdd(students):
 currentStudent = {}
 currentStudent["name"]=input("enter name :")
 currentStudent["modules"]= readModules()
 students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\Enter the first Module name (blank to quit) :").strip()

    while moduleName != "":
            module = {}
            module["name"]= moduleName
            # I am not doing error handling
            module["grade"]=int(input("\t\tEnter grade:"))
            modules.append(module)
            # now read the next module name
            moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print(f"\t{ module['name']} \t{ module['grade']}") 

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);


students =[]
choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")

    choice = displayMenu()
=======

>>>>>>> 7cc6159ad2e0805d6cb533866f0e100d63dbe023
