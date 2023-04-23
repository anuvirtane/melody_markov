"""Markov Chain generates melodies based on what has been inserted in the Tries"""

import random
try:
    import note_logic # pylint: disable=[import-error]
except:
    from . import note_logic

class MarkovChain:
    """Attributes:
    self.tries: Tries that contain melodies by keys
    self.states: pause and notes as strings in list
    self.keys: hard coded values of keys that teaching data used this far contained in list"""
    def __init__(self, path: str, key: str):
        self.tries = note_logic.TriesByKeys()
        self.states = ["z", "a", "b", "c", "d", "e", "f", "g"]
        self.keys = ['D', 'G', 'A', 'C', 'F']
        self.tries.insert_notes_from_dir(path)
        if key not in self.keys:
            raise ValueError("Given key should be one of these: ['D', 'G', 'A', 'C', 'F']")
        self.following_notes = self.tries.get_following_notes_by_key(key, 1)

    def generate_melody(self, max_length: int, given_start: str="") -> str:
        """
        Returns a melody generated using Markov chain logic.
        Parameters:
        given_start (str): (optional) starting notes for the melody.
        max_length (int): the maximum length of the melody.
        Returns: a generated melody (str).
        """
        if len(self.following_notes) == 0:
            return "no results"
        if not given_start:
            chosen_start = random.choice(list(self.following_notes.keys()))
            melody = str(chosen_start).split()
        while chosen_start in self.following_notes and len(melody) < max_length:
            possibilities = self.following_notes[chosen_start]
            next_note = None
            if possibilities:
                notes_as_weighted_possibilities_list = [key for key, value in
                                          possibilities.items() for i in range(value)]
                next_note = random.choice(notes_as_weighted_possibilities_list)
                melody.append(next_note)
        return "".join(melody)

 