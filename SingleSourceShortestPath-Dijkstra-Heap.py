#!/usr/bin/python

'''
Find the Shortest path from a single source to all its vertices

Dijkstra Algorithm using HEAP

Important point is the way in which the next vertex to process is chosen. It is a Greedy algorithm. 

Priority Q or Min Heap is used for chosing the next closest vertex
'''
import math
from heapq import *

def FindShortestPath(graph, N, src):
    if src not in graph:
        return None

    result = []
    dist = [math.inf] * N
    pq = []
    dist[src] = 0
    heappush(pq, (0,src))

    while pq:
        d, u = heappop(pq) # heap allows us the pick shortest distance naturally in O(log N)
 
        if d > dist[u]: #since we are using lazy deletion (keeping duplicates of vertex in heap) when we get duplicate from heap whose distance is greater ignore it
            continue

        result.append(u)
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]: #if there is a shorter route from u to v pick it
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))

    return result


def main():
    N = 5
    graph = { 0: {4:1}, 1: {3:3, 4:6}, 2:{1:2, 0:6, 3:7}, 3: {}, 4: {}}

    print(FindShortestPath(graph, N,2))




if __name__ == "__main__":
    main()
