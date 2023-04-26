"""Trie data structure for storing melodies in ABC notation."""

import sys

class TrieNode:
    """Single node, building block of trie structure.
    Attributes:
    - self. note: note in ABC notation
    - self.is_end: whether melody ends here
    - self.counter: how many times this particular melody has been inserted
      (if this node has is_end set to True)
    - self.children: child nodes, dict contains notes as keys, and nodes as values"""
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
        """
        self.root = TrieNode("")
        sys.setrecursionlimit(10**7)

    def insert(self, melody: str):
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
    
    def get_following_notes_with_frequencies(self, predecessors_amount: int):
        """
        Depth first search through the trie to find notes that come after a sequence of notes
        of wanted length (predecessors_amount).
        Args:
            predecessors_amount (int): How many notes' sequence to consider in getting followers.
        Returns:
            following_notes (dict): A nested dictionary. Keys are note sequences of wanted length (predecessors_amount)
            and values are dictionaries that contain following note as key and its frequency in Trie as value.
            Example: If only one melody is inserted ('adcf'), then get_following_notes_with_frequencies(3) returns
            {'adc': {'f': 1}} 
        """
        following_notes = {}

        def _dfs(node: TrieNode, melody_start: str):
            if node.is_end:
                notes = melody_start.split()
                if len(notes) >= predecessors_amount:
                    for i in range(len(notes) - predecessors_amount + 1):
                        next = "".join(notes[i:i + predecessors_amount])
                        if i + predecessors_amount < len(notes): 
                            follower = notes[i + predecessors_amount]   
                            if next not in following_notes:
                                following_notes[next] = {}
                            if follower not in following_notes[next]:
                                following_notes[next][follower] = 0
                            following_notes[next][follower] += 1
            for child_note, child_node in node.children.items():
                _dfs(child_node, melody_start + ' ' + child_note)

        _dfs(self.root, '')
        return following_notes
    