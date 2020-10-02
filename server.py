from flask import Flask, request, jsonify, json
from woofer_state import WooferState, StateHelper
from audio_alsa import AudioAlsa
from audio import Audio
from speech_transcriber import SpeechTranscriber
import asyncio
from werkzeug.serving import is_running_from_reloader

wooferState = WooferState()

initialState = wooferState.getState()
audio = Audio()

if False and not is_running_from_reloader():
    st = SpeechTranscriber()
    st.start()

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/woofer')
def woofer():
    return wooferState.getState()

@app.route('/woofer/save_power', methods=['POST'])
def savePower():
    power = getObjectFromRequest(request)[StateHelper.POWER_KEY]
    wooferState.setPower(power)
    audio.setPower(power)
    return wooferState.getState()

@app.route('/woofer/save_volume', methods=['POST'])
def saveVolume():
    volume = int(getObjectFromRequest(request)[StateHelper.VOLUME_KEY])
    wooferState.setVolume(volume)
    audio.setVolume(volume)
    return wooferState.getState()

@app.route('/woofer/save_frequency', methods=['POST'])
def saveFrequency():
    frequency = int(getObjectFromRequest(request)[StateHelper.FREQUENCY_KEY])
    wooferState.setFrequency(frequency)
    audio.setFreq(frequency)
    return wooferState.getState()

def getObjectFromRequest(request):
    return json.loads(request.data.decode())


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
    pass