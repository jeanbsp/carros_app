"""
Módulo principal da API de carros usando FastAPI.
Define as rotas para listar e criar carros.
"""
# backend/app/main.py
from fastapi import FastAPI
from app import crud, models

app = FastAPI()


@app.get("/carros")
def listar_carros():
    """Retorna a lista de carros cadastrados."""
    return crud.listar_carros()


@app.post("/carros")
def criar_carro(carro: models.Carro):
    """Cria um novo carro com os dados fornecidos."""
    return crud.criar_carro(carro)
