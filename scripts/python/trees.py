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

class TreeTraversals():
    def __init__(self):
        pass

class MutativeTraversals (TreeTraversals):
    def __init__(self, func=None):
        super().__init__()
        self.func = func

    def get_func(self):
        return self.func
    
    def apply_func(self, node):
        """Apply function to a single node's value."""
        node.set_val(self.func(node.get_val()))
    
    def base_case(self, root):
        assert isinstance(root, Tree), "TreeTraversal object cannot run BFS on non-tree objects"

        func = self.get_func()
        if root.get_children() == []:
            root.set_val(func(root.get_val()))
            return True
        else: 
            return False
    
    def bfs(self, root, iterative=False):
        assert isinstance(root, Tree), "bfs requires a Tree node"
        if self.is_leaf(root):
            self.apply_func(root)
            return

        self.apply_func(root)
        children = root.get_children()
        if iterative:
            queue = deque(children)
            while queue:
                node = queue.popleft()
                self.apply_func(node)
                queue.extend(node.get_children())
        else:
            for c in children:
                self.bfs(c, iterative=False)


    def inorder(self, root, iterative=False):
        assert isinstance(root, BinaryTree), "inorder traversal only works on binary tree objects."
        if self.is_leaf(root):
            self.apply_func(root)
            return
        
        children = root.get_children()
        if iterative:
            stack = []
            curr = root
            while stack or curr:
                while curr: # while loop runs populates stack we have no left child
                    stack.append(curr)
                    curr = curr.get_left()
                # process current node
                curr = stack.pop()
                self.apply_func(curr)
                curr = curr.get_right() # repopulate curr so the while loop triggers again searching for left child
        else:
            left = root.get_left()
            right = root.get_right()
            if left:
                self.inorder(left, iterative=False)
            self.apply_func(root)
            if right:
                self.inorder(right, iterative=False)
                

