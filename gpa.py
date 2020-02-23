#!/usr/bin/env python3

#  Author:      Enkidu
#  Date:        02/23/20 1:14 AM
#  Purpose:     GPA Calculator. This will calculate the GPA, Units taken
#               and the grade points earned.       

#*  Variable Declaration
unitsTaken = []    # array for units taken
gradePntsErn = []  # array for grade point earned in class
totalErn = 0       # Earned grade points accumulator
totalTaken = 0     # Taken units accumulator

#*  Program Starts
print("This program will calulate your; total units taken,\ntotal earned grade points and GPA.\n")
print("Grades: A = 4, B = 3, C = 2, D = 1, F = 0\n")    # Grade point equivalent for grade earned

#* Input Validation
while True: #While loop user input validation
    temp = input("Input the number of classes taken: ") # user input for number of classes stored in temp var
    try:    #try
        nClasses = int(temp)    # if temp is int store in nClasses
        break;  #break loop
    except ValueError:  #Error execption ask for valid input
        print ("This is not a valid number. Please enter a whole number.\n")

#*  User Input
for i in range(0, nClasses): # for loop in range of classes taken
    print(f"\nClass {i+1}:")

    #* Input Validation
    while True: #While loop user input validation
        temp = input("Enter Units taken: ") # user input stored in val
        try:    #try
            n = int(temp)   #if temp is int store in n
            break;  #break loop
        except ValueError:  #Error execption ask for valid input
            print ("This is not a valid number. Please enter a whole number.\n")

    unitsTaken.append(n)   # units taken appened to array

    #* Input Validation
    while True: #While loop user input validation
        temp = input("Enter grade points earned: ") 
        try:
            n = int(temp)
            break;
        except ValueError:
            print ("This is not a valid number. Please enter a whole number.\n")

    gradePntsErn.append(n)  # grade points earned appended to array

#*  GPA Calculation
for i in range(0, nClasses): #for loop in range of classes taken to find totals
    totalErn += (unitsTaken[i] * gradePntsErn[i])    # total earned grade points = units taken * grade points earned
    totalTaken += unitsTaken[i] # sum units taken add to total taken units

gpa = totalErn/totalTaken  # GPA Calculation GPA = total earned grade points / total taken units

#*  Outputs
print(f"\nYour total units taken are: {totalTaken}")
print(f"Your total earned grade points are: {totalErn}")
print("\nYour GPA is: {g:1.1f}\n".format(g=gpa))

#*  Exit Program
exit(0)
