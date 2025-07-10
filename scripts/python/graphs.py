from collections import defaultdict, deque

def toposort(adjList):
    indegrees = [0]*len(adjList)
    for neighbors in adjList:
        for node in neighbors:
            indegrees[node] += 1
    
    sorted_lst = []
    queue = deque([node for node in range(len(adjList)) if indegrees[node] == 0])
    while queue:
        curr = queue.popleft()
        sorted_lst.append(curr)
        for neighbor in adjList[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return sorted_lst

def bfs(adjList, visiting=False, target=None):
    
    path = []
    queue = deque([0])

    if visiting:
        visited = [False]*len(adjList)
        visited[0] = True

    while queue:
        curr = queue.popleft()
        path.append(curr)

        if target is not None and target == curr:
            return path
        
        for neighbor in adjList[curr]:
            if visiting:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
            queue.append(neighbor)
    return path

def dfs(adjList, visiting=False, reverseOrder=False, recursive=False):
    
    def recursive_helper(node, path, visited=None):
        path.append(node)
        neighbors = adjList[node]
        if visited:
            visited[node] = True
        for neighbor in (neighbors[::-1] if reverseOrder else neighbors):
            if visited:
                if visited[neighbor]:
                    continue
            recursive_helper(neighbor, path, visited)

    path = []

    if visiting:
            visited = [False]*len(adjList)
    else:
        visited = None

    if recursive:
        recursive_helper(0, path, visited)
    else: 
        stack = [0]
        if visiting: 
            visited[0] = True
        while stack:
            curr = stack.pop()
            path.append(curr)

            neighbors = adjList[curr]
            if reverseOrder:
                neighbors = neighbors[::-1]
            for neighbor in neighbors:
                if visiting:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                stack.append(neighbor)
    return path

def longest_path_dag(adjList):
    n = len(adjList)
    dp = [-1] * n  # dp[u] = length of longest path starting from u

    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        max_len = 0
        for v in adjList[u]:
            max_len = max(max_len, 1 + dfs(v))
        dp[u] = max_len
        return dp[u]

    return max(dfs(u) for u in range(n))
