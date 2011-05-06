import simpl
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# read audio samples
audio = read("flute.wav")[1]
# take just the first few frames
audio = audio[0:4096]
# Peak detection with SndObj
pd = simpl.SndObjPeakDetection()
pd.max_peaks = 20
pks = pd.find_peaks(audio)
# Partial Tracking with 
# the McAulay-Quatieri algorithm
pt = simpl.MQPartialTracking()
pt.max_partials = 20
partls = pt.find_partials(pks)
# plot the detected partials
simpl.plot.plot_partials(partls)
# set title and label axes
plt.title("Flute Partials")
plt.ylabel("Frequency (Hz)")
plt.xlabel("Frame Number")
plt.show()
