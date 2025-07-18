def faulty_longest_unqiue_substring(string):
    """
    Core Pieces of Logic
    - Window is dynamic and defined by a left and right pointer
    - Keep shifting our right pointer forward if the elem the right pointer is on is NOT a duplicate of the elem our left pointer is on
        - What about checking elems in between? Every element in between left and right pointer has been processed and compared by right pointer before.
    - If right pointer hits a duplicate of the elem our left pointer is on --> shift the left pointer until it excludes the elem the right pointer is on
        - Problem with this is that it can detect duplicates of the elem that left pointer is on but not duplicates of a different character within the window
        - eg abbcdae --> left pointer is stuck on a so when right pointer hits both bs it will incorporate them both as it just checks if it equals a
    """
    if string is None:
        return 0
    elif len(string) == 1:
        return 1
    elif len(string) == 2:
        if string[0] != string[1]:
            return 2
        else: 
            return 1

    left = 0
    max_size = 0
    for right in range(1, len(string)):
        if string[left] != string[right]: # if we have shifted right without encountering duplicate --> track the size
            curr_size = right - left
            max_size = max(max_size, curr_size)
        else:
            # if we have encountered duplicate --> define new window to include new instance and exclude old instance of duplicate elem
            while string[left] == string[right] or left != right: # shift left pointer as much as we can
                left += 1
            curr_size = right - left
            max_size = max(max_size, curr_size)
            # if left and right pointers overlap then let the for loop update the right pointer 
