from tkinter import *
import requests

# URL_api_pokemon: https://pokeapi.co/
# URL_info_amazon: https://www.nozamasol.com/que-es-la-api-de-amazon/
# API KEY: 584cab7a392df8bc3ddaebea0fa97b98
# URL: https://api.openweathermap.org/data/2.5/weather


def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "ºC"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "Intenta de nuevo"


def clima_json(nciudad):
    try:
        API_key = "584cab7a392df8bc3ddaebea0fa97b98"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID": API_key, "q": nciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params=parametros)
        clima = response.json()
        mostrar_respuesta(clima)
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
