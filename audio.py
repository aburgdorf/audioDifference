import sys

import IPython.display as ipd
import librosa as lr
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

sys.path.append('/Users/andreas/Downloads')

audio1 = 'sample_high'
audio2 = 'sample_low'


def shift(seq1, seq2):
    max1 = find_first_max(seq1)
    max2 = find_first_max(seq2)

    difference = abs(max1 - max2)

    if max1 > max2:
        new_seq1 = seq1[:len(seq1) - difference]
        new_seq2 = seq2[difference:]
    else:
        new_seq1 = seq1[difference:]
        new_seq2 = seq2[:len(seq2) - difference]

    return np.array(new_seq1), np.array(new_seq2)


def find_first_max(seq):
    max = np.argmax(seq)
    return max


def calc_sum(seq):
    pos_seq = []
    for v in seq:
        if v < 0:
            pos_seq.append(v * -1)
        else:
            pos_seq.append(v)
    return np.sum(np.array(pos_seq))


# Load old file

def calculate_similarity(filename1, filename2):
    y, sr = lr.load(filename1, offset=2.0, duration=2.0)
    ipd.Audio(y, rate=sr)
    plt.figure(figsize=(15, 5))
    lr.display.waveshow(y, sr=sr, alpha=0.8)

    # Load new file

    y_r, sr_r = lr.load(filename2, offset=2.0, duration=2.0)
    ipd.Audio(y_r, rate=sr_r)
    lr.display.waveshow(y_r, sr=sr_r, alpha=0.8)
    plt.show()

    # Shift audio files for matching at max

    new_seq1, new_seq2 = shift(y, y_r)
    plt.figure(figsize=(15, 5))
    plt.plot(new_seq1)
    plt.plot(new_seq2)
    # lr.display.waveshow(new_seq1, new_seq2, sr=sr, alpha=0.8)
    plt.show()

    diff = np.subtract(new_seq1, new_seq2)

    plt.figure(figsize=(15, 5))
    plt.plot(diff)
    plt.show()

    diff_score = calc_sum(diff)
    print('Difference Score:', diff_score)

    return diff_score


def convertm4atowav(filename):
    new_filename = filename.split('.')[0] + '.wav'
    audio = AudioSegment.from_file(filename)
    audio.export(filename=new_filename, format='wav')


convertm4atowav('sample_high_test.m4a')
