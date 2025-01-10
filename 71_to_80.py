# Q71) Write to File
# Prompt the user for a string
user_input = input("Enter a string to write to the file: ")

# Write the string to a text file named "output.txt"
with open("output.txt", "w") as file:
    file.write(user_input)

print("The string has been written to output.txt")

# Q72) Read from File
# Read the content of "output.txt"
with open("output.txt", "r") as file:
    content = file.read()

# Print the content to the console
print("The content of output.txt is:")
print(content)

# Q73) Copy File
# Function to copy the contents of one file to another
def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, "r") as source_file:
            content = source_file.read()
        with open(destination_filename, "w") as destination_file:
            destination_file.write(content)
        print(f"The contents of {source_filename} have been copied to {destination_filename}.")
    except FileNotFoundError:
        print(f"The file {source_filename} does not exist.")

# Specify the source and destination file names
source_filename = "output.txt"
destination_filename = "copy_output.txt"

# Copy the contents of the source file to the destination file
copy_file(source_filename, destination_filename)

# Q74) Count Lines in a File
# Function to count the number of lines in a file
def count_lines_in_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return len(lines)

# Specify the file name
filename = "output.txt"

# Count the number of lines in the file
line_count = count_lines_in_file(filename)

# Print the number of lines
print(f"The file {filename} contains {line_count} lines.")

# Q75) Count Words in a File
# Function to count the number of words in a file
def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return 0

# Specify the file name
filename = "output.txt"

# Count the number of words in the file
word_count = count_words_in_file(filename)

# Print the number of words
print(f"The file {filename} contains {word_count} words.")

# Q76) Find Longest Line in a File
# Function to find the longest line in a file
def find_longest_line(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            longest_line = max(lines, key=len)
            return longest_line.strip()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return ""

# Specify the file name
filename = "output.txt"

# Find the longest line in the file
longest_line = find_longest_line(filename)

# Print the longest line
if longest_line:
    print(f"The longest line in the file {filename} is:\n{longest_line}")

# Q77) Search for a Word in a File
# Function to search for a word in a file and return the line number(s) where it appears
def search_word_in_file(filename, word):
    line_numbers = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                if word in line:
                    line_numbers.append(i)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    return line_numbers

# Specify the file name
filename = "output.txt"

# Prompt the user for a word
word = input("Enter a word to search for in the file: ")

# Search for the word in the file
line_numbers = search_word_in_file(filename, word)

# Print the line number(s) where the word appears
if line_numbers:
    print(f"The word '{word}' appears in the file {filename} on line(s): {line_numbers}")
else:
    print(f"The word '{word}' does not appear in the file {filename}.")

# Q78) Append to a File
# Prompt the user for some text
user_input = input("Enter text to append to the file: ")

# Append the text to "output.txt" without overwriting existing content
with open("output.txt", "a") as file:
    file.write(user_input + "\n")

print("The text has been appended to output.txt")

# Q79) Remove Blank Lines
# Function to remove blank lines from a file and write to a new file
def remove_blank_lines(source_filename, destination_filename):
    try:
        with open(source_filename, "r") as source_file:
            lines = source_file.readlines()
        with open(destination_filename, "w") as destination_file:
            for line in lines:
                if line.strip():  # Check if the line is not blank
                    destination_file.write(line)
        print(f"Blank lines have been removed and content written to {destination_filename}.")
    except FileNotFoundError:
        print(f"The file {source_filename} does not exist.")

# Specify the source and destination file names
source_filename = "output.txt"
destination_filename = "output_no_blanks.txt"

# Remove blank lines and write to the new file
remove_blank_lines(source_filename, destination_filename)

# Q80) File Statistics
# Function to display file statistics
def file_statistics(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            total_characters = len(content)
            total_lines = content.count('\n') + 1
            total_words = len(content.split())
            print(f"File Statistics for {filename}:")
            print(f"Total characters: {total_characters}")
            print(f"Total lines: {total_lines}")
            print(f"Total words: {total_words}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Specify the file name
filename = "output.txt"

# Display file statistics
file_statistics(filename)