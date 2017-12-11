#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter
from PIL import Image, ImageTk
import time

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# tau * dy2/dt2 + 2*zeta*tau*dy/dt + y = Kp*u
Kp = 2.0    # gain
tau = 1.0   # time constant
zeta = 0.25 # damping factor
theta = 0.0 # no time delay
du = 1.0    # change in u

# (1) Transfer Function
num = [Kp]
den = [tau**2,2*zeta*tau,1]
sys1 = signal.TransferFunction(num,den)
t1,y1 = signal.step(sys1)

# (2) State Space
A = [[0.0,1.0],[-1.0/tau**2,-2.0*zeta/tau]]
B = [[0.0],[Kp/tau**2]]
C = [1.0,0.0]
D = 0.0
sys2 = signal.StateSpace(A,B,C,D)
t2,y2 = signal.step(sys2)

# (3) ODE Integrator
def model3(x,t):
    y = x[0]
    dydt = x[1]
    dy2dt2 = (-2.0*zeta*tau*dydt - y + Kp*du)/tau**2
    return [dydt,dy2dt2]
t3 = np.linspace(0,25,100)
x3 = odeint(model3,[0,0],t3)
y3 = x3[:,0]

class Second_Order_System_Simulation:
    def __init__(self):
        plt.figure(1)
        plt.plot(t1,y1*du,'b--',linewidth=3,label='Transfer Fcn')
        plt.plot(t2,y2*du,'g:',linewidth=2,label='State Space')
        plt.plot(t3,y3,'r-',linewidth=1,label='ODE Integrator')
        y_ss = Kp * du
        plt.plot([0,max(t1)],[y_ss,y_ss],'k:')
        plt.xlim([0,max(t1)])
        plt.xlabel('Time')
        plt.ylabel('Response (y)')
        plt.legend(loc='best')
        plt.savefig('2nd_order.png')
        plt.show()

imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/Second_Order_System_Simulation.png')
# modificamos el tamano de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("Second Order System Simulation")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# anadimos un boton para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)

Label(master, background="SkyBlue3", text="gain (Kp = 2.0)").grid(row=1)
Label(master, background="SkyBlue3", text="time constant (tau = 1.0)").grid(row=2)
Label(master, background="SkyBlue3", text="damping factor (zeta = 0.25)").grid(row=3)
Label(master, background="SkyBlue3", text="no time delay (theta = 0.0)").grid(row=4)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)
e4 = Entry(master, textvariable=v4)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)



Label(master, background="SkyBlue3", font=(None, 15), text="Second Order System Simulation").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate"  , command=lambda: Second_Order_System_Simulation()).grid(row=5)
master.mainloop()
