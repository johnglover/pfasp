# Transpose maintaining spectral envelope
from scipy.io.wavfile import write
import scipy as sp
import pysms

audio_file = "voice.wav"

# analyse audio, also calculate the Discrete Cepstrum Envelope
frames, sms_header, snd_header = \
    pysms.analyze(audio_file, env_type=pysms.SMS_ENV_FBINS, env_order=80)

# Set modification parameters
mod_params = pysms.SMS_ModifyParams()
mod_params.maxFreq = 12000 # only calculate envelope up to 12 kHz
mod_params.doSinEnv = True # apply envelope to sinusoidal component
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
write("voice_transposed_env.wav", snd_header.iSamplingRate, output)
