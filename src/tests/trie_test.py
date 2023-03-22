import unittest
from logic import trie_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_trie_root_has_empty_note(self):
        t = trie_logic.Trie()
        self.assertEqual(t.root.note, "")
