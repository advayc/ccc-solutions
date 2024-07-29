# we need to use a stack data structure 
# stacks are implmented using a list. they are last in first out (LIFO) meaning the first one out is the latest to be added
# queues are FIRST IN FIRST OUT (FIFO) - > DFS goes all the way down then up, which is just backtracking, 
import time
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def iterative_dfs(graph, starting_node):
    visited = set()
    stack = []
    visited.add(starting_node)
    stack.append(starting_node) 
    
    while stack: # while the stack is full
        s = stack.pop()
        print(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

# this here is a iterative approach - > this is O(V*E) -> vertices * edges 


start_time = time.time()
iterative_dfs(graph, 'A')
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
    