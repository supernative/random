import torchaudio
import torchaudio.functional as F

# Load the impulse response and normalise
rir_raw, sample_rate = torchaudio.load('path/to/impulse/response')
rir = rir_raw[:, int(sample_rate * 1.01) : int(sample_rate * 1.3)]
rir = rir / torch.norm(rir, p=2)

# Load the speech
speech, _ = torchaudio.load('path/to/sppech')

# Convolve speech with room impulse response
speech_with_reverb = F.fftconvolve(speech, rir)

torchaudio.save('path/to/speech-with-reverb', speech_with_reverb, sample_rate)
