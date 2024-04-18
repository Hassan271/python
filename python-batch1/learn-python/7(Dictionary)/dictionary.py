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

# ==========================================================
car =	{
  "Company": "Honda",
  "Model": "city",
  "Number": "TN-4599",
  "Year": 2014
}
print(car["Company"])          # Access items in Dictionary 

x = car.get("year")          # get() Value  
print("get year from dictionary = ",x)                            

y = car.keys()              # keys() of dictionary  
print("Keys are = " ,y)                            

v = car.values()            # values() of dictionary  
print("values are = " ,v)                            

item = car.items()            # values() of dictionary  
print("items are = " ,item)                            

car["color"] = "white"
print("Add Color white in Dictionary ",car)


if "Model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")





