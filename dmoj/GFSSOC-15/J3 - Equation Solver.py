c = input()
tokens = c.split()
result = 0
current_operator = 'P' 

for i in tokens:
    if i == '=':
        break  
    elif i == 'P':
        current_operator = 'P'
    elif i == 'M':
        current_operator = 'M'
    else:
        number = int(i)
        if current_operator == 'P':
            result += number
        elif current_operator == 'M':
            result -= number

print(result)
