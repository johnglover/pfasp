import scipy as sp
from scipy import int16
from scipy.io.wavfile import \
    read, write
import pylibpd as pd

num_chans = 1
sampling_rate = 44100
# open a Pure Data patch
m = pd.PdManager(num_chans, 
                 num_chans, 
                 sampling_rate, 
                 1)
p_name = "ring_mod.pd"
patch = \
    pd.libpd_open_patch(p_name)
# get the default frame size
f_size = pd.libpd_blocksize()
# read audio file
audio = read("drums.wav")[1]
# process each frame
i = 0
out = sp.array([], dtype=int16)
while i < len(audio):
    f = audio[i:i+f_size]
    p = m.process(f)
    p = sp.fromstring(p, int16)
    out = sp.hstack((out, p))
    i += f_size
# close the patch
pd.libpd_close_patch(patch)
# write the audio file to disk
write("out.wav", 44100, out)
