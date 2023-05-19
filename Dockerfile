# Imagen base de Python 3.10
FROM python:3.10

# Directorio de trabajo dentro del contenedor
WORKDIR /totemlogbd

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente del proyecto al contenedor
COPY . .

# Variable de entorno para la conexión a la base de datos
ENV DATABASE_URL postgresql://username:password@host:port/totemlog

# Puerto en el que la aplicación Flask estará expuesta
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
