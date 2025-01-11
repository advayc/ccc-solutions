n=int(input())
words=[]
get=set()

for i in range(n):
    bruh=input()
    if bruh in words:
        get.add(bruh)
    else:
        words.append(bruh)

for word in get:
    words.remove(word)
print(len(words))