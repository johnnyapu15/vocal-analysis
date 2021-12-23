###
## abstract class test  
# class FrameAnalyser(AbstractFrameAnalyser):
#     def __init__(self):
#         super().__init__()
#         print('frame analyser / init ... ')
#         self.analyseScale('test')
#         self.analyseTone()
#         print('frame analyser / loaded')

#     def analyseScale(self, test):
#         print('frame analyser / analysis scale test')
#         return super().analyseScale()
#     def analyseTone(self):
#         print('frame analyser / analysis tone test')
#         return super().analyseTone()


from abc import abstractmethod

from modules.analyser.structs import AudioAnalysed, AudioFormat

class AbstractFrameAnalyser:
    @abstractmethod
    def __init__(self, audioFormat: AudioFormat = None):
        if audioFormat == None:
            audioFormat = AudioFormat() # use default
        self.FORMAT     = audioFormat.FORMAT  
        self.CHANNELS   = audioFormat.CHANNELS
        self.RATE       = audioFormat.RATE    
        self.CHUNK      = audioFormat.CHUNK   
        self.analysed: AudioAnalysed = None
        return
    @abstractmethod
    def analyseScale(self):
        pass
    @abstractmethod
    def analyseTone(self):
        pass
    @abstractmethod
    def getResults(self):
        return self.analysed
    
  
