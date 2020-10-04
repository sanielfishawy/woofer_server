import  speech_recognition as sr
from threading import Thread
import logging


class SpeechTranscriber(Thread):

    MIC_INDEX = 0

    def __init__(
            self,
            callback=None,
        ):
        super(self.__class__, self).__init__()
        self.callback = callback
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
        response = Response(success=False)
        try:
            response.transcript =  self.recognizer.recognize_google(audio)
            response.success = True
        except sr.RequestError as err:
            response.error = 'Api not available'
        except sr.UnknownValueError as err:
            response.error = 'Unrecognized speech'
        return response

    def run(self):
        while True:
            audio = self.capture_audio()
            resp = self.get_text_from_audio(audio)
            if resp.success:
                txt = resp.transcript
                logging.debug('\033[92m' + txt + '\033[0m')
                self.callback and self.callback(txt)
                # command = CI.interpret_command(resp['transcript'])
                # command and logging.debug(command)
            else:
                logging.error(resp.error)


class Response():

    def __init__(
            self,
            success=None,
            error=None,
            transcript=None,
    ):
        self.success = success
        self.error = error
        self.transcript = transcript


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
    sc = SpeechTranscriber()
    sc.run()