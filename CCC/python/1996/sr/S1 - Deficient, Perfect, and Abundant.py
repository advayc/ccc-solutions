n=int(input())
for i in range(n):
    bruh=int(input())
    total=0
    for j in range(1,bruh//1):
        if bruh%j==0:
            total+=j
    if total < bruh:
        print(f'{bruh} is a deficient number.')
    elif total > bruh:
        print(f'{bruh} is an abundant number.')
    else:
        print(f'{bruh} is a perfect number.')