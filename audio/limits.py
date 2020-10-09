import os
import platform

DEFAULT_POWER = False

MIN_VOLUME = 0
MAX_VOLUME = 100
DEFAULT_VOLUME = 0

FREQUENCY = {
    'WOOFER_SPEAKER':{
        'MIN_FREQUENCY': 20,
        'MAX_FREQUENCY': 200,
        'DEFAULT_FREQUENCY': 40,
    },
    'NORMAL_SPEAKER':{
        'MIN_FREQUENCY': 200,
        'MAX_FREQUENCY': 600,
        'DEFAULT_FREQUENCY': 300,
    },
}

SCALED_VOLUME = {
    'WOOFER_SPEAKER': {
        'MIN_SCALED_VOLUME': 30,
        'MAX_SCALED_VOLUME': 100,
    },
    'NORMAL_SPEAKER': {
        'MIN_SCALED_VOLUME': 0,
        'MAX_SCALED_VOLUME': 100,
    },
}

class SpeakerHelper:
    USB_SPEAKER = 'usb_speaker'
    HEADPHONES = 'headphones'

    DEVICES = {
        'pi': {
            USB_SPEAKER: {'device':'hw', 'card':'Device', 'dev':0, 'control':'PCM'},
            HEADPHONES: {'device':'hw', 'card':'Headphones', 'dev':0, 'control':'Headphone'},
        },
        'mac': {
            'default': None,
        },
    }

    @classmethod
    def get_default_speaker(cls):
        return cls.get_output_device_from_env() or cls.USB_SPEAKER

    @classmethod
    def get_output_device_from_env(cls):
        od = os.environ.get('WOOFER_OUTPUT_DEVICE')
        if not od:
            return None
        elif od.lower() == cls.HEADPHONES:
            return cls.HEADPHONES
        elif od.lower() == cls.USB_SPEAKER:
            return cls.USB_SPEAKER
        else:
            raise NameError(f'Unknown WOOFER_OUTPUT_DEVICE: "{od}" in envirnment. Must be "{cls.HEADPHONES}" or "{cls.USB_SPEAKER}"')

    @classmethod
    def get_speaker(cls, device=None):
        if platform.system() == 'Darwin':
            return cls.DEVICES['mac']['default']
        elif platform.system() == 'Linux':
            if device == cls.USB_SPEAKER:
                return cls.DEVICES['pi'][cls.USB_SPEAKER]
            elif device == cls.HEADPHONES:
                return cls.DEVICES['pi'][cls.HEADPHONES]
            else:
                return cls.DEVICES['pi'][cls.get_default_speaker()]
        else:
            return 'unknown_speaker_due_to_unknown_os'

    @classmethod
    def get_speaker_str(cls, device=None):
        return device and f'{device["device"]}:CARD={device["card"]},DEV={device["dev"]}'

def speaker_type():
    return os.environ.get('WOOFER_SPEAKER_TYPE')

def isWooferSpeaker():
    return speaker_type() and speaker_type().lower() == 'woofer'

def get_default_power():
    return DEFAULT_POWER

def get_min_volume():
    return MIN_VOLUME

def get_max_volume():
    return MAX_VOLUME

def get_default_volume():
    return DEFAULT_VOLUME

def get_limited_volume(volume):
    return get_limited(volume, get_min_volume(), get_max_volume())

def get_limited_frequency(frequency):
    return get_limited(frequency, get_min_frequency(), get_max_frequency())

def get_limited(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

def get_frequency_limits():
    if isWooferSpeaker():
        return FREQUENCY['WOOFER_SPEAKER']
    else:
        return FREQUENCY['NORMAL_SPEAKER']

def get_min_frequency():
    return get_frequency_limits()['MIN_FREQUENCY']

def get_max_frequency():
    return get_frequency_limits()['MAX_FREQUENCY']

def get_default_frequency():
    return get_frequency_limits()['DEFAULT_FREQUENCY']

def get_scaled_volume_limits():
    if isWooferSpeaker():
        return SCALED_VOLUME['WOOFER_SPEAKER']
    else:
        return SCALED_VOLUME['NORMAL_SPEAKER']

def get_min_scaled_volume():
    return get_scaled_volume_limits()['MIN_SCALED_VOLUME']

def get_max_scaled_volume():
    return get_scaled_volume_limits()['MAX_SCALED_VOLUME']

def get_scaled_volume(volume):
    min = get_min_scaled_volume()
    max = get_max_scaled_volume()
    delta = max - min
    scale = delta / 100.0
    return (volume * scale) + min


if __name__ == '__main__':
    sh = SpeakerHelper
    pass