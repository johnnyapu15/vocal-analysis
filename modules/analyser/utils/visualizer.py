import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes

class Visualizer():
    def __init__(self) -> None:
        plt.ion()
        fig = plt.figure()
        ax : plt.Axes = fig.subplots()
        
        
        self.fig = fig
        self.ax = ax
        pass
    
    def show(self):
        self.fig.show()
    
    def update(self, data):
        self.ax.clear()
        self.ax.plot(data)

    
    