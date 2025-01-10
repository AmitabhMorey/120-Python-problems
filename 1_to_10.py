# Q1) Print Hello World
print("Hello World")

# Q2) Variables and Data Types
m = int(input("Enter a name: "))
n = int(input("Enter a age: "))
print("Your name is", m, "and your age is", n)

# Q3) Arithmetic Operations
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Sum:", a+b)
print("Difference:", a-b)
print("Product:", a*b)
print("Quotient:", a/b)
print("Remainder:", a%b)

# Q4) Convert Celsius to Fahrenheit
c = int(input("Enter temperature in Celsius: "))
f = (c*9/5)+32
print("Temperature in Fahrenheit:", f)

# Q5) Swap two numbers
s = int(input("Enter a number: "))
t = int(input("Enter another number: "))
s, t = t, s
print("Numbers after swapping:", s, t)

# Q6) Even or Odd
e = int(input("Enter a number: "))
if e%2 == 0:
    print("Even")
else:
    print("Odd")

# Q7) Check vowel or consonant
v = input("Enter a character: ")
if v in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# Q8) Square, Cube, and Square Root
d = int(input("Enter a number: "))
print("Square:", d**2)
print("Cube:", d**3)
print("Square Root:", d**0.5)

# Q9) Area of Circle
r = int(input("Enter radius of circle: "))
print("Area of circle: ", 3.14159*r**2)

# Q10) Simple Interest Calculation
s = int(input("Enter a principal amount: "))
t = int(input("Enter time in years: "))
r = int(input("Enter rate of interest: "))
print("Simple Interest: ", (s * t * r/100))