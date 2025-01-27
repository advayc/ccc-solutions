a, b = map(int, input().split())
d = []
for e in input():
    if e == "0":
        d.append(0)
    else:
        d.append(1)
e = d[:]
f = 1
while b != 0:
    # check if the current step is odd
    if b % 2 == 1:
        # swap the old and new generation
        e, d = d, e
        # update each cell based on the XOR of its neighbors
        for g in range(a):
            d[g] = e[(g - f) % a] ^ e[(g + f) % a]
    
    # reduce the steps by half and double the step size
    b //= 2
    f *= 2
print(*d, sep="")