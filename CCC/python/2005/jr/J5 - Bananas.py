w = input()
while w != 'X':
	while 'ANA' in w or 'BAS' in w:
		w = w.replace('ANA','A')
		w = w.replace('BAS','A')

	if w=='A':print('YES')
	else: print('NO')
	w = input()
