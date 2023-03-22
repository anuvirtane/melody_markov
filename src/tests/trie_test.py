import unittest
from logic import trie_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = trie_logic.Trie()

    def test_trie_root_has_empty_note(self):
        self.assertEqual(self.t.root.note, "")

    def test_trie_finds_inserted_sequence_with_right_start(self):
        self.t.insert("ABC")
        result = self.t.query("A")
        self.assertEqual(result, [('ABC', 1)])
    
    def test_trie_does_not_find_inserted_sequence_with_wrong_start(self):
        self.t.insert("ABC")
        result = self.t.query("B")
        self.assertEqual(result, [])
