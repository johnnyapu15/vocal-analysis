from pyaudio import paFloat32


class AudioFormat:
    def __init__(self, format=paFloat32, channels=1, rate=44100, chunk=1102) -> None:
        self.FORMAT = format
        self.CHANNELS = channels
        self.RATE = rate
        self.CHUNK = chunk
        
class AudioStorerParameters:
    def __init__(self, audioFormat = AudioFormat(), maxStoreLength = 100) -> None:
        self.audioFormat = audioFormat
        self.maxStoreLength = maxStoreLength
        
class AudioAnalysed:
    def __init__(self, analysedScale= None, analysedTone= None) -> None:
        self.scale = analysedScale
        self.tone = analysedTone
    
    def __repr__(self) -> str:
        return f"[SCALE] {self.scale} \n[TONE] {self.tone}"