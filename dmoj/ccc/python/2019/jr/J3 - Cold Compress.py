def encode(s):
    encoding = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoding.append((count, s[i - 1]))
            count = 1
    encoding.append((count, s[-1]))  # Add the last character count
    return encoding

n = int(input())

for _ in range(n):
    line = input().strip()
    encoding = encode(line)
    for pair in encoding:
        print(pair[0], pair[1], end=" ")
    print()
