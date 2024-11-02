import sys
input = sys.stdin.readline
n = int(input())
after = n % 60
newtime = 12.00

if n % 60 == 0:
    num = n // 60
    newtime += num
else:
    num = n % 60
    hours_to_add = n // 60
    newtime += hours_to_add + (num / 100)

newtime = int(newtime * 100)

def check_arithmetic(d1, d2, d3, d4):
    return (d2 - d1 == d3 - d2 == d4 - d3)

count = 0
current_hour = 12
current_minute = 0

while (current_hour * 100 + current_minute) <= newtime:
    h1 = current_hour // 10
    h2 = current_hour % 10
    m1 = current_minute // 10
    m2 = current_minute % 10

    if check_arithmetic(h1, h2, m1, m2):
        count += 1

    current_minute += 1
    if current_minute == 60:
        current_minute = 0
        current_hour = (current_hour % 12) + 1
print(count)
