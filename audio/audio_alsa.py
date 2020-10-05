import os
from subprocess import Popen, STDOUT, DEVNULL

class AudioAlsa:
    def __init__(self):
        super(self.__class__, self).__init__()
        self.testSpeakerProc = None

    def start(self):
        if not super().is_started()
            self.setVolume(self.volume)
            self.sendTestSpeakerCommand()
            self.set_started()

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
        speaker = super().get_speaker()
        return [
            'amixer',
            f'-D{speaker["device"]}',
            f'-c{speaker["card"]}',
            'set',
            f'{speaker["control"]}',
            f'{super().get_scaled_volume(volume)}%'
        ]

    def getTestSpeakerCommand(self):
        speaker = super().get_speaker()
        return ['speaker-test',
                f'-f{self.frequency}',
                f'-D{speaker["device"]}:CARD={speaker["card"]}',
                '-tsine',
                '-c2',
                '-X']

    def stop(self):
        self.testSpeakerProc and self.testSpeakerProc.terminate()
        self.testSpeakerProc = None
        self.set_stopped()
        return self


if __name__ == '__main__':
    a = AudioAlsa()
    a.start()
    pass