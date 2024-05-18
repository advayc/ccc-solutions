from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True

def solve(n):
    for i in range(2, n*2):
        if is_prime(i) and is_prime(n*2 - i):
            print(i, n*2 - i)
            return

t = int(input())
for i in range(t):
    solve(int(input()))