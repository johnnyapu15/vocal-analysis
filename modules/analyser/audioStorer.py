from modules.analyser.structs import AudioStorerParameters
from queue import Queue

class AudioStorer:
    def __init__(self, audioStorerParameters: AudioStorerParameters = AudioStorerParameters()):
        self.audioStoreParameters = audioStorerParameters
        self.queue = Queue(self.audioStoreParameters.maxStoreLength)
        pass
    
    
class MicAudioStorer(AudioStorer):
    def __init__(self, audioStorerParameters: AudioStorerParameters = AudioStorerParameters()):
        super().__init__(audioStorerParameters=audioStorerParameters)
        
    def push(self, data):
        self.queue.put(data)
        return self.queue
    def consume(self, timeout = 0.025):
        got = self.queue.get(timeout=timeout)
        return got
