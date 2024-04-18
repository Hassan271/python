# write a program that take the user input number,
# and verify it's even, if it's even check number is
# greater than 50, if so print the numer


# isEven = num1 % 2 == 0
# if num1 == 0:
#    print ("Number is zero")
# elif isEven:
#    print ("Number is even")
# else:
#    print ("Number is odd")

# write a prgram that takes user input of 3 numbers, and find the largest number

# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# num3 = int(input("Enter number3: "))

# if num1 > num2 and num1 > num3: 
#    print ("Number1 is greater", num1)
# elif num2 > num3 and num2 > num1:
#    print ("Number2 is greater", num2)
# else:
#    print ("Number3 is greater", num3)
   
   
# write a program that takes 3 numbers from user and make sum and verify sum is positive negative or zero

# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# num3 = int(input("Enter number3: "))

# sum = num1 + num2 + num3
# if sum > 0:
#    print ("Number is positive",sum)
# elif sum < 0: 
#    print ("Number is negative", sum)
# else: 
#    print("number is zero", sum)

# write a program that take input from user
# number of units, and calculate their electric
# bill, rate of unit  is 41.13, add tax 20% if more 200 units

# units = int(input("Enter units: "))
# bill = units * 41.33
# if units > 200: 
#    bill = bill + bill * 20 / 100
# print("Your outstanding bill is => ", int(bill))

# write a program, that takes the students score in english, urdu, math, science, and calculate student grade, marks more than 90 should be A+ grade and vice versa

# english = int(input("Enter english score: "))
# urdu = int(input("Enter urdu score: "))
# math = int(input("Enter math score:"))
# science = int(input("Enter science score"))

# percentage = (english + urdu + science + math)/ 400 * 100

# if percentage >= 90: 
#    print("Your grade is A+")
# elif percentage >= 80:
#    print("Your grade is A")
# elif percentage >= 70: 
#    print("Your grade is B")
# elif percentage >= 60:
#    print("Your grade is C")
# else:
#    print("Oh Sorry! you are fail, try luck again!")
   
   
   
#    ------------------------------
from typing import Union
PerType = Union[float, int]

percentages : list[PerType] = [88, 99.9, 50, 51,65,70]

grades : list[str] = []

for per in percentages:
    grade : str = ""

    if (per >= 0) and (per < 33):
        grade = "Fail"
    elif (per >= 33) and (per < 40):
        grade = "E"
    elif (per >= 40) and (per < 50):
        grade = "D"
    elif (per >= 50) and (per < 60):
        grade = "C"
    elif (per >= 60) and (per <70) :
        grade = "B"
    elif (per >= 70) and (per <80) :
        grade = "A"
    elif (per >=80) and (per <= 100):
        grade = "A+"

    grades.append(grade)

print(percentages)
print(grade)

    

# # Naveed Lec =========================================


# print("line1")
# print("line2")
# if 2==3: 
#     print("line3")
#     print("line10")
#     if 5 == 2: 
#         print("nested if")
#     elif 5 == 5: 
#         print("nested else if")
        
# elif 5 == 5:
#     print("elif")
# else: 
#     print("else line")
# def printSomething():
#     print("line4")
#     if 2 == 2:
#       print("line5")


# n = int(input("Enter week day number"))

# if n == 1: 
#     print("Monday")
# elif n == 2:
#     print("Tuesday")
# elif n == 3:
#     print("Wednesday")
# elif n == 4:
#     print("Thursday")
# elif n == 5:
#     print("Friday")
# elif n == 6:
#     print("Saturday")
# elif n==7:
#     print("Sunday")
# else: 
#     print("not a vaild number")

# match n:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
        

     

# day = input("Enter week day")
# match day:
#     case "Monday":
#         print(1)
#     case "Tuseday":
#         print(2)
#     case _:
#         print("default value")





