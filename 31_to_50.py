# Q31) List Operations
# Create a list of integers
lst = [1, 2, 3, 4, 5]
print(f"Initial list: {lst}")

# Append an element to the list
lst.append(6)
print(f"After append(6): {lst}")

# Insert an element at a specific position
lst.insert(2, 10)
print(f"After insert(2, 10): {lst}")

# Remove an element from the list
lst.remove(3)
print(f"After remove(3): {lst}")

# Pop an element from the list
popped_element = lst.pop()
print(f"After pop(): {lst}, Popped element: {popped_element}")

# Display the final list
print(f"Final list: {lst}")

# Q32) Maximum and Minimum in a List
# Take a list of numbers from the user
lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

# Find the maximum and minimum values
max_value = max(lst)
min_value = min(lst)

print(f"The maximum value in the list is: {max_value}")
print(f"The minimum value in the list is: {min_value}")

# Q33) Second Largest Element
# Take a list of unique integers from the user
lst = list(map(int, input("Enter the list of unique integers separated by spaces: ").split()))

# Find the second largest element
if len(lst) < 2:
    print("List must contain at least two unique integers.")
else:
    lst.sort()
    second_largest = lst[-2]
    print(f"The second largest element in the list is: {second_largest}")

# Q34) Sum and Average of a List
# Take a list of numbers from the user
lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

# Calculate the sum and average
total_sum = sum(lst)
average = total_sum / len(lst)

print(f"The sum of the list is: {total_sum}")
print(f"The average of the list is: {average}")

# Q35) Count Positive, Negative, Zero
# Take a list of integers from the user
lst = list(map(int, input("Enter the list of integers separated by spaces: ").split()))

# Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0

# Count positive, negative, and zero values
for num in lst:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeroes: {zero_count}")

# Q36) Remove Duplicates from a List
# Take a list of integers from the user
lst = list(map(int, input("Enter the list of integers separated by spaces: ").split()))

# Create a new list with duplicates removed
unique_lst = list(set(lst))

print(f"The list with duplicates removed is: {unique_lst}")

# Q37) Concatenate Two Lists
# Take two lists of integers from the user
lst1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
lst2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))

# Concatenate the two lists
concatenated_lst = lst1 + lst2

print(f"The concatenated list is: {concatenated_lst}")

# Q38) List Reversal
def reverse_list(lst):
    lst.reverse()

# Take a list of integers from the user
lst = list(map(int, input("Enter the list of integers separated by spaces: ").split()))

# Reverse the list in place
reverse_list(lst)

print(f"The reversed list is: {lst}")

# Q39) Find Common Elements of Two Lists# Q39) Find Common Elements of Two Lists
# Take two lists of integers from the user
lst1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
lst2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))

# Find the common elements
common_elements = list(set(lst1) & set(lst2))

print(f"The common elements in the two lists are: {common_elements}")

# Q40) Element-wise Sum of Two Lists
# Take two lists of integers from the user
lst1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
lst2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))

# Check if the lists are of equal length
if len(lst1) != len(lst2):
    print("The lists must be of equal length.")
else:
    # Create a third list that stores the element-wise sum
    sum_list = [a + b for a, b in zip(lst1, lst2)]
    print(f"The element-wise sum of the two lists is: {sum_list}")

# Q41) Tuple Creation and Access
# Create a tuple of strings
tup = ("apple", "banana", "cherry", "date", "elderberry")

# Prompt the user for an index
index = int(input("Enter an index to access the element: "))

# Check if the index is within the valid range
if 0 <= index < len(tup):
    print(f"The element at index {index} is: {tup[index]}")
else:
    print("Invalid index")

# Q42) Tuple to List
# Take a tuple of integers from the user
user_input = input("Enter the elements of the tuple separated by spaces: ")
tup = tuple(map(int, user_input.split()))

# Convert the tuple to a list
lst = list(tup)
print(f"List converted from tuple: {lst}")

# Modify the list (example: append an element)
lst.append(int(input("Enter an element to append to the list: ")))
print(f"Modified list: {lst}")

# Convert the list back to a tuple
tup = tuple(lst)
print(f"Tuple converted back from list: {tup}")

# Q43) Check if Element Exists in Tuple
# Create a tuple of integers
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Prompt the user for an element
element = int(input("Enter an element to check if it exists in the tuple: "))

# Check if the element exists in the tuple
if element in tup:
    print(f"The element {element} exists in the tuple.")
else:
    print(f"The element {element} does not exist in the tuple.")

# 044) Dictionary: Word Count
# Prompt the user for a string
user_input = input("Enter a string: ")

# Split the string into words
words = user_input.split()

# Build a dictionary to count word occurrences
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count dictionary:", word_count)

# Q45) Dictionary: Student Grades
# Create a dictionary with student names and their grades
student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "B",
    "Eve": "A"
}

# Prompt the user for a student name
student_name = input("Enter the student's name to get their grade: ")

# Display the grade
if student_name in student_grades:
    print(f"{student_name}'s grade is: {student_grades[student_name]}")
else:
    print(f"Student {student_name} not found.")

# Q46) Dictionary: Keys and Values
# Create a dictionary
sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

# Print just the keys
print("Keys:", sample_dict.keys())

# Print just the values
print("Values:", sample_dict.values())

# Q47) Merge Two Dictionaries
# Create two dictionaries
dict1 = {
    "name": "Alice",
    "age": 25
}

dict2 = {
    "city": "New York",
    "occupation": "Engineer"
}

# Merge the two dictionaries into a new dictionary
merged_dict = {**dict1, **dict2}

print("Merged dictionary:", merged_dict)

# Q48) Invert Dictionary
# Create a dictionary
sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

# Check if all values are unique
if len(sample_dict.values()) == len(set(sample_dict.values())):
    # Invert the dictionary
    inverted_dict = {value: key for key, value in sample_dict.items()}
    print("Inverted dictionary:", inverted_dict)
else:
    print("The dictionary has non-unique values and cannot be inverted.")

# Q49) Set Operations
# Prompt the user for two lists
list1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)

# Display the union, intersection, and difference of these sets
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print(f"Union of the sets: {union_set}")
print(f"Intersection of the sets: {intersection_set}")
print(f"Difference of the sets (set1 - set2): {difference_set}")

# Q50) Set Membership Testing
# Create a set of names
names_set = {"Alice", "Bob", "Charlie", "David", "Eve"}

# Prompt the user for a name
name = input("Enter a name to check if it is in the set: ")

# Check if the name is in the set
if name in names_set:
    print(f"The name {name} is in the set.")
else:
    print(f"The name {name} is not in the set.")