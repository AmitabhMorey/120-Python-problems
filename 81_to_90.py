# Q81) Create a Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)
print(f"The area of the rectangle is: {rectangle.area()}")
print(f"The perimeter of the rectangle is: {rectangle.perimeter()}")

# Q82) Class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

# Example usage
radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)
print(f"The area of the circle is: {circle.area()}")
print(f"The circumference of the circle is: {circle.circumference()}")

# Q83) Class BankAccount
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        return self.balance

# Example usage
account = BankAccount()

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        print(f"Current balance: {account.check_balance()}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Q84) Class Student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

# Example usage
student = Student("John Doe", "12345")

while True:
    print("\n1. Add Grade\n2. Calculate Average Grade\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        grade = float(input("Enter grade to add: "))
        student.add_grade(grade)
    elif choice == '2':
        print(f"Average grade: {student.average_grade()}")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

# Q85) Class Car and Inheritance

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def car_info(self):
        return f"{super().car_info()} with a {self.battery_size}-kWh battery"

# Example usage
car = Car("Toyota", "Corolla", 2020)
print(car.car_info())

electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
print(electric_car.car_info())

# Q86) Class ComplexNumber

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Example usage
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(f"Complex number 1: {c1}")
print(f"Complex number 2: {c2}")

c3 = c1 + c2
print(f"Sum: {c3}")

c4 = c1 - c2
print(f"Difference: {c4}")

# Q87) Class Point

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example usage
point1 = Point(3, 4)
point2 = Point(6, 8)

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")

distance = point1.distance_from(point2)
print(f"Distance between Point 1 and Point 2: {distance}")

# Setting new coordinates for point1
point1.set_coordinates(1, 2)
print(f"New coordinates of Point 1: {point1}")

# Q88) Classmethod and Staticmethod

class MyClass:
    def __init__(self, value):
        self.value = value

    # Regular instance method
    def instance_method(self):
        return f"Instance method called. Value: {self.value}"

    # Class method
    @classmethod
    def class_method(cls):
        return "Class method called."

    # Static method
    @staticmethod
    def static_method():
        return "Static method called."

# Example usage
obj = MyClass(10)

# Calling the instance method
print(obj.instance_method())

# Calling the class method
print(MyClass.class_method())
print(obj.class_method())  # Can also be called on the instance, but it doesn't use the instance

# Calling the static method
print(MyClass.static_method())
print(obj.static_method())  # Can also be called on the instance, but it doesn't use the instance

# Q89) Property Decorators

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    # Deleter for age
    @age.deleter
    def age(self):
        del self._age

# Example usage
person = Person("John Doe", 30)

# Accessing the age using the getter
print(f"Person's age: {person.age}")

# Setting the age using the setter
person.age = 35
print(f"Updated age: {person.age}")

# Trying to set a negative age (will raise an exception)
try:
    person.age = -5
except ValueError as e:
    print(e)

# Deleting the age attribute
del person.age
try:
    print(person.age)
except AttributeError:
    print("Age attribute has been deleted.")

# Q90) Class Employee with Inheritance

class Employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def display_info(self):
        return f"Employee Name: {self.name}, ID: {self.ID}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, ID, salary, department, team_size):
        super().__init__(name, ID, salary)
        self.department = department
        self.team_size = team_size

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Department: {self.department}, Team Size: {self.team_size}"

# Example usage
employee = Employee("Alice", "E123", 50000)
print(employee.display_info())

manager = Manager("Bob", "M456", 80000, "IT", 10)
print(manager.display_info())