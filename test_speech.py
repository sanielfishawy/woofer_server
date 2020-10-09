import logging
from speech_commands.runner import Runner
from speech_commands.command_interpreter import CommandInterpreter
from speech_commands.command_executor import post_command

class RequestPaths:
    WOOFER_PATH = '/woofer'
    SAVE_POWER_PATH = WOOFER_PATH + '/save_power'
    SAVE_VOLUME_PATH = WOOFER_PATH + '/save_volume'
    SAVE_FREQUENCY_PATH = WOOFER_PATH + '/save_frequency'
    CHANGE_VOLUME_PATH = WOOFER_PATH + '/change_volume'
    CHANGE_FREQUENCY_PATH = WOOFER_PATH + '/change_frequency'

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

if __name__ == '__main__':
    Runner(RequestPaths, StateHelper, '0.0.0.0', '5000').run()
    # ci = CommandInterpreter(RequestPaths, StateHelper)
    # command = ci.interpret_command('volume up three')
    # command and post_command(command)