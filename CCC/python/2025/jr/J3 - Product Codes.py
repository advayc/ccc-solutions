import sys
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    original_code = input().strip()
    uppercase_letters = []
    integer_sum = 0
    i = 0
    while i < len(original_code):
        char = original_code[i]
        if 'A' <= char <= 'Z':
            uppercase_letters.append(char)
            i += 1
        elif 'a' <= char <= 'z':
            i += 1
        elif '0' <= char <= '9':
            j = i
            while j < len(original_code) and '0' <= original_code[j] <= '9':
                j += 1
            number_str = original_code[i:j]
            integer_sum += int(number_str)
            i = j
        elif char == '-':
            if i + 1 < len(original_code) and '0' <= original_code[i+1] <= '9':
                j = i + 1
                while j < len(original_code) and '0' <= original_code[j] <= '9':
                    j += 1
                number_str = original_code[i:j]
                integer_sum += int(number_str)
                i = j
            else:
                i += 1
        else:
            i += 1
            
    result = "".join(uppercase_letters) + str(integer_sum)
    print(result)