# Convertidor de Artículos de Noticias a Audio

Este script convierte un artículo de noticias, dado su enlace URL, en un archivo de audio utilizando tecnología de síntesis de voz.

### Funcionalidades:
- Permite al usuario ingresar una URL de un artículo de noticias.
- Extrae el texto y título del artículo.
- Convierte el texto en un archivo de audio en formato `.mp3`.
- Reproduce el audio generado con el texto del artículo.

### Requisitos:
Este proyecto requiere las siguientes bibliotecas de Python:

- `tkinter` (para la interfaz gráfica de usuario).
- `newspaper3k` (para extraer contenido de la URL).
- `gTTS` (para convertir el texto en audio).
- `playsound` (para reproducir el archivo de audio).
- `os` (para manejar el archivo de audio temporal).

Para instalar las dependencias, ejecuta el siguiente comando:

```bash
pip install tkinter newspaper3k gTTS playsound
```
Uso:
Ejecuta el script en tu entorno de desarrollo.

Introduce la URL del artículo de noticias en el campo correspondiente.

Haz clic en "Confirmar" para procesar la URL.

Haz clic en "Reproducir audio" para escuchar el artículo convertido en voz.

# Descripción del Código:
### Interfaz Gráfica (tkinter):

Se utiliza para permitir al usuario ingresar una URL y controlar el proceso de conversión y reproducción de audio.

### Extracción de Contenido (newspaper3k):

La clase Articulo se encarga de descargar y analizar el artículo desde la URL proporcionada, extrayendo el título y el texto del artículo.

### Conversión a Audio (gTTS):

El texto extraído del artículo se convierte a voz utilizando la librería gTTS (Google Text-to-Speech) y se guarda en un archivo .mp3.

### Reproducción de Audio (playsound):

El archivo .mp3 generado se reproduce, y una vez finalizado, se elimina automáticamente.

### Autor: 
Francisco Javier García Pasadas
[Gpasadas](https://github.com/Gpasadasfj)
