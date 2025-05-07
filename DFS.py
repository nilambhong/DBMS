graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]

}

def dfs_iterative(graph,start_node):
    visited=set()
    stack=[start_node]
    print("Following is the Depth_First_Search(iteratie")
    while stack:
        node= stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
         # add neighbor reversed to maintain left to right order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                   stack.append(neighbor)
dfs_iterative(graph,'5')