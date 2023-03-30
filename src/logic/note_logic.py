"""Parse abc notes and insert into Trie. Query trie. Hard-coded values for testing purposes."""

from sjkabc import parse_dir
import trie_logic # pylint: disable=[import-error]

d_trie = trie_logic.Trie()
for tune in parse_dir('../abc-notes/'):
    if len(tune.key) == 1:
        if tune.key[0] == 'C':
            STRIP = "wranscriptioncjackcampin2009nomirroringorrepblicationwithotpermission"
            abc = tune.expanded_abc.replace(STRIP, "")           
            print(f'Parsed {tune.title} with abc {abc}')
            d_trie.insert(abc)
d_trie.query("ggg")
print(d_trie.output)
            