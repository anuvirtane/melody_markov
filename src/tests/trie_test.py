import unittest
from logic import trie_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = trie_logic.Trie()
        self.tn = trie_logic.TrieNode("A")

    def test_node_has_note(self):
        self.assertEqual(self.tn.note, "A")

    def test_trie_root_has_empty_note(self):
        self.assertEqual(self.t.root.note, "")

    def test_trie_does_not_find_sequence_when_empty(self):
        result = self.t.get_following_notes_with_frequencies(1)
        self.assertEqual(result, {})

    def test_trie_returns_inserted_sequence(self):
        self.t.insert("ABC")
        result = self.t.get_following_notes_with_frequencies(1)
        self.assertEqual(result, {'A': {'B': 1}, 'B': {'C': 1}})
    



    
