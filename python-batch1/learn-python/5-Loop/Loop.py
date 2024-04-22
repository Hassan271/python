
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

#  ==============================================================

# import sys

# print("line1")
# print("line2")

# print(type(sys.argv)) 

# if sys.argv[1] == '-g':
#     print("I will install this package on globally in your system!")

# print(sys.argv) # iterative data type list[str] 0=filename **value user define




# For Loop ==============================================

# nums=[1,2,3,4,5,6,7,8,9,10]
# for item in nums:
#     print("print Numbers: ", item)


# for j in range(0,20,4):
#     print("for Loop Range: ", j)


# Alphabet=["a","b","c","d","e"]
# for k in Alphabet:
#     if k == "d":
#         print("print Alphabet: ", k[i])
#         break
    


# nums = [10,11,30,13,50,19,70,80]
# def multi(item):
#     return item 
# newList = list(filter(multi, nums))
# print(newList)


# def multi(item):
#     if item % 2 == 0:
#       return item * 2
#     else:
#         return item
# newList = list(map(multi, nums))
# print(newList)


# userNames = ["Naveed", "john", "Alice", "Ali", "Umar", "Umair"]
# def changeUserNames(item):
#     print(item)
#     return f"Hello {item}"
# newNames = list(map(changeUserNames,userNames))

# print(newNames)  


# for index, item in  enumerate(userNames):
#     print("loop runing", item, index)
#     if item == "Ali":
#         print("Search is found", item ,index ) 
#         break

# for item in  range(0, len(userNames)):
#     print("loop runing", item)
#     if userNames[item] == "Ali":
#         print("Search is found", userNames[item] ,item ) 
#         break
    

# nums = [10,20,30,40,50,60,70,80]
# i = 0
# while i < len(nums):
#     print ("Hello world - while", nums[i])
#     i = i + 1
# write a search program, search the name ali from the list userName if ali found please stop the loop, print ali

    
# output  = list(range(10,50,2))
# print("output",output)

# for j in range(0,10,4):
#     print("for loop range j", j)