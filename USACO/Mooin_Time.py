# moo = chara, charai, charai
# if moo is there atleast f times it from bessie
# print all possible moos taking the potential error into account, sorted in alphabetical order
import sys
input = sys.stdin.readline

def count_substring_occurrences(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

N, F = map(int, input().split())
contest = input().strip()
possible_moos = set()

for i in range(N-2):
    if contest[i] != contest[i+1] and contest[i+1] == contest[i+2]:
        moo = contest[i:i+3]
        if count_substring_occurrences(contest, moo) >= F:
            possible_moos.add(moo)

for pos in range(N):
    original_char = contest[pos]
    for new_char in 'abcdefghijklmnopqrstuvwxyz':
        if new_char == original_char:
            continue
            
        modified = contest[:pos] + new_char + contest[pos+1:]
        
        for i in range(N-2):
            if modified[i] != modified[i+1] and modified[i+1] == modified[i+2]:
                moo = modified[i:i+3]
                if count_substring_occurrences(modified, moo) >= F:
                    possible_moos.add(moo)

sorted_moos = sorted(list(possible_moos))

print(len(sorted_moos))
for moo in sorted_moos:
    print(moo)