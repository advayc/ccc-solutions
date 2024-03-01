def count_occurrences(word, rows, cols, grid):
    occurrences = 0

    # Check horizontally
    for row in grid:
        row_str = "".join(row)
        occurrences += row_str.count(word)

    # Check vertically
    for col in range(cols):
        col_str = "".join(grid[row][col] for row in range(rows))
        occurrences += col_str.count(word)

    # Check diagonally
    for row in range(rows):
        for col in range(cols):
            # Check right-down diagonal
            if col + len(word) <= cols and row + len(word) <= rows:
                diagonal_str = "".join(grid[row + i][col + i] for i in range(len(word)))
                occurrences += diagonal_str.count(word)

            # Check right-up diagonal
            if col + len(word) <= cols and row - len(word) + 1 >= 0:
                diagonal_str = "".join(grid[row - i][col + i] for i in range(len(word)))
                occurrences += diagonal_str.count(word)

    return occurrences

# Read input
word = input().strip()
rows = int(input())
cols = int(input())

grid = [input().split() for _ in range(rows)]

# Calculate and print the result
result = count_occurrences(word, rows, cols, grid)
print(result)
