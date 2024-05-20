n = int(input())
count = 0
people = []

for i in range(n):
    t = int(input())
    people.append(t)
people.sort(reverse=True)
    
bronze = sorted(set(people), reverse=True)[2]

for z in range(n):
    if people[z] == bronze:
        count += 1

print(bronze, count)