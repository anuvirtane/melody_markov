"""This is a first version of mid player to be able to play the abc notes
generated by Markov chain. At the moment hard-coded for testing purposes."""

from music21 import converter
import pygame

s = converter.parse('logic/expanded.abc')
s.write('midi', fp='output.mid')
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load("output.mid")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)

