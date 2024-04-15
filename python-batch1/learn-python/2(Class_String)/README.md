# Class Topics

## Python Data Types
1. Numeric - **int**, **float**, **complex**
2. String - **str**
3. Boolean - **bool**
4. None - **NoneType**

## Built-in function type()
- type(123)
```
num1 = 123
result = type(123) 
print(result)
```

## Python Type Casting

- **Python Implicit** Casting
  language compiler/interpreter automatically converts object of one type into other, it is called automatic or implicit casting
  ``` 
  a=10   # int object 
  b=10.5 # float object
  ```

- **Python Explicit Casting**
Although automatic or implicit casting is limited to int to float conversion, you can use Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.
    ```
    a = int(10)
    a = float(9.99)
    a = str(10)
    ```

# Class 2: String Formatting and Definitions in Python with Static Typing

## Youtube link 
2 hours live session: https://youtube.com/live/rwDHhx76MMg
## Table of Contents

- [String Definitions](#string-definitions)
- [String Formatting](#string-formatting)
  - [Basic Techniques](#basic-techniques)
  - [Advanced Techniques](#advanced-techniques)
- [Naming Conventions](#naming-conventions)

## String Definitions

### Single Quotes

You can define a string with single quotes.

```python
my_string: str = 'Hello, World!'
```

### Double Quotes

Alternatively, you can define a string with double quotes.

```python
my_string: str = "Hello, World!"
```

### Triple Single Quotes

Triple single quotes allow for string definitions that span multiple lines.

```python
my_string: str = '''Hello,
World!'''
```

### Triple Double Quotes

Like triple single quotes, triple double quotes also allow for multi-line string definitions.

```python
my_string: str = """Hello,
World!"""
```

## String Formatting

### Basic Techniques

#### Using `%s` and `%d`

You can use `%s` for string and `%d` for integers.

```python
name: str = "Alice"
age: int = 30
print("My name is %s and I am %d years old." % (name, age))
```

#### Using `.format()`

The `.format()` method is another way to format your strings.

```python
name: str = "Alice"
age: int = 30
print("My name is {} and I am {} years old.".format(name, age))
```

#### Using f-string (Python 3.6+)

f-strings provide a concise and readable way to include the value of Python expressions inside strings.

```python
name: str = "Alice"
age: int = 30
print(f"My name is {name} and I am {age} years old.")
```

### Advanced Techniques

#### f-string Expressions

You can include Python expressions within f-strings.

```python
x: int = 10
y: int = 20
print(f"The sum of {x} and {y} is {x+y}.")
```

#### f-string with Format Specification

You can format numbers using f-strings.

```python
pi: float = 3.14159
print(f"Value of pi to 2 decimal places: {pi:.2f}")
```

## Naming Conventions

### Variables

- Use `snake_case` for variable names.
  
```python
my_variable: int = 10
```

### Constants

- Use `UPPER_SNAKE_CASE` for constants.

```python
PI: float = 3.14159
```

