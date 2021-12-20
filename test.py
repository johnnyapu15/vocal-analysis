import time
from modules.analyser import MicAudioAnalyser


analyser = MicAudioAnalyser()

analyser.start()
while (analyser.loader.stream.is_active()): # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
    time.sleep(2.0)
analyser.stop()