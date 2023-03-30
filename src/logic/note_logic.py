
from sjkabc import parse_dir

for tune in parse_dir('../abc-notes/'):
   print('Parsed {} with abc {} and key {}.'.format(tune.title, tune.expanded_abc, tune.key))
 