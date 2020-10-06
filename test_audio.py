import logging
from audio.audio_alsa import AudioAlsa
from audio.audio_sox import AudioSox

logging.basicConfig(level=logging.DEBUG)
a = AudioSox()
a.start()
a.setVolume(15)
pass
