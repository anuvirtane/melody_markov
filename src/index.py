"""First sounddevice recording and playing experiment: 
run program, make sounds for 5 s
and then hear the program play your own sounds"""

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write


fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('my_first_recording.wav', fs, myrecording)  # Save as WAV file 

#play:

# Extract data and sampling rate from file
data, fs = sf.read('my_first_recording.wav', dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing