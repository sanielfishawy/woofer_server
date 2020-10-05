import logging
from audio.audio_alsa import AudioAlsa

logging.basicConfig(level=logging.DEBUG)
a = AudioAlsa()
a.start()
a.setVolume(20)
pass
