MOD = 10**6 + 3
R = MOD  # number of buckets (each possible release time s in [0, MOD-1])
NEG_INF = -10**15
n = 1
while n < R:
    n *= 2
seg_total = [0] * (2 * n)
seg_best = [NEG_INF] * (2 * n)

T_arr = [0] * R
count_arr = [0] * R

for i in range(R):
    seg_total[n + i] = T_arr[i]  # initially 0
    seg_best[n + i] = i if count_arr[i] > 0 else NEG_INF
for i in range(R, n):
    seg_total[n + i] = 0
    seg_best[n + i] = NEG_INF
for i in range(n - 1, 0, -1):
    seg_total[i] = seg_total[2 * i] + seg_total[2 * i + 1]
    seg_best[i] = seg_best[2 * i]
    right_val = seg_best[2 * i + 1] - seg_total[2 * i]
    if right_val > seg_best[i]:
        seg_best[i] = right_val

fenw_n = 0  # will set this after reading Q.
fenw = []   # will be allocated after Q is read.

def fenw_update(i, delta):
    # i: 0-indexed assignment index in our assignments list.
    i += 1
    while i <= fenw_n:
        fenw[i] += delta
        i += i & -i

def fenw_sum(i):
    s = 0
    i += 1
    while i:
        s += fenw[i]
        i -= i & -i
    return s

def fenw_find(k):
    idx = 0
    bit = 1 << (fenw_n.bit_length() - 1)
    while bit:
        nxt = idx + bit
        if nxt <= fenw_n and fenw[nxt] < k:
            k -= fenw[nxt]
            idx = nxt
        bit //= 2
    return idx  # 0-indexed

def seg_update(pos, new_total, new_best):
    i = pos + n
    seg_total[i] = new_total
    seg_best[i] = new_best
    i //= 2
    while i:
        left = 2 * i
        right = left + 1
        seg_total[i] = seg_total[left] + seg_total[right]
        candidate = seg_best[left]
        # Right child candidate adjusted by left's total:
        temp = seg_best[right] - seg_total[left]
        if temp > candidate:
            candidate = temp
        seg_best[i] = candidate
        i //= 2

import sys
input_data = sys.stdin.read().splitlines()
q_line = input_data[0].strip()
Q = int(q_line)
fenw_n = Q
fenw = [0] * (fenw_n + 1)

assignments = []  # list to store (s, t) for each added assignment.
ans = 0  # previous answer, initially 0.
out_lines = []  # to collect output lines.

line_index = 1
for _ in range(Q):
    parts = input_data[line_index].split()
    line_index += 1
    typ = parts[0]
    if typ == 'A':
        s_val = int(parts[1])
        t_val = int(parts[2])
        s = (s_val + ans) % MOD
        t = (t_val + ans) % MOD
        assignments.append((s, t))
        idx = len(assignments) - 1
        fenw_update(idx, 1)
        # Update bucket for release time s.
        count_arr[s] += 1
        T_arr[s] += t
        new_tot = T_arr[s]
        new_cand = s if count_arr[s] > 0 else NEG_INF
        seg_update(s, new_tot, new_cand)
    else:
        i_val = int(parts[1])
        # i is 1-indexed among active assignments.
        i_del = (i_val + ans) % MOD
        k = i_del  # k-th active assignment (1-indexed)
        pos = fenw_find(k)  # pos is 0-indexed in assignments list.
        s, t = assignments[pos]
        fenw_update(pos, -1)
        count_arr[s] -= 1
        T_arr[s] -= t
        new_tot = T_arr[s]
        new_cand = s if count_arr[s] > 0 else NEG_INF
        seg_update(s, new_tot, new_cand)
    total_t = seg_total[1]         # total processing time for all buckets.
    best_candidate = seg_best[1]     # max_{active bucket} (i - prefix sum of T for indices < i)
    M_val = best_candidate
    if M_val < 0:
        M_val = 0
    answer_value = M_val + total_t - 1
    out_lines.append(str(answer_value))
    ans = answer_value

sys.stdout.write("\n".join(out_lines))
