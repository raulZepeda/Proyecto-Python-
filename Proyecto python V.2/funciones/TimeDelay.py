#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk


class val():
    def __init__(self, kp, taup, thetap):
        self.kp = kp
        self.taup = taup
        self.thetap = thetap

def PedirDatos(kp, taup, thetap):
    kp = int(kp)
    taup = int(taup)
    thetap = int(thetap)
    return val(kp, taup, thetap)
va = PedirDatos(0, 0, 0)



# specify number of steps
ns = 100
# define time points
t = np.linspace(0,ns/10.0,ns+1)

class model(object):
    # process model
    Kp = 2.0
    taup = 200.0
    thetap = 0.0

def process(y,t,u,Kp,taup):
    # Kp = process gain
    # taup = process time constant
    dydt = -y/taup + Kp/taup * u
    return dydt

def calc_response(t,m):
    # t = time points
    # m = process model
    Kp = m.Kp
    taup = m.taup
    thetap = m.thetap
    # specify number of steps
    ns = len(t)-1

    delta_t = t[1]-t[0]

    # storage for recording values
    op = np.zeros(ns+1)  # controller output
    pv = np.zeros(ns+1)  # process variable

    # step input
    op[10:]=2.0

    # Simulate time delay
    ndelay = int(np.ceil(thetap / delta_t))

    # loop through time steps
    for i in range(0,ns):
        # implement time delay
        iop = max(0,i-ndelay)
        y = odeint(process,pv[i],[0,delta_t],args=(op[iop],Kp,taup))
        pv[i+1] = y[-1]
    return (pv,op)
def TimeDelay(kp, taup, thetap):
    va1 = PedirDatos(kp, taup, thetap)
    va.kp = va1.kp
    va.taup = va1.taup
    va.thetap = va1.thetap

    # calculate step response
    model.Kp = va.kp
    model.taup = va.taup
    model.thetap = va.thetap
    (pv,op) = calc_response(t,model)

    pv2 = np.zeros(len(t))
    for i in range(len(t)):
        pv2[i] = model.Kp * (1.0 - np.exp(-(t[i]-model.thetap-1.0)/model.taup))*2.0

    pv3 = np.zeros(len(t))
    for i in range(len(t)):
        pv3[i] = model.Kp * (1.0 - np.exp(-(t[i]-1.0)/model.taup))*2.0

    plt.figure(1)

    plt.subplot(2,1,1)
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    plt.plot(t,pv3,'r--',linewidth=1,label=r'$y(t)$')
    plt.plot(t,pv2,'k.-',linewidth=2,label=r'$y(t-\theta_p)$')
    plt.plot([0,4,4.0001,10],[0,0,1,1],'g:',linewidth=3,label=r'$S(t- \theta _p)$')
    plt.plot(t,pv,'b-',linewidth=4,label=r'$x(t)$')
    plt.legend(loc='best')
    plt.ylabel('Process Output')
    plt.ylim([-4,5])

    plt.subplot(2,1,2)
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    plt.plot(t,op,'r-',linewidth=3,label=r'$u(t)$')
    plt.plot(t+3.0,op,'k--',linewidth=3,label=r'$u(t-\theta_p)$')
    plt.ylim([-0.1,2.1])
    plt.xlim([0,10])
    plt.legend(loc='best')
    plt.ylabel('Process Input')

    plt.xlabel('Time')

    plt.savefig('output.png')
    plt.show()



imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/TimeDelay.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("Time Delay")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, background="SkyBlue3", text="Kp").grid(row=2)
Label(master, background="SkyBlue3", text="taup").grid(row=3)
Label(master, background="SkyBlue3", text="theta_p").grid(row=4)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)
Label(master, background="SkyBlue3", font=(None, 15), text="Time Delay").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: TimeDelay(v1.get(), v2.get(), v3.get())).grid(row=5)
master.mainloop()
