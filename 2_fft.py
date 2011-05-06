import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt

# read audio samples
input_data = read("flute.wav")
audio = input_data[1]
# apply a Hanning window
window = hann(1024)
audio = audio[0:1024] * window
# fft
mags = abs(rfft(audio))
# convert to dB
mags = 20 * scipy.log10(mags)
# normalise to 0 dB max
mags -= max(mags)
# plot
plt.plot(mags)
# label the axes
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")
# set the title
plt.title("Flute Spectrum")
plt.show()
