---
layout: default
title: "Binary Search"
date: 2026-02-08
categories: DSA Conceptual
---

# Binary Search Conceptual

# Binary Search Toolkit and Tips
### Implementation
Recursive
```python
class Solution:
    def helper(self, nums, target, l, r):      
        if l > r:
            # we iterated past => no value found
            return -1
       
        mid = (r - l) // 2 + l # midpoint is window length // 2 then add left to adjust for shift


        # compare target with elem at midpoint
        if target > nums[mid]:
            # if larger next range starts to the right of midpoint
            return self.helper(nums, target, mid + 1, r)
        elif target < nums[mid]:
            # if smaller next range starts to the left of midpoint
            return self.helper(nums, target, l, mid - 1)
        else:
            return mid
   
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        return self.helper(nums, target, l, r)
```

Iterative
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        l, r = 0, len(nums) - 1
        while l <= r: # condition is to keep left pointer less than right
            mid = (r - l) // 2 + l # midpoint is window length // 2 then add left to adjust for shift


            # compare target with elem at midpoint
            if target > nums[mid]:
                l = mid + 1 # if larger next range starts to the right of midpoint
            elif target < nums[mid]:
                r = mid - 1 # if smaller next range starts to the left of midpoint
            else:
                return mid
        return -1  # if loop completes without return search failed
```

# Binary Search Leetcode
## Capacity to Ship Capacity within D Days

### Main Idea
Intuition
- We know the value we need to return (ship capacity) we prob need to binary search
    - We also need to count for the fact that we're finding a capacity that will ship all weights in `days` days OR LESS
    - Or less is a little weird but the problem remains finding a capacity
- What's the smallest and largest possible value? 
    - Smallest is the max weight (or else we can't ship at all)
    - Largest is the sum of all weights (ship everything on day 1)
- So we have a range of possible ship capacities --> can binary search
- Why binary search specifically: There's feedback from having a ship capacity too high and too low
    - If capacity is too small --> days too long --> search right search space
    - If capacity is too large --> days are valid but we want min ship capacity that stil yields valid days --> search left search space
        
Main Idea
- Set an initial midpoint as (max_capacity - min_capacity) // 2 + min_capacity
- Calculate the number of partitions 
    - We calculate partitions by just iterating thru the weights array and counting whenver we're over capacity
    - Iterating thru gives us the min number of days needed to ship all weights given capacity
    - We just need the min days given capacity to be <= the inputted `days`, not exactly equal
- If num partitions is over the target (`days`) then we continue the search 
- If num partitions is under the targer (`days`) see if we can try for a better ship capacity that's still valid
- Binary search allows to to garuantee that once we're under we won't go over again

### Implementation
```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Given weights what should the ship cap be such that we can partition the weights array into `days` partitions. 

        Intuition
        - We know the value we need to return (ship capacity) we prob need to binary search
            - We also need to count for the fact that we're finding a capacity that will ship all weights in `days` days OR LESS
            - Or less is a little weird but the problem remains finding a capacity
        - What's the smallest and largest possible value? 
            - Smallest is the max weight (or else we can't ship at all)
            - Largest is the sum of all weights (ship everything on day 1)
        - So we have a range of possible ship capacities --> can binary search
        - Why binary search specifically: There's feedback from having a ship capacity too high and too low
            - If capacity is too small --> days too long --> search right search space
            - If capacity is too large --> days are valid but we want min ship capacity that stil yields valid days --> search left search space
        
        Main Idea
        - Set an initial midpoint as (max_capacity - min_capacity) // 2 + min_capacity
        - Calculate the number of partitions 
            - We calculate partitions by just iterating thru the weights array and counting whenver we're over capacity
            - Iterating thru gives us the min number of days needed to ship all weights given capacity
            - We just need the min days given capacity to be <= the inputted `days`, not exactly equal
        - Then if num partitions is over the target (`days`) then we continue the search
        """

        def check(capacity):
            num_days = 1
            curr_capacity = weights[0]
            for i in range(1, len(weights)):
                if curr_capacity + weights[i] > capacity:
                    num_days += 1
                    curr_capacity = weights[i]
                else:
                    curr_capacity += weights[i]
            return num_days

        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (r - l) // 2 + l # start with midpoint capacity

            # taking too long, need a larger capacity 
            if check(mid) > days:
                l = mid + 1
            else:
                r = mid
        return l
```