# Import dependencies:

import numpy as np
from scipy.io.wavfile import read, write
import sounddevice as sd

def stSampler( sRate, length = 1 ):
    _sample = sd.rec( int(sRate * length), samplerate = sRate, channels = 1 )
    sd.wait()
    write( 'audio/sample.wav', sRate, _sample )
