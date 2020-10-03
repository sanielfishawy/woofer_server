import  speech_recognition as sr
from threading import Thread
import logging
import command_interpreter as CI

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class SpeechTranscriber(Thread):

    MIC_INDEX = 0

    def __init__(self):
        super(self.__class__, self).__init__()
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = False
        self.recognizer.energy_threshold = 400
        self.recognizer.pause_threshold = 0.5
        self.mic = sr.Microphone(device_index=self.__class__.MIC_INDEX)

    def capture_audio(self):
        audio = None
        with self.mic as source:
            logging.debug(f'energy threshold {self.recognizer.energy_threshold}')
            logging.debug('listening...')
            audio = self.recognizer.listen(source)
        return audio

    def get_text_from_audio(self, audio):
        logging.debug('processing...')
        response = {'success': False}
        try:
            response['transcript'] =  self.recognizer.recognize_google(audio)
            response['success'] = True
        except sr.RequestError as err:
            response['error'] = f'Api not available: {err}'
        except sr.UnknownValueError as err:
            response['error'] = f'Unrecognized speech: {err}'
        return response

    def run(self):
        while True:
            audio = self.capture_audio()
            resp = self.get_text_from_audio(audio)
            if resp['success']:
                logging.debug('\033[92m' + resp['transcript'] + '\033[0m')
                command = CI.interpret_command(resp['transcript'])
                command and logging.debug(command)
            else:
                logging.debug(resp['error'])

if __name__ == '__main__':
    sc = SpeechTranscriber()
    sc.run()