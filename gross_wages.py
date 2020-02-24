#!/usr/bin/env python3

#  Author:      Enkidu
#  Date:        02/23/20 8:40 PM
#  Purpose:     Wage Calculator. This will calculate the gross wages

#*  Variable Declaration
hrs = []            # array for hours worked
hrsTotal = 0        # Total hours accumulator
wageRate = 0        # WageRate variable
minConversion = 60  # Minuites Conversion

#*  Program Starts
print("This program will calulate your gross wages.\n")

#* Input Validation dayswrk
while True: #While loop user input validation
    temp = input("Enter the number of days you worked: ") # user input for number of days worked stored in temp var
    try:    #try
        dayswrk = int(temp)    # if temp is int store in dayswrk
        break;  #break loop
    except ValueError:  #Error execption ask for valid input
        print ("This is not a valid number. Please enter a whole number.\n")

#* Input Validation wages
while True: #While loop user input validation
    temp = input("Enter your hourly wage: ") # user input for wage stored in temp var
    try:    #try
        wageRate = int(temp)    # if temp is int store in wageRate
        break;  #break loop
    except ValueError:  #Error execption ask for valid input
        print ("This is not a valid number. Please enter a whole number.\n")

#*  User Input
for i in range(0, dayswrk): # for loop in range of dayswrk
    print(f"\nDay {i+1}:")

    #* Input Validation
    while True: #While loop user input validation
        temp = input("Enter hours worked: ") # user input stored in val
        try:    #try
            n = float(temp)   #if temp is int store in n
            break;  #break loop
        except ValueError:  #Error execption ask for valid input
            print ("This is not a valid number. Please enter a whole number.\n")

    hrs.append(n)   # hours worked appened to array

#*  Wage Calculation
for i in range(0, dayswrk): #for loop in range of dayswrk to find totals
    hrsTotal += hrs[i] # sum hrs add to total hours

grossWage = hrsTotal*wageRate  # Wage Calculation Gross wage = total hours * wage rate

#*  Outputs
print(f"\nTotal hours worked: {hrsTotal} hours")
print("Your Gross wages: ${g:1.2f}\n".format(g=grossWage))

#*  Exit Program
exit(0)
