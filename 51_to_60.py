# Q51) Reverse a String
# Input a string from the user
user_input = input("Enter a string: ")

# Reverse the string
reversed_string = user_input[::-1]

print(f"The reversed string is: {reversed_string}")

# Q52) Palindrome String Checker
# Input a string from the user
user_input = input("Enter a string: ")

# Convert the string to lowercase for case-insensitive comparison
normalized_string = user_input.lower()

# Check if the string is a palindrome
is_palindrome = normalized_string == normalized_string[::-1]

if is_palindrome:
    print(f"The string '{user_input}' is a palindrome.")
else:
    print(f"The string '{user_input}' is not a palindrome.")

# Q53) Count Vowels in a String
# Input a string from the user
user_input = input("Enter a string: ")

# Define the set of vowels
vowels = set("aeiouAEIOU")

# Count the number of vowels in the string
vowel_count = sum(1 for char in user_input if char in vowels)

print(f"The number of vowels in the string is: {vowel_count}")

# Q54) Check Anagram
# Input two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Normalize the strings by converting to lowercase and sorting the characters
normalized_str1 = sorted(str1.lower())
normalized_str2 = sorted(str2.lower())

# Check if the normalized strings are equal
if normalized_str1 == normalized_str2:
    print(f"The strings '{str1}' and '{str2}' are anagrams.")
else:
    print(f"The strings '{str1}' and '{str2}' are not anagrams.")

# Q55) Remove Spaces
# Input a string from the user
user_input = input("Enter a string: ")

# Remove all spaces from the string
no_spaces_string = user_input.replace(" ", "")

print(f"The string without spaces is: {no_spaces_string}")

# Q56) Longest Word in a Sentence
# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

print(f"The longest word in the sentence is: {longest_word}")

# Q57) String Case Conversion
# Input a string from the user
user_input = input("Enter a string: ")

# Convert the string to upper case
upper_case = user_input.upper()

# Convert the string to lower case
lower_case = user_input.lower()

# Convert the string to title case
title_case = user_input.title()

# Print all three versions
print(f"Upper case: {upper_case}")
print(f"Lower case: {lower_case}")
print(f"Title case: {title_case}")

# Q58) Capitalize Every Word
# Input a string from the user
user_input = input("Enter a string: ")

# Capitalize the first letter of every word
capitalized_string = user_input.title()

print(f"The string with every word capitalized is: {capitalized_string}")

# Q59) Count Special Characters
import string

# Input a string from the user
user_input = input("Enter a string: ")

# Define the set of special characters
special_characters = set(string.punctuation)

# Count the number of special characters in the string
special_char_count = sum(1 for char in user_input if char in special_characters)

print(f"The number of special characters in the string is: {special_char_count}")

# Q60) Character Frequency in String
# Input a string from the user
user_input = input("Enter a string: ")

# Build a dictionary to count character occurrences
char_frequency = {}
for char in user_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character frequency dictionary:", char_frequency)