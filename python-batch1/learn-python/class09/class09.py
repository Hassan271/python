
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
