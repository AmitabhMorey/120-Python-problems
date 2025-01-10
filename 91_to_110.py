# Q91) Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swapping happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping happens, the array is already sorted
        if not swapped:
            break

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
bubble_sort(arr)
print("Sorted list:", arr)

# Q92) Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
insertion_sort(arr)
print("Sorted list:", arr)

# Q93) Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
selection_sort(arr)
print("Sorted list:", arr)

# Q94) Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
merge_sort(arr)
print("Sorted list:", arr)

# Q95) Quick Sort

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print("Sorted list:", arr)

# Q96) Binary Search

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore the left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore the right half
        elif arr[mid] > x:
            high = mid - 1
        # x is present at mid
        else:
            return mid

    # x is not present in the array
    return -1

# Example usage
arr = list(map(int, input("Enter a sorted list of integers separated by spaces: ").split()))
x = int(input("Enter the element to search for: "))

# Perform binary search
result = binary_search(arr, x)

if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the list.")

# Q97) Linear Search

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
x = int(input("Enter the element to search for: "))

# Perform linear search
result = linear_search(arr, x)

if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the list.")

# Q98) Knuth Shuffle (Fisher–Yates Shuffle)

def knuth_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = int((i + 1) * random())
        arr[i], arr[j] = arr[j], arr[i]

def random():
    # A simple linear congruential generator (LCG) for demonstration purposes
    # This is not a cryptographically secure random number generator
    random.seed = (random.seed * 1103515245 + 12345) % (2**31)
    return random.seed / (2**31)

# Initialize the seed for the random number generator
random.seed = 1

# Example usage
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
knuth_shuffle(arr)
print("Shuffled list:", arr)

# Q99) Matrix Addition

def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# Function to input a matrix from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Input dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input the two matrices
print("Matrix 1:")
matrix1 = input_matrix(rows, cols)
print("Matrix 2:")
matrix2 = input_matrix(rows, cols)

# Compute the sum of the matrices
result_matrix = matrix_addition(matrix1, matrix2)

# Print the result
print("The sum of the matrices is:")
for row in result_matrix:
    print(" ".join(map(str, row)))

# Q100) Matrix Multiplication

def matrix_multiplication(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])
    
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Function to input a matrix from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Input dimensions of the matrices
rows_matrix1 = int(input("Enter the number of rows for Matrix 1: "))
cols_matrix1 = int(input("Enter the number of columns for Matrix 1: "))
rows_matrix2 = int(input("Enter the number of rows for Matrix 2: "))
cols_matrix2 = int(input("Enter the number of columns for Matrix 2: "))

# Check if the matrices can be multiplied
if cols_matrix1 != rows_matrix2:
    print("Matrices cannot be multiplied due to incompatible dimensions.")
else:
    # Input the two matrices
    print("Matrix 1:")
    matrix1 = input_matrix(rows_matrix1, cols_matrix1)
    print("Matrix 2:")
    matrix2 = input_matrix(rows_matrix2, cols_matrix2)

    # Compute the product of the matrices
    result_matrix = matrix_multiplication(matrix1, matrix2)

    # Print the result
    print("The product of the matrices is:")
    for row in result_matrix:
        print(" ".join(map(str, row)))

# Q101) Transposition of a Matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

# Function to input a matrix from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Input dimensions of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input the matrix
matrix = input_matrix(rows, cols)

# Compute the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
print("The transpose of the matrix is:")
for row in transposed_matrix:
    print(" ".join(map(str, row)))

# Q102) Check if a Matrix is Symmetric

def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Function to input a matrix from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Input dimensions of the matrix
n = int(input("Enter the number of rows and columns (square matrix): "))

# Input the matrix
matrix = input_matrix(n, n)

# Check if the matrix is symmetric
if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")

# Q103) Longest Common Substring

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    max_length = 0
    ending_index = m

    # Create a 2D array to store lengths of longest common suffixes of substrings
    lcsuff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Build the lcsuff array in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcsuff[i][j] = lcsuff[i - 1][j - 1] + 1
                if lcsuff[i][j] > max_length:
                    max_length = lcsuff[i][j]
                    ending_index = i
            else:
                lcsuff[i][j] = 0

    # If no common substring is found, return an empty string
    if max_length == 0:
        return ""

    # Return the longest common substring
    return str1[ending_index - max_length: ending_index]

# Example usage
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = longest_common_substring(str1, str2)
print(f"The longest common substring is: '{result}'")

# Q104) Longest Common Subsequence (LCS)

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D array to store lengths of longest common subsequence
    lcs_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Build the lcs_table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Following code is used to print LCS
    index = lcs_table[m][n]
    lcs_str = [""] * (index + 1)
    lcs_str[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs_str
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_str)

# Example usage
str1 = input("Enter the first sequence: ")
str2 = input("Enter the second sequence: ")

result = lcs(str1, str2)
print(f"The longest common subsequence is: '{result}'")

# Q105) Coin Change (Greedy)

def coin_change_greedy(coins, amount):
    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        if amount == 0:
            break
        # Use as many of the current coin as possible
        count += amount // coin
        amount %= coin
    
    # If the amount is not zero, it means we cannot make the exact amount with the given coins
    if amount != 0:
        return -1  # Indicating that it's not possible to make the exact amount
    return count

# Example usage
coins = list(map(int, input("Enter the coin denominations separated by spaces: ").split()))
amount = int(input("Enter the target amount: "))

result = coin_change_greedy(coins, amount)
if result != -1:
    print(f"The minimum number of coins needed: {result}")
else:
    print("It's not possible to make the exact amount with the given coins.")

# Q106) Coin Change (DP)

def coin_change_dp(coins, amount):
    # Initialize the dp array with a value greater than the maximum possible number of coins
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

    # Build the dp array
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[amount] is still float('inf'), it means it's not possible to make the exact amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = list(map(int, input("Enter the coin denominations separated by spaces: ").split()))
amount = int(input("Enter the target amount: "))

result = coin_change_dp(coins, amount)
if result != -1:
    print(f"The minimum number of coins needed: {result}")
else:
    print("It's not possible to make the exact amount with the given coins.")

# Q107) Knapsack Problem (0/1 DP)

def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D array to store the maximum value that can be obtained with a given weight and items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array in bottom-up fashion
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
weights = list(map(int, input("Enter the weights of the items separated by spaces: ").split()))
values = list(map(int, input("Enter the values of the items separated by spaces: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

result = knapsack(weights, values, capacity)
print(f"The maximum value that can be obtained is: {result}")

# Q108) Permutations of a List

def permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]

    perms = []
    for i in range(len(arr)):
        m = arr[i]
        remaining_elements = arr[:i] + arr[i+1:]
        for p in permutations(remaining_elements):
            perms.append([m] + p)
    return perms

# Example usage
arr = list(map(int, input("Enter a list of distinct integers separated by spaces: ").split()))
result = permutations(arr)
print("All permutations of the list are:")
for perm in result:
    print(perm)

# Q109) Backtracking: N-Queens

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    # base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_nqueens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in this column col then return false
    return False

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

# Example usage
n = int(input("Enter the value of N for the N-Queens puzzle: "))
solve_nqueens(n)

# Q110) Shortest Path in a Grid

def is_valid_move(grid, visited, row, col):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and grid[row][col] == 1

def bfs_shortest_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions for moving right and down
    directions = [(0, 1), (1, 0)]
    
    # Queue for BFS
    queue = [(0, 0, 0)]  # (row, col, distance)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True
    
    while queue:
        row, col, dist = queue.pop(0)
        
        # If we have reached the bottom-right corner
        if row == rows - 1 and col == cols - 1:
            return dist
        
        # Explore the neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))
    
    # If there is no path to the bottom-right corner
    return -1

# Example usage
grid = []
rows = int(input("Enter the number of rows in the grid: "))
for _ in range(rows):
    grid.append(list(map(int, input().split())))

result = bfs_shortest_path(grid)
if result != -1:
    print(f"The shortest path length is: {result}")
else:
    print("There is no path from the top-left to the bottom-right corner.")