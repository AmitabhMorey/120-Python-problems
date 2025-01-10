# Q111) Simple Password Generator

def random():
    # A simple linear congruential generator (LCG) for demonstration purposes
    # This is not a cryptographically secure random number generator
    random.seed = (random.seed * 1103515245 + 12345) % (2**31)
    return random.seed / (2**31)

def random_choice(sequence):
    index = int(random() * len(sequence))
    return sequence[index]

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    
    all_characters = letters + digits + special_characters
    password = "".join(random_choice(all_characters) for _ in range(length))
    return password

# Initialize the seed for the random number generator
random.seed = 1

# Example usage
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print(f"Generated password: {password}")

# Q112) Contact Book

def add_contact(filename, name, number, email):
    with open(filename, "a") as file:
        file.write(f"{name},{number},{email}\n")
    print("Contact added successfully.")

def search_contact(filename, search_term):
    with open(filename, "r") as file:
        contacts = file.readlines()
        found_contacts = [contact.strip() for contact in contacts if search_term.lower() in contact.lower()]
    
    if found_contacts:
        print("Found contacts:")
        for contact in found_contacts:
            print(contact)
    else:
        print("No contacts found.")

# Example usage
filename = "contacts.txt"

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        email = input("Enter email: ")
        add_contact(filename, name, number, email)
    elif choice == '2':
        search_term = input("Enter name, number, or email to search: ")
        search_contact(filename, search_term)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

# Q113) Quiz Game

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = int(input("Enter the number of your answer: "))
    return answer == correct_option

def quiz_game(questions):
    score = 0
    for question, options, correct_option in questions:
        if ask_question(question, options, correct_option):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your final score is: {score}/{len(questions)}")

# Example questions
questions = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], 1)
]

# Start the quiz game
quiz_game(questions)

# Q114) Hangman Game

import random

def hangman():
    """
    Implements the Hangman word-guessing game with hints and answers.
    """

    words = ["python", "java", "javascript", "c++", "ruby", "php", "swift", "kotlin", "go", "rust"]
    word = random.choice(words)
    hidden_word = "-" * len(word)
    guesses_left = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(hidden_word)

    while guesses_left > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in word:
            print("Correct!")
            new_hidden_word = ""
            for i, letter in enumerate(word):
                if letter == guess:
                    new_hidden_word += guess
                else:
                    new_hidden_word += hidden_word[i]
            hidden_word = new_hidden_word

        else:
            print("Incorrect.")
            guesses_left -= 1
            print(f"Guesses left: {guesses_left}")

            if guesses_left == 0:
                print("You lose! The word was:", word)
                break

            # Provide a hint after an incorrect guess
            hint = "The word is related to "
            if word in ["python", "java", "javascript", "c++", "ruby", "php", "swift", "kotlin", "go", "rust"]:
                hint += "programming languages."
            print(hint)

        print(hidden_word)

        if hidden_word == word:
            print("Congratulations, you win!")
            break

if __name__ == "__main__":
    hangman()

# Q115) Tic-Tac-Toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
                if row in range(3) and col in range(3):
                    if board[row][col] == " ":
                        break
                    else:
                        print("Cell already taken. Try again.")
                else:
                    print("Invalid input. Row and column must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")

        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        turn += 1

    print_board(board)
    print("It's a draw!")

# Start the Tic-Tac-Toe game
tic_tac_toe()

# Q116) Text-based Adventure

def show_instructions():
    print("""
    Text-based Adventure Game
    =========================
    Commands:
      go [direction]
      get [item]
    """)

def show_status():
    print("---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("---------------------------")

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

# Start the player in the Hall
current_room = 'Hall'
inventory = []

show_instructions()

# Loop infinitely
while True:
    show_status()

    # Get the player's next 'move'
    move = input("> ").lower().split()

    # If they type 'go' first
    if move[0] == 'go':
        # Check that they are allowed to move where they want to go
        if move[1] in rooms[current_room]:
            # Set the current room to the new room
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")

    # If they type 'get' first
    if move[0] == 'get':
        # If the room contains an item, and the item is the one they want to get
        if "item" in rooms[current_room] and move[1] == rooms[current_room]['item']:
            # Add the item to their inventory
            inventory.append(move[1])
            # Display a helpful message
            print(f"{move[1]} got!")
            # Delete the item from the room
            del rooms[current_room]['item']
        else:
            # Tell them they can't get it
            print(f"Can't get {move[1]}!")

    # If a player enters a room with a monster
    if 'item' in rooms[current_room] and 'monster' in rooms[current_room]['item']:
        print("A monster has got you... GAME OVER!")
        break

    # Define how a player can win
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house... YOU WIN!")
        break

# Q117) Rock-Paper-Scissors

import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Your choice: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        choice = input("Your choice: ")
    return ["rock", "paper", "scissors"][int(choice) - 1]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Start the Rock-Paper-Scissors game
play_game()

# Q118) Email Slicer

def email_slicer(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return None, None

# Example usage
email = input("Enter your email address: ")
username, domain = email_slicer(email)

if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email address.")

# Q119) Dictionary App

def load_dictionary(filename):
    dictionary = {}
    with open(filename, "r") as file:
        for line in file:
            word, definition = line.strip().split(':', 1)
            dictionary[word.strip()] = definition.strip()
    return dictionary

def lookup_word(dictionary, word):
    return dictionary.get(word, "Word not found in the dictionary.")

# Example usage
filename = "dictionary.txt"  # Ensure this file exists with word:definition pairs
dictionary = load_dictionary(filename)

while True:
    print("\n1. Look up a word\n2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        word = input("Enter the word to look up: ").strip()
        definition = lookup_word(dictionary, word)
        print(f"Definition: {definition}")
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")

# Q120) Basic To-Do List Manager

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully.")

def mark_task_done(tasks, task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number] += " [DONE]"
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# Example usage
filename = "tasks.txt"
tasks = load_tasks(filename)

while True:
    print("\n1. Add Task\n2. Mark Task as Done\n3. View Tasks\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(tasks, task)
        save_tasks(filename, tasks)
    elif choice == '2':
        view_tasks(tasks)
        task_number = int(input("Enter the task number to mark as done: ")) - 1
        mark_task_done(tasks, task_number)
        save_tasks(filename, tasks)
    elif choice == '3':
        view_tasks(tasks)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")