# ref: https://stackoverflow.com/questions/59056786/python-librosa-with-microphone-input

import numpy as np
import pyaudio
import time
import librosa

class AudioHandler(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1102
        self.p = None
        self.stream = None

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)
    

    def stop(self):
        self.stream.close()
        self.p.terminate()
    # CHUNK / RATE 만큼의 시간마다 콜백이 실행된다.
    # 만약 25ms마다 실행하고 싶다면 CHUNK / 44100 = 0.025 =: CHUNK = 1102.5
    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        librosa.feature.mfcc(numpy_array)
        print(f'{frame_count} during {self.CHUNK / self.RATE}s -> {len(numpy_array)} {time_info}')
        return None, pyaudio.paContinue

    def mainloop(self):
        while (self.stream.is_active()): # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
            time.sleep(2.0)


audio = AudioHandler()
audio.start()     # open the the stream
audio.mainloop()  # main operations with librosa
audio.stop()