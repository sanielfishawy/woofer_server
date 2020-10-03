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
        return self

    def stop(self):
        return self

    def restart(self):
        if self.isStarted():
            self.stop()
            self.start()

    def setFrequency(self, frequency):
        return self

    def setVolume(self, volume):
        return self

    def setSpeaker(self, speaker):
        return self

    def get_scaled_volume(self, volume):
        return Limits.get_scaled_volume(volume)
