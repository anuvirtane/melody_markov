"""Trie data structure for storing melodies in ABC notation.
Instead of notes, chords can be used."""

class TrieNode:
    """Single node, building block of trie structure.
    Attributes:
    - note in ABC notation
    - whether melody ends here
    - how many times this particular melody has been inserted
      (if this node has is_end set to True)
    - child nodes, dict contains notes as keys, and nodes as values"""
    def __init__(self, note: str):
        self.note = note
        self.is_end = False
        self.counter = 0
        self.children = {}

class Trie:
    """Trie data structure for melodies"""
    def __init__(self):
        """ The root has an empty string as note.
        That way when querying with "" as input it finds "everything".
        Trie has output list, that is used to return query results.
        """
        self.root = TrieNode("")
        self.output = []

    def insert(self, melody: list):
        """Insert a melody into Trie.
        Start from the root node.
        Go through nodes and if note is not found in Trie nodes,
        create a new node for it and continue from there.
        If note is found in Trie nodes, continue from there.
        When melody finished, set node's is_end to True.
        Then set melody count up with one in the ending node.
        """
        node = self.root
        for note in melody:
            if note in node.children:
                node = node.children[note]
            else:
                new_node = TrieNode(note)
                node.children[note] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1

    def dfs(self, node: TrieNode, melody_start: str):
        """Depth first search through the trie.
        node: starting node.
        melody_start: start of melody to look for
        """
        if node.is_end:
            self.output.append((melody_start + node.note, node.counter))
        for child in node.children.values():
            self.dfs(child, melody_start + node.note)

    def query(self, melody_start: str) -> list:
        """Use input string (one or multiple notes that melody starts with)
        to retrieve all melodies stored in
        the trie with that starting sequence sorted by the number of
        times they have been inserted. Return them in list.
        """
        self.output.clear()
        node = self.root
        for note in melody_start:
            if note in node.children:
                node = node.children[note]
            else:
                return []
        self.dfs(node, melody_start[:-1])
        return sorted(self.output, key=lambda x: x[1], reverse=True)
    