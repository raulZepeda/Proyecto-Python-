#!/usr/bin/python
# -*- coding: utf-8 -*-\

from Tkinter import *
import numpy as np
from scipy.misc import derivative
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import Tkinter
from PIL import Image, ImageTk

class val():
    def __init__(self,U, X):
        self.U = U
        self.X = X

def PedirDatos(v1, v2):
    U = float(v1)
    X = float(v2)
    return val(U, X)





#######################################


# numeric solution with Python

def Linearization(v1, v2):
    sp.init_printing()
    # define symbols
    x,u = sp.symbols(['x','u'])
    # define equation
    dxdt = -x**2 + sp.sqrt(u)

    texto6.set(sp.diff(dxdt,x))
    texto7.set(sp.diff(dxdt,u))
    va = PedirDatos(v1, v2)
    u = va.U
    x = va.X
    def pd_x(x):
        dxdt = -x**2 + np.sqrt(u)
        return dxdt
    def pd_u(u):
        dxdt = -x**2 + np.sqrt(u)
        return dxdt

    texto8.set('Approximate Partial Derivatives')
    texto9.set(derivative(pd_x,x,dx=1e-4))
    texto10.set(derivative(pd_u,u,dx=1e-4))

    texto11.set('Exact Partial Derivatives')
    texto12.set(-x*x) # exact d(f(x,u))/dx
    texto13.set(0.5 / np.sqrt(u)) # exact d(f(x,u))/du



    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(0, 4, 0.25)
    U = np.arange(0, 20, 0.25)
    X, U = np.meshgrid(X, U)
    DXDT = -X**2 + np.sqrt(U)
    LIN = -4.0 * (X-x) + 1.0/8.0 * (U-u)

    # Plot the surface.
    surf = ax.plot_wireframe(X, U, LIN)
    surf = ax.plot_surface(X, U, DXDT, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-10.0, 5.0)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # Add labels
    plt.xlabel('x')
    plt.ylabel('u')

    plt.show()

master = Tk()
master.title("Linearization")


imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('/home/raul/Documentos/Otros/Proyecto/imagenes/Linearization.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(master, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
atras=Tkinter.Button(master, text="back",command=master.quit)
atras.grid(row=0, column=1)

Label(master, text="U").grid(row=1)
Label(master, text="X").grid(row=2)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)


texto6 = StringVar()
texto7 = StringVar()
texto8 = StringVar()
texto9 = StringVar()
texto10 = StringVar()
texto11 = StringVar()
texto12 = StringVar()
texto13 = StringVar()

Label(master, textvariable=texto6).grid(row=6)
Label(master, textvariable=texto7).grid(row=7)
Label(master, textvariable=texto8).grid(row=8)
Label(master, textvariable=texto9).grid(row=9)
Label(master, textvariable=texto10).grid(row=10)
Label(master, textvariable=texto11).grid(row=11)
Label(master, textvariable=texto12).grid(row=12)
Label(master, textvariable=texto13).grid(row=13)

Button(master, text="Calculate", command=lambda: Linearization(v1.get(), v2.get())).grid(row=5)
mainloop()
