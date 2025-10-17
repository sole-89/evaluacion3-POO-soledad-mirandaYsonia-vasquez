# politica_turno.py
# =======================================
# Modelo 5 — PoliticaTurno (abstracta) y subtipos
# =======================================
from abc import ABC, abstractmethod
from clases.turno_asignado import TurnoAsignado

class PoliticaTurno(ABC):
    """Clase abstracta que define el contrato para asignar turnos."""
    @abstractmethod
    def asignar(self, semana, colaboradores, franjas):
        pass


class TurnoFijo(PoliticaTurno):
    """Asigna turnos respetando la preferencia de cada colaborador."""
    def asignar(self, semana, colaboradores, franjas):
        turnos = []
        idx = 0
        for franja in franjas:
            colaborador = colaboradores[idx % len(colaboradores)]
            # marca forzado si rompe preferencia
            marcado = not (colaborador.preferencia == "indistinto" or
                           (colaborador.preferencia == "manana" and int(franja.hora_inicio.split(":")[0]) < 12) or
                           (colaborador.preferencia == "tarde" and int(franja.hora_inicio.split(":")[0]) >= 12))
            turno = TurnoAsignado(franja, colaborador, marcado_forzado=marcado)
            turnos.append(turno)
            colaborador.registrar_evento("turno_asignado", f"{franja} (forzado={marcado})")
            idx += 1
        return turnos
