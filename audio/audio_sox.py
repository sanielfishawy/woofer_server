from .audio import Audio
from . import limits as Limits
from subprocess import Popen, STDOUT, DEVNULL

class AudioSox(Audio):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.sox_process = None

    def start(self):
        if not super().is_started():
            self.send_sox_command()
        super().set_started()
        return self

    def stop(self):
        self.sox_process and self.sox_process.terminate()
        super().set_stopped()
        return self

    def send_sox_command(self):
        self.sox_process = self.speaker_process = Popen(
                self.get_sox_command(),
                stdout=DEVNULL,
                stderr=STDOUT,
            )

    def get_sox_command(self):
        return ['play',
                '-V',
                '-r48000',
                '-n',
                '-b16',
                '-c2',
                'synth', 'sin',
                f'{self.frequency}',
                'vol', f'{self.get_sox_scaled_volume(self.volume)}']

    def get_sox_scaled_volume(self, volume):
        # sox wants 0-1
        return super().get_scaled_volume(volume) / Limits.get_max_volume()

