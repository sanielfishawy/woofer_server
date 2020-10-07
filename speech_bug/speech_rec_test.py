import platform
import speech_bug.speech_recognition_local as sr

I_TALK = 0
PULSE = 2

device_index = PULSE

print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=device_index, sample_rate=44100, chunk_size=1024)
recog = sr.Recognizer()
recog.dynamic_energy_threshold = False
recog.energy_threshold = 1500
recog.pause_threshold = 0.5

print('listening')
with mic as source:
    audio = recog.listen(source)

with open("voice.wav","wb") as f:
    f.write(audio.get_wav_data())
pass