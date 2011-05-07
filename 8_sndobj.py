from sndobj import SndObj, SndRTIO, SND_OUTPUT
import scipy as sp
from scipy.signal import firwin
from scipy.io.wavfile import read
    
# read audio file
audio = read("voice.wav")[1]

# use SciPy to low pass filter
order = 101
cutoff = 0.1
filter = firwin(order, cutoff)
audio = sp.convolve(audio, filter, "same")

# convert to 32-bit floats
audio = sp.asarray(audio, sp.float32)

# create a SndObj to hold frames of output audio
obj = SndObj()

# create a SndObj to output to the sound card
outp = SndRTIO(1, SND_OUTPUT)
outp.SetOutput(1, obj)

# get the default frame size
frame_size = outp.GetVectorSize()

# output each frame
for i in range(0, len(audio), frame_size):
    obj.PushIn(audio[i:i+frame_size])
    outp.Write()
