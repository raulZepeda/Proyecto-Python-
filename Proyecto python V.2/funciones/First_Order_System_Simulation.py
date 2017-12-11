#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter
from PIL import Image, ImageTk
import time

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from scipy import signal

# Simulate taup * dy/dt = -y + K*u
Kp = 3.0
taup = 2.0

# (1) Transfer Function
num = [Kp]
den = [taup,1]
sys1 = signal.TransferFunction(num,den)
t1,y1 = signal.step(sys1)

# (2) State Space
A = -1.0/taup
B = Kp/taup
C = 1.0
D = 0.0
sys2 = signal.StateSpace(A,B,C,D)
t2,y2 = signal.step(sys2)

# (3) ODE Integrator
def model3(y,t):
    u = 1
    return (-y + Kp * u)/taup
t3 = np.linspace(0,14,100)
y3 = odeint(model3,0,t3)

class First_Order_System_Simulation:
    def __init__(self):
        plt.figure(1)
        plt.plot(t1,y1,'b--',linewidth=3,label='Transfer Fcn')
        plt.plot(t2,y2,'g:',linewidth=2,label='State Space')
        plt.plot(t3,y3,'r-',linewidth=1,label='ODE Integrator')
        plt.xlabel('Time')
        plt.ylabel('Response (y)')
        plt.legend(loc='best')
        plt.show()


imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/First_Order_System_Simulation.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("First Order System Simulation")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)


Label(master, background="SkyBlue3", text="gain (kp)").grid(row=2)
Label(master, background="SkyBlue3", text="time constant (taup)").grid(row=3)

v2 = StringVar()
v3 = StringVar()

e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)


e2.grid(row=2, column=1)
e3.grid(row=3, column=1)




Label(master, background="SkyBlue3", font=(None, 15), text="First Order System Simulation").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate"  , command=lambda: First_Order_System_Simulation()).grid(row=5)
master.mainloop()
