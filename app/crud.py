"""
Módulo criar elistar carros carros.
"""

from app.models import Carro

db = []


def listar_carros():
    """Módulo lista de carros."""
    return db


def criar_carro(carro: Carro):
    """Módulo add os carros no banco."""
    db.append(carro)
    return carro
