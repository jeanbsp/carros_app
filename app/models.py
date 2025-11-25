"""Estrutura de Dados dos carros"""

from pydantic import BaseModel


class Carro(BaseModel):
    """valores das colunas"""

    id: int
    marca: str
    modelo: str
    ano: int
