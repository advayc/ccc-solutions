dir = "right"
degre = ""
inst = ""
sum = 0
results = []

while True:
    inst = input()
    sum = int(inst[:1]) + int(inst[1:2])
    last = int(inst[2:5])
    if inst == "99999":  
        break

    if sum == 0 and dir != "":
        degre = dir
    elif sum % 2 == 0:
        degre = "right"
        dir = "right"
    else:
        degre = "left"
        dir = "left"

    results.append(f"{degre} {last}")

for result in results:
    print(result)
