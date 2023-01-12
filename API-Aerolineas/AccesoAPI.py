from tkinter import *
import requests


def mostrar_respuesta(mensaje):
    try:
        texto = mensaje["text"]

        ciudad["text"] = texto
    except:
        ciudad["text"] = "Intenta de nuevo"


def clima_json(name):
    try:
        url = "/Iberia-sample-api"
        parametros = {"name": name}
        response = requests.get(url, params=parametros)
        mensaje = response.json()
        mostrar_respuesta(mensaje)
    except:
        print("Error")


app = Tk()
app.geometry("350x550")

texto_ciudad = Entry(app, font=("Courier", 20, "normal"), justify="center")
texto_ciudad.pack(padx=30, pady=30)

obtener_clima = Button(app, text="Obtener Clima", font=("Courier", 20, "normal"), command=lambda:
clima_json(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font=("Courier", 20, "normal"))
ciudad.pack(padx=20, pady=20)

temperatura = Label(font=("Courier", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(font=("Courier", 20, "normal"))
descripcion.pack(padx=10, pady=10)

app.mainloop()
