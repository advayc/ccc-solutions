N, K = map(int, input().split())
gifts = list(map(int, input().split()))

if K == 0:
    print(0)

gifts_with_index = [(abs(val), val, i) for i, val in enumerate(gifts)]
gifts_with_index.sort(reverse=True)

max_happiness = 0
original_gifts = [g[1] for g in gifts_with_index]

# try different numbers of flips to find optimal balance
for num_flips in range(min(K, N) + 1):
    test_gifts = list(original_gifts)
    
    # flip the largest negative numbers
    flipped = 0
    for abs_val, val, idx in gifts_with_index:
        if val < 0 and flipped < num_flips:
            test_gifts[idx] = -val
            flipped += 1
    
    # sort and take best gifts we can open with remaining moves
    test_gifts.sort(reverse=True)
    openable = min(K - num_flips, N)  # can't open more than n gifts
    
    # sum up positive values we can open
    happiness = sum(val for val in test_gifts[:openable] if val > 0)
    max_happiness = max(max_happiness, happiness)

print(max_happiness)