#matplot05.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot([1,2,3],[2,4,6])

x=[1,2,3]
y=[4,5,6]

plt.plot(x,y)
plt.title("Our first Graph!", fontdict={"fontname" : "Comic Sans MS", "fontsize" : 20})
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.plot(show)