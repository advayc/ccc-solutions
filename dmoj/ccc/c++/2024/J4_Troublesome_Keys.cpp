press = input() 
result = input() 
maxquiet = len(press) - len(result)
quietcount = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
troublekeys = []

#finding troublekeys and wrong letter:
for i in alphabet:
    if i in press and i not in result:
        troublekeys.append(i)
    elif i in result and i not in press:
        wrongletter = i

if len(result) < len(press): 
    
    if result.replace(wrongletter, troublekeys[0]) == press.replace(troublekeys[1], ""):
        #troublekey[0] is silly, troublekey[1] is quiet
        sillykey = troublekeys[0]
        quietkey = troublekeys[1]
    else:
        sillykey = troublekeys[1]
        quietkey = troublekeys[0]   
else: 
    sillykey = troublekeys[0]
    quietkey = "-"

print(f"{sillykey} {wrongletter}")
print(quietkey)