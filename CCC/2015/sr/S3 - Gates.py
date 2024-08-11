import sys
input = sys.stdin.readline
gates = int(input())
planes = int(input())
gates_arr = list(range(gates + 1))
count = 0

for i in range(planes):
    gte = int(input())
    
    # Find the highest available gate  
    root = gte
    while root > 0 and gates_arr[root] != root:
        root = gates_arr[root]
    
    if root == 0:
        break

    # update the gate to point directly to the next available gate
    while gte != root:
        next_gate = gates_arr[gte]
        gates_arr[gte] = root
        gte = next_gate
    
    # Dock the plane at the root gate and mark it as used
    gates_arr[root] = root - 1
    count += 1

print(count)
