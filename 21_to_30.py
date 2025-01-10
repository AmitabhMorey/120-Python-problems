# Q21) Create a Simple Calculator (Functions)
# Simple Calculator

def add(x, y):
  """This function adds two numbers"""
  return x + y

def subtract(x, y):
  """This function subtracts two numbers"""
  return x - y

def multiply(x, y):
  """This function multiplies two numbers"""
  return x * y

def divide(x, y):
  """This function divides two numbers"""
  if y == 0:
    return "Cannot divide by zero"
  else:
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
  # Take input from the user
  choice = input("Enter choice(1/2/3/4): ")

  # Check if choice is one of the four options
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

    # Check if user wants another calculation
    next_calculation = input("Let's do next calculation? (y/n): ").lower()
    if next_calculation in ('n', 'no'): 
      break
  else:
    print("Invalid Input")

# Q22) Power Function
# Write a function power(base, exponent) that returns base^exponent without using the built-in ** operator (use a loop).
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(power(base, exponent))

# Q23) Count Characters in a String (Function)
def count_characters(s):
    return len(s)

s = input("Enter a string: ")
print(f"The number of characters in the string is: {count_characters(s)}")

# Q24) Check Prime (Function)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number to check if it is prime: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

# Q25) Fibonacci Series (Function)
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")

# Q26) GCD of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")

# Q27) LCM of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The LCM of {a} and {b} is: {lcm(a, b)}")

# Q28) Factorial (Recursive)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number to compute its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")

# Q29) Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')

# Q30) Count Occurrences of an Element
def count_occurrences(lst, x):
    return lst.count(x)

lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
x = int(input("Enter the number to count occurrences of: "))
print(f"The number {x} appears {count_occurrences(lst, x)} times in the list.")