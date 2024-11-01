# Utiliza la imagen base de Python
FROM python:3.10.14

# Copia todo el contenido del directorio actual al directorio /app en el contenedor
COPY . /app

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r blacklists/src/requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "blacklists/src/application.py"]