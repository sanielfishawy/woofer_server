import os
import platform

from audio_pyo import AudioPyo
from audio_alsa import AudioAlsa
from audio import Audio

def get_audio():
    if os.environ.get('WOOFER_STUB_AUDIO'):
        return Audio()
    elif platform.system() == 'Darwin':
        return AudioPyo()
    elif platform.system()  == 'Linux':
        return AudioAlsa()
    else:
        return Audio()