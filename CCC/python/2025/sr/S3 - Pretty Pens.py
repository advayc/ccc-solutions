# wrote half of this during ccc, then thought it was wrong and didnt continue and missed out on easy 5 partials

from math import inf
import sys
input=sys.stdin.readline
n, m, q = map(int, input().split())
pens = []
pen_by_color = {c: [] for c in range(1, m+1)}
for _ in range(n):
    c, p = map(int, input().split())
    pens.append((c, p))
    pen_by_color[c].append(p)

best = {} # best[c] is highest prettiness in colour c
second_best = {}  # second_best[c] is second highest; if none then -infty
for c in range(1, m+1):
    vals = pen_by_color[c]
    vals.sort(reverse=True)
    best[c] = vals[0]
    second_best[c] = vals[1] if len(vals) > 1 else -inf

base_sum = sum(best[c] for c in range(1, m+1))
ans = base_sum

min_val = inf
min_col = -1
second_min_val = inf
for c in range(1, m+1):
    val = best[c]
    if val < min_val:
        second_min_val = min_val
        min_val = val
        min_col = c
    elif val < second_min_val:
        second_min_val = val

for orig, p in pens:
    loss = 0
    if p == best[orig]:
        loss = best[orig] - second_best[orig]
    target_best = second_min_val if orig == min_col else min_val
    gain = p - target_best if p > target_best else 0
    candidate = base_sum - loss + gain
    if candidate > ans:
        ans = candidate

print(ans)