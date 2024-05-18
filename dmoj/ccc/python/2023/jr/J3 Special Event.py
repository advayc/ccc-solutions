n = int(input())
days = [0] * 5
best_days = []

for i in range(n):
    avail = input()
    for k in range(5):
        if avail[k] == 'Y':
            days[k] += 1
        
max_day = max(days)

for r in range(5):
    if days[r] == max_day:
        best_days.append(str(r+1))

print(",".join(best_days))