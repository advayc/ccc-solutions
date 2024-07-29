# we need to use a queue data structure 
# queues are lists. the elment that was added first is the first to be removed
# queues are FIRST IN FIRST OUT (FIFO) - > BFS goes layer by layer, 
# -> visit first at the same layer then move on to the next layer
# add nodes to queue, pop nodes off the queue and add to visited
# we do this by defining a variable to whatever is being popped from the queue(0)
import time
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def graph_bfs(graph, starting_node): # this is a BFS with a GRAPH - > implmented using a dictonary to show vertices and edges
    visited = set()
    queue = []
    queue.append(starting_node) # add starting node into the queue
    visited.add(starting_node) # add starting node to visited set

    while queue: #loop untill the queue is empty
        current_node = queue.pop(0) # remove the first element from the queue - > using the first in first out principle
        print(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

start_time = time.time()
graph_bfs(graph, 'A')
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for Graph BFS: {execution_time} seconds \n---------------\n")

dlist = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F']
]

def list_bfs(dlist, startx,starty):
    directions = [(0,1),(0,-1),(-1,0),(1,0)] # directions up down left right  
    rows = len(dlist)
    cols = len(dlist[0])
    visited = set()
    queue = []
    queue.append((startx, starty))
    visited.add((startx,starty))

    while queue: # loop till the queue is empty
        x,y = queue.pop(0)
        print(dlist[x][y])
        for dx,dy in directions:
            newx = x+dx
            newy = y+dy
            if 0 <= newx <= rows and 0 <= newy <= cols and (newx,newy) not in visited:
                queue.append((newx,newy))
                visited.add((newx,newy))

start_time = time.time()
list_bfs(dlist, 0,0) # run the list bfs functon s
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for 2D list BFS: {execution_time} seconds")
# run the bfs function starting at our node A