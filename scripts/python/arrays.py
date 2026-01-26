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
        dp[i] = dp[i] + dp[i - 1]
    
    return dp

def max_prefix_sum(nums: List[int]) -> int :
    """
    Here we implicitly do a prefix sum but recursively adding on the previous value
    Except we don't track the prefix sum of the arr up to every single prefix in a dp array
    We don't need to track every single prefix sum cuz we just need the max
    """
    if not nums:
        return []
    
    best_sum = 0
    curr_sum = 0
    for val in nums:
        curr_sum += val
        if curr_sum > best_sum:
            best_sum = curr_sum
    return best_sum

def max_subarray_prefix_sum(nums, k):
    """
    """
    # Dictionary to store number of times a prefix sum has occurred
    # key: prefix_sum, value: count
    # Initialize with {0: 1} to handle subarrays starting from index 0
    prefix_counts = {0: 1}
    
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        
        # Check if (current_sum - k) exists in our map
        diff = current_sum - k
        if diff in prefix_counts:
            # Add the NUMBER OF TIMES that difference has appeared
            count += prefix_counts[diff]
        
        # Update the map with the current sum
        if current_sum in prefix_counts:
            prefix_counts[current_sum] += 1
        else:
            prefix_counts[current_sum] = 1
            
    return count

def carPooling(trips, capacity):
    """
    :type trips: List[List[int]]
    :type capacity: int
    :rtype: bool
    - I need to keep track of capacity
    - across locations at distinct indicies
    - so it's difference array! mark the start and stops --> do the prefix sum and return false if you ever exceed capacity 

    - the only difficulty is that I don't have all the indices for the trip (so I don't know how long to make the diff array) --> ig i can do an arbitrarily large diff_array?
    """
    diff_array = [0] * 1001 # problem says from_i < to_i <= 1000 
    # so we set for size 1001 (constant size == ok to do this)
    max_end = 0
    for p, start, end in trips:
        # zero-indexing since 0 <= from_i
        # should be ending exclusive because we're dropping them off at index `end`` so we carry them up to and including only index `end - 1`
        diff_array[start] += p
        diff_array[end] -= p
        if end > max_end:
            max_end = end
            # keep track of end anyway to avoid running over if we don't need to 
    
    curr_sum = 0
    for i in range(max_end + 1):
        # max_end + 1 to make sure we include the doff_array[max_end] in the sum
        curr_sum += diff_array[i]
        if curr_sum > capacity:
            return False

    return True

def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        Time Complexity: O(N log N) (dominated by sort)
        Space Complexity: O(1) (excluding return space)

        - variation of carpooling but with arbitrarily large interval ends
        - do inplace with same approach as unique elems in non-increasing arr problem
        """
        if not intervals:
            return []

        intervals.sort() 
        
        write_index = 0 # tracks beginning of window of processed elems
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            prev_end = intervals[write_index][1] 
            
            if curr_start > prev_end:
                # No Overlap:
                # Move our write pointer forward and copy the current interval there
                write_index += 1
                intervals[write_index] = intervals[i]
            else:
                # Overlap:
                # Merge into the existing spot at write_index
                # We don't need to change the start time (it's already sorted min)
                # We just maximize the end time
                intervals[write_index][1] = max(curr_end, prev_end)
                
        # Return only the portion of the list we used
        return intervals[:write_index + 1]

        
    
            




        
    