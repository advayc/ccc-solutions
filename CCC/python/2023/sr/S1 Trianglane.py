n = int(input())
i = 0
a = input().split(' ')
b = input().split(' ')
pa = '0'
pb = '0'
for x in range(0, len(a)):
    if a[x] == '1' and b[x] == '1' and x % 2 == 0:
      i += 4
    elif a[x] == '1' and b[x] == '1' and x % 2 != 0:
      i += 6
    elif (a[x] == '1' and b[x] == '0') or (b[x] == '1' and a[x] == '0'):
      i += 3
    if pa == '1' and a[x] == '1':
      i -= 2
    if pb == '1' and b[x] == '1':
      i -= 2
    pa = a[x]
    pb = b[x]
print(i)
