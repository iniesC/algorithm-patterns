#!/usr/bin/python

'''
Topological Sort Pattern: using DFS and checking for back edges

Used for linear ordering of vertices in a Directed Acyclic Graph (DAG). The vertices in real life could be tasks or courses or different items that
could be scheduled in a linear order by meeting all pre-requisites. 

Note: The pre-requisites are never cyclic. If they are cyclic they cannot be linearly ordered.

Problem Statement:
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need 
to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, 
find out if it is possible to schedule all the tasks.

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2] 

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.


'''

def isCycle_DFS(node, adjList, visited, recstack, result):
    visited[node] = True
    recstack[node] = True # Keep record of the node in current stack

    for next_node in adjList[node]:
        if not visited[next_node]:
            if isCycle_DFS(next_node, adjList, visited, recstack, result): # if there is a cycle exit
                return True
        elif recstack[next_node] == True: # check for back edges meaning did we see this vertex earlier in current path
            return True
    

    result.append(node) # store the topo order in reverse

    recstack[node] = False # pop the node from the stack
    return False

def isPossibleLinearOrder(N, prerequisite):
    if N <=1 or len(prerequisite) <= 1:
        return True

    visited= {i : False for i in range(N)}
    recstack= {i : False for i in range(N)}
    adjList = {i: [] for i in range(N)}
    
    for p in prerequisite:
        src, dest = p[0], p[1]
        adjList[src].append(dest)

    result = []
    for i in range(N):
        if not visited[i]: # start with a task that is not done and has no preprequisite
            if isCycle_DFS(i, adjList, visited, recstack, result):
                return False
    
    print("Topological Linear order: ", result[::-1]) # Topological sorted order on a DAG
    
    return True


def main():
    Tasks = 3
    Prerequisites=[[0, 1], [1, 2]]
    print(isPossibleLinearOrder(Tasks, Prerequisites))

    Tasks=6
    Prerequisites=[[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
    print(isPossibleLinearOrder(Tasks, Prerequisites))

    Tasks=3
    Prerequisites=[[0, 1], [1, 2], [2, 0]]
    print(isPossibleLinearOrder(Tasks, Prerequisites))

    Tasks=5
    Prerequisites=[[0, 1], [1, 2], [2, 4], [2,3]]
    print(isPossibleLinearOrder(Tasks, Prerequisites))
    
    Tasks=5
    Prerequisites=[[0, 1], [1, 2], [2, 0], [2,3]]
    print(isPossibleLinearOrder(Tasks, Prerequisites))

if __name__ == "__main__":
    main()

