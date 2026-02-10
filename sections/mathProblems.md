---
layout: default
title: "Math-Based Algorithms"
date: 2026-02-10
categories: DSA
---

# Math Problems Conceptual

## Patterns in Differences: Telescoping Sum

## Patterns in Differences: Parity Algorthms

# Math Problems Toolkit and Tips

## Data 140 Appraoch: Unifying Conceptual & Question-Banking
- Look for occurences of the concepts above & refer to your internal memory of past questions
- Then match to see if there are sumilar cues

## Telescoping Sum Cues
- If you're tracking, conditioning on and summing up the differences of values across discrete time 
    - Whereas if you're summing up all values, creating subintervals, not tracking differences => prefix sum


# Math Problems Leetcode 
## [Best Time to Buy and Sell Stock II] (https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii/question)

### Main Idea
Intuition

- Buying and selling items across discrete time then adding up the differences => Telescoping Sums. Buying at time $t_1$ then selling at time $t_n$ is the same as: 
$$\sum_{i=1}^{n-1} t_{i+1} - t_i$$
- So we don't have to handle for behavior where we buy a stock then hold it for multiple days. The profit will equal summing up all the positive intermediate differences
- To maxamize profit across some time interval $t\in\{1, 2, ..., n\}, \forall t$ we just want to take the telescoping sum pairings where the intermediate differences are positive, eliminating all the pairings that contribute negatively. 
$$\max = \sum_{i=1}^{n-1} t_{i+1} - t_i : t_{i+1} - t_i > 0$$

Main Explanation
- We check if the current day's price > the previous day's price => if so then the telescoping sum pairing formed by these two numbers is positive => we want to add this pairing to our running sum. 

### Implementation
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Telescoping sum: difference from buying at time t1 then selling at time tn is equal
        to the sum of t1 - t2 + t2 - t3 + ... + tn-1 - tn

        This means we don't have to handle for actually holding the stock for a certain amount of days. 
        We can just take all the intermediate sums which adds up to be the same. 

        Some differences are positive whereas others are negative so to maxamize profit
        So to max profit we just want to register the tk-1 - tk pairings that are positive.
        """

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit_today = prices[i] - prices[i-1]
                max_profit += profit_today
                
        return max_profit
```

## Palindrome Password

### Problem
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

### Main Idea
Intuition

Main Explanation

### Implementation
```python
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
```