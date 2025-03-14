'''import sys
input=sys.stdin.readline
bruh=input()
newbruh=bruh
c=int(input())
alpha='abcdefghijklmnopqrstuvwxyz'
x=''
y=''
numbers=[]

for i in range(len(bruh)):
    current=bruh[i]

    if current in alpha:
        x+=current
        newbruh = newbruh.replace(current, ' ')

newbruh=newbruh.split(' ')
newbruh.remove('')
nums=newbruh

for i in range(len(x)):
    y += str(x[i]) * int(nums[i])

print(y[c%len(y)])
'''


import sys
input=sys.stdin.readline
s=input().strip()
c=int(input())
pairs =[]
i=0
while i < len(s):
    letter = s[i]
    i += 1
    num_str = ""
    while i < len(s) and s[i].isdigit():
        num_str += s[i]
        i += 1
    count = int(num_str)
    pairs.append((letter, count))

total_length = sum(count for _, count in pairs)
#print(total_length)
target = c % total_length

acc = 0
for letter, count in pairs:
    acc += count
    if target < acc:
        print(letter)
        break
