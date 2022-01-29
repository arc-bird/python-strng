# Import prerequisite packages:

import numpy as np  # For data manipulation
import matplotlib.pyplot as ppl # For data visualization
from scipy.io.wavfile import read, write    # To interpret audio data
import sounddevice as sd    # Used to record

Fs = 6600 # Sample rate
sx = 1  # Length of recording

sample = sd.rec(int(sx * Fs), samplerate = Fs, channels = 2) # Call python-sounddevice's record function
sd.wait()   # Wait until recording is finished
write('audio/sample.wav', Fs, sample) # Save file as .wav

Fs, data = read('audio/sample.wav')

data = data[:,0]

cat = ''

data = data[ (data >= 0.0001) ]

for i in range(len(data)):
    print(data[i])
    cat = cat + str(data[i])

cat = cat.replace('.', '')
cat = int(cat)
print(cat)
