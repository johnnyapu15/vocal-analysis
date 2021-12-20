from modules.analyser.audioStorer import AudioStorer
from modules.analyser.frameAnalyser.FrameAnalyser import MicFrameAnalyser
from modules.analyser.audioLoader import MicAudioLoader
from modules.analyser.struct import AudioFormat



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
        self.storer = AudioStorer()
        print('audio analyser loaded')
    def start(self):
        self.loader.callback = self.frameAnalyser.callback
        self.loader.start()
    def stop(self):
        self.loader.stop()
