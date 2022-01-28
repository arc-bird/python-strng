# Import prerequisite packages:

import numpy as np  # For data manipulation
import matplotlib.pyplot as ppl # For data visualization
from scipy.io.wavfile import read, write    # To interpret audio data
import sounddevice as sd

Fs = 44000 # Sample rate
sx = 1  # Length of recording

sample = sd.rec(int(sx * Fs), samplerate = Fs, channels = 2)
sd.wait()   # Wait until recording is finished
write('audio/sample.wav', Fs, sample) # Save file as .wav

Fs, data = read('audio/sample.wav')

data = data[:,0]

cat = ''

for i in range(len(data)):
    if data[i] < 0: data[i] = -data[i]
    cat = cat + str(data[i])

print(cat)
