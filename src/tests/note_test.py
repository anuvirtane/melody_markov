import unittest
from logic import note_logic

class TestTriesInKeys(unittest.TestCase):
    def setUp(self):
        self.tries = note_logic.TriesByKeys()

    def test_key_longer_than_one_char_not_inserted(self):
        self.tries.insert_notes_from_dir(path="src/tests/test-notes/longkey/") 
        keys = self.tries.get_trie_keys()
        self.assertEqual(keys, set([]))

    def test_trie_returns_only_key_it_contains(self):
        self.tries.insert_notes_from_dir(path="src/tests/test-notes/shortkey/")
        keys = self.tries.get_trie_keys()
        self.assertEqual(keys, set(['D']))

    def test_get_notes_contains_what_it_should(self):
        self.tries.insert_notes_from_dir(path="src/tests/test-notes/shortkey/")
        possibilities_dict = self.tries.get_following_notes_by_key("D", predecessors_amount=2)
        self.assertTrue('az' in possibilities_dict and possibilities_dict['az'] == {"b": 1})


    
    



    