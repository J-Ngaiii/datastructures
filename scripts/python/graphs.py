from collections import defaultdict, deque

def toposort(adjList):
    """
    Docstring for toposort
    
    Why deque? In the case that:
    - Two neighbor nodes (i, j) of some starter get decremented to indegree == 0 
    - Then a third node k, that's a neighbor of i gets decremented to indegree == 0
    
    We want to make sure that all neigbors of the original starter (both i and j) get processed
    before the second degree neighbor k (which is a neighbor of i not the starter directly)
    """
    indegrees = [0]*len(adjList)
    for neighbors in adjList:
        for node in neighbors:
            indegrees[node] += 1 
            # we go into the neighbors list of all nodes
            # then each time a node shows up as a neighbor we increment tthe indegrees list
    
    sorted_lst = []
    queue = deque([node for node in range(len(adjList)) if indegrees[node] == 0])
    # we start with the node that is the neighbor of no one, with no indiegrees
    # 
    while queue:
        curr = queue.popleft()
        sorted_lst.append(curr)
        for neighbor in adjList[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
            # then for every neighbor of our starter node, we decrement the indegree vector by one
            # until we find a new node that has no indegree then add that to the queue

    return sorted_lst

def bfs(adjList, visiting=False, target=None):
    """
    Docstring for bfs
    - Visited mode is option, just allows us to skip revisiting nodes if there's a cycle

    We use a queue so that all the first degree children of a node get processed before any second degree connections
    
    """
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
            # early stop 
        
        for neighbor in adjList[curr]:
            if visiting:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
            queue.append(neighbor)
            # we go through the neighbors of the current node and add them to the queue
    return path

def dfs(adjList, visiting=False, reverseOrder=False, recursive=False):
    """
    Docstring for dfs
    - Again visiting mode is just for maintating a visited array that lets us skip nodes ocassionally
    
    We us a stack that way the latest child is the first popped out --> allows us to path down to the end of a graph
    """
    def recursive_helper(node, path, visited=None):
        """
        Docstring for recursive_helper
        Recursive implementation does three things
        - Takes in ONE node and processes it (in this case add to a path array that's maintained)
        - Then iterate through neighbors feeding the neighbors into the node arg to restart the cycle
        - It becomes DFS because the first recursive call will keep opening new function calls before letting the for loop iterate forward
        """
        path.append(node)
        neighbors = adjList[node]
        if visited:
            visited[node] = True
        for neighbor in (neighbors[::-1] if reverseOrder else neighbors):
            if visited:
                if visited[neighbor]:
                    continue
            recursive_helper(neighbor, path, visited)
            # iterate through all neighbors then 

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
