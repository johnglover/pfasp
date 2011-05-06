from sndobj import SndObj, SndRTIO, SND_OUTPUT
import scipy as sp
from scipy.signal import firwin
from scipy.io.wavfile import read
    
# read audio file
audio = read("drums.wav")[1]

# use SciPy to low pass filter
order = 101
cutoff = 0.02
filter = firwin(order, cutoff)
audio = sp.convolve(audio, filter, "same")

# convert to 32-bit floats
audio = sp.asarray(audio, sp.float32)

# create a SndObj that will hold
# frames of output audio
obj = SndObj()

# create a SndObj that will
# output to the sound card
outp = SndRTIO(1, SND_OUTPUT)
outp.SetOutput(1, obj)

# get the default frame size
f_size = outp.GetVectorSize()

# output each frame
i = 0
while i < len(audio):
    obj.PushIn(audio[i:i+f_size])
    outp.Write()
    i += f_size
