import os
from subprocess import Popen, STDOUT, DEVNULL
import logging
import shlex
from .audio import Audio


class AudioAlsa(Audio):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.testSpeakerProc = None

    def start(self):
        pass
        if not super().is_started():
            self.sendTestSpeakerCommand()
            self.sendVolumeCommand()
            self.set_started()

    def sendTestSpeakerCommand(self):
        cmd = self.getTestSpeakerCommand()
        logging.debug(shlex.join(cmd))
        self.testSpeakerProc = Popen(
                cmd,
                stdout=DEVNULL,
                # stdout=DEVNULL,
                # stdout=STDOUT,
                # stderr=STDOUT,
            )

    def sendVolumeCommand(self):
        cmd = self.getVolumeCommand(self.volume)
        logging.debug(shlex.join(cmd))
        return Popen(
            cmd,
            stdout=DEVNULL,
            # stdout=STDOUT,
            # stderr=STDOUT,
        )

    def getVolumeCommand(self, volume):
        speaker = super().get_speaker()
        return [
            'amixer',
            f'-D{speaker["device"]}',
            f'-c{speaker["card"]}',
            'set',
            f'{speaker["control"]}',
            f'{super().get_scaled_volume(volume)}%',
        ]

    def getTestSpeakerCommand(self):
        speaker = super().get_speaker()
        return [
            'speaker-test',
            f'-f{self.frequency}',
            f'-D{speaker["device"]}:CARD={speaker["card"]}',
            '-tsine',
            '-c2',
            '-X',
        ]

    def stop(self):
        self.testSpeakerProc and self.testSpeakerProc.terminate()
        self.testSpeakerProc = None
        self.set_stopped()
        return self


if __name__ == '__main__':
    a = AudioAlsa()
    a.start()
    pass