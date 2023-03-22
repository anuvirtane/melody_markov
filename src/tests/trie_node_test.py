import unittest
from logic import trie_logic

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.tn = trie_logic.TrieNode("F")

    def test_node_has_note(self):
        self.assertEqual(self.tn.note, "F")