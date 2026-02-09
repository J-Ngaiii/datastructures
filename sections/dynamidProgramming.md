---
layout: default
title: "Range Sum Query 2D"
date: 2026-02-08
categories: DSA leetcode
---
# Dynamic Programming Conceptual

# Dynamic Programming Toolkit and Tips

# Dynamic Programming Leetcode
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

