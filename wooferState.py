class WooferState:
    POWER = 'power'
    VOLUME = 'volume'
    FREQUENCY = 'frequency'
    DEFAULT_STATE = {POWER: False, VOLUME: 0, FREQUENCY: 40}

    def __init__(self):
        self.state = self.__class__.DEFAULT_STATE

    def getState(self):
        return self.state

    def getPower(self):
        return self.getState()[self.__class__.POWER]

    def getVolume(self):
        return self.getState()[self.__class__.VOLUME]

    def getFrequency(self):
        return self.getState()[self.__class__.FREQUENCY]

    def setPower(self, power):
        self.state[self.__class__.POWER] = power
        return self

    def setVolume(self, volume):
        self.state[self.__class__.VOLUME] = volume
        return self

    def setFrequency(self, frequency):
        self.state[self.__class__.FREQUENCY] = frequency
        return self


