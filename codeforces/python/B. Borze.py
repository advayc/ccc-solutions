d = input()
c = ''
i = 0
while(i<len(d)):
    if d[i] == '.':
        c+= '0'
        i+=1
    elif d[i] == '-' and d[i+1] == '-':
        c+= '2'
        i+=2
    else:
        i+=2
        c += '1'

print(c)
