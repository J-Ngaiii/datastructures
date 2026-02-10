---
layout: default
title: Heaps and Priority Queues
date: 2026-02-10
categories: DSA
---

# Heaps & Priority Queues Conceptual

## Heap Definition
A tree like data structure that defined by 2 invariants:
- Completeness: all layers must be completely filled (as according to the branching factor) except for the last layer which itself must be filled from left to right
- Heap Property
    - Min version: each element must be smaller than all elements of its children => root is smallest
    - Max version: each element must be larger than all elements of its children => root is largest

## Heap Methods
- Find min: Just return the root
- Insert:
    - Insert Steps (Bubbling Up):
        - We add at the bottom row, left to right
        - Bubbling up (swap until heap property maintained)
        - Then swap with parent if added value is < parent value
        - Keep swapping until added value > parent value or added value is the new root
    - Runtime: 
        - Best case O(1) 
            - You insert at the bottom and don’t have to bubble up
        - Worst case O(log N) 
            - Based on layers of the tree and number of swaps (long tree with lots of swaps)
            - Assuming completeness => non-spindly tree/branching factor > 1
- RemoveMin:
    - Remove Steps (Bubbling Down):
        - Swap element to be removed (in this case root, but doesn’t necessarily have to be the root) with the bottom rightmost value
        - Remove the new bottom rightmost value (in this case previous root slated to removed) from the tree
        - Bubble down (swap until heap property maintained)
        - Then swap the original bottom rightmost value that’s somewhere in the tree up if its value < parent value or otherwise disobeys the min/max heap property 
        - If two elements are BOTH lesser than the swapped element that we need to bubble down → bubble down to the smaller of the two elements
        - Otherwise if you bubble down with the larger of two smaller elements, then you violate heap property
            - 6 Left: 3 and Right:2 → 3 Left: 6 Right: 2 (Violation) if you choose the to bubble down to the larger of the two smaller elems
        - In max case bubble down to the larger of the two elements
    - Runtime: 
        - Best case O(1)
            - If everything on the one branch is larger than everything on another branch and you swap an element from the smaller branch then bubble down into the larger branch 
            - Or as long as there’s a layer of nodes that is larger than the bottom rightmost node being swapped then bubbled down into the other branch, that way the swapped node gets stopped early before hitting the bottomost leaf layer of the heap
            - Cuz any element you draw from the smaller branch to replace the root with will be smaller than any element in the larger branch => you don’t have to do much swapping
        -  Worst case O(log N) based on layers of the tree and number of swaps (long tree with lots of swaps)
        - Assuming non-spindly tree/branching factor > 1

# Heaps Toolkit and Tips

## Basic Implementations
```python
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
  
   def in_heap(self, val):
       return self._check_membership(0, val)


   def _check_membership(self, idx, val):
       if idx >= len(self.heap):
           return False
      
       # don't need to check children directly just check the curr node
       curr = self.heap[idx]
       if curr == val:
           return True


       # Pruning logic:
       # In a Max-Heap, if curr < val, val cannot be below this point.
       if self.is_max_heap and curr < val:
           return False
       # In a Min-Heap, if curr > val, val cannot be below this point.
       if not self.is_max_heap and curr > val:
           return False


       # Then search both branches
       return (self._check_membership(2 * idx + 1, val) or
               self._check_membership(2 * idx + 2, val))    
      
   def remove_val(self, val):
       idx = None # locate the idx
       for i in range(len(self.heap)):
           if self.heap[i] == val:
               idx = i
               break
      
       if idx is None:
           print(f"Inputted value `{val}` is not in the heap")
           return


       # pop out the last elem to swap
       last_val = self.heap.pop()
      
       # we either happened to remove the last elem or we need to rebalance
       if idx < len(self.heap):
           self.heap[idx] = last_val # this is where we delete the actual val via reassignment
          
           # swapped elem can go up or down
           # we run both but only one will actually move the element
           self._heapify_up(idx)
           self._heapify_down(idx)
```

## Python heapq (min heap)
heapq.heapify(x)
Transform list x into a min-heap
In-place and in linear time.

heapq.heappush(heap: List, item)
Push the value item onto the heap
Properties
Maintains the min-heap invariant.

heapq.heappop(heap: List)
Pop and return the root (smallest item from the heap)
Properties:
Mains the min-heap invariant. 
If the heap is empty, IndexError is raised. 
To access the smallest item without popping it, use heap[0].

heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap.
Will never return an item larger than the item added (we either pop what we just pushed or pop something smaller after bubbling down)
Properties
The combined action runs more efficiently than heappush() followed by a separate call to heappop().
heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. 
Returns a value that may be larger than the item added (if the heap min is larger than item)

Properties
The heap size doesn’t change. 
If the heap is empty, IndexError is raised.
This one step operation is more efficient than a heappop() followed by heappush() 

## Python heapq (max heap)
heapq.heapify_max(x)
Transform list x into a max-heap, in-place, in linear time.

heapq.heappush_max(heap, item)
Push the value item onto the max-heap heap, maintaining the max-heap invariant.

heapq.heappop_max(heap)
Pop and return the largest item from the max-heap heap

heapq.heappushpop_max(heap, item)
Push item on the max-heap heap, then pop and return the largest item from heap.
The value returned will never be smaller than the item added (we either pop what we just pushed if the new item is the largest or we pop a larger item from the root after bubbling down)

heapq.heapreplace_max(heap, item)
Pop and return the largest item from the max-heap heap and also push the new item. 
The value returned may be smaller than the item added (if the root/largest item in the max heap is smaller than the item being added)

# Heaps Leetcode