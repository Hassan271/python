
# ->                    0        1         2
names : list[str] = ["Qasim","Sir Zia", "Sir Inam"]
# <-                    -3     -2          -1

print(names[-2])

# input List of num and create a new List  ==============================================================

i = 0
inputList = [10,20,19, 18,30,40,50,255, 333]
evenSum = 0
oddSum = 0
print("before while")
while i < len(inputList):
    if inputList[i] % 2 == 0:
        evenSum = evenSum + inputList[i]
    else:
        oddSum = oddSum + inputList[i]
    i += 1
print("even",evenSum, "odd", oddSum )

# ==============================================================

# i=1
# print("before while Loop")
# while i<6:
#     print("Print Hello World!")
#     i+=1
#     print("After While Loop")
    
# ==============================================================
    
# i=1
# print("before while Loop")
# while i<11:
#     print("Print", i)
#     i+=1
#     print("After While Loop")
    
#     i=11
# print("before while Loop")
# while i>1:
#     print("Print", i)
#     i-=1
#     print("After While Loop")

# Table ==============================================================

# num = int( input("Enter table Number : "))
# i=1
# print("before Loop")
# while i< 11:
#     print(num, "*", i, "=", num*i)
#     i+=1
#     print("After Loop")



student1 = "zain"
student2 = "Umar"
student3 = "ali"
listOfNumbers = [10,20,30]
studentNames = ["zain","umar", "ali", "usman", "umar", "umair"]
studentNames[1] = "new name"
output = studentNames[0:-3]
print( "output", output )
# nestedStudent= ["zain","ali", ["usman","Naveed"]]
# 
# output = ['Hi!'] * 4
# output = student1 in studentNames
# output = studentNames + listOfNumbers
# studentNames.append("Naveed")
# output = len(studentNames)
# output = studentNames.clear()
# output = studentNames.reverse()
# output = studentNames.sort()
# output = studentNames.count("Zain")
# output = studentNames.index("usman")
# output = studentNames.remove("umar")
# output = studentNames.insert(6,"Naveed")

# result = studentNames.append("Naveed Sarwar")
# output = studentNames.pop()
# output1 = studentNames.extend(listOfNumbers)

# print(studentNames)

# Function ==============================================
# print("before Add function")
# def Add(num1,num2, num3 = 25, a=4):
#    print("a ->", num1, "b ->", num2)
#    result =  num1 + num2 + num3 + a
#    print(result)
# Add(10,20,5)
# print("After Add function")
# Add(50,100,6,10)
# Add(100,200,7,10)

#  ==============================================

# nums = [10,20,30,40,50,20]

# nums = list(set(nums))
# print(nums)


# =========================================================
# if an Email exist in database so it alert Email already exist 

studentEmails = ["test@test.com", "test2@test.com", "test3@test.com"]
newEmail = "test1@test.com"

"n" in ["naveed"]
"n" not in "naveed"

if newEmail not in studentEmails:
    studentEmails.append(newEmail)
print(studentEmails)
# =========================================================
# studentEmailsSet  = {"test1@test.com", "test2@test.com", "test3@test.com", "test1@test.com"}
# studentEmailsSet.add("test1@test.com")
# studentEmailsSet.remove("test2@test.com")
# studentEmailsSet.update("test1@test.com", "test5@test.com")
# print(studentEmailsSet)

# Tuple ================================
# A tuple is a collection which is ordered and unchangeable.


# thistuple = ("one", "Two", "Three","Four","Five")
# print(thistuple)        #  ('one', 'Two', 'Three', 'Four', 'Five')
# print(len(thistuple))   #  5
# print(type(thistuple,)) # <class 'tuple'>


# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# print(tuple1)
# print(tuple2)
# print(tuple3)

# It is also possible to use the tuple() constructor to make a tuple.
# tuple4 = tuple(("one", "Two", "Three","Four","Five"))
# print(tuple4)












