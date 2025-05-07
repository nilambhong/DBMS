graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

def bfs(graph,start_node):
    visited=[]
    queue=[]
    visited.append(start_node)
    queue.append(start_node)
    print("Following is the Breadth first Search")
    while queue:
        node=queue.pop(0)
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
bfs(graph,'5')