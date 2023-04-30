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
    def __init__(self, path: str = '../../abc-notes', key: str='C'):
        self.tries = note_logic.TriesByKeys()
        self.states = ["z", "a", "b", "c", "d", "e", "f", "g"]
        self.key_possibilities = ['D', 'G', 'A', 'C', 'F']
        self.tries.insert_notes_from_dir(path)
        if key not in self.key_possibilities:
            raise ValueError("Given key should be one of these: ['D', 'G', 'A', 'C', 'F']")
        self.key = key

    def generate_melody(self, given_start: str="", max_length: int=20) -> str:
        """
        Returns a melody generated using Markov chain logic.
        Parameters:
        given_start (str): (optional) starting notes for the melody.
        max_length (int): the maximum length of the melody.
        Returns: a generated melody (str).
        """
        if not given_start:
            predecessors_amount = max_length
        else:
            predecessors_amount = len(given_start)
            chosen_start = given_start
        following_notes = self.tries.get_following_notes_by_key(self.key, predecessors_amount)
        if len(following_notes) == 0:
            return ""
        if not given_start:
            chosen_start = random.choice(list(following_notes.keys()))
        melody = str(chosen_start).split()
        while chosen_start in following_notes and len(melody) < max_length:
            possibilities = following_notes[chosen_start]
            next_note = 'z'
            if possibilities:
                notes_as_weighted_possibilities_list = [key for key, value in
                                          possibilities.items() for i in range(value)]
                next_note = random.choice(notes_as_weighted_possibilities_list)
            melody.append(next_note)
        return "".join(melody)
