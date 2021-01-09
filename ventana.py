import tkinter as tk
from tkinter import Menu
import requests

def About():
    print("Proyecto final de Programación con Python, Gerardo Zúñiga")

def mostrar_pais():
    response = requests.get("http://localhost:5000/pais/")
    
    data = response.json()

    textwidget = tk.Text()
    textwidget.insert(tk.END, data)
    textwidget.grid(row=1, column=0, sticky="WE", padx=3, pady=3)

def mostrar_ciudad():
    response = requests.get("http://localhost:5000/ciudad/")
    text_response = response.text

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=5, column=0, sticky="WE", padx=3, pady=3)

def mostrar_lider():
    response = requests.get("http://localhost:5000/lider-pais/")
    text_response = response.text

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=5, column=0, sticky="WE", padx=3, pady=3)
    
def Agregar_Pais_Vent():
     ventAgregarPais = tk.Tk()
     ventAgregarPais.geometry("400x300")
     ventAgregarPais.title("Agregar País")
    
     
     ventAgregarPais.mainloop()



def Agregar_Pais():

    pais_label = tk.Label( text="Digite el nombre del país")
    pais_label.grid(row=1, column=0, sticky="WE", padx=10)

    pais_input = tk.Entry()
    pais_input.grid(row=2, column=0, sticky="WE", padx=10)

    user_input = pais_input.get()
    payload = {"id": id, "nombre": user_input}
    response = requests.post("http://localhost:5000/pais/", params=payload)

    pais_button = tk.Button(text="Agregar", command=Agregar_Pais)
    pais_button.grid(row=2, column=1, sticky="WE", padx=10, pady=10)



def Agregar_Ciudad():
    response = requests.get("http://localhost:5000/ciudad/")
    text_response = response.text

def Agregar_Lider():
    response = requests.get("http://localhost:5000/Lider/")
    text_response = response.text

def Modificar_Pais():
    response = requests.put("http://localhost:5000/Pais/<string:id>/")
    text_response = response.text

def Modificar_Ciudad():
    response = requests.put("http://localhost:5000/Ciudad/<string:id>/")
    text_response = response.text

def Modificar_Lider():
    response = requests.put("http://localhost:5000/Lider/<string:id>/")
    text_response = response.text

def Borrar_Pais():
    response = requests.delete("http://localhost:5000/Pais/<string:id>/")
    text_response = response.text

def Borrar_Ciudad():
    response = requests.delete("http://localhost:5000/Ciudad/<string:id>/")
    text_response = response.text

def Borrar_Lider():
    response = requests.delete("http://localhost:5000/Lider/<string:id>/")
    text_response = response.text

#root o master
ventana = tk.Tk()

ventana.title("Aplicacion de Países")
ventana.geometry("650x420")
#ventana.option_add('*tearOff',FALSE)
menu=Menu(ventana)
mnuMostrar=Menu(menu)
mnuEdicion=Menu(menu)
mnuMostrar.add_command(label='Mostrar Países', command=mostrar_pais)
mnuMostrar.add_command(label='Mostrar Ciudades', command=mostrar_ciudad)
mnuMostrar.add_command(label='Mostrar Líderes', command=mostrar_lider)
menu.add_cascade(label='Datos', menu=mnuMostrar)
mnuEdicion.add_command(label='Agregar País', command=Agregar_Pais)
mnuEdicion.add_command(label='Agregar Ciudad', command=Agregar_Ciudad)
mnuEdicion.add_command(label='Agregar Líder', command=Agregar_Lider)
mnuEdicion.add_separator()
mnuEdicion.add_command(label='Modificar País', command=Modificar_Pais)
mnuEdicion.add_command(label='Modificar Ciudad', command=Modificar_Ciudad)
mnuEdicion.add_command(label='Modificar Líder', command=Modificar_Lider)
mnuEdicion.add_separator()
mnuEdicion.add_command(label='Borrar País', command=Borrar_Pais)
mnuEdicion.add_command(label='Borrar Ciudad', command=Borrar_Ciudad)
mnuEdicion.add_command(label='Borrar Líder', command=Borrar_Lider)
menu.add_cascade(label='Edición', menu=mnuEdicion)
ventana.config(menu=menu)

aboutmenu = Menu(menu)
menu.add_cascade(label="Ayuda", menu=aboutmenu)
aboutmenu.add_command(label="Acerca...", command=About)

ventana.mainloop()