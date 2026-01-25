def generative_combinations(nums, k):
    """
    Docstring for combinations
    
    :param nums: Candidate array
    :param k: How many times we choose from the candidate array
    """
    results = []
    
    def backtrack(start_index, current_comb):
        # Base Case: If the combo is size k, we found one
        if len(current_comb) == k:
            results.append(current_comb[:]) # [:] creates a copy
            return
        
        # Loop through valid candidates
        # We start from 'start_index' to ensure we only move forward
        for i in range(start_index, len(nums)):
            current_comb.append(nums[i])      # 1. Choose
            backtrack(i + 1, current_comb)    # 2. Explore (i+1 ensures no repeats)
            current_comb.pop()                # 3. Un-choose (Backtrack)

    backtrack(0, [])
    return results

def counting_combinations(n, k):
    """
    Docstring for counting_combinations

    This is just n choose k
    
    :param n: Number of elems
    :param k: How many elems we can choose out
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k  # Optimization: C(n, k) == C(n, n-k)
        
    res = 1
    for i in range(k):
        # res = res * (n - i) / (i + 1)
        res = res * (n - i)
        res = res // (i + 1) 
    return res

def generative_permutations(nums, k):
    results = []
    
    def backtrack(current_perm, used_indices):
        if len(current_perm) == k:
            results.append(current_perm[:])
            return

        for i in range(len(nums)):
            if i not in used_indices:          # Check if available
                
                # 1. Choose
                current_perm.append(nums[i])
                used_indices.add(i)
                
                # 2. Explore
                backtrack(current_perm, used_indices)
                
                # 3. Un-choose
                used_indices.remove(i)
                current_perm.pop()

    backtrack([], set())
    return results