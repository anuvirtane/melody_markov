"""Parse all abc notes available and insert into Trie if key is just one letter long."""

from sjkabc import parse_dir
import trie_logic

class TriesByKeys:
    def __init__(self):
        self.tries = {}
        self.strip = "wranscriptioncjackcampin2009nomirroringorrepblicationwithotpermission"
        
    def insert_notes_from_dir(self, path: str='../../abc-notes/'):
        for tune in parse_dir(path):
            if len(tune.key) == 1:
                key = tune.key[0]
                if len(key) == 1:
                    if tune.key[0] not in self.tries.keys():
                        trie = trie_logic.Trie()
                        self.tries[key] = trie
                    abc = tune.expanded_abc.replace(self.strip, "")           
                    self.tries[key].insert(abc)
                 
    def get_trie_keys(self):
        return self.tries.keys()
    
    def query_by_key(self, key: str, query: str):
        if key not in self.tries.keys():
            return "No data available for this key"
        return self.tries[key].query(query)

            