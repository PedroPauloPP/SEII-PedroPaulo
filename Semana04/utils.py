#funções da dinâmica e Runge-Kutta
import numpy as np
import matplotlib.pyplot as plt

def q_dot(t, q, u):
    
    v = 0.5
    d = 0.75
    tal = 0.5

    x_dot = np.cos(q[2]) * v
    y_dot = np.sin(q[2]) * v
    phi_dot = np.tan(q[3])* v/d
    alf_dot = -tal * q[3] + u;

    qkp1 = np.array([x_dot, y_dot, phi_dot, alf_dot])

    return qkp1


def rk4(tk, h, qk, uk):

    k1 = q_dot(tk, qk, uk)
    k2 = q_dot(tk + h/2, qk + h*k1/2, uk)
    k3 = q_dot(tk + h/2, qk + h*k2/2, uk)
    k4 = q_dot(tk + h, qk + h*k3, uk)

    qkp1 = qk + (h/6)*(k1 + 2*k2 + 2*k3 + k4);
    
    alf_max = 15*np.pi/180;
    qkp1[3] = np.min(np.array([np.max(np.array([qkp1[3],-alf_max])), alf_max]))

    return qkp1


def plota(u, q, t):

    fig1, ax1 = plt.subplots(1,1)
    ax1.plot(q[0,:],q[1,:])
    ax1.set_xlabel('x [m]')
    ax1.set_ylabel('y [m]')
    ax1.set_title('Caminho percorrido')
    fig2, ax2 = plt.subplots(1,1)
    x2 = np.append(t,100.0)
    y2 = q[3,:]*(180/np.pi)
    ax2.plot(x2, y2)
    ax2.set_xlabel('tempo [s]')
    ax2.set_ylabel('alpha [o]')
    ax2.set_title('Ângulo de esterçamento')
    plt.show()