#!/usr/bin/python

'''
    Strongly Connected Components (SCC)

    Kosaraju Algorithm using Topoogical sort to find all SCCs in a graph.

    Note: In this case the topo sort won't exit when cycle is detected but just loads the stack in reverse topo order.
    
    Given a graph list out all SCCs of it.
'''


def dfs(vertex, graph, visited, stack):
    visited[vertex] = True

    for next_vertex in graph[vertex]:
        if not visited[next_vertex]:
            dfs(next_vertex, graph, visited, stack)
    
    stack.append(vertex)

def getGraphTranspose(graph):
    graphTranspose = {i : [] for i in range(1,len(graph)+1)}

    for src,dests in graph.items():
        for dest in dests:
            graphTranspose[dest].append(src)

    return graphTranspose

def getSCCs(vertex, graphTranspose, SCC, visited, count):
    visited[vertex] = True
    SCC[count].append(vertex)

    for next_vertex in graphTranspose[vertex]:
        if not visited[next_vertex]:
            getSCCs(next_vertex, graphTranspose, SCC, visited, count)
    

def ListAllSCCs(N, Edges):
    graph = {i: [] for i in range(1,N+1)}
    visited = {i: False for i in range(1,N+1)}
    stack = []

    for e in Edges:
        src, dest = e[0], e[1]
        graph[src].append(dest)

    for vertex in range(1, N+1):
        if not visited[vertex]:
            dfs(vertex, graph, visited, stack)

    graphTranspose = getGraphTranspose(graph)
    visited = {i: False for i in range(1,N+1)}
    count = 0
    SCC = {}
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            count += 1
            if count not in SCC:
                SCC[count] = []
            getSCCs(vertex, graphTranspose, SCC, visited, count)
    
    print("List of SCCs: ", SCC)
    print("Number of SCCs: ", count)

    

def main():
    N = 9
    Edges = [[1,2], [2,3], [3,1], [3,4], [3,5], [4,6], [4,9], [5,6], [9,7], [6,7], [7,8], [8,6]]
    ListAllSCCs(N, Edges)


if __name__ == "__main__":
    main()
