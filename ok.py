# Python Program Demonstrating Grammar and Common Features

# 1. Importing Libraries
import math
import random

# 2. Variables and Data Types
integer_var = 10
float_var = 3.14
string_var = "Hello, Python!"
boolean_var = True

# 3. Data Structures
list_var = [1, 2, 3, 4, 5]
tuple_var = (6, 7, 8)
set_var = {9, 10, 11}
dict_var = {'name': 'Alice', 'age': 25}

# 4. Control Structures
# If-Else
if integer_var > 5:
    print("Integer is greater than 5")
else:
    print("Integer is 5 or less")

# For Loop
for item in list_var:
    print(f"List item: {item}")

# While Loop
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# 5. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))

# 6. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person1 = Person("Bob", 30)
person1.introduce()

# 7. List Comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# 8. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 9. File Handling
with open("sample.txt", "w") as file:
    file.write("Hello, file!")

# 10. Lambda Functions
multiply = lambda x, y: x * y
print(multiply(3, 4))

# 11. Using Standard Libraries
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

circle_area = math.pi * (5 ** 2)
print(f"Area of circle with radius 5: {circle_area:.2f}")
