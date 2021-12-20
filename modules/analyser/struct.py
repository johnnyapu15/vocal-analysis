from pyaudio import paFloat32


class AudioFormat:
    def __init__(self, format=paFloat32, channels=1, rate=44100, chunk=1102) -> None:
        self.FORMAT = format
        self.CHANNELS = channels
        self.RATE = rate
        self.CHUNK = chunk
        