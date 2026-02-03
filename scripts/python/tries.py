trie = {}
for word in dictionary:
    node = trie
    for char in word:
        # If char isn't in node, add it as a new dictionary
        node = node.setdefault(char, {})
    # Mark the end of a word with a special key
    node['#'] = True