import speech_bug.speech_recognition_local as sr

print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0, sample_rate=8000, chunk_size=1024)
recog = sr.Recognizer()

with mic as source:
    audio = recog.listen(source)

with open("voice.wav","wb") as f:
    f.write(audio.get_wav_data())
pass