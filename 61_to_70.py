# Q61) Armstrong Number
# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Input an integer from the user
num = int(input("Enter an integer: "))

# Check if the number is an Armstrong number
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Q62) Strong Number
import math

# Function to check if a number is a strong number
def is_strong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    # Calculate the sum of the factorials of the digits
    strong_sum = sum(math.factorial(int(digit)) for digit in num_str)
    # Check if the sum is equal to the original number
    return strong_sum == num

# Input an integer from the user
num = int(input("Enter an integer: "))

# Check if the number is a strong number
if is_strong_number(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")

# Q63) Perfect Number
# Function to check if a number is a perfect number
def is_perfect_number(num):
    # Calculate the sum of proper divisors
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    # Check if the sum of divisors is equal to the original number
    return divisors_sum == num

# Input an integer from the user
num = int(input("Enter an integer: "))

# Check if the number is a perfect number
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

# Q64) Sum of Digits
# Function to compute the sum of digits of an integer
def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum

# Input an integer from the user
num = int(input("Enter an integer: "))

# Compute the sum of digits
result = sum_of_digits(num)

print(f"The sum of the digits of {num} is: {result}")

# Q65) Binary to Decimal Conversion
# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Input a binary string from the user
binary_str = input("Enter a binary string: ")

# Convert the binary string to decimal
decimal_number = binary_to_decimal(binary_str)

print(f"The decimal equivalent of binary {binary_str} is: {decimal_number}")

# Q66) Decimal to Binary Conversion
# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

# Input a decimal integer from the user
decimal_num = int(input("Enter a decimal integer: "))

# Convert the decimal integer to binary
binary_str = decimal_to_binary(decimal_num)

print(f"The binary equivalent of decimal {decimal_num} is: {binary_str}")

# Q67) Prime Factors of a Number
# Function to find all prime factors of a number
def prime_factors(num):
    factors = []
    # Check for number of 2s that divide num
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    # num must be odd at this point, so we can skip even numbers
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i
    # This condition is to check if num is a prime number greater than 2
    if num > 2:
        factors.append(num)
    return factors

# Input an integer from the user
num = int(input("Enter an integer: "))

# Find the prime factors
factors = prime_factors(num)

print(f"The prime factors of {num} are: {factors}")

# Q68) Number to Words
# Function to convert a digit to its corresponding word
def digit_to_word(digit):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return words[digit]

# Function to convert a number to words
def number_to_words(num):
    if num == 0:
        return "zero"
    words = []
    while num > 0:
        words.append(digit_to_word(num % 10))
        num //= 10
    return " ".join(reversed(words))

# Input an integer from the user
num = int(input("Enter an integer: "))

# Convert the number to words
words = number_to_words(num)

print(f"The number {num} in words is: {words}")

# Q69) LCM of a Range
# Function to compute the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the LCM of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Function to compute the LCM of all numbers in a given range [1..n]
def lcm_of_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

# Input an integer from the user
n = int(input("Enter an integer n to compute the LCM of the range [1..n]: "))

# Compute the LCM of the range
result = lcm_of_range(n)

print(f"The LCM of the range [1..{n}] is: {result}")

# Q70) Sieve of Eratosthenes
# Function to implement the Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Input an integer from the user
n = int(input("Enter an integer n to find all prime numbers up to n: "))

# Find all prime numbers up to n
prime_numbers = sieve_of_eratosthenes(n)

print(f"All prime numbers up to {n} are: {prime_numbers}")