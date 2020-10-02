import os
from subprocess import Popen, STDOUT, DEVNULL
import multiprocessing as mp
import time

class AudioAlsa:
    USB_SPEAKER = {'device':'hw', 'card':'Device', 'control':'PCM'}
    HEADPHONES = {'device':'hw', 'card':'Headphones', 'control':'Headphone'}
    SCALED_VOLUME = {'min':30, 'max':100}

    def __init__(
            self,
            power=True,
            volume=50,
            frequency=200,
            speaker=None,
        ):

        self.volume = volume
        self.frequency = frequency
        self.power = power
        self.speaker = speaker or self.__class__.USB_SPEAKER
        self.testSpeakerProc = None

    def setPower(self, power):
        self.power = power
        if power:
            self.start()
        else:
            self.stop()

    def start(self):
        if not self.isStarted():
            self.setVolume(self.volume)
            self.sendTestSpeakerCommand()

    def isStarted(self):
        return self.testSpeakerProc is not None

    def sendTestSpeakerCommand(self):
        self.testSpeakerProc = Popen(
                self.getTestSpeakerCommand(),
                stdout=DEVNULL,
                stderr=STDOUT,
            )

    def sendVolumeCommand(self, volume):
        return Popen(
            self.getVolumeCommand(volume),
                stdout=DEVNULL,
                stderr=STDOUT,
        )

    def getVolumeCommand(self, volume):
        return [
            'amixer',
            f'-D{self.speaker["device"]}',
            f'-c{self.speaker["card"]}',
            'set',
            f'{self.speaker["control"]}',
            f'{volume}%'
        ]


    def getTestSpeakerCommand(self):
        return ['speaker-test',
                f'-f{self.frequency}',
                f'-D{self.speaker["device"]}:CARD={self.speaker["card"]}',
                '-tsine',
                '-c2',
                '-X']

    def stop(self):
        self.testSpeakerProc and self.testSpeakerProc.terminate()
        self.testSpeakerProc = None
        return self

    def restart(self):
        if self.isStarted():
            self.stop()
            self.start()

    def setFrequency(self, frequency):
        self.frequency = frequency
        self.restart()
        return self

    def setFreq(self, freq):
        return self.setFrequency(freq)

    def setVolume(self, volume):
        self.volume = volume
        self.sendVolumeCommand(self.getScaledVolume(volume))
        return self

    def setSpeaker(self, speaker):
        self.speaker = speaker
        self.restart()

    def getScaledVolume(self, volume):
        min = self.__class__.SCALED_VOLUME['min']
        max = self.__class__.SCALED_VOLUME['max']
        delta = max - min
        scale = delta / 100.0
        return (volume * scale) + min


if __name__ == '__main__':
    a = AudioAlsa()
    a.start()
    a.setSpeaker(a.__class__.HEADPHONES)
    pass