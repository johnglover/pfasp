from scipy.io.wavfile import write
import scipy as sp
import pysms

# Have to analyze source again for now, should really be a way to copy/clone frames
audio_file = "voice.wav"
frames, sms_header, snd_header = pysms.analyze(audio_file)

# Set modification parameters
mod_params = pysms.SMS_ModifyParams()
mod_params.doTranspose = True
mod_params.transpose = 4 # 4 semi-tones up

# apply modification to each frame
for frame in frames:
    pysms.sms_modify(frame, mod_params)

# Synthesis
output = pysms.synthesize(frames, sms_header)

# convert audio to int values
output /= output.max()
output = sp.asarray(output*32768, sp.int16)

# write output files
write("voice_transposed.wav", snd_header.iSamplingRate, output)
