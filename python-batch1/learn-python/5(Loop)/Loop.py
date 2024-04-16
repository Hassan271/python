# A for loop is used for iterating over a sequence ==========================

Letters = ["A", "B", "C", "D", "E"]
for x in Letters:
   print(x)
   
# Looping Through a String===================================================
# Even strings are iterable objects, they contain a sequence of characters:

# for x in "horse":
#   print(x)
  
# Break Statement==================================================

# Letters = ["A", "B", "C", "D", "E", "F", "G"]
# for x in Letters:
#    print(x)
#    if x == "D":
#       break
   
# Continue Statement==================================================

# Letters = ["A", "B", "C", "D", "E", "F", "G"]
# for x in Letters:
#    if x == "D":
#       continue
#    print(x)
   
   
# range() Function================================================
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# for x in range(10):
#   print(x) 

# Range between  ============

# for x in range(2, 6):
#   print(x) 

# Range from 2 to 30 and plus of 3 =================

# for x in range(2, 30, 3):
#   print(x) 
  
  
# else in For Loop==================
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
  

# break =========================

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# #If the loop breaks, the else block is not executed.


# Nested Loop=============================
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Letters1 = ["A", "B", "C", "D", "E"]
# Letters2 = ["F", "G", "H", "I", "J"]

# for x in Letters1:
#    for y in Letters2:

#       print(x,y)
      
# Pass Statement ===============================
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# for x in [0, 1, 2]:
#   pass

# # having an empty for loop like this, would raise an error without the pass statement


