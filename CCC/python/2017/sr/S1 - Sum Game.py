n = int(input())
swifts = list(map(int, input().split()))
sem = list(map(int, input().split()))
final=[]
culmsw = [0 for _ in range(n)]
culmswem = [0 for _ in range(n)]
for i in range(n):
    culmsw[i] = culmsw[i-1]+swifts[i]
    culmswem[i] = culmswem[i-1]+sem[i]
    if culmsw[i] == culmswem[i]:
        final.append(i+1)
    
if len(final) == 0: print(0)
else: print(max(final))
# simple imp using prefix array