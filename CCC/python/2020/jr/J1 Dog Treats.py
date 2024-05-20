S = int(input())
M = int(input())
L = int(input())
dog_happy = 1 * S + 2 * M + 3 * L

if dog_happy >= 10:
    print('happy')
elif dog_happy < 10:
    print('sad')
