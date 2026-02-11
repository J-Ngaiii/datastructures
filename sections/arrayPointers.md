---
layout: default
title: "Arrays and Pointers"
date: 2026-02-10
categories: DSA
---

# Arrays and Pointers Conceptual

# Arrays and Pointers Toolkit and Tips

# Arrays and Pointers Leetcode Classics

## [Remove Duplicates From Sorted Array](https://neetcode.io/problems/remove-duplicates-from-sorted-array/question)

### Main Idea
Intuition
- Ordered list => you should be doing something with skipping numbers, comaping valuees, etc rather than hashing
- Why it's a classic: 
    - Sorted Array Properties: rather than explicitly tracking duplicates --> we take advantage of the sorted nature 
    - Processed Pointer: we use a pointer to keep track of elems that have already been processed which doubles as the slot for mutative insertions

### Implementation
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Non-decreasing order means we can utilize a pointer and greater-than comparison to detect duplicates.
        Don't need to use a hashset.
        """
        p = 0 # p marks last processed elem
        for i in range(1, len(nums)): # i marks elem to process next
            if nums[i] != nums[p]:
                p += 1 # we need to shift p up to the empty spot before replacing
                nums[p] = nums[i]
                
        return p + 1 # return length not index
```

## [Two Integer Sum II](https://neetcode.io/problems/two-integer-sum-ii/question)

### Main Idea
Intuition
- Array is sorted
- We're trying to match a target using sum of elems
- Thus => we use l, r pointer and iterate (3 sum method)

- Why its classic: we're using a l, r pointer on a sorted array and monitoring if the aggregation is greater than or less then some target to adjust l or r accordingly

### Implementation
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Cues
        - Array is sorted
        - We're trying to match a target using sum of elems

        Thus => we use l, r pointer and iterate (3 sum method)
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l + 1, r + 1]
```

## [Three Sum](https://neetcode.io/problems/three-integer-sum/question)

### Main Idea
Intuition
- You just need to find indices that match to equal 0 => you can sort and use l, r pointers
- First sort the array then manage how to shift and manage 3 pointers

- You have 3 values so => you want an i pointer to explore all numbers then for a given locked in i pointer
- Then you construct an l and r pointer that have the classic l, r tightening window search stratedgy
- This works cuz you try all candidates for i then all feasible candidates given i for l and r
- For duplicate handling => once you try a value for i, l or r => you cannot retry that value for that poointer. Because you've sorted the array => you can detect if a pointer is on a duplicate by just checking if the elem right before the elem the pointer is currently pointing to is the same

Main Explanation
- Main Idea: Use 3 pointersL i, l and r pointers scan through all relevant combinations for a starting i.
    - i pointer tries all starts
    - l and r pointer tries all relevant starts given i

- One pointer (i) sets the starting number of a running sequence
- Two other pointers (l and r) set at the beginning and end of the remaining numbers in the candidate array
- (i) is fixed at index at first, (l) and (r) at opposite ends

- First sort the array  Cuz:
    - If the sum is > 0 => we want a smaller sum next time => move r pointer left to choose a smaller number
    - If the sum is < 0 => we want a larger sum next time => move l pointer right to choose a larger number
- l Pointer Logic: Move right if sum is < 0
    - Duplicate skipping for l: if curr elem same as last elem → we’ve alr tried having this value as the second integer => skip until we get a diff number or l overlaps with r and we’ve processed all combos
- r Pointer Logic: Move left if the sum is < 0
    - Duplicate skipping for r: if curr elem same as last elem → we’ve alr tried having this value as the third integer => skip until we get a diff number or r overlaps with l and we’ve processed all combos
- i Pointer Logic: if l and r are at the same index, shift i over to the right by one then reset r to be at the end and l to be right of i 
    - Duplicate skipping for i: if curr elem same as last elem → we’ve alr tried searching for a valid sequence where the first integer is this value => skip to next, each unique value of nums[i] only gets to serve as ‘anchor’ once 

- Why are duplicates handled the way they are?
    - Think of i, l and r moving through the array as searching through the array
    - Duplicate sequences only come about if our pointers hit a duplicate character then try to search despite being on a duplicate  => whenever our pointers hit a duplicate character they need to not process it again
    - Eg. if we’ve already searched through the array for combinations while having 1 as the first ‘anchor’ integer then we hit another instance of 1 and we search again → might get duplicate
    - If point i/l/r has already tried value X then they should move on
    - l/r can try value X again given that pointer i has moved onto a different iteration
    - After sorting duplicates numbers are adjacent => to skip past duplicates move forward until we hit a diff num
    - Don’t have to worry about -1, 1, -1 duplicate sequences cuz we sorted the array

### Implementation
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort so we can use classic l, r pointer

        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # i pointer duplicate check
                # check if we've alr tried some value as the first num
                continue 
            
            # once we lock an i pointer, we define a window to its right
            # then we search that window with the l and r pointers
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # core logic comparing 
                curr_sum = nums[i] + nums[l] + nums[r]
                
                if curr_sum < 0:
                    l += 1  
                elif curr_sum > 0:
                    r -= 1
                else:
                    # we have a match but once we iterate we need to check duplicates
                    ans.append([nums[i], nums[l], nums[r]])
                    # l pointer duplicate check
                    # check if we've alr tried this num in the second slot
                    l += 1 
                    while nums[l] == nums[l - 1] and l < r:
                        # nums[l] == nums[l - 1] checks duplicate
                        # l < r checks that we're still in a valid l, r window (l & r haven't overlapped)
                        l += 1

                    if r < len(nums) - 1: # if r == len(nums) - 1 => on last elem, no possible duplicate
                        # r always starts at the end no matter where i is
                        # r pointer duplicate check
                        # check if we've alr tried this number in the third slot
                        if nums[r] == nums[r + 1] and l < r:
                            # nums[r] == nums[r + 1] checks duplicate
                            # l < r checks that we're still in a valid l, r window (l & r haven't overlapped)
                            r -= 1
        return ans
```
