from wand.drawing import Drawing
from wand.color import Color
import math

# Función para dibujar las figuras (círculo, cuadrado, triángulo, etc.)
def dibujar_figuras(img, icono):
    with Drawing() as draw:
        # Establecer el grosor de la línea y color de relleno
        draw.stroke_color = Color('black')
        draw.stroke_width = 5
        draw.fill_color = Color('black')

        # Definir las propiedades de las figuras
        center_x, center_y = 200, 150  # Centro de la figura
        size = 100  # Tamaño de la figura

        # Función para dibujar un hexágono
        def hexagono():
            points = []
            for i in range(6):
                angle = math.radians(60 * i)
                x = center_x + size * math.cos(angle)
                y = center_y + size * math.sin(angle)
                points.append((x, y))
            return points

        # Función para dibujar un cuadrado
        def cuadrado():
            return [
                (center_x - size, center_y - size),
                (center_x + size, center_y - size),
                (center_x + size, center_y + size),
                (center_x - size, center_y + size)
            ]

        # Función para dibujar un triángulo
        def triangulo():
            return [
                (center_x, center_y - size),  # Vértice superior
                (center_x - size, center_y + size),  # Vértice izquierdo
                (center_x + size, center_y + size)  # Vértice derecho
            ]

        # Función para dibujar un rectángulo
        def rectangulo():
            return [
                (center_x - size, center_y - size),
                (center_x + size * 2, center_y - size),
                (center_x + size * 2, center_y + size),
                (center_x - size, center_y + size)
            ]

        # Función para dibujar un pentágono
        def pentagono():
            points = []
            for i in range(5):
                angle = math.radians(72 * i)
                x = center_x + size * math.cos(angle)
                y = center_y + size * math.sin(angle)
                points.append((x, y))
            return points

        # Selección de la figura dependiendo del icono
        if icono == "01d" or icono == "01n":  # Cielo despejado
            draw.fill_color = Color('yellow')  # Color del círculo
            draw.polygon(hexagono())  # Hexágono
        elif icono == "02d" or icono == "02n":  # Pocas nubes
            draw.fill_color = Color('skyblue')  # Color del cuadrado
            draw.polygon(cuadrado())  # Cuadrado
        elif icono == "03d" or icono == "03n":  # Nubes dispersas
            draw.fill_color = Color('lightgray')  # Color del triángulo
            draw.polygon(triangulo())  # Triángulo
        elif icono == "04d" or icono == "04n":  # Nubes rotas
            draw.fill_color = Color('gray')  # Color del rectángulo
            draw.polygon(rectangulo())  # Rectángulo
        elif icono == "09d" or icono == "09n":  # Lluvia de lluvia
            draw.fill_color = Color('blue')  # Color del pentágono
            draw.polygon(pentagono())  # Pentágono
        elif icono == "10d" or icono == "10n":  # Lluvia
            draw.fill_color = Color('lightblue')  # Color del pentágono
            draw.polygon(pentagono())  # Pentágono
        elif icono == "11d" or icono == "11n":  # Tormenta
            draw.fill_color = Color('purple')  # Color del triángulo
            draw.polygon(triangulo())  # Triángulo
        elif icono == "13d" or icono == "13n":  # Nieve
            draw.fill_color = Color('white')  # Color del cuadrado
            draw.polygon(cuadrado())  # Cuadrado
        elif icono == "50d" or icono == "50n":  # Niebla
            draw.fill_color = Color('red')  # Color del rectángulo
            draw.polygon(rectangulo())  # Rectángulo

        # Aplicar el dibujo a la imagen
        draw(img)