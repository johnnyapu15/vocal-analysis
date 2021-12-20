from modules.analyser.frameAnalyser.AbstractFrameAnalyser import AbstractFrameAnalyser
import numpy as np
import pyaudio
import time
import librosa

from modules.analyser.struct import AudioFormat


class TestFrameAnalyser(AbstractFrameAnalyser):
    def __init__(self):
        super().__init__()
        print('frame analyser / init ... ')
        self.analyseScale('test')
        self.analyseTone()
        print('frame analyser / loaded')
    def analyseScale(self, test):
        print('frame analyser / analysis scale test')
        return super().analyseScale()
    def analyseTone(self):
        print('frame analyser / analysis tone test')
        return super().analyseTone()
    
class MicFrameAnalyser(AbstractFrameAnalyser):
    def __init__(self, audioFormat: AudioFormat):
        print('frame analyser / init ... ')
        super().__init__(audioFormat)
        print('frame analyser / loaded')
        
    def callback(self, in_data, frame_count, time_info, flag):
        print('frame analyse / callback start')
        scaleResult = self.analyseScale(in_data, frame_count, time_info, flag)
        toneResult = self.analyseTone(in_data, frame_count, time_info, flag)
        return toneResult
        
    def analyseScale(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        librosa.feature.mfcc(numpy_array)
        print(f'{frame_count} during {self.CHUNK / self.RATE}s -> {len(numpy_array)} {time_info}')
        return None, pyaudio.paContinue

    def analyseTone(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        librosa.feature.mfcc(numpy_array)
        print(f'{frame_count} during {self.CHUNK / self.RATE}s -> {len(numpy_array)} {time_info}')
        return None, pyaudio.paContinue