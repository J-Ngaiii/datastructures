from collections import defaultdict, Counter

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

def get_min_changes(s: str, k: int):
    """
    Password Palindrome problem 

    Solution explanation points
    - Visited array allows us to track connected components 
        - for an arbitrary index/node i, the indices/nodes i + 1 and n - 1 - i would form the same group
        - visited prevents us from revisiting indices/nodes corresponding to already known groups

    - Point of traversal:
        - when he hit a index/node belonging to an unkown group we traverse all its neighbors (either bfs or dfs)
        - traversing all neighbors --> defines the full group 
    """
    n = len(s)
    adj = defaultdict(list)
    
    for i in range(n):
        # We create an edge based on Palindrome connection (i connects to n - 1 - i)
        target_palindrome = n - 1 - i
        if i != target_palindrome:
            adj[i].append(target_palindrome)
            adj[target_palindrome].append(i)
        
        # We create an edge based on K-Periodicity connection (i connects to i + k)
        if i + k < n:
            adj[i].append(i + k)
            adj[i + k].append(i)
            # we only make this call once because the for loop above will loop to the 
            # (i + k)th node on its own then that loop iteration will create the next edge
            
    # 2. Traverse the Graph to find Connected Components
    visited = [False] * n
    total_changes = 0
    
    for i in range(n):
        if not visited[i]:
            # visited is for tracking entire groups groups 
            # traversal is for retrieving every node/index/char in a Connected Component Group
            component_chars = []
            stack = [i]
            visited[i] = True
            
            while stack:
                curr = stack.pop()
                component_chars.append(s[curr])
                
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            # 3. Calculate Changes for this Group
            # We want to make all chars in this group the same.
            # Best choice: the most frequent character currently in the group.
            count = Counter(component_chars)
            most_common_freq = count.most_common(1)[0][1]
            
            # Number of changes = Total nodes in group - Frequency of the most popular char
            group_size = len(component_chars)
            changes_needed = group_size - most_common_freq
            
            total_changes += changes_needed
        # we can just for loop through because the problem is disjointly seperable
        # the inputted string can always be seperated into distinct Connected Component Groups with no overlap
        # thus min num of swaps overall = min(num swaps group 1) + min(num swaps group 2) + ... etc
            
    return total_changes

def num_combo_schedules(n: int, n_intervals: int) -> int:
    # Edge case: If we have more than 1 slot but only 1 process,
    # we can't avoid repeats.
    if n_intervals > 1 and n == 1:
        return 0
    if n_intervals == 1:
        return n
        
    # First slot has 'n' choices.
    # The remaining (n_intervals - 1) slots each have 'n-1' choices.
    return n * ((n - 1) ** (n_intervals - 1))