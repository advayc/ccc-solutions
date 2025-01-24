# sol for m=3, thx to editorial
# THE worst possible code you could ever make
import sys
from functools import lru_cache
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m=map(int, input().split())
MOD = 1000000007

'''@lru_cache(maxsize=None)
def a(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0
    else:
        return (a(n - 1) + b(n - 2) + c1(n - 3)) % MOD

@lru_cache(maxsize=None)
def b(n):
    if n <= 0:
        return 0
    else:
        a_n_1 = a(n - 1)
        a_n_2 = a(n - 2)
        a_n_3 = a(n - 3)
        b_n_2 = b(n-2)
        b_n_4 = b(n - 4)
        c2_n_3 = c2(n-3)
        return (a_n_1 + b_n_2 + a_n_2 + a_n_3 + b_n_4 + c2_n_3) % MOD

@lru_cache(maxsize=None)
def c1(n):
    if n <= 0:
        return 0
    else:
        a_n_2 = a(n-2)
        c2_n = c2(n)
        return (a_n_2 + c2_n) % MOD

@lru_cache(maxsize=None)
def c2(n):
    if n <= 0:
        return 0
    else:
        a_n_1 = a(n-1)
        b_n_2 = b(n-2)
        a_n_2 = a(n-2)
        a_n_3 = a(n-3)
        b_n_4 = b(n-4)
        c2_n_3 = c2(n-3)
    
        return (2 * a_n_1 + b_n_2 + a_n_2 + a_n_3 + b_n_4 + c2_n_3) % MOD
'''

if m == 1:
    print(1)
elif m == 2:
    dp = [0] * (n + 1)
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 3]) % MOD
    print(dp[n])
else:
    dp_a = [0] * (n + 1)
    dp_b = [0] * (n + 1)
    dp_c1 = [0] * (n + 1)
    dp_c2 = [0] * (n + 1)

    if n >= 1:
        dp_a[1] = 1

    for i in range(2, n + 1):
        dp_c2[i] = (2 * dp_a[i - 1] + (dp_b[i - 2] if i >= 2 else 0) +
                    (dp_a[i - 2] if i >= 2 else 0) + (dp_a[i - 3] if i >= 3 else 0) +
                    (dp_b[i - 4] if i >= 4 else 0) + (dp_c2[i - 3] if i >= 3 else 0)) % MOD

        dp_c1[i] = ((dp_a[i - 2] if i >= 2 else 0) + dp_c2[i]) % MOD

        dp_b[i] = (dp_a[i - 1] + (dp_b[i - 2] if i >= 2 else 0) + 
                   (dp_a[i - 2] if i >= 2 else 0) + (dp_a[i - 3] if i >= 3 else 0) + 
                   (dp_b[i - 4] if i >= 4 else 0) + (dp_c2[i - 3] if i >= 3 else 0)) % MOD

        dp_a[i] = (dp_a[i - 1] + (dp_b[i - 2] if i >= 2 else 0) + (dp_c1[i - 3] if i >= 3 else 0)) % MOD

    print(dp_a[n])