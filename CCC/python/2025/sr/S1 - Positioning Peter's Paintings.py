# A * B
# X * Y

'''
minimum permimeter to display 
'''
import sys
input=sys.stdin.readline


a,b,x,y=map(int, input().split())
print(min(2 *((a+x)+max(b, y)), 2 * (max(a, x) +(b+y))))
