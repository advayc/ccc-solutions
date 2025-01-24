n = int(input())
f0, f1, MOD = 1, 0, 1000000007
for b in "00" + bin(n)[2:]:
    f0, f1 = (f0 * f0 + f1 * f1) % MOD, (f1 * (2 * f0 + f1)) % MOD
    if b == '1':
        f0, f1 = f1, (f1 + f0) % MOD

print(f1)
