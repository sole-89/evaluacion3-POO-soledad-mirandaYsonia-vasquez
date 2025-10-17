# cancha.py
# =======================================
# Modelo 1 — Cancha
# =======================================
from datetime import datetime
from clases.calendario_cancha import CalendarioCancha

class Cancha:
    """Representa una cancha con posibles bloqueos por mantención."""

    def __init__(self, id_cancha, nombre):
        if not nombre:
            raise ValueError("El nombre de la cancha no puede estar vacío.")
        self.id_cancha = id_cancha
        self.nombre = nombre
        self.calendario = CalendarioCancha()
        self._historial_eventos = []

    @property
    def historial_eventos(self):
        return list(self._historial_eventos)

    def bloquear_mantencion(self, inicio, fin):
        """Agrega un intervalo de mantención."""
        self.calendario.agregar(inicio, fin)
        self._registrar_evento("bloqueo_mantencion", f"{inicio} a {fin}")

    def _registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })
