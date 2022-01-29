import numpy as np
from scipy.io.wavfile import read, write

def concat( arr, tolerance = 0.0001 ):
    cat = ''
    data = data[ ( data >= tolerance ) ]

    for i in range(len(data)):
        cat = cat + str( data[i] )

    cat = cat.replace( '.', '' )
    cat = int(cat)

    return(cat)


def stParse( sample, method = 'catPass', channels = 1 ):
    Fs, data = read( sample )

    if method.lower() == 'print':
        for i in range(len(data)):
            print( data[i] )

    elif method.lower() == 'concat':
        print( concat( data ) )

    elif method == 'catPass'
        concat( data )
