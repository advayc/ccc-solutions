P = int(input()) #packages dev
C = int(input()) #collision 

if P > C:
    F = (50*P) - (10*C) + 500

else:
    F = (50*P) - (10*C)

print(F)