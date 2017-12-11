#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from PIL import Image, ImageTk
imagenAnchuraMaxima=300
imagenAlturaMaxima=200
# abrimos una imagen
img = Image.open('../imagenes/SWODIENT_Problema_1.png')
# modificamos el tamaño de la imagen
img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
root = Tkinter.Tk()
# titulo de la ventana
root.title("Mostrar imagen")
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(root, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima)
label.grid(row=0, column=0)
# añadimos un botón para cerrar
buttonStart2=Tkinter.Button(root, text="Cerrar",command=root.quit)
buttonStart2.grid(row=1, column=0)
# Mostramos la ventana
root.mainloop()
