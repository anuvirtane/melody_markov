import unittest
from logic import trie_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = trie_logic.Trie()

    def test_trie_root_has_empty_note(self):
        self.assertEqual(self.t.root.note, "")
