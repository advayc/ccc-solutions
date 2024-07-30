start_end_distance=int(input())
clubs = int(input())
distances = [int(input()) for _ in range(clubs)]
queue = [(0,0)] # starting position, we havent done any strokes
visited = set()
win=False
while queue:
    cur, strokes = queue.pop(0)
    if start_end_distance == cur:
        print('Roberta wins in',strokes,'strokes.')
        win = True
        break
    # go through each club move
    for club in distances:
        next = cur + club

        if next <= start_end_distance and next not in visited: # check if it works and we havent done it already
            visited.add(next)
            queue.append((next,strokes+1))

if not win:
    print("Roberta acknowledges defeat.")

# BFS going through each distance -> storing each distance as a node