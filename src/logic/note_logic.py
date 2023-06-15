"""Parse all abc notes available and insert into Trie if key is just one letter long."""

import os
from sjkabc import parse_dir


try:
    import trie_logic
except:
    from . import trie_logic

class TriesByKeys:
    """Attributes:
    self.tries: dict of tries by keys
    self.strip: a string that sometimes ends up in abc if not stripped"""
    def __init__(self):
        self.tries = {}
        self.strip = "wranscriptioncjackcampin2009nomirroringorrepblicationwithotpermission"

    def insert_notes_from_dir(self, path: str='../../abc-notes/'):
        """Parses all abc notes in given directory and inserts them in self.tries
        if their keys are one character long"""
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Got directory that is not a directory as argument: {path}")
        for tune in parse_dir(path):
            if len(tune.key) == 1:
                key = tune.key[0]
                if len(key) == 1:
                    if tune.key[0] not in self.tries.keys():
                        trie = trie_logic.Trie()
                        self.tries[key] = trie
                    abc = tune.expanded_abc.replace(self.strip, "")
                    abc_cleaned = ""
                    for char in abc:
                        if char in ["z", "a", "b", "c", "d", "e", "f", "g"]:
                            abc_cleaned = abc_cleaned + char
                    for i in range(len(abc_cleaned)):
                        if i+5 < len(abc_cleaned):
                            end_index = 5
                        else: 
                            end_index = len(abc_cleaned) - i
                        abc_chars_five_or_less = abc_cleaned[i:i+end_index]
                        self.tries[key].insert(abc_chars_five_or_less)

    def get_trie_keys(self):
        """Returns all available keys as dict keys formatted like so:
        dict_keys(['D', 'G', 'A', 'C', 'F'])
        """
        return self.tries.keys()

    def get_following_notes_by_key(self, key: str, predecessors_amount: int):
        """Returns dict with following notes by wanted key"""
        if key not in self.tries.keys():
            return {}
        return self.tries[key].get_following_notes_with_frequencies(predecessors_amount)
        