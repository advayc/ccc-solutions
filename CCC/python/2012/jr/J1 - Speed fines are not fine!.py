limit=int(input())
ur=int(input())
if ur <= limit:
    print('Congratulations, you are within the speed limit!')
elif (ur-limit) >= 31:
    print('You are speeding and your fine is $500.')
elif (ur-limit) >= 21 and (ur-limit) <= 30:
    print('You are speeding and your fine is $270.')
elif (ur-limit) >= 1 and (ur-limit) <= 20:
    print('You are speeding and your fine is $100.')