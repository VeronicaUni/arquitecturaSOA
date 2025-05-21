FROM python:3.10-slim

WORKDIR /app
COPY . .

# Exponer el puerto que usará el servidor
EXPOSE 5000

# Comando para ejecutar un servidor web simple
CMD ["python", "-m", "http.server", "5000"] 