# solved using a BFS and a bunch of simple input handling
graph = {
    1: [6],
    2: [6],
    3: [4, 5, 6, 15],
    4: [3, 5, 6],
    5: [3, 4, 6],
    6: [1, 2, 3, 4, 5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10, 12],
    10: [9, 11],
    11: [10, 12],
    12: [9, 11, 13],
    13: [12, 14, 15],
    14: [13],
    15: [3, 13],
    16: [17, 18],
    17: [16, 18],
    18: [16, 17]
}

def bfs(graph, starting_node, ending_node):
    if starting_node not in graph or ending_node not in graph:
        return "Not connected"
    count = 0
    visited = set()
    queue = []
    queue.append((starting_node, [])) # with add every traversed node into the queue
    visited.add(starting_node)
    while queue:
        current_node,count = queue.pop(0)
        if current_node == ending_node:
            return len(count)
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.append((neighbour, count+[neighbour]))
                visited.add(neighbour)
    return "Not connected"

while True:
    dfriends=set()
    move = input()
    if move == 'q':
        break
    elif move == 'd':
        x = int(input())
        y = int(input())
        graph[x].remove(y)
        graph[y].remove(x)
    elif move == 'i':
        x = int(input())
        y = int(input())
        graph[y].append(x)
        try: # using try and except to determine if this is a new person added to friends graph
            graph[x].append(y)
        except:
            graph[x] = [y]
    elif move == 'n':
        x = int(input())
        print(len(graph[x]))
    elif move == 'f':
        x = int(input())
        for i in graph[x]:
            for j in graph[i]:  
                if j not in graph[x] and j != x: # go through the friend, loop through each friend
                    dfriends.add(j)
        print(len(dfriends))
    elif move == 's':
        x = int(input())
        y = int(input())
        print(bfs(graph, x, y))

'''
graph after given test case
i
20
10
i
20
9
n
20
f
20
s
20
6
q

{1: [6], 
2: [6], 
3: [4, 5, 6, 15], 
4: [3, 5, 6], 
5: [3, 4, 6], 
6: [1, 2, 3, 4, 5, 7], 
7: [6, 8], 
8: [7, 9], 
9: [8, 10, 12, 20], 
10: [9, 11, 20], 
11: [10, 12], 
12: [9, 11, 13], 
13: [12, 14, 15], 
14: [13], 
15: [3, 13], 
16: [17, 18], 
17: [16, 18], 
18: [16, 17], 
20: [10, 9]}'''