"""Parse all abc notes available and insert into Trie if key is just one letter long."""

from sjkabc import parse_dir
import trie_logic # pylint: disable=[import-error]

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
        for tune in parse_dir(path):
            if len(tune.key) == 1:
                key = tune.key[0]
                if len(key) == 1:
                    if tune.key[0] not in self.tries.keys(): # pylint: disable=[consider-iterating-dictionary]
                        trie = trie_logic.Trie()
                        self.tries[key] = trie
                    abc = tune.expanded_abc.replace(self.strip, "")
                    self.tries[key].insert(abc)

    def get_trie_keys(self):
        """Returns all available keys"""
        return self.tries.keys() # pylint: disable=[consider-iterating-dictionary]

    def query_by_key(self, key: str, query: str):
        """Queries if wanted string is in trie by wanted key"""
        if key not in self.tries.keys(): # pylint: disable=[consider-iterating-dictionary]
            return "No data available for this key"
        return self.tries[key].query(query)
        