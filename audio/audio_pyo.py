from pyo import *
from . import limits as Limits
from .audio import Audio

class AudioPyo(Audio):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.server = Server().boot()
        self.wave = Sine().out()
        self.setFrequency(Limits.get_default_frequency())
        self.setVolume(Limits.get_default_volume())


    def start(self):
        self.server.start()
        self.is_started = True
        return self

    def stop(self):
        self.server.stop()
        self.is_started = False
        return self

    def setFrequency(self, frequency):
        self.wave.setFreq(frequency)
        return self

    def setVolume(self, volume):
        r = self.get_scaled_volume(volume)/100.0
        self.wave.range(-r, r)
        return self

if __name__ == '__main__':
    a = AudioPyo()
    a.server.gui(locals())