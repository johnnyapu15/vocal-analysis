from queue import Empty
import time

from matplotlib import pyplot as plt
from modules.analyser import MicAudioAnalyser
from modules.analyser.utils.visualizer import Visualizer


analyser = MicAudioAnalyser()
# vis = Visualizer()
# vis.show()

analyser.start()
while (analyser.loader.stream.is_active()): # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
    result = analyser.getResult()
    if not isinstance(result, Exception):
        plt.cla()
        plt.ylim((-1,1))
        plt.plot(result.scale)
        plt.pause(0.0001)
    else:
        print(f'{result}------waiting for analyse... 절취선이얌--------------')
        
