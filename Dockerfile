FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o código para o container
COPY . /app

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta
EXPOSE 5000

# Definir o comando para iniciar o aplicativo
CMD ["python", "app.py"]