# Usa uma imagem oficial do Python como base

FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência
COPY . .

# Instala as dependências 
RUN pip install --no-cache-dir fastapi uvicorn

RUN mv app/__init__.py app/__init__.p

# Copia o restante da aplicação
COPY app/ .



# Expõe a porta padrão do Uvicorn
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

