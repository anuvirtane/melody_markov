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
    self.states: pause and notes as strings in list"""
    def __init__(self):
        self.tries = note_logic.TriesByKeys()
        self.states = ["z", "a", "b", "c", "d", "e", "f", "g"]
        # after making Trie return possible transitions, 
        # add possible transitions, like [["aa","ab","ac"],["cc","ca","cb"],["bb","ba","bc"]]
        # add transition matrix: probabilities of transitions like [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

    def generate_melody(self, melody_start: str):
        pass