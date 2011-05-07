import scipy as sp
from scipy.io.wavfile import read, write
import pylibpd as pd

num_chans = 1
sampling_rate = 44100

# open a Pure Data patch
m = pd.PdManager(num_chans, num_chans, sampling_rate, 1)
patch = pd.libpd_open_patch("ring_mod.pd")

# get the default frame size
frame_size = pd.libpd_blocksize()

# read audio file
audio = read("drums.wav")[1]

# process each frame
out = sp.array([], dtype=sp.int16)
for i in range(0, len(audio), frame_size):
    f = audio[i:i+frame_size]
    p = m.process(f)
    p = sp.fromstring(p, sp.int16)
    out = sp.hstack((out, p))

# close the patch
pd.libpd_close_patch(patch)

# write the audio file to disk
write("drums_ringmod.wav", 44100, out)
