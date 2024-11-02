city, temp = map(str, input().split())
temp = int(temp)
values = {temp: city}
while city != 'Waterloo':
    city, temp = map(str, input().split())
    temp=int(temp)
    values[temp] = city

m = sorted(values.keys())[0]
print(values[m])