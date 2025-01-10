# # Q11) Largest of three numbers.
# d = int(input("Enter first number: "))
# l = int(input("Enter second number: "))
# q = int(input("Enter third number: "))
# if d > l and d > q:
#     print("The largest number is: ", d)
# elif l > d and l > q:
#     print("The largest number is: ", l)
# else:
#     print("The largest number is: ", q)

# # Q12) Leap Year Checker.
# l = int(input("Enter the year: "))
# if l % 4 == 0:
#     if l % 100 == 0:
#         if l % 400 == 0:
#             print("The year is a leap year.")
#         else:
#             print("The year is not a leap year.")
#     else:
#         print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")

# # Q13) Multiplication Table.
# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# # Q14) Sum of N natural numbers.
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("The sum of first", n, "natural numbers is: ", sum)

# # Q15) Factorial of a number.
# p = int(input("Enter the number: "))
# fact = 1
# for i in range(1, p+1):
#     fact *= i
# print("The factorial of", p, "is: ", fact)

# # # Q16) Number Guessing (While loop).
# import random

# # Generate a random number
# random_number = random.randint(1, 100)
# guesses_taken = 0

# print("I'm thinking of a number between 1 and 100.")
# print("You have 7 guesses to find it.")

# while guesses_taken < 7:
#     guess = int(input("Take a guess: "))
#     guesses_taken += 1

#     if guess < random_number:
#         print("Too low!")
#     elif guess > random_number:
#         print("Too high!")
#     else:
#         break  # Correct guess

# if guess == random_number:
#     print(f"You got it in {guesses_taken} tries!")
# else:
#     print(f"Sorry, you ran out of guesses. The number was {random_number}.")

# # Q17) Count digits of a number.
# n = int(input("Enter the number: "))
# count = 0
# while n != 0:
#     n //= 10
#     count += 1
# print("The number of digits in the number is: ", count)

# # Q18) Reverse a number.(While loop)
# n = int(input("Enter the number: "))
# rev = 0
# while n != 0:
#     rev = rev*10 + n%10
#     n //= 10
# print("The reversed number is: ", rev)

# # Q19) Sum of Even and Odd Numbers Separately.
# w = int(input("Enter the number: "))
# sum_even = 0
# sum_odd = 0
# while w != 0:
#     if w%2 == 0:
#         sum_even += w%10
#     else:
#         sum_odd += w%10
#     w //= 10
# print("Sum of even digits: ", sum_even)
# print("Sum of odd digits: ", sum_odd)

# # Q20) Palindrome Checker (Integer)
# # Get input from the user
# num = int(input("Enter an integer: "))

# # Convert the integer to a string
# temp = str(num)

# # Reverse the string
# reverse_temp = temp[::-1]

# # Check if the original string is equal to the reversed string
# if temp == reverse_temp:
#     print(num, "is a palindrome.")
# else:
#     print(num, "is not a palindrome.")