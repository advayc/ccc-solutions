import sys
import math
sys.setrecursionlimit(10000)
input = sys.stdin.readline
total=0
n=int(input())
trees = int(input())
yard = [[0 for _ in range(n)] for __ in range(n)]

for i in range(trees): # add tree to n * n yard
    c,r = map(int, input().split())
    yard[c-1][r-1] = 1


for x in range(n):
    print(yard[x])
# finish later 