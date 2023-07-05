"""Simple text based user interface for generating and playing melodies"""

from logic import markov_logic
from music import abc_to_mid
from random import choice
import pygame
import importlib

class UI:
    def __init__(self):
        self.path = "abc-notes"
        self.keys = ['D', 'G', 'A', 'C', 'F']
        self.filepath = "src/music/output.mid"      
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
        print(f"Key chosen is {key.upper()}")
        mc = markov_logic.MarkovChain(self.path, key.upper())
        print("You can generate melody from scratch or by inputting beginning of melody.\n")
        melody_start = str(input("Input wanted beginning of melody as text that contains note letters (a, b, c, d, e, f, g, z). z means pause in melody: "))
        if not melody_start:
            print("For empty input, a melody start is randomly chosen.")
            states = 2
        else:
            melody_start = melody_start.replace(" ", "")
            print(f"Melody will start like this: {melody_start}")
            states = input("How many previous notes do you wish to consider? Input number 2, 3 or 4: ")
            if int(states) != 2 and int(states) != 3 and int(states) != 4:
                states = 2
            if int(states) > len(melody_start):
                print("The given start for melody is shorter than amount of notes you wish to consider - no melody can be generated")
                return
        melody = mc.generate_melody(melody_start, prev_states=int(states))
        with open("src/music/generated.abc", "w") as abc_file:
            abc_file.write("L:1/8\n")
            abc_file.write(f"K:{key.upper()}\n")
            abc_file.write(melody)
        abc_to_mid
        print(f"Generated a melody from teaching data in key {key} considering {states} previous notes ")
        
    def play(self):
        importlib.reload(abc_to_mid)
        pygame.init() # pylint: disable=[no-member]
        pygame.mixer.init()
        pygame.mixer.music.load(self.filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
        print("Finished playing melody")
        pygame.quit()

    def initialize(self):
        while True:
            cmd = input("\nInput command, 'exit' to close, 'help' for a list of commands" + "\n")
            if cmd == "exit":
                break
            elif cmd in self.commands:
                func = f"self.{cmd}()"
                exec(func)
            else:
                print("Not a command")

    
    