import unittest
from logic import markov_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.mc = markov_logic.MarkovChain("src/tests/test-notes/shortkey/", "A")

    def test_melody_generated_without_data_is_empty(self):
        melody = self.mc.generate_melody()
        self.assertTrue(melody == '')