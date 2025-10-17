# reserva.py
# =======================================
# Modelo 3 — Reserva
# =======================================
from datetime import datetime

class Reserva:
    """Representa una reserva de una cancha."""

    def __init__(self, id_reserva, cancha, cliente, inicio, fin):
        if not cliente:
            raise ValueError("El cliente no puede estar vacío.")
        if inicio >= fin:
            raise ValueError("El inicio debe ser menor que el fin.")
        self.id_reserva = id_reserva
        self.cancha = cancha
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        self.estado = "creada"
        self.importe = None
        self.desglose_tarifa = None
        self._historial_eventos = []

    @property
    def historial_eventos(self):
        return list(self._historial_eventos)

    def cotizar(self, tarifa):
        """Calcula el importe usando una tarifa polimórfica."""
        data = tarifa.calcular_importe(self.inicio, self.fin)
        self.importe = data["total"]
        self.desglose_tarifa = data["detalle"]
        self._registrar_evento("cotizada", f"Importe calculado: ${self.importe}")

    def confirmar(self, motivo, reservas_existentes):
        """Confirma si no hay solape y no cae en mantención."""
        if self.cancha.calendario.intersecta(self.inicio, self.fin):
            raise ValueError("La cancha está en mantención en ese horario.")
        for r in reservas_existentes:
            if r.cancha.id_cancha == self.cancha.id_cancha and r.estado != "cancelada":
                if self.inicio < r.fin and self.fin > r.inicio:
                    raise ValueError("Existe otra reserva en ese horario.")
        self.estado = "confirmada"
        self._registrar_evento("confirmada", motivo)

    def cancelar(self, motivo, politica):
        """Aplica política de penalización al cancelar."""
        if self.estado not in ("creada", "confirmada"):
            raise ValueError("Solo puede cancelarse una reserva creada o confirmada.")
        horas_previas = (self.inicio - datetime.now()).total_seconds() / 3600
        penal = politica.penalizacion(horas_previas, self.importe or 0)
        self.estado = "cancelada"
        self._registrar_evento("cancelada", f"{motivo} | Penalización: ${penal['monto_penalizacion']}")
        return penal

    def _registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })

    def __str__(self):
        return (f"Reserva {self.id_reserva}: {self.cliente} en {self.cancha.nombre} "
                f"({self.inicio} - {self.fin}) [{self.estado}] ${self.importe or 'sin cotizar'}")
