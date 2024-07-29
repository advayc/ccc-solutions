n = int(input())
possible = [100,20,10,5,1] 
count = 0
for each in possible:
    count += n // each
    n %= each
    print(n)
print(count)
# starting from 100, doing integer division for number of ways the denomination can go into the current bill value
# update the bill value by getting the remainder of the bill value divided by the current denomination