# Python Static Typing for Dictionaries

This guide demonstrates the creation of dictionaries in Python using static typing. We'll explore dictionaries with different hashable key types and values of type `Any`, `Optional`, and `Union`. Additionally, we'll use dictionary comprehensions and demonstrate swapping keys and values.

## YouTube link
[2 hour live session](https://youtube.com/live/u0K3m7ZAUnI)

## Table of Contents
1. [Setting up Static Typing](#setting-up-static-typing)
2. [Creating Dictionaries](#creating-dictionaries)
    - [Using `Any` Type](#using-any-type)
    - [Using `Optional` Type](#using-optional-type)
    - [Using `Union` Type](#using-union-type)
3. [Dictionary Comprehensions](#dictionary-comprehensions)
4. [Swapping Keys and Values](#swapping-keys-and-values)

## Setting up Static Typing

To use static typing in Python, we'll need to import the required types from the `typing` module. For this guide, we're specifically interested in `Any`, `Optional`, and `Union`.

```python
from typing import Any, Optional, Union
```

## Creating Dictionaries

### Using `Any` Type

`Any` is the most flexible type. It can represent any type at all. Here's how to create a dictionary with keys of any hashable type and values of any type:

```python
from typing import Dict

my_dict: Dict[Any, Any] = {
    1: "one",
    "two": 2,
    (3, 4): [3, 4]
}
```

### Using `Optional` Type

`Optional` is a shorthand for a value that can either be of a specific type or `None`.

```python
from typing import Dict

my_optional_dict: Dict[Any, Optional[int]] = {
    1: 10,
    "two": None,
    (3, 4): 34
}
```

### Using `Union` Type

`Union` type allows us to specify that a value can be one of several types.

```python
from typing import Dict

my_union_dict: Dict[Any, Union[int, str]] = {
    1: "one",
    "two": 2,
    (3, 4): "three-four"
}
```

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries.

```python
squared_numbers = {i: i**2 for i in range(5)}
```

## Swapping Keys and Values

To swap the keys and values of a dictionary:

```python
swapped_dict = {v: k for k, v in my_dict.items()}
```


# Python Dictionary Guide

This guide provides an overview of how to work with dictionaries in Python, including how to create dictionaries, access values, add key-value pairs, and use various dictionary methods.

## YouTube link
[2 hour live session](https://youtube.com/live/5HswPZa8iDA)

## Table of Contents
1. [Introduction to Dictionaries](#introduction-to-dictionaries)
2. [Creating a Dictionary](#creating-a-dictionary)
3. [Accessing Values](#accessing-values)
4. [Adding Key-Value Pairs](#adding-key-value-pairs)
5. [Dictionary Methods](#dictionary-methods)
    - [clear](#clear)
    - [copy](#copy)
    - [fromkeys](#fromkeys)
    - [get](#get)
    - [items](#items)
    - [keys](#keys)
    - [pop](#pop)
    - [popitem](#popitem)
    - [setdefault](#setdefault)
    - [update](#update)
    - [values](#values)
6. [Conclusion](#conclusion)

## Introduction to Dictionaries
Dictionaries in Python are a collection of key-value pairs, where each key is unique. They are mutable, meaning you can change their content without changing their identity.

## Creating a Dictionary
You can create a dictionary by enclosing a comma-separated sequence of key-value pairs in curly braces `{}`, with a colon `:` separating the keys and values.

```python
from typing import Dict

my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}
print(my_dict)  # Output: {'apple': 5, 'banana': 3}
```

## Accessing Values
You can access the value associated with a specific key using the square bracket `[]` notation.

```python
value = my_dict['apple']
print(value)  # Output: 5
```

## Adding Key-Value Pairs
Adding a key-value pair to the dictionary is straightforward.

```python
my_dict['cherry'] = 7
print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
```

## Dictionary Methods
### clear
Removes all the elements from the dictionary.

```python
my_dict.clear()
print(my_dict)  # Output: {}
```

### copy
Returns a shallow copy of the dictionary.

```python
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
```

### fromkeys
Creates a new dictionary with keys from a sequence and values set to a specified value.

```python
sequence = ('apple', 'banana', 'cherry')
new_dict = dict.fromkeys(sequence, 0)
print(new_dict)  # Output: {'apple': 0, 'banana': 0, 'cherry': 0}
```

### get
Returns the value for a specified key if the key is in the dictionary.

```python
value = my_dict.get('apple', 'Not Found')
print(value)  # Output: 5
```

### items
Returns a view object that displays a list of dictionary's key-value tuple pairs.

```python
items = my_dict.items()
print(items)  # Output: dict_items([('apple', 5), ('banana', 3), ('cherry', 7)])
```

### keys
Returns a view object that displays a list of all the keys in the dictionary.

```python
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['apple', 'banana', 'cherry'])
```

### pop
Removes the element with the specified key.

```python
my_dict.pop('apple')
print(my_dict)  # Output: {'banana': 3, 'cherry': 7}
```

### popitem
Removes the last inserted key-value pair.

```python
my_dict.popitem()
print(my_dict)  # Output: {'banana': 3}
```

### setdefault
Returns the value of the specified key. If the key does not exist, insert the key, with the specified value.

```python
value = my_dict.setdefault('banana', 6)
print(value)  # Output: 3
```

### update
Updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.

```python
my_dict.update({'banana': 4})
print(my_dict)  # Output: {'banana': 4}
```

### values
Returns a view object that displays a list of all the values in the dictionary.

```python
values = my_dict.values()
print(values)  # Output: dict_values([4])
```

## Conclusion
Dictionaries are a versatile way to store and manipulate data in Python. This guide has covered the basics, as well as a variety of methods that can be used to work with dictionaries.



## ======================================

# Class Topics

## Python - loops
```
list = [2,30,30,50]
for i in list:
    print(i)


list = [2,30,30,50]
for i,item in enumerate(list, start=10):
    print(f"{i},{item}")


    for i in range(1,10,2):
    for j in range(1,10,2):
        print(i,j)

list3 = [2,30,30,50]
list2 = [203,3023,3023,32450]
def sumCal(i):
    print(i)
    return i * 2
output = list(filter(sumCal, list3))
print(output)
```
