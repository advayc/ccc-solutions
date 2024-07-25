# we need to use a queue data structure 
# queues are lists. the elment that was added first is the first to be removed
# queues are FIRST IN FIRST OUT (FIFO) - > BFS goes layer by layer, 
# -> visit first at the same layer then move on to the next layer
# add nodes to queue, pop nodes off the queue and add to visited
# we do this by defining a variable to whatever is being popped from the queue(0)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, starting_node):
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

bfs(graph, 'A')
# run the bfs function starting at our node A