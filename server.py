from flask import Flask, request, jsonify, json
from wooferState import WooferState
from audio_pyo import AudioPyo

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

wooferState = WooferState()
initialState = wooferState.getState()
audio = Audio(
    power=initialState[WooferState.POWER],
    volume=initialState[WooferState.VOLUME],
    frequency=initialState[WooferState.FREQUENCY],)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/woofer')
def woofer():
    return wooferState.getState()

@app.route('/woofer/save_power', methods=['POST'])
def savePower():
    power = getObjectFromRequest(request)[WooferState.POWER]
    wooferState.setPower(power)
    audio.setPower(power)
    return wooferState.getState()

@app.route('/woofer/save_volume', methods=['POST'])
def saveVolume():
    volume = int(getObjectFromRequest(request)[WooferState.VOLUME])
    wooferState.setVolume(volume)
    audio.setVolume(volume)
    return wooferState.getState()

@app.route('/woofer/save_frequency', methods=['POST'])
def saveFrequency():
    frequency = int(getObjectFromRequest(request)[WooferState.FREQUENCY])
    wooferState.setFrequency(frequency)
    audio.setFreq(frequency)
    return wooferState.getState()

def getObjectFromRequest(request):
    return json.loads(request.data.decode())

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)