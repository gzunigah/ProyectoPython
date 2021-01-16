import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import requests
import json

def About():
    print("Proyecto final de Programación con Python, Gerardo Zúñiga")

def Mostrar_Pais():
    response = requests.get("http://localhost:5000/pais/")
    text_response = response.text
    data = json.loads(text_response)

    textwidget = tk.Text()
  
    textwidget.insert(tk.END, data)
    textwidget.grid(row=5, column=0, sticky="WE", padx=3, pady=3)

def Mostrar_Ciudad():
    response = requests.get("http://localhost:5000/ciudad/")
    text_response = response.text

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=5, column=0, sticky="WE", padx=3, pady=3)

def Mostrar_Lider():
    response = requests.get("http://localhost:5000/lider-pais/")
    text_response = response.text

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=5, column=0, sticky="WE", padx=3, pady=3)

def Agregar_Pais(nombre, cod_iso):

    payload = { "nombre": nombre, "cod_iso": cod_iso }
    response = requests.post("http://localhost:5000/pais/", headers={ 'Content-Type': 'application/json' } , data=json.dumps(payload))
    
def Agregar_Pais_Vent():
     ventAgregarPais = tk.Tk()
     ventAgregarPais.geometry("400x300")
     ventAgregarPais.title("Agregar País")
     
     Pais_Label = tk.Label(ventAgregarPais, text="Digite el nombre del país")
     Cdo_Iso_Label = tk.Label(ventAgregarPais, text= "Código ISO")
     Pais_Label.grid(row=2, column=0, sticky="WE", padx=10)
     Cdo_Iso_Label.grid(row=1, column=0, padx=10)
     
     input_nombre = tk.Entry(ventAgregarPais)
     input_nombre.grid(row=2, column=1, sticky="WE", padx=10)
     pais = input_nombre.get()

     input_cod = tk.Entry(ventAgregarPais)
     input_cod.grid(row=1, column=1, padx=10)
     cod_iso = input_cod.get()
     # pais = "Polonia"
     # cod_iso = "pl"
     Pais_Button = tk.Button(ventAgregarPais, text="Agregar", command=lambda: Agregar_Pais(input_nombre.get(), input_cod.get()))
     Pais_Button.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
     
     ventAgregarPais.mainloop()


def Agregar_Ciudad(nombre, pais, capital):

    payload = {"nombre": nombre, "pais": pais, "capital": capital }
    response = requests.post("http://localhost:5000/ciudad/", headers={ 'Content-Type': 'application/json' } , data=json.dumps(payload))
    
    
def Agregar_Ciudad_Vent():
    ventAgregarCiudad = tk.Tk()
    ventAgregarCiudad.geometry("400x300")
    ventAgregarCiudad.title("Agregar Ciudad")

    Ciudad_Label = tk.Label(ventAgregarCiudad, text="Digite el nombre de la Ciudad")
    Pais_Label = tk.Label(ventAgregarCiudad, text= "Id Pais")
    Ciudad_Label.grid(row=1, column=0, sticky="W", padx=10)
    Pais_Label.grid(row=3, column=0, sticky="E", padx=10)
     
    input_Ciudad = tk.Entry(ventAgregarCiudad)
    input_Ciudad.grid(row=1, column=1, sticky="W", padx=10)
    nombre = input_Ciudad.get()

    input_Pais = tk.Entry(ventAgregarCiudad)
    input_Pais.grid(row=3, column=1, sticky="W", padx=10)
    pais = input_Pais.get()

    Boolean_var = tk.BooleanVar(ventAgregarCiudad)
    Checkbutton = ttk.Checkbutton(ventAgregarCiudad, text="Marque si es Capital", variable=Boolean_var)
    Checkbutton.grid(row=2, sticky="SE")
    capital = Boolean_var.get()

    Ciudad_Button = tk.Button(ventAgregarCiudad, text="Agregar", command=lambda: Agregar_Ciudad(input_Ciudad.get(), input_Pais.get(), Boolean_var.get() ))
    Ciudad_Button.grid(row=4, column=0, sticky="WE", padx=10, pady=10)
    print(capital, nombre, pais)
    ventAgregarCiudad.mainloop()


def Agregar_Lider():

    payload = {"nombre": nombre, "pais": pais, "capital": capital }
    response = requests.post("http://localhost:5000/lider/", headers={ 'Content-Type': 'application/json' } , data=json.dumps(payload))
    

def Modificar_Pais():
    response = requests.put("http://localhost:5000/Pais/<string:id>/")
    text_response = response.text

def Modificar_Ciudad():
    response = requests.put("http://localhost:5000/Ciudad/<string:id>/")
    text_response = response.text

def Modificar_Lider():
    response = requests.put("http://localhost:5000/Lider/<string:id>/")
    text_response = response.text

def Borrar_Pais(id):
    payload = {"id": id }
    response = requests.delete("http://localhost:5000/Pais/<string:id>", headers={ 'Content-Type': 'application/json' } , data=json.dumps(payload))

def Borrar_Pais_Vent():
     VentBorrarPais = tk.Tk()
     VentBorrarPais.geometry("400x300")
     VentBorrarPais.title("Borrar País")
     
     Pais_Label = tk.Label(VentBorrarPais, text="Digite el id del país")
     #Cdo_Iso_Label = tk.Label(VentBorrarPais, text= "Código ISO")
     Pais_Label.grid(row=2, column=0, sticky="WE", padx=10)
     #Cdo_Iso_Label.grid(row=1, column=0, padx=10)
     
     input_id = tk.Entry(VentBorrarPais)
     input_id.grid(row=2, column=1, sticky="WE", padx=10)
     pais = input_id.get()

     Pais_Button = tk.Button(VentBorrarPais, text="Borrar", command=lambda: Borrar_Pais(input_id.get()))
     Pais_Button.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
     
     VentBorrarPais.mainloop()

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
mnuMostrar.add_command(label='Mostrar Países', command=Mostrar_Pais)
mnuMostrar.add_command(label='Mostrar Ciudades', command=Mostrar_Ciudad)
mnuMostrar.add_command(label='Mostrar Líderes', command=Mostrar_Lider)
menu.add_cascade(label='Datos', menu=mnuMostrar)
mnuEdicion.add_command(label='Agregar País', command=Agregar_Pais_Vent)
mnuEdicion.add_command(label='Agregar Ciudad', command=Agregar_Ciudad_Vent)
mnuEdicion.add_command(label='Agregar Líder', command=Agregar_Lider)
mnuEdicion.add_separator()
mnuEdicion.add_command(label='Modificar País', command=Modificar_Pais)
mnuEdicion.add_command(label='Modificar Ciudad', command=Modificar_Ciudad)
mnuEdicion.add_command(label='Modificar Líder', command=Modificar_Lider)
mnuEdicion.add_separator()
mnuEdicion.add_command(label='Borrar País', command=Borrar_Pais_Vent)
mnuEdicion.add_command(label='Borrar Ciudad', command=Borrar_Ciudad)
mnuEdicion.add_command(label='Borrar Líder', command=Borrar_Lider)
menu.add_cascade(label='Edición', menu=mnuEdicion)
ventana.config(menu=menu)

aboutmenu = Menu(menu)
menu.add_cascade(label="Ayuda", menu=aboutmenu)
aboutmenu.add_command(label="Acerca...", command=About)

ventana.mainloop()