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
- Multi-Sourced BFS: Implementing a BFS that runs simulatneously for multiple nodes. Involves populating the queue with all initial starts from which we want to BFS from then using a Level-Tracking BFS => so that all the nodes in a "level" define a particular "generation" that needs to be progressed and taking the `len(queue)` (in conjunction with first-in-first-out queue appending) allows us to select all the nodes defining a particular "level"/"genertation" that needs to be progressed forward.

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

## [Course Schedule](https://neetcode.io/problems/course-schedule/question)

### Main Idea
Intuition
- We’re checking how elems link to each other / dealing with elements that can be grouped by some property (like in palindrome password), in this case prerequisite connections → graph 
- Graph in this case it's intuitive to have classes as nodes 
- For traversal: consider the sol space → notice how impossible schedules would cycle back → means you’re checking for cycles → BFS or Toposort
- If DFS cycle check its a little rough cuz there’s two kinds of cycles that may happen and they don’t count the same:
    - Let define a ‘Dive’ as a starting from a node and going until you hit a leaf node 
    - Dives from two separate nodes may link up or be completely disjoint separate
    - A cycle happens when in the middle of a ‘Dive’ you hit a node that you’ve already traversed in your current ‘Dive’
    - It doesn’t count if you initiate a new ‘Dive’ and hit a node from a previous ‘Dive’ (even though you’ve technically already visited it)

Why it's classic
- Kahn's algorithm: Using toposort for cycle detection and to construct an ordered sequence given a set of unorganized nodes and their neighbors/connections.

Main Explanation
- We need a graph conversion then → graph traversal and checking algorithm → the only way you can’t take all courses is if you have a cycle

- Main Idea of Kahn's algo: if there’s a cycle → there will be some nodes that always have a nonzero indegree => toposort cannot complete
    - Graph representation = adjacency list where index is node # and value is a list of neighbors
    - Toposort indegree tracker: list where index is node # and value is # of indegrees
    - Iterate through prereqs counting nodes that show up and adding indegrees accordingly
    - Run the toposort with a queue:
    - Add all nodes that have indegree 0
    - While queue is not empty → popleft() → decrement indegrees accordingly & increment courses_taken counter using adjacency list → after decrementing indegree add node to queue if indegree == 0
    - Return is courses taken == numCourses

    - If there’s a cycle and numCourses is high enough taken will be < numCourses as we not enough nodes will ever have indegree 0 => can’t add enough nodes to queue then pop them to increment taken enough
    - If we run out of courses before a cycle then target < numCourses also triggers

- Main Idea of DFS Cycle: Keep track of nodes we're diving vs nodes we've dived
    - Run DFS until you run out of courses or hit a cycle
    - Graph representation = adjacency list
    - Visited array with (0 : unvisited, 1 : visiting and 2 : visited) 
        - If you’re in the middle of a dfs ‘Dive’ path and you hit a node with 1 : visiting => you just cycled
        - If you’ve finished a whole dfs ‘Dive’ path from some node without hitting a cycle => mark that node as explored and having no cycle (set visited[node] = 2)

### Implementation - Kahn
```python
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = [[] for i in range(numCourses)]
        indegree = [0] * numCourses


        for a, b in prerequisites:
            # grouping is prereq --> class that has that prereq
            neighbors[a].append(b)
            indegree[b] += 1


        # add the index of all nodes
        # deque here operates conceptually the same as a queue, popleft() operates in O(1)
        # if all nodes cycle => all have indegree[i] > 0 => they never enter queue => queue clears early
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])


        taken = 0
        while queue:
            curr = queue.popleft()
            taken += 1
            for n in neighbors[curr]:
                indegree[n] -= 1
                # if we cycle then the nodes never enter the queue => queue clears early
                if indegree[n] == 0:
                    queue.append(n)

        return taken == numCourses
```
### Implementation - DFS
```python
from collections import defaultdict


def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)


    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited


    def has_cycle(course):
        if visited[course] == 1:  # cycle detected
            return True
        if visited[course] == 2:
            return False


        visited[course] = 1
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        visited[course] = 2 # mark branches of node: ‘course’ has possessing no cycle
        return False


    for i in range(numCourses):
        if has_cycle(i):
            return False


    return True
```
# Graph Leetcode Nifty
