# syntax=docker/dockerfile:1

# Usar la imagen base de Python 3.12 con Alpine
FROM python:3.12-alpine

# Crear el directorio /app y configurarlo como el directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias del sistema necesarias (gcc, musl-dev, linux-headers, imagemagick)
RUN apk add --no-cache gcc musl-dev linux-headers imagemagick

# Instalar las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Crear la carpeta estática para las imágenes generadas
RUN mkdir -p /app/static

# Si necesitas crear enlaces simbólicos (si es necesario, verifica si no los necesitas)
RUN ln -s /usr/lib/libMagickCore-7.Q16HDRI.so.10.0.2 /usr/lib/libMagickCore.so
RUN ln -s /usr/lib/libMagickWand-7.Q16HDRI.so.10.0.2 /usr/lib/libMagickWand.so

# Exponer el puerto 5000 para que la aplicación Flask sea accesible
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
