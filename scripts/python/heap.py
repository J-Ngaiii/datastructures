class Heap:
    def __init__(self, is_max_heap = False):
        self.heap = []
        self.is_max_heap = is_max_heap
    
    def insert(self, val):
        self.heap.append(val)

        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, idx):
        parent_idx = (idx - 1 ) // 2 # parent index is a func of child, don't need to pass as arg

        if idx <= 0:
            return
        
        if self._should_swap(idx, parent_idx):
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[idx]
            self.heap[idx] = temp

            self._bubble_up(parent_idx) # inserted node has moved up to parenst index so we bubble up from tgere

    def _should_swap(self, curr_idx, parent_idx):
        curr_val = self.heap[curr_idx]
        parent_val = self.heap[parent_idx]

        if self.is_max_heap:
            return curr_val > parent_val
        return curr_val < parent_val
    
    def remove_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self._heapify_down(0)
        
        return root_value
    
    def _bubble_down(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        target = idx

        # compare parent vs left --> reassign
        if left_child < len(self.heap) and self._compare(left_child, target):
            target = left_child

        # if we reassigned then compare(right_child, target) --> compares left vs right to find min child
        if right_child < len(self.heap) and self._compare(right_child, target):
            target = right_child

        # if we couldn't reassign target => not valid child swaps exist => elem is where its supposed to be
        if target != idx: 
            self.heap[idx], self.heap[target] = self.heap[target], self.heap[idx]
            self._heapify_down(target)

    def _compare(self, idx1, idx2):
        """Helper to compare two indices based on heap type."""
        if self.is_max_heap:
            return self.heap[idx1] > self.heap[idx2]
        return self.heap[idx1] < self.heap[idx2]