# Dictionaries are used to store data values in key:value pairs.


# from typing import Dict, Union, Optional
# import pprint


# Key = Union[int,str] # create custom type
# Value = Union[int, str, list, dict, tuple, set]

# # List                    0                1            2
# data : Dict[Key,Value] = {
#                         "fname":"Muhammad Aslam",
#                         "name":"Muhammad Qasim",
#                         "education": "MSDS"
#                         }

# pprint.pprint(data)


# ==========================================================
# dictionary1 =	{
#   "A": "Apple",
#   "B": "Bat",
#   "year": 1964,
#   "year": 1994                  # Dublication Not Allowed 
# }
# print(dictionary1)

# print(dictionary1["A"])

# print(len(dictionary1))         # Length 
# print(type(dictionary1))        # Data Type 

# # ==========================================================
# car =	{
#   "company": "Honda",
#   "model": "city",
#   "number": "TN-4599",
#   "year": 2014
# }
# print(car["company"])          # Access items in Dictionary 

# x = car.get("year")          # get() Value  
# print("get year from dictionary = ",x)                            

# y = car.keys()              # keys() of dictionary  
# print("Keys are = " ,y)                            

# v = car.values()            # values() of dictionary  
# print("values are = " ,v)                            

# item = car.items()            # values() of dictionary  
# print("items are = " ,item)                            


# car["color"] = "white"
# print("Add Color white in Dictionary ",car)


# if "Model" in car:
#   print("Yes, 'model' is one of the keys in the car dictionary")

# car["year"] = 2018
# print("year has been changed from 2014 to = " ,car)

# car.update({"year": 2020})
# print("again year has been changed from 2018 to = " ,car)

# # del car["color"]
# car.pop("color")
# print("color has been changed Removed from Dictionary = " ,car)

# # car.clear()
# # print("clear the Dictionary = " ,car)

# for a in car:
#     print("Loop is = ",a)

# carCopy = car.copy()
# print(carCopy)


# # Access Nested ============================================
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)

# # Loop Through Nested Dictionaries-----------------------------

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])
        
        
        
# # class 8 -----------------------------
# from flask import Flask
# from flask import jsonify

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     d = {'left': 0.17037454, 'right': 0.82339555, '_unknown_': 0.0059609693}
#     message = {
#         'status': 200,
#         'message': 'OK',
#         'scores': d
#     }
#     resp = jsonify(message)
#     print(type(resp))
#     resp.status_code = 200
#     print(resp)
#     return resp

# if __name__ == '__main__':
#     app.run()