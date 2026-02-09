---
layout: default
title: "Binary Tree Basics"
date: 2026-02-08
categories: DSA Conceptual
---

## Binary Tree Basics

---

### Implementations

Python
```python
from collections.abc import Iterable
from collections import deque

class Tree:
    def __init__(self, val=None, children=None):
        if val is not None and isinstance(val, Iterable):
            raise TypeError("Node value cannot be an iterable.")
        else:
            self.val = val
        
        if children is not None:
            assert isinstance(children, Iterable), "Children value must be an itertable"
            assert all(isinstance(elem, Tree) for elem in children), "All children must be tree objects"
            if len(children) == 0:
                print('Alert, inputted children is an empty iterable')
            self.children = list(children)
        else:
            self.children = []

    def get_val(self):
        return self.val
    
    def set_val(self, val):
        assert not isinstance(val, Iterable), "Node value cannot be an iterable."
        self.val = val

    def get_children(self):
        return self.children
    
    def set_children(self, children):
        assert isinstance(children, Iterable), "Children value must be an itertable"
        assert all(isinstance(elem, Tree) for elem in children), "All children must be tree objects"
        if len(children) == 0:
            print('Alert, inputted children is an empty iterable')
        self.children = list(children)

    def is_leaf(self, node):
        """Check if a Tree node has no children."""
        return not node.get_children()

class BinaryTree (Tree):

    def __init__(self, val=None, left=None, right=None):
        super().__init__(val)
        assert (left is None or isinstance(left, BinaryTree)), "Left child must be a BinaryTree or None"
        assert (right is None or isinstance(right, BinaryTree)), "Right child must be a BinaryTree or None"
        self.left = left
        self.right = right
        self.children = [self.left, self.right]

    def set_children(self, children):
        assert isinstance(children, Iterable), "Children value must be an iterable"
        assert all(isinstance(elem, BinaryTree) for elem in children), "All children must be binary tree objects"
        assert len(children) <= 2, "Binary tree nodes must have at most two children"

        if len(children) == 0:
            self.left = None
            self.right = None
        elif len(children) == 1:
            self.left = children[0]
            self.right = None
        else:
            self.left, self.right = children[:2]

        self.children = [self.left, self.right]

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_left(self, left):
        assert isinstance(left, BinaryTree), "Can only set binary tree objects as left child"
        self.left = left
    
    def set_right(self, right):
        assert isinstance(right, BinaryTree), "Can only set binary tree objects as right child"
        self.right = right

    def _depth_helper(self, node):
        """
        Docstring for _depth_helper
        
        If we encounter a leaf passing none as node.left and node.right will make the max statement = 0
        then we just do + 1 to count the leaf

        Otherwise it will update the depth to whichever child was deeper and +1 to count current node

        Rather than using an counter in the argument that can be referenced in recursive calls (topdown)
        we return the counter in the output which can also be referenced in recursive calls (bottomup)
        """
        if node is None:
            return 0
        
        return max(self._depth_helper(node.left), self._depth_helper(node.right)) + 1

    def depth(self):
        return self._depth_helper(self)
```

Java
```Java
import java.util.List;

public class Tree {
    protected int val;
    private List<Tree> children;

    public Tree(int val, List<Tree> children) {
        this.val = val;
        this.children = children;
    }

    public Tree(int val) {
        this.val = val;
        this.children = null;
    }

    public Tree(List<Tree> children) {
        this.val = Integer.MIN_VALUE;
        this.children = children;
    }

    public Tree() {
        this.val = Integer.MIN_VALUE;
        this.children = null;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }

    public List<Tree> getChildren() {
        return children;
    }

    public void setChildren(List<Tree> children) {
        this.children = children;
    }
}

public class BinaryTree extends Tree{
    private BinaryTree left;
    private BinaryTree right;

    public BinaryTree(int val, BinaryTree left, BinaryTree right) {
        super(val);
        this.left = left;
        this.right = right;
    }
    
     public BinaryTree getLeft() {
        return left;
    }

    public BinaryTree getRight() {
        return right;
    }
}
```