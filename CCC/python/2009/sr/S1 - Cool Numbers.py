a = int(input())
b = int(input())
c = 0
d = int(b **(1/2))
f = round(a **(1/3))
e = []

for i in range(f, d+1):
  e.append(int(i*i))

for i in range(f, d+1):
  if i ** 3 in e:
    c += 1

print(c)