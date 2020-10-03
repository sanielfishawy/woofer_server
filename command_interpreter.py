import re
from woofer_state import StateHelper

KEYWORDS = [
    'volume',
    'frequency',
    'power',
]

NUMBER_WORDS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
}

NUMBER_REGEX = re.compile('\d+')
UP_DOWN_REGEX = re.compile(r'\bup\b|\bdown\b')
ON_OFF_REGEX = re.compile(r'\bon\b|\boff\b')

def preprocess(txt):
    return txt.lower()

def interpret_command(txt):
    txt = preprocess(txt)
    kwd = get_keyword(txt)
    if kwd:
        if kwd == 'power':
            path = 'save_power'
            on_off = get_on_off(txt)
            if on_off == 'on':
                return get_path_payload_dict(path, {StateHelper.POWER_KEY:True})
            elif on_off == 'off':
                return get_path_payload_dict(path, {StateHelper.POWER_KEY:False})
            else:
                return None

        elif kwd == 'volume':
            num = get_number(txt)
            up_down = get_up_down(txt)

            if not num and not up_down:
                return None
            elif not num and up_down:
                num = 10

            if not up_down:
                return get_path_payload_dict('save_volume', {StateHelper.VOLUME_KEY: num})
            elif up_down == 'up':
                return get_path_payload_dict('change_volume', {StateHelper.VOLUME_KEY: num})
            elif up_down == 'down':
                return get_path_payload_dict('change_volume', {StateHelper.VOLUME_KEY: -num})

        elif kwd == 'frequency':
            num = get_number(txt)
            up_down = get_up_down(txt)

            if not num and not up_down:
                return None
            elif not num and up_down:
                num = 10

            if not up_down:
                return get_path_payload_dict('save_frequency', {StateHelper.FREQUENCY_KEY: num})
            elif up_down == 'up':
                return get_path_payload_dict('change_frequency', {StateHelper.FREQUENCY_KEY: num})
            elif up_down == 'down':
                return get_path_payload_dict('change_frequency', {StateHelper.FREQUENCY_KEY: -num})
    return None

def get_path_payload_dict(path, payload):
    return {'path': path, 'payload':payload}

def get_keyword(txt):
    for kwd in KEYWORDS:
        if kwd in txt:
            return kwd
    return False

def get_number(txt):
    for word in NUMBER_WORDS:
        if word in txt:
            return NUMBER_WORDS[word]
    match = NUMBER_REGEX.search(txt)
    return match and int(match.group())

def get_up_down(txt):
    match = UP_DOWN_REGEX.search(txt)
    return match and match.group().strip()

def get_on_off(txt):
    match = ON_OFF_REGEX.search(txt)
    return match and match.group().strip()

if __name__ == '__main__':
    print(get_number('lkjasdf ljsadlj 567 asdflj 56'))
    print(get_number('lkj zero ljsadlj 567 asdflj 56'))
    print(get_number('lkj foo bar'))
    print(get_up_down('frequency down 10'))
    print(get_on_off('power on'))