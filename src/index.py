"""Generate and play melody before having GUI made. Randomly chooses key and 
length of melody and generates it without initial input."""

from logic import markov_logic # pylint: disable=[import-error]
from music import play_abc
from random import choice

path ="abc-notes"
key = choice(['D', 'G', 'A', 'C', 'F'])
melody_length = choice([10, 20, 50, 75, 100])
mc = markov_logic.MarkovChain(path, key)
melody = mc.generate_melody(max_length=melody_length)
print(f"Generated and played a melody from teaching data randomly in {key} using length {melody_length}")
with open("src/music/generated.abc", "w") as abc_file:
    abc_file.write("L:1/8\n")
    abc_file.write(melody)
play_abc

