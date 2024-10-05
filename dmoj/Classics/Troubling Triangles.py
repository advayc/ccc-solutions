import math

N = int(input())

for _ in range(N):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    A = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

    P = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) + math.sqrt((x3 - x2)**2 + (y3 - y2)**2) + math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

    print("{:.2f} {:.2f}".format(A, P))