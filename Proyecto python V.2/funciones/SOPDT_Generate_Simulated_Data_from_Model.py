#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import time
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk
from scipy.optimize import minimize
from scipy.interpolate import interp1d


# define process model (to generate process data)
def process(y,t,n,u,Kp,taup):
    # arguments
    #  y[n] = outputs
    #  t    = time
    #  n    = order of the system
    #  u    = input value
    #  Kp   = process gain
    #  taup = process time constant

    # equations for higher order system
    dydt = np.zeros(n)
    # calculate derivative
    dydt[0] = (-y[0] + Kp * u)/(taup/n)
    for i in range(1,n):
       dydt[i] = (-y[i] + y[i-1])/(taup/n)
    return dydt

# specify number of steps
ns = 50
# define time points
t = np.linspace(0,40,ns+1)
delta_t = t[1]-t[0]
# define input vector
u = np.zeros(ns+1)
u[5:20] = 1.0
u[20:30] = 0.1
u[30:] = 0.5

# use this function or replace yp with real process data
def sim_process_data():
    # higher order process
    n=10       # order
    Kp=3.0    # gain
    taup=5.0   # time constant
    # storage for predictions or data
    yp = np.zeros(ns+1)  # process
    for i in range(1,ns+1):
        if i==1:
            yp0 = np.zeros(n)
        ts = [delta_t*(i-1),delta_t*i]
        y = odeint(process,yp0,ts,args=(n,u[i],Kp,taup))
        yp0 = y[-1]
        yp[i] = y[1][n-1]
    return yp
yp = sim_process_data()

# Construct results and save data file
# Column 1 = time
# Column 2 = input
# Column 3 = output
data = np.vstack((t,u,yp)) # vertical stack
data = data.T              # transpose data
np.savetxt('data.txt',data,delimiter=',')
class SOPDT_Generate_Simulated_Data_from_Model:
    def __init__(self):
        # plot results
        plt.figure()
        plt.subplot(2,1,1)
        plt.plot(t,yp,'kx-',linewidth=2,label='Output')
        plt.ylabel('Output Data')
        plt.legend(loc='best')
        plt.subplot(2,1,2)
        plt.plot(t,u,'bx-',linewidth=2)
        plt.legend(['Input'],loc='best')
        plt.ylabel('Input Data')
        plt.show()

imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/SOPDT_Generate_Simulated_Data_from_Model.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
master = Tkinter.Tk()
master.configure(background="SkyBlue3")
# titulo de la ventana
master.title("SOPDT Generate Simulated Data from Model")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, background="SkyBlue3",  image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, background="DodgerBlue2", text="back",command=master.quit)
atras.grid(row=0, column=1)

Label(master, background="SkyBlue3", text="order (n)").grid(row=1)
Label(master, background="SkyBlue3", text="gain (kp)").grid(row=2)
Label(master, background="SkyBlue3", text="time constant (taup)").grid(row=3)
Label(master, background="SkyBlue3", text="number steps (ns)").grid(row=4)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
e3 = Entry(master, textvariable=v3)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)



Label(master, background="SkyBlue3", font=(None, 15), text="SOPDT Generate Simulated Data from Model").place(relx=0.5, rely=0.03, anchor=CENTER)
Button(master, background="DodgerBlue2", text="Calculate" , command=lambda: SOPDT_Generate_Simulated_Data_from_Model()).grid(row=5)
master.mainloop()
