import matplotlib.pyplot as plt
from numpy import *
class Grafics():
    def __init__(self,string):
        self.n = 10
        self.f=string
    def constructor(self):
        lag = 0.01
        x = arange(-self.n, self.n, lag)
        try:
            y = eval(self.f)
        except Exception:
            return True
        figsize = (10, 10)
        fig = plt.figure(figsize=figsize,dpi=70,)
        plt.plot(x, y)
        plt.title('F(X)')
        plt.ylabel('Y')
        plt.xlabel('X ')

        plt.grid(True)

        plt.savefig('pic.png')