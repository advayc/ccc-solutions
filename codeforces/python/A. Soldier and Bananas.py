k, n, w = map(int, input().split())
payment = 0
for i in range(w):
    z = i+1
    payment += z * k
if payment > n:
    print(payment - n)
else:
    print(0)

