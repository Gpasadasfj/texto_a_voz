"""Este script recibe una URL de un artículo de noticias y lo convierte en audio."""

import tkinter as tk  # Modulo para la interfaz gráfica
from newspaper import Article  # Modulo para extraer el texto de la URL
from gtts import gTTS  # Modulo para convertir texto a voz
from playsound import playsound  # Módulo para reproducir el audio
import os  # Modulo para eliminar el audio.mp3


# Crear la interfaz gráfica
class Ventana:
    def crear_ventana(self) -> None:  # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Texto a Voz")
        self.ventana.geometry("500x500")

        # Texto para indicar que introduzla la URL
        txt = tk.Label(self.ventana, text="Introduzca URL: ")
        txt.pack()

        # Campo de texto para introducir la URL
        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        # Boton para confirmar la URL
        self.get_url = tk.Button(
            self.ventana, text="Confirmar", command=self.procesar_url
        )
        self.get_url.pack()

        # Boton para reproducir audio
        audio_btn = tk.Button(
            self.ventana, text="Reproducir audio", command=self.reproducir_audio
        )
        audio_btn.pack()

    # Procesar la URL introducida por el usuario
    def procesar_url(self):
        self.url = self.entrada.get()
        articulo = Articulo(self.url)
        self.titulo = articulo.extraer_titulo()
        self.contenido = articulo.extraer_texto()

    # Reproducir el texto del artículo
    def reproducir_audio(self):
        audio_texto = Audio(self.titulo + self.contenido, "audio_texto.mp3")
        audio_texto.reproducir_audio()

    # Iniciar la interfaz gráfica
    def iniciar_ventana(self) -> None:
        self.ventana.mainloop()


# Extraer información de la URL
class Articulo:
    def __init__(self, url):
        self.url = url

        # Crear un objeto Article
        self.articulo = Article(url, languaje="es")

        # Descargar y analizar el artículo
        self.articulo.download()
        self.articulo.parse()

    # Extraer el titulo del artículo
    def extraer_titulo(self):
        self.titulo = self.articulo.title
        return self.titulo

    # Extraer el texto del artículo
    def extraer_texto(self):
        self.texto = self.articulo.text[:1000]
        return self.texto


# Clase para crear el audio
class Audio:
    def __init__(self, texto, filename):
        self.audio_file = filename
        tts = gTTS(text=texto, lang="es")  # Crear objeto tts en español
        tts.save(self.audio_file)  # Guardar el audio en un archivo mp3

    def reproducir_audio(self):  # Reproducir el audio guardado
        playsound(self.audio_file)
        os.remove(self.audio_file)  # Eliminar el audio al acabar de reproducirlo


ventana = Ventana()  # Crear una instancia de la clase Ventana
ventana.crear_ventana()  # Crear la ventana principal
ventana.iniciar_ventana()  # Iniciar la interfaz gráfica
