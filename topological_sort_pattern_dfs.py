#!/usr/bin/python

'''
Topological Sort Pattern: using DFS

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

def dfs(node, adjList, visited, indegree, result):
    visited[node] = True
    result.append(node) # pick that task
    
    for next_node in adjList[node]:
        indegree[next_node] -= 1 # once prerequisite task is done remove dependency of next tasks
        if not visited[next_node]:
            dfs(next_node, adjList, visited, indegree, result)

def isPossibleLinearOrder(N, prerequisite):
    if N <=1 or len(prerequisite) <= 1:
        return True

    visited= {i : False for i in range(N)}
    adjList = {i: [] for i in range(N)}
    indegree = {i: 0 for i in range(N)}
    
    for p in prerequisite:
        src, dest = p[0], p[1]
        adjList[src].append(dest)
        indegree[dest] += 1
    
    # print(indegree)
    result = []
    for i in range(N):
        if not visited[i] and indegree[i] == 0: # start with a task that is not done and has no preprequisite
            dfs(i, adjList, visited, indegree, result)
    # print(result)
    
    return len(result) == N


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

