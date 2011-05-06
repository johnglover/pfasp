from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("flute.wav")
audio = input_data[1]
# plot the first 1024 samples 
plt.plot(audio[0:1024]) 
# label the axes
plt.ylabel("Amplitude") 
plt.xlabel("Time (samples)") 
# set the title
plt.title("Flute Sample")
# display the plot
plt.show()
