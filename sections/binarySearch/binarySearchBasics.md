---
layout: default
title: "Binary Search Basics"
date: 2026-02-08
categories: DSA Conceptual
---

## Binary Search Basics

---

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