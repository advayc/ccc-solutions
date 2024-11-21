import sys
input = sys.stdin.readline
# no clue what this code even is bruh

def count_distinct_substrings(s):
    # append a unique sentinel character to ensure proper suffix sorting
    s += "$"
    n = len(s)
    
    # build suffix array
    suffixes = sorted((s[i:], i) for i in range(n))
    suffix_array = [x[1] for x in suffixes]
    
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    
    total_substrings = n * (n - 1) // 2 - sum(lcp)
    return total_substrings+1

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(count_distinct_substrings(s))