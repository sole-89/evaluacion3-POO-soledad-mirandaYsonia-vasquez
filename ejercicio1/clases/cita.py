# cita.py
# ==========================
# Modelo: Cita
# ==========================
from datetime import datetime, timedelta
from clases.servicio import Servicio

class Cita:
    """Representa una cita entre un cliente y un profesional."""

    def __init__(self, id_cita, cliente, profesional, inicio):
        if not cliente or not profesional:
            raise ValueError("Cliente y profesional no pueden estar vacíos.")
        if inicio <= datetime.now():
            raise ValueError("La fecha de inicio debe ser futura.")

        self._id_cita = id_cita
        self._cliente = cliente
        self._profesional = profesional
        self._inicio = inicio
        self._duracion_min = None
        self._estado = "creada"
        self._historial_eventos = []

    # --- Propiedades de solo lectura ---
    @property
    def id_cita(self):
        return self._id_cita

    @property
    def cliente(self):
        return self._cliente

    @property
    def profesional(self):
        return self._profesional

    @property
    def inicio(self):
        return self._inicio

    @property
    def duracion_min(self):
        return self._duracion_min

    @property
    def fin(self):
        if self._duracion_min:
            return self._inicio + timedelta(minutes=self._duracion_min)
        return None

    @property
    def estado(self):
        return self._estado

    @property
    def historial_eventos(self):
        return list(self._historial_eventos)  # Copia inmutable externamente

    # --- Operaciones del dominio ---
    def asignar_servicio(self, servicio):
        """Asigna un servicio y fija la duración mínima."""
        if not isinstance(servicio, Servicio):
            raise TypeError("El servicio debe ser un subtipo de Servicio.")
        self._duracion_min = servicio.duracion_min()
        self._registrar_evento("servicio_asignado", f"Duración fijada: {self._duracion_min} min")

    def confirmar(self, motivo, agenda):
        """Confirma la cita si cumple todas las condiciones."""
        if self._estado != "creada":
            raise ValueError("Solo una cita en estado 'creada' puede confirmarse.")
        if self._duracion_min is None:
            raise ValueError("Debe asignarse un servicio antes de confirmar.")
        #  Excluir la propia cita del chequeo de solapamiento
        if agenda.existe_solape(self._profesional, self._inicio, self.fin, exclude_id=self._id_cita):
            raise ValueError("El profesional tiene otra cita en ese horario.")

        self._estado = "confirmada"
        self._registrar_evento("confirmada", motivo)

    def cancelar(self, motivo):
        """Cancela la cita según las reglas de transición válidas."""
        if self._estado not in ("creada", "confirmada"):
            raise ValueError("Solo se puede cancelar si la cita está 'creada' o 'confirmada'.")
        self._estado = "cancelada"
        self._registrar_evento("cancelada", motivo)

    # --- Registro de eventos ---
    def _registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })

    def __str__(self):
        return (f"Cita {self._id_cita} | Cliente: {self._cliente} | Profesional: {self._profesional} | "
                f"Inicio: {self._inicio} | Fin: {self.fin} | Estado: {self._estado}")
