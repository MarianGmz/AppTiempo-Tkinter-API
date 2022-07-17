
from tkinter import *
from tkinter import messagebox
import tkinter
import requests

def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]
        ciudad.grid()
        temperatura.grid()
        descripcion.grid()

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp))+"°C"
        descripcion["text"] = desc
    except Exception as e:
        messagebox.showerror("Error",f"No se indico ninguna ciudad {e}")
def clima_json(ciudad):
    try:
        #Ingrese su api key en esta variable
        API_key =""
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID":API_key,"q":ciudad,"units":"metric","lang":"es"}
        response = requests.get(URL,params=parametros)
        clima = response.json()
    except Exception as e:
        messagebox.showerror("Error","No se indico ninguna ciudad")
    
    
    mostrar_respuesta(clima)



ventana = tkinter.Tk()
ventana.geometry("350x550")
ventana.title("App Clima")
ventana.maxsize(width=350,height=550)
ventana.minsize(width=350,height=550)
ventana.columnconfigure(0,weight=10)
ventana.rowconfigure(1,weight=2)
ventana.rowconfigure(2,weight=2)
ventana.rowconfigure(3,weight=2)
ventana.rowconfigure(4,weight=2)

imagen = PhotoImage(file = "nubes.png")


background = Label(image = imagen, text = "Imagen S.O de fondo")

background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

texto_ciudad = tkinter.Entry(ventana,font=("Courier",15,"normal"),width=25,justify="center",bg="white")
texto_ciudad.grid(column=0,columnspan=2,row=0,pady=20)

imagen_boton = PhotoImage(file = "button_visualizar-clima.png")

obtener_clima = tkinter.Button(ventana,image=imagen_boton,bg="white",bd=1,command=lambda: clima_json(texto_ciudad.get()))
obtener_clima.grid(column=0,row=1,columnspan=1)

ciudad = tkinter.Label(ventana,font=("Courier",20,"normal"))
ciudad.grid(column=0,row=2)
ciudad.grid_remove()


temperatura = tkinter.Label(ventana,font=("Courier",50,"normal"))
temperatura.grid(column=0,row=3)
temperatura.grid_remove()


descripcion = tkinter.Label(ventana,font=("Poplar Std",20,"normal"),background="white")
descripcion.grid(column=0,row=4)
descripcion.grid_remove()




ventana.mainloop()