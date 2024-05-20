n = int(input())
result = ""

for i in range(n):
    ln, l = input().split()
    ln = int(ln)    
    result += ln * l + "\n"

print(result)
