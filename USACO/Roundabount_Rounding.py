import sys
input=sys.stdin.readline

chain_cache = {}
direct_cache = {}

def round(n,p):
	digit = (n//(10**(p-1))) % 10
	if digit >=5:
		n+=10**p
	return (n// (10**p)) * (10**p)

def chain(n):
	if n in chain_cache:
		return chain_cache[n]
		
	highpow = 1
	while highpow * 10 <= n:
		highpow = 10*highpow
	
	power = 1
	curr = n
	tenpow = 1
	while tenpow <= highpow:
		curr = round(curr, power)
		power += 1
		tenpow = 10*tenpow
	
	chain_cache[n] = curr
	return curr

def direct(n):
	if n in direct_cache:
		return direct_cache[n]
		
	p=1
	po=1
	while po*10 <=n:
		p+=1
		po=po*10
	result = round(n,p)
	direct_cache[n] = result
	return result

test_cases = []
max_n = 0
t=int(input())
for _ in range(t):
	n=int(input())
	test_cases.append(n)
	max_n = max(max_n, n)

diff_counts = [0] * (max_n + 1)
running_count = 0
for j in range(2, max_n + 1):
	if chain(j) != direct(j):
		running_count += 1
	diff_counts[j] = running_count

for n in test_cases:
	if n < 2:
		print(0)
	else:
		print(diff_counts[n])