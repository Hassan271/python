# Python Lists and Their Methods

In this guide, we'll explore Python lists, their features, and the available methods. Lists are one of the most versatile and commonly used data types in Python.

## Youtube link 
2 hours live session: https://youtube.com/live/NzFLZkVtwMw

## Table of Contents

1. [Introduction to Lists](#introduction-to-lists)
2. [Indexing](#indexing)
3. [Slicing](#slicing)
4. [Positive and Negative Indexing](#positive-and-negative-indexing)
5. [List Methods in Python](#list-methods-in-python)

## Introduction to Lists

A list in Python is an ordered collection of items. Lists can contain a mix of different data types, including numbers, strings, and other lists. Lists are created by placing the items inside square brackets `[]`, separated by commas.

Example:
```python
fruits = ["apple", "banana", "cherry"]
```

## Indexing

You can access individual items in a list using an index. Indices start at 0 for the first item, 1 for the second, and so on.

Example:
```python
print(fruits[0])  # Outputs: apple
```

## Slicing

Slicing allows you to obtain a subset of items from a list. The syntax for slicing is `list[start:stop:step]`.

Example:
```python
print(fruits[1:3])  # Outputs: ['banana', 'cherry']
```

## Positive and Negative Indexing

- **Positive Indexing**: Starts from the beginning of the list.
  
  Example:
  ```python
  print(fruits[1])  # Outputs: banana
  ```

- **Negative Indexing**: Starts from the end of the list.
  
  Example:
  ```python
  print(fruits[-1])  # Outputs: cherry
  ```

## List Methods in Python

Python lists come with a set of built-in methods:

- `append()`: Adds an element to the end of the list.
- `clear()`: Removes all elements from the list.
- `copy()`: Returns a copy of the list.
- `count()`: Returns the number of elements with the specified value.
- `extend()`: Adds elements from another list (or any iterable) to the current list.
- `index()`: Returns the index of the first element with the specified value.
- `insert()`: Adds an element at a specified position.
- `pop()`: Removes the element at a specified position.
- `remove()`: Removes the first item with the specified value.
- `reverse()`: Reverses the order of the list.
- `sort()`: Sorts the list.

For more details and examples on each method, refer to the [official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).


list1 = ["Rohan", "Physics", 21, 69.75] list2 = [1, 2, 3, 4, 5] list3 = ["a", "b", "c", "d"]

Python List Operations
Python Expression Concatenation [1, 2, 3] + [4, 5, 6] [1, 2, 3, 4, 5, 6] Repetition ['Hi!'] * 4 ['Hi!', 'Hi!', 'Hi!', 'Hi!'] Membership 3 in [1, 2, 3] True

Creating Lists: You can create a list by enclosing a comma-separated sequence of items within square brackets []. For example:
my_list = [1, 2, 3, 'four', 5.0] 2. Accessing Elements: Indexing: Lists are zero-indexed, meaning the first element has an index of 0. You can access elements using positive or negative indexing.

first_element = my_list[0] # Accessing the first element last_element = my_list[-1] # Accessing the last element Slicing: You can extract a sublist by specifying a range of indices.

sublist = my_list[1:4] # Extract elements at index 1, 2, and 3 3. List Methods: append(): Adds an element to the end of the list.

my_list.append(6) extend(): Appends the elements of another iterable to the end of the list.

another_list = [7, 8, 9] my_list.extend(another_list) insert(): Inserts an element at a specified position.

my_list.insert(2, 'inserted') remove(): Removes the first occurrence of a specified value.

my_list.remove(3) pop(): Removes and returns an element at a specified index (or the last element if no index is specified).

popped_element = my_list.pop(4) index(): Returns the index of the first occurrence of a specified value.

index_of_four = my_list.index('four') count(): Returns the number of occurrences of a specified value.

count_of_2 = my_list.count(2) sort(): Sorts the elements of the list in ascending order.

my_list.sort() reverse(): Reverses the order of the elements in the list.

my_list.reverse() clear(): Removes all elements from the list.

my_list.clear()

List Concatenation: You can concatenate lists using the + operator.
concatenated_list = my_list + another_list

List Copying: Be cautious when copying lists, as simple assignment (new_list = old_list) creates a reference, not a new copy. To create a copy, you can use the copy() method or the built-in list() constructor.
copied_list = my_list.copy()

List Length: The len() function returns the number of elements in a list.
length_of_list = len(my_list)

List Membership: You can check if an element is present in a list using the in keyword.
is_present = 3 in my_list

List as Stack or Queue: You can use lists as a basic stack (Last In, First Out) or queue (First In, First Out).
Stack my_list.append(10) # Push popped_item = my_list.pop() # Pop

Queue my_list.append(10) # Enqueue dequeued_item = my_list.pop(0) # Dequeue 11. Nested Lists: Lists can contain other lists, creating nested structures.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

python-genai-batch1/learn-python/class08/README.md at master · techloset/python-genai-batch1 


## =======================================
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
