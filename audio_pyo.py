from pyo import *

class AudioPYO:

    def __init__(
        self,
        power=True,
        volume=50,
        frequency=500,
        ):
        self.server = Server().boot()
        self.volume = volume
        self.frequency = frequency
        self.wave = Sine().out()
        if power is True:
            self.start()

    def setPower(self, power):
        if power:
            self.start()
        else:
            self.stop()

    def start(self):
        self.server.start()
        return self

    def stop(self):
        self.server.stop()
        return self

    def setFrequency(self, frequency):
        self.wave.setFreq(frequency)
        return self

    def setFreq(self, frequency):
        self.setFrequency(frequency)
        return self

    def setVolume(self, volume):
        self.volume = volume
        r = volume/100.0
        self.wave.range(-r, r)
        return self

if __name__ == '__main__':
    a = AudioPyo()
    a.server.gui(locals())