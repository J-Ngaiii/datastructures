
## [Remove Duplicates From Sorted Array
](https://neetcode.io/problems/remove-duplicates-from-sorted-array/question)

### Main Idea
- Ordered list => you should be doing spmething with skipping numbers, comaping valuees, etc rather than hashing
- 

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