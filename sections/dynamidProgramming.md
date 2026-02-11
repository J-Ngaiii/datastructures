---
layout: default
title: "Dynamic Programming"
date: 2026-02-08
categories: DSA
---
# Dynamic Programming Conceptual

# Dynamic Programming Toolkit and Tips

## Longest Path Dag

Simple max-aggregation DP algorithm for calculating the longest path in a DAG. Some cool engineering features:
- The base case is not explicitly handled, instead we instantiate a forloop through all neighbors of a given node that is meant to not run if the given node happens to be a leaf node (thus possessing a depth of 0).
- DFS is the go to method for explore the full depth of a path whereas BFS is better for cycle detection show we use DFS here. However, DFS alone is not garuanteed to give the longest path. 
- The final return statement is a max call over calling the iterative dfs starting from every single node => garuantees that we update `dp[u]` accordingly if another starting spot provides a longer path and we take a max over all returned values. Aggregating over all returned values of a recursive DP function is a really common way of consolidating the final answer. 

```python
def longest_path_dag(adjList):
    n = len(adjList)
    dp = [-1] * n  # dp[u] = length of longest path starting from u

    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        max_len = 0

        # dag means we will hit a non-cyclic leaf
        # for loop doesn't execute and we just store max length = 0

        # then for non-leaf cases we compare the lengths of all neighbors 
        # add + 1 to account for current node
        for v in adjList[u]: 
            max_len = max(max_len, 1 + dfs(v))
        dp[u] = max_len
        return dp[u]

    return max(dfs(u) for u in range(n))
```

# Dynamic Programming Leetcode Classics
## Climbing Up Stairs
### Problem
- You are climbing a staircase. It takes n steps to reach the top.
- Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
- Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
- Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

### Main Idea
Intuition: Why DP?
- Iterative problem where the answer at arbitrary index i is a non-memoryless function of all previous answers at all previous indices
- Good Substructure: The number of ways there are to climb up k stairs is related to the number of ways there are to climb up k - 1and k - 2 stairs, specifically # of ways to climb k = # of ways to climb k-1 + # of ways to climb k-2
- Overlapping subproblems to cache you compute # of ways to climb k multiple times to feed in as a solution to larger values of k

Intuition: What to notice
- For 1 step there is 1 way up
- For 2 steps there are 2 ways up
- For 3 steps there are 3 ways up = # ways up 1 step + # ways up 2 steps
- For 4 steps there are 5 ways up = # ways up 3 steps + # ways up 2 steps
- So for $k$ steps, the # ways up $k$ setps = # ways up $k-1$ steps $+$ # ways up $k-2$ steps

Main Explanation
- DP array with index i represents the nuymber of ways up i steps.

### Implemenatations

Naive (recursive no brute force - backtracking)
```python
def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2


        n -= 1
        ones = self.climbStairs(n) # take one step
        n -= 1
        twos = self.climbStairs(n) # take two steps
        return ones + twos
```

Top Down Recursive Memoization
```python
class Solution(object):
        def climbStairs(self, n):
            memo = {}


            def dfs(steps):
                if steps == 0:
                    return 1  # One way to do nothing
                if steps < 0:
                    return 0  # No way to go negative
                if steps in memo:
                    return memo[steps]


                # Try taking 1 or 2 steps and cache the result
                memo[steps] = dfs(steps - 1) + dfs(steps - 2)
                return memo[steps]


            return dfs(n)
```

Bottom-Up Iterative Tabular
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```
# Dynamic Programming Leetcode Nifty

## [Range Sum Query 2D](https://neetcode.io/problems/range-sum-query-2d-immutable/question)

### Main Idea
Intuition
- O(1) time means you need to do some precomputation
- Since we’re summing up over intervals and ranges we can use a prefix sum
- For a given square in the prefix sum matrix, we need to incorporate info summed along the row and along the col (geometric inclusion exclusion)
- Then to return the right sum it’s just geometry, every single prefix sum matrix elem (with coords [i, j]) is a square from [0, 0] to [i, j] (geometric inclusion exclusion)

Main Idea
- We use a padded matrix so that prefix_sum_matrix[i + 1][j + 1] corresponds to matrix[i][j]
- Then use recursive formula: prefix_sum_matrix[i + 1][j + 1] = matrix[i][j] + prefix_sum_matrix[i][j + 1] + prefix_sum_matrix[i + 1][j] - prefix_sum_matrix[i][j]
- Then to calculate the sum do prefix_sum_matrix[row2 + 1][col2 + 1] - prefix_sum_matrix[row2][col1] - prefix_sum_matrix[row1][col2] + prefix_sum_matrix[row1][col1]

### Implementation
```python
from typing import List

class NumMatrix:


    def __init__(self, matrix: List[List[int]]):
        """
        DP prefixsum problem where you sum along the axis then subtract
        """
        # [row][col] indexing setup, we do + 1 to pad the matrix
        prefix_matrix = [ [0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        print("dim of prefix matrix", len(prefix_matrix), len(prefix_matrix[0]))


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print("coords", (i + 1, j + 1))
                curr = matrix[i][j] # base matrix[i][j] corresponds to prefix[i + 1][j + 1]
                dp_prev = prefix_matrix[i][j]
                dp_top = prefix_matrix[i][j + 1]
                dp_left = prefix_matrix[i + 1][j]


                prefix_matrix[i + 1][j + 1] = curr + dp_top + dp_left - dp_prev


        self.pref = prefix_matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.pref[row2 + 1][col1]
        top = self.pref[row1][col2 + 1]
        topleft = self.pref[row1][col1]


        return self.pref[row2 + 1][col2 + 1] + topleft - left - top
```

