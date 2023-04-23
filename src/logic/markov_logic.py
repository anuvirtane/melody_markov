"""Markov Chain generates melodies based on what has been inserted in the Tries"""

import random
try:
    import note_logic # pylint: disable=[import-error]
except:
    from . import note_logic

# # Possible sequences of events
# transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

# # Probabilities matrix (transition matrix)
# transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

class MarkovChain:
    """Attributes:
    self.tries: Tries that contain melodies by keys
    self.states: pause and notes as strings in list
    self.keys: hard coded values of keys that teaching data used this far contained in list"""
    def __init__(self):
        self.tries = note_logic.TriesByKeys()
        self.states = ["z", "a", "b", "c", "d", "e", "f", "g"]
        self.keys = ['D', 'G', 'A', 'C', 'F']
        self.tries.insert_notes_from_dir()
        self.ngrams = self.tries.get_following_notes_by_key("D", 1)

    def generate_melody(self, given_start: str="", max_length=100) -> str:
        """
        Returns a melody generated using Markov chain logic.
        Parameters:
        given_start (str): (optional) starting notes for the melody.
        max_length (int): the maximum length of the melody.
        Returns: a generated melody (str).
        """
        if not given_start:
            chosen_start = random.choice(list(self.ngrams.keys()))
            melody = str(chosen_start).split()

        while chosen_start in self.ngrams and len(melody) < max_length:
            possibilities = self.ngrams[chosen_start]
            next_note = None

            if possibilities:
                notes_as_weighted_possibilities_list = [key for key, value in
                                          possibilities.items() for i in range(value)]
                next_note = random.choice(notes_as_weighted_possibilities_list)
                melody.append(next_note)
        return "".join(melody)

 