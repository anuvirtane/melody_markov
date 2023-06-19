import unittest
from logic import markov_logic

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.mc = markov_logic.MarkovChain("src/tests/test-notes/shortkey/", "D")
        self.teaching_melody="azbabzgbcczddddecefzafgbagz"

    def test_melody_beginswith_given_start(self):
        melody = self.mc.generate_melody(given_start="dd")
        self.assertEqual(melody[:2], 'dd')

    def test_melody_end_contains_only_sequences_found_in_teaching_melody(self):
        melody = self.mc.generate_melody(given_start="dd")
        sequence_found = False
        for i in range(2, len(melody)):
            sequence_found = melody[i-2:i] in self.teaching_melody
            if not melody[i-2:i]:
                sequence_found=False
        self.assertTrue(sequence_found)
