import os
import json
import requests
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from dibuja import dibujar_figuras  # Importar la función desde dibuja.py

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
api_key = os.getenv("API_KEY")

# Inicializar la aplicación Flask
app = Flask(__name__)

# Asegurarnos de que existe el directorio 'static' para las imágenes generadas
if not os.path.exists('static'):
    os.makedirs('static')

# Función para obtener el clima de una ciudad usando la API de OpenWeatherMap
def obtener_clima(api_key, ciudad):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        clima = respuesta.json()
        icono = clima['weather'][0]['icon']  # Obtén el código del ícono
        return clima, icono
    else:
        return None, None


# Generar la imagen del clima con el icono correspondiente
def generar_imagen_clima(clima_data, ciudad, icono):
    temperatura = clima_data['main']['temp']
    descripcion = clima_data['weather'][0]['description']

    # Crear una nueva imagen con fondo blanco
    with Image(width=400, height=300, background=Color('white')) as img:
        # Llamamos a la función de dibujar figuras pasando el icono
        dibujar_figuras(img, icono)

        # Establecer la fuente y el tamaño del texto
        with Drawing() as draw:
            draw.font_size = 20
            draw.fill_color = Color('black')  # Texto en color negro
            draw.text(10, 50, f'Clima en {ciudad}: {descripcion}')
            draw.text(10, 100, f'Temperatura: {temperatura}°C')

            # Dibujar el texto sobre la imagen
            draw(img)

        # Guardar la imagen como un archivo en el directorio static
        image_path = f'static/clima_imagen_{ciudad}.png'
        img.save(filename=image_path)

        return image_path  # Regresar la ruta para la imagen


# Ruta para la página principal
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ciudad = request.form['ciudad']
        # Obtener los datos del clima y el ícono
        clima, icono = obtener_clima(api_key, ciudad)

        if clima:
            # Guardar los datos del clima en un archivo JSON
            with open(f'{ciudad}_clima.json', 'w') as f:
                json.dump(clima, f, indent=4)

            # Construir la URL del ícono
            icon_url = f'http://openweathermap.org/img/wn/{icono}.png'

            # Generar la imagen del clima
            imagen_clima = generar_imagen_clima(clima, ciudad, icono)

            # Renderizar el template con los datos
            return render_template('index.html', 
                                   ciudad=ciudad,
                                   descripcion=clima['weather'][0]['description'],
                                   temperatura=clima['main']['temp'],
                                   imagen=imagen_clima, 
                                   icon=icon_url)
        else:
            return jsonify({"error": "No se pudo obtener los datos del clima."}), 404

    return render_template('index.html')

# Punto de entrada para la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)