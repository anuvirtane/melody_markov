"""Convert abc notation to mid file in order to be able to play it"""

from music21 import converter

s = converter.parse('src/music/generated.abc')
s.write('midi', fp='src/music/output.mid')
