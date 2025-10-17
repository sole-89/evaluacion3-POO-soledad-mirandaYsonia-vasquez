# franja.py
# =======================================
# Modelo 2 — Franja
# =======================================
from datetime import datetime

class Franja:
    """Bloque horario de un día específico."""
    def __init__(self, dia, hora_inicio, hora_fin):
        if hora_inicio >= hora_fin:
            raise ValueError("La hora de inicio debe ser menor que la de fin.")
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    @property
    def duracion_horas(self):
        """Duración en horas del bloque."""
        h1 = datetime.strptime(self.hora_inicio, "%H:%M")
        h2 = datetime.strptime(self.hora_fin, "%H:%M")
        return round((h2 - h1).seconds / 3600, 2)

    def __str__(self):
        return f"{self.dia} {self.hora_inicio}-{self.hora_fin} ({self.duracion_horas}h)"
