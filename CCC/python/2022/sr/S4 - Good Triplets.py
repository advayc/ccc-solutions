import sys
input=sys.stdin.readline
n, c = map(int, input().split())
pts = list(map(int, input().split()))
freq = {}
for p in pts:
    freq[p] = freq.get(p, 0) + 1
distinct = sorted(freq.keys())
m = len(distinct)
if m < 3:
    print(0)
else:
    X = distinct
    F = [freq[x] for x in X]
    X2 = X + [x + c for x in X]
    F2 = F + F
    N2 = 2 * m
    P = [0] * N2
    Q = [0] * N2
    P[0] = F2[0]
    Q[0] = F2[0] * F2[0]
    for i in range(1, N2):
        P[i] = P[i - 1] + F2[i]
        Q[i] = Q[i - 1] + F2[i] * F2[i]
    tot = sum(F)
    sum_sq = sum(f * f for f in F)
    sum_cube = sum(f * f * f for f in F)
    total_weight = (tot * tot * tot - 3 * tot * sum_sq + 2 * sum_cube) // 6
    thresh = c // 2 if c % 2 == 0 else (c - 1) // 2
    bad_weight = 0
    brooo = 0
    for bruh in range(m):
        if brooo < bruh + 1:
            brooo = bruh + 1
        while brooo < bruh + m and X2[brooo] - X2[bruh] <= thresh:
            brooo += 1
        L_idx = bruh + 1
        R_idx = brooo - 1
        if R_idx - L_idx + 1 >= 2:
            s_val = P[R_idx] - P[bruh]
            q_val = Q[R_idx] - Q[bruh]
            pair_sum = (s_val * s_val - q_val) // 2
            bad_weight += F2[bruh] * pair_sum
    good = total_weight - bad_weight
    print(good)