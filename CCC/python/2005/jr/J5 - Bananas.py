w = input()
while w != 'X':
	while 'ANA' in w or 'BAS' in w:
		w = w.replace('ANA','A')
		w = w.replace('BAS','A')

	print('YES' if w == 'A' else 'NO')
	w = input()
