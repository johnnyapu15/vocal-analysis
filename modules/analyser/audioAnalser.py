from queue import Empty
import pyaudio
from modules.analyser.audioStorer import AudioStorer, MicAudioStorer
from modules.analyser.frameAnalyser.FrameAnalyser import MicFrameAnalyser
from modules.analyser.audioLoader import MicAudioLoader
from modules.analyser.structs import AudioFormat

class MicAudioAnalyser:
    def __init__(
        self,
        audioFormat: AudioFormat = None
        ) -> None:
        if audioFormat != None:
            self.audioFormat = audioFormat
        else:
            self.audioFormat = AudioFormat()

        self.loader = MicAudioLoader(self.audioFormat)
        self.frameAnalyser = MicFrameAnalyser(self.audioFormat)
        self.storer = MicAudioStorer()
        print('audio analyser loaded')
    def start(self):
        def callback(in_data, frame_count, time_info, flag):
            next = self.frameAnalyser.analyse(in_data, frame_count, time_info, flag)
            result = self.frameAnalyser.getResults()
            self.storer.push(result)
            return next
        self.loader.callback = callback
        self.loader.start()
    def stop(self):
        self.loader.stop()
    
    def getResult(self):
        try:
            return self.storer.consume()
        except Empty as e:
            return Exception('NO VALUE')