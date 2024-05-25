n = int(input())
values = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
}


for i in range(n):
    l = input()
    ld = l.replace('-', '')
    for z in ld:
        if z in values:
            ld = ld.replace(z, values[z])
    print(f"{ld[:3]}-{ld[3:6]}-{ld[6:10]}")
