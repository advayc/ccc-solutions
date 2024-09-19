current = 1
while True:
    n = int(input())
    if n == 0:
        print("You Quit!")
        break
    current += n

    if current > 100:
        current = current - n

    if current == 9:
        current = 34
    if current == 40:
        current = 64
    if current == 54:
        current = 19
    if current == 67:
        current = 86
    if current == 90:
        current = 48
    if current == 99:
        current = 77

    print(f'You are now on square {current}')
    if current == 100:
        print("You Win!")
        break    
