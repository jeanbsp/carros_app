# Aplicação Carros App

Bem-vindo ao **Carros App**, uma aplicação desenvolvida em Python utilizando o framework FastAPI para criar uma API robusta e eficiente.

## Sobre a Aplicação

Esta aplicação é uma API construída com FastAPI, destinada a gerenciar informações relacionadas com carros. A aplicação está estruturada no diretório `backend`, onde se encontram os ficheiros principais da aplicação, incluindo o ponto de entrada `main.py`.

## Estrutura do Projeto

- **backend/**: Contém o código fonte da aplicação.
  - **app/**: Diretório principal da aplicação FastAPI.
    - `main.py`: Ponto de entrada da aplicação.
    - `crud.py`: Operações de criação, leitura, atualização e exclusão.
    - `models.py`: Definições dos modelos de dados.
    - `database.py`: Configuração da base de dados.
  - **tests/**: Testes automatizados para a aplicação.
- **dockerfile**: Ficheiro de configuração para criar uma imagem Docker da aplicação.
- **requirements.txt**: Lista de dependências necessárias para executar a aplicação.

## Detalhes do Dockerfile

O `dockerfile` foi configurado para criar uma imagem Docker que executa a aplicação utilizando a versão **Python 3.11**. Aqui está uma explicação detalhada do conteúdo do ficheiro:

- **Imagem Base**: Utiliza `python:3.11-slim` como imagem base, uma versão leve do Python 3.11, para minimizar o tamanho da imagem.
- **Diretório de Trabalho**: Define `/app` como o diretório de trabalho dentro do container.
- **Dependências**: Copia o ficheiro `backend/requirements.txt` para o container e instala as dependências listadas usando `pip install --no-cache-dir -r requirements.txt`. O parâmetro `--no-cache-dir` reduz o tamanho da imagem ao não armazenar cache desnecessário.
- **Cópia da Aplicação**: Copia todo o conteúdo do diretório do projeto para o container, garantindo que todos os ficheiros necessários estejam disponíveis.
- **Comando de Execução**: Está comentado no momento, mas pode ser configurado para executar a aplicação com `uvicorn`, o servidor ASGI para FastAPI, usando algo como `CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]`. O parâmetro `--reload` permite recarregar a aplicação automaticamente durante o desenvolvimento.

## Ficheiro de Requisitos (requirements.txt)

O ficheiro `requirements.txt` no diretório `backend` lista todas as dependências necessárias para executar a aplicação. As principais bibliotecas incluídas são:

- **fastapi**: Framework para construir APIs com Python.
- **uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
- **pydantic**: Biblioteca para validação de dados e serialização.
- **pytest**: Framework para testes automatizados.
- **pylint**: Ferramenta de linting para garantir a qualidade do código.
- **black**: Formatador de código para manter um estilo consistente.
- **isort**: Organizador de imports para manter o código limpo.
- **bandit**: Ferramenta de segurança para identificar vulnerabilidades no código.
- **pre-commit**: Ferramenta para executar verificações antes de commits no Git.

Estas dependências são instaladas automaticamente ao construir a imagem Docker.

## Como Executar a Aplicação no Docker

Para executar a aplicação utilizando Docker, siga os passos abaixo:

1. **Construir a Imagem Docker**:
   Abra um terminal no diretório `carros_app` e execute o seguinte comando para construir a imagem Docker:
   ```
   docker build -t carros_app_image -f dockerfile .
   ```
   Este comando cria uma imagem chamada `carros_app_image` utilizando o `dockerfile` no diretório atual.

2. **Executar o Container**:
   Depois de construir a imagem, você pode executar um container com o comando abaixo. Como o comando `CMD` está comentado no Dockerfile, você precisará especificar o comando de execução manualmente:
   ```
   docker run -d -p 8000:8000 --name carros_app_container carros_app_image uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
   - `-d`: Executa o container em modo detached (em segundo plano).
   - `-p 8000:8000`: Mapeia a porta 8000 do container para a porta 8000 do host, permitindo que você aceda à API através de `http://localhost:8000`.
   - `--name carros_app_container`: Nomeia o container como `carros_app_container`.
   - O restante do comando especifica que o `uvicorn` deve ser usado para executar a aplicação FastAPI.

3. **Aceder à Aplicação**:
   Após iniciar o container, a API estará disponível em `http://localhost:8000`. Você pode usar ferramentas como `curl` ou Postman para interagir com os endpoints da API. Para documentação interativa, aceda a `http://localhost:8000/docs` no seu navegador.

4. **Parar o Container**:
   Quando terminar, você pode parar o container com o comando:
   ```
   docker stop carros_app_container
   ```
   E removê-lo, se necessário, com:
   ```
   docker rm carros_app_container
   ```

## Notas Finais

