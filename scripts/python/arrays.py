from typing import List, Tuple

def remove(arr, x) -> Tuple[List, int]:
    """
    Returns the original array but with all occurences of x removed and the size of the updated array.

    Core pieces of logic are: 
    - The boundary pointer designates the boundary (next open slot) of the processed array and updates in sync with the forloop
        - The boundary pointer becomes detached only if it encounters an instance of the x elem to be removed
        - In which case it lets the forloop pointer move forward and stays on the index where arr[index] == x
        - Such that the next time the forloop pointer hits an elem that isn't an instance of x it overwrites the element to be removed
    - Then we can also return the boundary itself as a count of the number of valid numbers in the final array
    """
    boundary = 0
    for i in range(len(arr)):
        elem = arr[i]
        if elem != x:
            arr[boundary] = arr[i]
            boundary += 1
    return arr[:boundary], boundary

def kadane(arr) -> int:
    """
    Returns max possible sum of a continuous sequence of values within an array.

    Core logic is for any elem i:
    - If arr[i] + running_sum < arr[i] => running_sum is negative and dragging us down, discard it
    - If arr[i] + running_sum > arr[i] => running_sum is positive and contributing well, keep it
    """
    curr_sum = 0
    best_sum = float('-inf')
    for i in range(len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i]) # choose between starting at arr[i] or extending curr sum with arr[i] based on which is greater
        best_sum = max(curr_sum, best_sum) # update best_sum if the current window's sum is better
    return best_sum

def size_kadane(arr, k) -> int:
    """
    Returns max possible sum of a continuous sequence of length k within an array.

    Much simpler because we don't need to handle for variable window size.
    Just like a convolution operation we slide a window of fixed size across the whole array

    Core Logic
    - curr_sum += arr[i] adds the elem then - arr[i-k] removes the first elem => effectively shifting the window over by one
    """
    if len(arr) < k:
        return sum(arr)  

    curr_sum = sum(arr[:k])
    best_sum = curr_sum

    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i - k] 
        best_sum = max(best_sum, curr_sum)

    return best_sum



def longest_unique_substring(s) -> int:
    """
    Returns the length of the longest substring of unique characters within the inputted string.

    
    Core Logic
    - If the right pointer character is NOT in the existing set --> add to the set, check the size and push the right pointer forward
    - If the right pointer character IS in the existing set --> we keep moving the left pointer until we the right pointer character is no longer in the set 
        - Why incorporate the new character the right pointer is on? We have to be able to keep moving forward

    Lesson
    - Whenever you have to maintain a sequence/window of unique elements/know what each elem is => generally need a set
    - If you just need a sequence/window that satisfies some quality (eg. sums to some amount)/don't care about what elems are in the window, just the condition => generally can get away with just pointers
    """
    if s is None:
        return 0
    elif len(s) == 1:
        return 1
    elif len(s) == 2:
        if s[0] != s[1]:
            return 2
        else: 
            return 1

    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Shrink the window from the left if we hit a duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Expand the window to include s[right]
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

def remove_duplicates_sorted(nums: List[int]) -> int:
        """
        Removes all duplicates in a sorted non-decreasing list.
        
        Core Logic: 
        - i pointer acts as boundary to valid section of the array to the left thats been filtered for duplicates
        - j pointer checks numbers against the i boundary pointer
        - if not duplciate then move both pointers up
        - if duplicate --> we wanna keep moving the j pointer forward until we no longer hit a duplicate
            - then the i pointer will update accordingly everytime the j pointer hits a non-diplicate element
            - automatically leaving a gap between the i and j pointers that excludes duplicates
            - automatically overwriting duplicate elements with non-duplicate elements
        """
        assert sorted(nums) == nums, 'input must be non-decreasing list'
        
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i

def remove_duplicates_unsorted(nums: List[int]) -> int:
    """
    Returns a copy of the inputted list with all duplicates removed.
    
    Core Logic: 
    - i pointer acts as boundary to valid section of the array to the left thats been filtered for duplicates
    - j pointer checks numbers against the i boundary pointer
    - if not duplciate then move both pointers up
    - if duplicate --> we wanna keep moving the j pointer forward until we no longer hit a duplicate
        - then the i pointer will update accordingly everytime the j pointer hits a non-diplicate element
        - automatically leaving a gap between the i and j pointers that excludes duplicates
        - automatically overwriting duplicate elements with non-duplicate elements
    """
    processed = set(nums[0])
    for i in range(1, len(nums)):
        if nums[i] not in processed:
            set.add(nums[i])
    return list(processed)

def basic_prefix_sum(nums: List[int], inplace: bool = False):
    if not nums:
        return []
    
    if inplace:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return
    
    dp = len(nums)*[0]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = nums[i] + dp[i - 1]
    
    return dp
            




        
    