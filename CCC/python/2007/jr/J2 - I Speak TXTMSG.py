values={
    'CU':"see you",
    ':-)':"I'm happy",
    ':-(':"I'm unhappy",
    ';-)':"wink",
    ':-P':"stick out my tongue",
    '(~.~)':"sleepy",
    'TA':"totally awesome",
    'CCC':"Canadian Computing Competition",
    'CUZ':"because",
    'TY':"thank-you",
    'YW':"you're welcome",
    'TTYL':"talk to you later",
}
i=input()
while i != 'TTYL':
    try:
        print(values[i])
    except:
        print(i)
    i=input()