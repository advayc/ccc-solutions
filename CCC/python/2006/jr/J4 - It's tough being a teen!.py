first=[1,1,2,3,3]
second=[7,4,1,4,5]
todo=[]
y=int(input())
u=int(input())
while y!=0 and u!=0:
    first.append(y)
    second.append(u)
    y=int(input())
    u=int(input())
inst=[1,2,3,4,5,6,7]
for i in range(7):
    if [r for r in inst if r not in second]==[]:
        print ('Cannot complete these tasks. Going to bed.')
        break
    put=min([r for r in inst if r not in second])
    todo.append(put)
    inst.remove(put)
    while put in first:
        first[first.index(put)]=0
    for q in range(0,len(first)):
        if first[q]==0:
            second[q]=0
if len(todo)==7:
    print (' '.join(list(map(str,todo))))