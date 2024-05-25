mins = int(input())
n = int(input())
tasks = []
for i in range(n):
    e = int(input())
    tasks.append(e)
tasks.sort()

t_nums = t_mins = 0
for i in tasks:
    t_mins += i
    if t_mins > mins:
        break
    t_nums += 1
print(t_nums)