J = int(input())
count = 0

for a in range(1, J - 2):
    for b in range(a + 1, J - 1):
        for c in range(b + 1, J):
            if a < b < c < J:
                count += 1

print(count)
