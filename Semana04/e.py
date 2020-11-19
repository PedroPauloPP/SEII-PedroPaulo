#e
from utils import *

# condições iniciais
q = np.array([[0], [0], [0*np.pi/180], [0*np.pi/180]])

# run
h = 0.1
t = np.arange(0, 100.2, h)

for k, val in enumerate(t, start = 1):
    u = 5*np.sin(2*np.pi*0.1*t[k-1])*np.pi/180
    q = np.c_[q, rk4(t[k-1], h, q[:,k-1], u)]

plota(u, q, t)