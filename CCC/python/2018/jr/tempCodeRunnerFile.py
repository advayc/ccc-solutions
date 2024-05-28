N = int(input())

table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

# Check if the table is already in the original arrangement
is_original = True
for i in range(1, N):
    if table[i][0] < table[i-1][-1]:
        is_original = False
        break

if not is_original:
    # Rotate the table 90 degrees to the right
    rotated_table = [[table[j][i] for j in range(N-1, -1, -1)] for i in range(N)]
    table = rotated_table

# Print the table
for row in table:
    print(' '.join(map(str, row)))