alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=input()
msg=input()
msg = ''.join([i for i in msg if i.isalpha()]) # get rid of da stupid characters
lenkey=len(key)
bru={}
for i in key:
    bru[i] = []

for char in range(len(msg)):
    index=char%lenkey
    bru[key[index]].append(msg[char])

for k in key:
    shift_amount = alphabet.index(k)
    for j in range(len(bru[k])):
        bru[k][j] = alphabet[(alphabet.index(bru[k][j]) + shift_amount) % 26]

new = ''
num_rows = (len(msg) + lenkey - 1) // lenkey

for i in range(num_rows):
    for k in key:
        if i < len(bru[k]):
            new += bru[k][i]

print(new)