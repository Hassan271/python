# Python Control Flow and Typing Guide

This guide provides an overview of Python's control flow structures including if, if-else, if-elif-else, and nested if-else-elif statements. Additionally, it covers the use of Python's static type variables, the `Union` and `Optional` types from the `typing` module, the `zip` function with lists, and sorting a list of tuples based on the second tuple index.

## Youtube link 
2 hours live session: https://youtube.com/live/ASNTpFSQHPo

## Table of Contents

- [If Statement](#if-statement)
- [If-Else Statement](#if-else-statement)
- [If-Elif-Else Statement](#if-elif-else-statement)
- [Nested If-Else-Elif](#nested-if-else-elif)
- [Static Type Variables](#static-type-variables)
- [Union and Optional Types](#union-and-optional-types)
- [Zip Function with Lists](#zip-function-with-lists)
- [Sorting a List of Tuples](#sorting-a-list-of-tuples)

## If Statement

```python
x: int = 10
if x > 5:
    print("x is greater than 5")
```

## If-Else Statement

```python
x: int = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## If-Elif-Else Statement

```python
x: int = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Nested If-Else-Elif

```python
x: int = 10
y: int = 5
if x > 5:
    if y > 5:
        print("x and y are both greater than 5")
    else:
        print("x is greater than 5 but y is not")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Static Type Variables

In Python 3.6 and later, you can use static type annotations to indicate the expected type of a variable.

```python
x: int = 10
y: str = "Hello"
z: float = 3.14
```

## Union and Optional Types

`Union` allows a variable to be one of several types. `Optional` is a shorthand for `Union[T, None]`.

```python
from typing import Union, Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"

age: Union[int, str] = "Twenty"
print(greet())
print(greet("John"))
```

## Zip Function with Lists

The `zip` function is used to combine two or more iterables.

```python
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 30, 35]

zipped = zip(names, ages)
for name, age in zipped:
    print(f"{name} is {age} years old")
```

## Sorting a List of Tuples

You can sort a list of tuples based on the second tuple index using the `sorted` function.

```python
tuples: list[tuple[str, int]] = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```


<!-- Naveed Lec ----------------------------------- -->
# Class Topics
- Decision-making Statements
- The if Statement
- The match Statement
``` match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number" ```


## Python - Lists
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

### Python List Operations
Python Expression	
Concatenation
[1, 2, 3] + [4, 5, 6]	  [1, 2, 3, 4, 5, 6]	
Repetition
['Hi!'] * 4	  ['Hi!', 'Hi!', 'Hi!', 'Hi!']
Membership
3 in [1, 2, 3]	True	


Addition Checker:

Input: Two numbers (e.g., 7, 5)
Output: Sum of the numbers (e.g., 12)
Even or Odd Detector:

Input: A number (e.g., 9)
Output: Whether the number is even or odd (e.g., Odd)
Positive Product Finder:

Input: Two numbers (e.g., -4, 3)
Output: Product of the numbers if both are positive; otherwise, display a message (e.g., "Product is: 12" or "One of the numbers is not positive.")
Minimum Value Identifier:

Input: Three numbers (e.g., 2, 8, 5)
Output: The smallest number (e.g., 2)
Currency Converter:

Input: Amount in USD (e.g., 50)
Output: Equivalent amount in Euros (use a fixed conversion rate, e.g., 1 USD = 0.85 Euros)
Square or Rectangle Recognizer:

Input: Two side lengths (e.g., 4, 4)
Output: Whether the shape is a square or a rectangle (e.g., Square)
Positive Difference Calculator:

Input: Two numbers (e.g., 9, 4)
Output: The positive difference between the numbers (e.g., 5)
Simple Interest Calculator:

Input: Principal amount, interest rate, and time (e.g., P=1000, R=5%, T=2 years)
Output: Simple interest calculated (e.g., 100)
Vowel Counter:

Input: A word (e.g., "programming")
Output: Number of vowels in the word (e.g., 3)
Character Replacer:

Input: A sentence and a character to replace (e.g., "Hello, world!", 'o')
Output: Sentence with the specified character replaced (e.g., "Hell*, w*rld!")