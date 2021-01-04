from tkinter import *
from tkinter import Menu

def About():
    print("Proyecto final de Programación con Python, Gerardo Zúñiga")

#root o master
ventana = Tk()

ventana.title("Aplicacion de Países")
ventana.geometry("320x420")
ventana.option_add('*tearOff',FALSE)
menu=Menu(ventana)
new_item=Menu(menu)
new_item.add_command(label='Agregar Pais')
menu.add_cascade(label='Menu', menu=new_item)
ventana.config(menu=menu)

aboutmenu = Menu(menu)
menu.add_cascade(label="Ayuda", menu=aboutmenu)
aboutmenu.add_command(label="Acerca...", command=About)

ventana.mainloop()