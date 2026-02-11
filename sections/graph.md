---
layout: default
title: "Graphs"
date: 2026-02-10
categories: DSA
---

# Graph Conceptual

# Graph Toolkit and Tips

# Graph Leetcode Classics

## [Rotting Fruit](https://neetcode.io/problems/rotting-fruit/question?list=neetcode250)

### Main Idea

Intuition
- Cues
    - Every adjecent fruit rots => we want to explore all neighbors once => BFS
    
- Thus
    - We start at each rotten => BFS BUT we track each "level" of BFS we iterate thru to track mins
    - To track we just instantiate a queue and when the length of the queue matches 
    - => we know we've exhausted all k-degree neighbors defining a certain "level" of a BFS search
    - Then we return mins to exhaust everything for all rotten fruit then take the min

- Extra Insights I Needed:
    - Checking every single orange is inefficient so => we mutate the grid using it as a seen array
    - All oranges begin rotting simultaneously
    - To check fresh oranges => as we BFS track fresh oranges and see if fresh orange count = 0 by the end

Why it's classic:
- Level-Tracking BFS: Using a `while queue` loop followed by --> checking `len(queue)` then for looping thru only the first few nodes that define a "level"
- Multi-Sourced BFS: Implementing a BFS that runs simulatneously for multiple nodes. Involves populating the queue with all initial starts from which we want to BFS from then using a Level-Tracking BFS => so that all the nodes in a "level" define a particular "generation" that needs to be progressed and taking the `len(queue)` (in conjunction with first-in-first-out queue appending) allows us to select all the nodes defining a particular "level"/"genertation" that needs to be progressed forward

Main Explanation
- First we preprocessing tracking all organges alr rotten and counting total # of fresh fruit
- Then we initiate a Multi-Sourced AND level-tracking BFS
- Update the grid, using it as our seen array
- At the end check if the num of fresh fruit remaining is non-zero

### Implementation
```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # preprocess: find all wrotten and fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # base case: 0 fresh oranges => 0 minutes needed to have no fresh fruit
        if fresh_count == 0:
            return 0
            
        minutes = 0
        # Multi-Sourced BFS: Starting with multiple nodes in the queue 
        # then progressing all of them at once
        while queue and fresh_count > 0:
            minutes += 1
            #process all oranges currently in the queue at the current "level"
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    # if neighbor is within bounds and is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # rot it! to track seen fresh oranges
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc)) # then propogate
        
        # check if fresh oranges remain
        return minutes if fresh_count == 0 else -1
```
# Graph Leetcode Nifty
