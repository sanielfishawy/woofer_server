import limits as Limits

class Audio:
    def __init__(self):
        self.is_started = False

    def isStarted(self):
        return self.self.is_started

    def setPower(self, power):
        if power:
            self.start()
        else:
            self.stop()

    def start(self):
        self.is_started = True
        return self


    def stop(self):
        self.is_started = False
        return self

    def restart(self):
        if self.isStarted():
            self.stop()
            self.start()

    def setFrequency(self, frequency):
        return self

    setFreq = setFrequency

    def setVolume(self, volume):
        scaled_volume = Limits.get_scaled_volume(volume)
        return self

    def setSpeaker(self, speaker):
        return self

