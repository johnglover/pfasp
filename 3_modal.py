from modal.onsetdetection import OnsetDetection
from modal.detectionfunctions import ComplexODF
from modal.ui.plot import plot_detection_function, plot_onsets
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import scipy as sp

# read audio file
audio = read("drums.wav")[1]

# values between -1 and 1
audio = audio / 32768.0

# create detection function
codf = ComplexODF()
hop_size = codf.get_hop_size()
odf = sp.zeros(len(audio)/hop_size, dtype=sp.double)
codf.process(audio, odf)

# create onset detection object
od = OnsetDetection()
onsets = od.find_onsets(odf) * hop_size

# plot onset detection results
plt.subplot(2,1,1)
plt.title("Audio And Detected Onsets")
plt.ylabel("Sample Value")
plt.xlabel("Sample Number")
plt.plot(audio, "0.4")
plot_onsets(onsets)
plt.subplot(2,1,2)
plt.title("Detection Function And Threshold")
plt.ylabel("Detection Function Value")
plt.xlabel("Sample Number")
plot_detection_function(odf, hop_size)
thresh = od.threshold
plot_detection_function(thresh, hop_size, "green")
plt.show()
