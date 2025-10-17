# colaborador.py
# =======================================
# Modelo 1 — Colaborador
# =======================================
from datetime import datetime

class Colaborador:
    """Persona elegible para cubrir franjas del plan semanal."""

    def __init__(self, id_colaborador, nombre, horas_semana_max, preferencia):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if horas_semana_max <= 0:
            raise ValueError("Las horas semanales deben ser mayores que 0.")
        if preferencia not in ("manana", "tarde", "indistinto"):
            raise ValueError("Preferencia inválida. Use manana, tarde o indistinto.")

        self.id_colaborador = id_colaborador
        self.nombre = nombre
        self.horas_semana_max = horas_semana_max
        self.preferencia = preferencia
        self.no_disponible = []  # lista de intervalos {"dia": "Lunes", "hora_inicio": "09:00", "hora_fin": "12:00"}
        self._historial_eventos = []

    @property
    def historial_eventos(self):
        return list(self._historial_eventos)

    def registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })
