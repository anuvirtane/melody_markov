import unittest
from logic import markov_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.mc = markov_logic.MarkovChain("src/tests/test_notes/shortkey", "A")

    def test_generate_melody(self):
        melody = self.mc.generate_melody(1)
        self.assertTrue(melody, "")