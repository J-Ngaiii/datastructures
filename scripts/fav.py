from collections import defaultdict, Counter
def palindrome_password():
    """
    You are given a password represented as a string of lowercase letters. Your task is to transform it into a new password of the same length that satisfies two conditions:
    1. The new password must be a palindrome.
    2. Every k-th character must be identical (i.e., positions separated by k share the same character).

    Return the minimum number of character changes required to make the original password valid.

    Input:
        A string s (1 ≤ |s| ≤ 10^5), consisting of lowercase English letters.
        An integer k (1 ≤ k ≤ |s|).

    Output:
        An integer representing the minimum number of changes required.

    Example:
        Input:  
            s = "abcda"  
            k = 2  
        Output:  
            2  
        Explanation:  
            To make it a palindrome, positions (0,4) and (1,3) must match.  
            To satisfy the k=2 condition, positions (0,2,4) must be identical and (1,3) must be identical.  
            Minimum 2 changes are required.  
    """

def get_min_changes(s: str, k: int):
    """
    My solution to the Password Palindrome problem which is in the docstring of the function above.

    The problem is solved by initiating it as a graph traversal problem. 
    We define each character as a node, connect them based on the palindrome and k-periodicity restrictions
    then traverse the graph to find all the groups of connected nodes. 

    What's elegant about the problem is the fact that the wider problem (minimizng character mutations for the whole string)
    can be solved by solving individual subproblems (minimizing character mutations for groups of characters). 
    
    This is because the nodes connected into groups by the palindrome and k-periodicity restrictions form disjointly seperable groups.
    """
    n = len(s)
    adj = defaultdict(list)
   
    for i in range(n): # this creates groupings of nodes
        # create an edge based on palindrome connection (i connects to n - 1 - i)
        target_palindrome = n - 1 - i
        if i != target_palindrome:
            adj[i].append(target_palindrome)
            adj[target_palindrome].append(i)
       
        # create an edge based on k-periodicity connection (i connects to i + k)
        if i + k < n:
            adj[i].append(i + k)
            adj[i + k].append(i)
            # we only make this call once because the for loop above will loop to the
            # (i + k)th node on its own then that loop iteration will create the next edge

    # traverse the graph to find groupings of nodes 
    visited = [False] * n
    total_changes = 0
   
    for i in range(n):
        if not visited[i]:
            # visited is for tracking entire groups of nodes
            component_chars = []
            stack = [i]
            visited[i] = True

            # traversal is for retrieving every node/index/char in a node group
            while stack:
                curr = stack.pop()
                component_chars.append(s[curr])
               
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
           
            # once we have a group we make all chars the same
            # min number of changes by mutating all chars to the most frequently appearding char
            count = Counter(component_chars)
            most_common_freq = count.most_common(1)[0][1]
            group_size = len(component_chars)
            changes_needed = group_size - most_common_freq
           
            total_changes += changes_needed
           
    return total_changes