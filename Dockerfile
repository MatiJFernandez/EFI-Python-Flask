# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Define las variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expone el puerto 5000
EXPOSE 5000

# Comando para correr la aplicación
CMD ["flask", "run"]
