n = int(input())
computers = []

for i in range(n):
    name, ram, speed, dspace = input().split()
    ram, speed, dspace = int(ram), int(speed), int(dspace)
    total = (2 * ram) + (3 * speed) + dspace
    computers.append((total, name))

def sort_key(computer):
    return (-computer[0], computer[1])

computers.sort(key=sort_key)

if len(computers) > 0:
    print(computers[0][1])
if len(computers) > 1:
    print(computers[1][1])
