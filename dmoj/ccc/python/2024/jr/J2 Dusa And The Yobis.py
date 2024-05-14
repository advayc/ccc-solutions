start = int(input())

while True:
    next = int(input())
    if start > next:
        start += next
    else:
        break

print(start)