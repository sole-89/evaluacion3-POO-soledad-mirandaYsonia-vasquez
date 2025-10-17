# calendario_cancha.py
# =======================================
# Modelo 2 — CalendarioCancha
# =======================================
from datetime import datetime

class CalendarioCancha:
    """Encapsula los bloques de mantención de una cancha."""

    def __init__(self):
        self.mantencion = []

    def agregar(self, inicio, fin):
        if inicio >= fin:
            raise ValueError("El inicio debe ser menor que el fin.")
        if self.intersecta(inicio, fin):
            raise ValueError("El nuevo bloque se solapa con otro de mantención existente.")
        self.mantencion.append({"inicio": inicio, "fin": fin})

    def intersecta(self, inicio, fin):
        """Verifica si el rango propuesto intersecta alguna mantención existente."""
        for bloque in self.mantencion:
            if inicio < bloque["fin"] and fin > bloque["inicio"]:
                return True
        return False
