from dataclasses import dataclass


@dataclass
class Linea:
    id_linea: int
    nome: str
    velocita: float
    intervallo: float
    colore: str
