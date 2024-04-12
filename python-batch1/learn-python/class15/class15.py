
# ========================================

# class Car:
#     def __init__(self):
#         self.brand = "Honda"
#         self.model = "IVTech 2014"
#         self.price =  4500000
     
#     def drive(self, driver):
#         mybrand = self.brand

#         return driver + "Start driving" + mybrand

# car1 = Car()
# print(car1)  # Output: 20


class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.model = price
        self.price =  4500000
     
    def drive(self, driver):
        mybrand = self.brand

        return driver + "Start driving" + mybrand

car1 = Car("Honda", 4500000)
print(car1.brand)  # Output: Honda

# # ========================================

# class Animal:
#     def sound(self):
#         pass
    

# class Dog(Animal):
#     def sound(self):
#         self.__name = "Dog"
#         return "Woof!"

# class Cat(Animal):
#     def sound(self):
#         return "Meow!"

# def make_sound(animal):
#     print(animal.sound())

# dog = Dog()
# cat = Cat()
# make_sound(dog)  # Output: Woof!
# make_sound(cat)  # Output: Meow!

# # ========================================

# class Person:
#    def setProperties(self):
#        pass
    
#    def getProperty(self):
#        pass

# class Student(Person):
#     def __init__(self, rollNo, name):
#         self.rollNo = rollNo
#     def getRollNo(self):
#         return self.rollNo
#     def setProperties(self, name):
#         self.name = name
#         return self.name
#     def getProperty(self):
#         return self.name
        

# obj = Student(2342, "Ali")
# obj.setProperties("Naveed")
# obj.getProperty()
# obj.getRollNo()
# obj.rollNo

# # obj = Person("Ali")
# # print(obj.getProperty())
# # obj.setProperties("Naveed")
# # username = obj.getProperty()
# # print(username)

# # ========================================
