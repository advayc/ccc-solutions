number,length=map(int, input().split())

words=[]
for j in range(number):
    word=input()
    words.append(word)

def heavy(word,letter):
    return word.count(letter)>1 # is heavy if letter in occurs string more then once 
    
def alt(word):
    for i in range(length-1):
        if heavy(word,word[i]) == heavy(word,word[i+1]):
            return 'F'
    return 'T'
        
for each in words:
    print(alt(each))