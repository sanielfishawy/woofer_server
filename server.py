import os
import logging
import argparse
import sys
from flask import Flask, request, json
import asyncio
from werkzeug.serving import is_running_from_reloader
from woofer_state import WooferState, StateHelper
from audio.audio_helper import get_audio
from speech_commands.runner import Runner as SpeachRunner

logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-9s) %(message)s',)

HOST = '0.0.0.0'

arg_parser = argparse.ArgumentParser(description='Start Woofer server.')
arg_parser.add_argument('-p', '--port',
                        default=80,
                        type=int,
                        help='Port to use for server.',
                        metavar='port',)
PORT = arg_parser.parse_known_args()[0].port

class RequestPaths:
    WOOFER_PATH = '/woofer'
    SAVE_POWER_PATH = WOOFER_PATH + '/save_power'
    SAVE_VOLUME_PATH = WOOFER_PATH + '/save_volume'
    SAVE_FREQUENCY_PATH = WOOFER_PATH + '/save_frequency'
    CHANGE_VOLUME_PATH = WOOFER_PATH + '/change_volume'
    CHANGE_FREQUENCY_PATH = WOOFER_PATH + '/change_frequency'

wooferState = WooferState()
initialState = wooferState.getState()

if not is_running_from_reloader():
    SpeachRunner(RequestPaths, StateHelper, HOST, PORT).run()
    Audio = get_audio()

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route(RequestPaths.WOOFER_PATH)
def woofer():
    return wooferState.getState()

@app.route(RequestPaths.SAVE_POWER_PATH, methods=['POST'])
def savePower():
    power = getObjectFromRequest(request)[StateHelper.POWER_KEY]
    wooferState.setPower(power)
    Audio.setPower(power)
    return wooferState.getState()

@app.route(RequestPaths.SAVE_VOLUME_PATH, methods=['POST'])
def saveVolume():
    volume = int(getObjectFromRequest(request)[StateHelper.VOLUME_KEY])
    wooferState.setVolume(volume)
    Audio.setVolume(wooferState.getVolume())
    return wooferState.getState()

@app.route(RequestPaths.SAVE_FREQUENCY_PATH, methods=['POST'])
def saveFrequency():
    frequency = int(getObjectFromRequest(request)[StateHelper.FREQUENCY_KEY])
    wooferState.setFrequency(frequency)
    Audio.setFrequency(wooferState.getFrequency())
    return wooferState.getState()

@app.route(RequestPaths.CHANGE_VOLUME_PATH, methods=['POST'])
def changeVolume():
    volume = int(getObjectFromRequest(request)[StateHelper.VOLUME_KEY])
    wooferState.changeVolume(volume)
    Audio.setVolume(wooferState.getVolume())
    return wooferState.getState()

@app.route(RequestPaths.CHANGE_FREQUENCY_PATH, methods=['POST'])
def changeFrequency():
    frequency = int(getObjectFromRequest(request)[StateHelper.FREQUENCY_KEY])
    wooferState.changeFrequency(frequency)
    Audio.setFrequency(wooferState.getFrequency())
    return wooferState.getState()

def getObjectFromRequest(request):
    return json.loads(request.data.decode())

if __name__ == '__main__':
    app.run(host= HOST, debug=False, port=PORT)