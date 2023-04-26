"""Simple text based user interface for generating and playing melodies"""

from logic import markov_logic # pylint: disable=[import-error]
from music import play_abc
from random import choice

class UI:
    def __init__(self):
        self.path = "abc-notes"
        self.keys = ['D', 'G', 'A', 'C', 'F']
        self.melody_lengths = [10, 20, 50]
        self.commands = {
            "exit":"Exit program",
            "melody": "Generate melody",
            "play": "Play generated melody",
            "help": "Print the list of available commands"
        }

    def help(self):
        for key, value in self.commands.items():
            print(f"'{key}': {value}")

    def melody(self):
        print("Start generating melody by inputting key. Options are: D, G, A, C, F")
        key = str(input("Input wanted key from options (D, G, A, C, F). Empty or invalid input means key will be chosen for you: "))
        if not key or key.upper() not in self.keys:
            key = choice(self.keys)
        print(f"Key chosen is {key}")
        mc = markov_logic.MarkovChain(self.path, key.upper())
        print("You can generate melody from scratch or by inputting beginning of melody.\n")
        print("Shorter input is likely to result in longer melody result.\n")
        melody_start = str(input("Input wanted beginning of melody as text that contains note letters (a, b, c, d, e, f, g, z). z means Pause in melody: "))
        if not melody_start:
            print("For empty input, a melody start is randomly chosen.")
        else:
            print(f"Melody will start like this: {melody_start}")
        melody = mc.generate_melody(melody_start)
        with open("src/music/generated.abc", "w") as abc_file:
            abc_file.write("L:1/8\n")
            abc_file.write(f"K:{key}\n")
            abc_file.write(melody)
        print(f"Generated a melody from teaching data in key {key}")
        
    def play(self):
        play_abc

    def initialize(self):
        while True:
            cmd = input("Input command, 'exit' to close, 'help' for a list of commands" + "\n")
            if cmd == "exit":
                break
            elif cmd in self.commands:
                func = f"self.{cmd}()"
                exec(func)
            else:
                print("Not a command")
    