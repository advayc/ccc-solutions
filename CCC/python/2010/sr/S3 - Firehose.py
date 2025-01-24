import sys

input = sys.stdin.readline
MN = 10**6
N = int(input())
locs = sorted([int(input()) for _ in range(N)])
H = int(input())

def other():
    low = 0
    high = MN // 2
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        
        works_from_any_start = False
        for start_index in range(N):
            houses = locs[start_index:] + [house + MN for house in locs[:start_index]]
            hydrants_used = 0
            last_covered_house = -1

            works_from_this_start = True
            for house_location in houses:
                if house_location > last_covered_house:
                    hydrants_used += 1
                    last_covered_house = house_location + 2 * mid
                if hydrants_used > H:
                    works_from_this_start = False
                    break
            if works_from_this_start:
                works_from_any_start = True
                break
        
        if works_from_any_start:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(other())