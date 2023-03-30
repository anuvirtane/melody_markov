"""Parse abc notes and insert into Trie. Query trie. Hard-coded values for testing purposes."""

from sjkabc import parse_dir
import trie_logic

d_trie = trie_logic.Trie()
for tune in parse_dir('../abc-notes/'):
  # print('Parsed {} with abc {} and key {}.'.format(tune.title, tune.expanded_abc, tune.key))
    if len(tune.key) == 1:
        if tune.key[0] == 'C':
            abc = tune.expanded_abc.replace("wranscriptioncjackcampin2009nomirroringorrepblicationwithotpermission", "")           
            print('Parsed {} with abc {}'.format(tune.title, abc))
            d_trie.insert(abc)
d_trie.query("ggg")
print(d_trie.output)
        
       