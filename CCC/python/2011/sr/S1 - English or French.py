num_lines = int(input())

# Count occurrences of 't' and 's' in each line
t_count = 0
s_count = 0

for _ in range(num_lines):
    line = input().strip()
    for char in line:
        if char.lower() == 't':
            t_count += 1
        elif char.lower() == 's':
            s_count += 1

# Determine the language
if t_count > s_count:
    print("English")
elif t_count < s_count:
    print("French")
else:
    print("French")  # If counts are equal, default to French
