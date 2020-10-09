import os
import platform

# from .audio_pyo import AudioPyo
from .audio_alsa import AudioAlsa
from .audio_sox import AudioSox
from .audio import Audio

def get_audio():
    stub_audio = os.environ.get('WOOFER_STUB_AUDIO')
    if stub_audio and stub_audio.lower == 'true':
        return Audio()
    elif platform.system() == 'Darwin':
        return AudioSox()
    elif platform.system()  == 'Linux':
        return AudioSox()
    else:
        return Audio()