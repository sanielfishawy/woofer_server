import limits as Limits

class StateHelper:
    POWER_KEY = 'power'
    MIN_VOLUME_KEY = 'min_volume'
    VOLUME_KEY = 'volume'
    MAX_VOLUME_KEY = 'max_volume'
    DEFAULT_VOLUME_KEY = 'default_volume'
    MIN_FREQUENCY_KEY = 'min_frequency'
    FREQUENCY_KEY = 'frequency'
    MAX_FREQUENCY_KEY = 'max_frequency'
    DEFAULT_FREQUENCY_KEY = 'default_frequency'

    @classmethod
    def get_default_state(cls):
        return {
            cls.POWER_KEY: Limits.get_default_power(),
            cls.MIN_VOLUME_KEY: Limits.get_min_volume(),
            cls.VOLUME_KEY: Limits.get_default_volume(),
            cls.MAX_VOLUME_KEY: Limits.get_max_volume(),
            cls.DEFAULT_VOLUME_KEY: Limits.get_default_volume(),
            cls.MIN_FREQUENCY_KEY: Limits.get_min_frequency(),
            cls.FREQUENCY_KEY: Limits.get_default_frequency(),
            cls.MAX_FREQUENCY_KEY: Limits.get_max_frequency(),
            cls.DEFAULT_FREQUENCY_KEY: Limits.get_default_frequency(),
        }


class WooferState:

    def __init__(self):
        self.state = StateHelper.get_default_state()

    def getState(self):
        return self.state

    def getPower(self):
        return self.getState()[StateHelper.POWER_KEY]

    def getVolume(self):
        return self.getState()[StateHelper.VOLUME_KEY]

    def getFrequency(self):
        return self.getState()[StateHelper.FREQUENCY_KEY]

    def setPower(self, power):
        self.state[StateHelper.POWER_KEY] = power
        return self

    def setVolume(self, volume):
        self.state[StateHelper.VOLUME_KEY] = Limits.get_limited_volume(volume)
        return self

    def setFrequency(self, frequency):
        self.state[StateHelper.FREQUENCY_KEY] = Limits.get_limited_frequency(frequency)
        return self


