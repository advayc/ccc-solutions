n = int(input())
cor = []
us = []
count = 0
for i in range(n):
    a = input()
    us.append(a)
    
for i in range(n):
    c = input()
    cor.append(c)

for i in range(len(cor)):
    if cor[i] == us[i]:
        count += 1
print(count)