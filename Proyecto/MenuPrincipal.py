#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import os
import time
def Ejecutar():
    funcion()
    os.system('python ~/Documentos/Otros/Proyecto/funciones/'+combo.get()+'.py')
    funcion2()

def funcion():
    master.withdraw()
def funcion2():
    master.deiconify()
master = tk.Tk()

combo = ttk.Combobox(master, state="readonly")
combo.grid(row=0, column=0)
combo['values']= ('SolveWithODEINT','BalanceEquations','Linearization','FirstOrder','LaplaceTransforms','StateSpace','SecondOrder','SimulateTF_SS_ODE')
combo.current(0)
master.title("Menu Principal")
master.geometry("300x200+10+10")
tk.Button(master, text="Execute", command=lambda: Ejecutar()).grid(row=0, column=2)
tk.mainloop()
