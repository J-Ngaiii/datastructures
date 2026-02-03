# ---------------------------
# Lightweight Dict Trie Implementation
# ---------------------------

trie = {}

def add_word(word):
    node = trie
    for char in word:
        # Get the next dict, or create it if missing
        node = node.setdefault(char, {})
    # Mark the end of the word
    node['#'] = True

def check_word(word):
    node = trie
    for char in word:
        if char not in node:
            return False  # Path doesn't exist
        node = node[char] # Move to the next level
    
    # Check if a word actually ends here
    return '#' in node

# ---------------------------
# Full Trie Implementation
# ---------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:


    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                # handles adding words w/ new chars to be directly under root
                # handles slotting words w/ seen prefixes
            curr = curr.children[char]
            # if we have seen this character --> go down the tree by calling the node for that char
            # until eventually we hit a char we haven't seen (in children only) --> then even after adding new node we need to move down into it
        curr.is_end = True
        # once we run out of chars the node that `curr` points to is the end
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
                # no match cuz we run off the tree
            curr = curr.children[char]
        return curr.is_end # curr updated to last char node --> check `is_end`


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
                # no match cuz we run off the tree
            curr = curr.children[char]
        return True # if we didn't run off tree that means its in the Trie