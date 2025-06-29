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
                # process the current node
                node = queue.popleft()
                self.apply_func(node)
                # add the current node's children to be processed
                queue.extend(node.get_children())
        else:
            for c in children:
                self.bfs(c, iterative=False)


    def inorder(self, root, iterative=False):
        """
        Inorder traversal order is:
            - traverse left
            - process curr node
            - traversr right

        Cannot simply check if a node has no left child then process and move to next in the stack because --> you can't check for nodes you've already processed
        Fix:
        - use a while loop for a left/curr variable to keep traversing in one direction (eg keep going left) until theres no child in that direction
        - reset the left/curr variable when you process the node

        eg. 
        - for tree: 
                    10
                8       12
            3       9
        - initially stack is empty so you rely on curr = root to trigger the while loop
        - while loop kills after appending 3 to the stack and curr is set equal to None
        - 3 gets processed then --> reset curr to equal None (which is okay because the stack is still not empty)
        """
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

    def preoreder(self, root, iterative=False):
        assert isinstance(root, BinaryTree), "inorder traversal only works on binary tree objects."
        if self.is_leaf(root):
            self.apply_func(root)
            return
        
        children = root.get_children()
        if iterative:
            stack = []
            stack.append(root)
            while stack:
                curr = stack.pop()
                self.apply_func(curr)
                right = curr.get_right()
                if right: stack.append(right)
                left = curr.get_left()
                if left: stack.append(left)
                
        else:
            self.apply_func(root)
            left = root.get_left()
            right = root.get_right()
            if left:
                self.preoreder(left, iterative=False)
            if right:
                self.preoreder(right, iterative=False)

    def postorder(self, root, iterative=False):
        """
        Postorder iterative needs two stacks because the order of visiting is too different from the order of processing

        eg. 
        - for tree: 
                    10
                8       12
            3       9
        - after processing 3 you need to be able to go up to 8 --> then go to 9 without revisiting 3 or processing 8 itself
        - so you need one datastructure to keep track of nodes you've visited to avoid revisiting and another to keep track of the actual order in which you want to process
        """
        assert isinstance(root, BinaryTree), "inorder traversal only works on binary tree objects."
        if self.is_leaf(root):
            self.apply_func(root)
            return
        
        children = root.get_children()
        if iterative:
            stack = [root] # stack keeps track of the nodes we've visited/children we need to visit as we traverse down the tree
            output = [] # output keeps nodes we've visited in the correct order so that they get processed in the right order
            while stack: # while loop is updates the stack --> to keep track of visited nodes AND orders the nodes correctly by adding them to output at the right time
                node = stack.pop()
                output.append(node)
                if node.get_left():
                    stack.append(node.get_left())
                if node.get_right():
                    stack.append(node.get_right())
            while output: # stack is exhausted => all nodes visited, output is popped in order to carry out postorder processing
                self.apply_func(output.pop())
                
        else:
            left = root.get_left()
            right = root.get_right()
            if left:
                self.postorder(left, iterative=False)
            if right:
                self.postorder(right, iterative=False)
            self.apply_func(root)
                

