import simpl
from scipy.io.wavfile import read, write
import scipy as sp

# read audio samples
audio = read("flute.wav")[1]

# convert to doubles between -1 and 1
audio = sp.asarray(audio, dtype=sp.double) / 32768.0  

# Peak detection with SndObj
pd = simpl.SndObjPeakDetection()
pd.max_peaks = 20
peaks = pd.find_peaks(audio)

# Partial Tracking with the McAulay-Quatieri algorithm
pt = simpl.MQPartialTracking()
pt.max_partials = 20
partials = pt.find_partials(peaks)

# Synthesise output
synth = simpl.SndObjSynthesis()
audio_out = synth.synth(partials)
audio_out = sp.asarray(audio_out * 32768, sp.int16)
write('synth_flute.wav', 44100, audio_out)
