def find_words(board, words):
  rows, cols = len(board), len(board[0])
  word_locations = {}
  for word in words:
    word_locations[word] = []
    for row in range(rows):
      for col in range(cols):
        if search_word(board, row, col, word, 0, rows, cols):
          word_locations[word].append((row, col, 0))
        if search_word(board, row, col, word, 1, rows, cols):
          word_locations[word].append((row, col, 1))
        if search_word(board, row, col, word, 2, rows, cols):
          word_locations[word].append((row, col, 2))
  return word_locations

def search_word(board, row, col, word, direction, rows, cols):
  word_len = len(word)
  for i in range(word_len):
    if direction == 0:
      new_col = col + i  # Horizontal search
    elif direction == 1:
      new_row = row + i  # Vertical search (previously missing assignment)
      new_col = col
    else:
      new_row = row + i  # Diagonal search
      new_col = col + i
    if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != word[i]:
      return False
  return True

def solve(puzzle):
  rows, cols, board, words = puzzle
  word_locations = find_words(board, words)
  marked_board = [['.' for _ in range(cols)] for _ in range(rows)]
  for word, locations in word_locations.items():
    for row, col, _ in locations:
      for i in range(len(word)):
        marked_board[row][col + i] = word[i]
  secret_message = ""
  for row in marked_board:
    secret_message += ''.join([char for char in row if char == '.'])
  return secret_message

# Replace with your actual input handling (provided in your previous message)
rows, cols = map(int, input().split())
board = [input() for _ in range(rows)]
num_words = int(input())
words = [input().upper() for _ in range(num_words)]

puzzle = (rows, cols, board, words)

# Solve the puzzle
secret_message = solve(puzzle)

# Print the secret message
print(secret_message)
