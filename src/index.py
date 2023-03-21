"""First sounddevice recording and playing experiment: 
run program, make sounds for 5 s
and then hear the program play your own sounds"""

import sounddevice as sd
import soundfile as sf
import scipy.io.wavfile as sciwav

import numpy as np
import aubio as bio
import pydtmc as mc

#record:
fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
sciwav.write('my_first_recording.wav', fs, myrecording)  # Save as WAV file 

#play:

#Extract data and sampling rate from file
audio_data, fs = sf.read('my_first_recording.wav', dtype='float32')  
sd.play(audio_data, fs)
status = sd.wait()  # Wait until file is done playing



# Load the .wav file using aubio
filename = 'my_first_recording.wav'
downsample = 1
samplerate = 44100 // downsample
win_s = 4096 // downsample # fft size
hop_size = 256
s = bio.source(filename, samplerate, hop_size)
p = bio.pitch("default", win_s, hop_size, samplerate)
p.set_unit("midi")
p.set_tolerance(0.8)

# Extract pitch and duration events from the audio file
events = []
total_frames = 0
while True:
    samples, read = s()
    pitch = p(samples)[0]
    total_frames += read
    if read < hop_size:
        break
    if pitch != 0:
        duration = read / samplerate
        events.append((int(round(pitch)), duration))

#print(events)

# Convert events into a sequence of discrete states
state_seq = []
for event in events:
    pitch, duration = event
    print(pitch)
    print(duration)
 

# #Save the state sequence to a text file
# with open('output.txt', 'w') as f:
#     for state in state_seq:
#         f.write(str(state) + '\n')


# # Load the state sequence from the text file
# with open('output.txt', 'r') as f:
#     state_seq = [int(line.strip()) for line in f]





