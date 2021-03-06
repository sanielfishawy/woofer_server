import logging
from threading import Lock
import time
from . import limits as Limits

class Audio:
    def __init__(self):
        self._is_started = False
        self.is_started_lock = Lock()
        self.volume = None
        self.frequency = None
        self.speaker = None
        self.volume = (Limits.get_default_volume())
        self.frequency = (Limits.get_default_frequency())
        self.speaker = (Limits.SpeakerHelper.get_speaker())
        logging.debug(f'Speaker = {self.speaker}')

    def get_is_started_lock(self):
        return self.is_started_lock

    def is_started(self):
        return self._is_started

    def set_started(self):
        self._is_started = True
        return self

    def set_stopped(self):
        self._is_started = False
        return self

    def setPower(self, power):
        if power:
            self.start()
        else:
            self.stop()

    def start(self):
        return self

    def stop(self):
        return self

    def restart(self):
        with self.get_is_started_lock():
            if self.is_started():
                self.stop()
                self.start()

    def setFrequency(self, frequency):
        self.frequency = frequency
        self.restart()
        return self

    def setVolume(self, volume):
        self.volume = volume
        self.restart()
        return self

    def setSpeaker(self, speaker):
        self.speaker = speaker
        self.restart()
        return self

    def get_speaker(self):
        return self.speaker

    def get_speaker_str(self):
        return Limits.SpeakerHelper.get_speaker_str(self.get_speaker())

    def get_scaled_volume(self, volume):
        return Limits.get_scaled_volume(volume)
