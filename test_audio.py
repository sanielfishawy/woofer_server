import logging
from audio.audio_alsa import AudioAlsa
from audio.audio_sox import AudioSox

logging.basicConfig(level=logging.DEBUG)
a = AudioSox()
a.setVolume(15)
a.start()
a.restart()
pass
