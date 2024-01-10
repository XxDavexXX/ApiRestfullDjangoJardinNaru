# Usa una imagen de Python como base
FROM python:3.11

# Establece el directorio de trabajo en /api
WORKDIR /api

# Copia el archivo de requerimientos a la imagen
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual del directorio al directorio de trabajo en la imagen
COPY . .

# Expone el puerto 8000 para acceder a la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
