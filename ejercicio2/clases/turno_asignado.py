# turno_asignado.py
# =======================================
# Modelo 3 — TurnoAsignado
# =======================================
from datetime import datetime

class TurnoAsignado:
    """Bloque horario cubierto por un colaborador."""

    def __init__(self, franja, responsable, marcado_forzado=False):
        self.franja = franja
        self.responsable = responsable
        self.marcado_forzado = marcado_forzado
        self._historial_eventos = []
        self.registrar_evento("asignado", f"Turno asignado a {responsable.nombre} ({franja})")

    @property
    def duracion_horas(self):
        return self.franja.duracion_horas

    @property
    def historial_eventos(self):
        return list(self._historial_eventos)

    def registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })
