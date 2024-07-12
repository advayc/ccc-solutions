# silly = wrong letter every time its pressed 
# quiet = nothing 
# silly key has to be sonething
# he never dies -> silly -> quiet and quiet -> silly
'''
forloops
fxrlxxps

forloops
fxrlxxp

forloops
frlpz

'''
og = input()
after = input()
quiet = '-'
x=[]
alpha='abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if (i in og) and (i not in after):
        x.append(i)
    elif i in after and i not in og:
        replaced = i

if len(og)>len(after): # length of cant be equal for there to be a quiet key
    if after.replace(replaced,x[0]) == og.replace(x[1],''): 
        quiet = x[1]
        sil = x[0]
    else:
        quiet = x[0]
        sil = x[1]
else:
    sil = x[0]
print(sil, replaced)
print(quiet)