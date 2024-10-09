values = {}
while True:
    city, temp = map(str, input().split())
    temp=int(temp)
    if city == 'Waterloo':
        break
    values[city] = temp
    print(values)