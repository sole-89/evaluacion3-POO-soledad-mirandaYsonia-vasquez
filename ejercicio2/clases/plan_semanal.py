# plan_semanal.py
# =======================================
# Modelo 4 — PlanSemanal
# =======================================
from datetime import datetime

class PlanSemanal:
    """Resultado de la planificación para una semana."""
    def __init__(self, semana, franjas, colaboradores):
        self.semana = semana
        self.franjas = franjas
        self.colaboradores = colaboradores
        self.turnos_asignados = []
        self._historial_eventos = []

    @property
    def historial_eventos(self):
        return list(self._historial_eventos)

    def generar_plan(self, politica):
        """Genera turnos según la política elegida."""
        self.turnos_asignados = politica.asignar(self.semana, self.colaboradores, self.franjas)
        self._registrar_evento("plan_generado", f"Plan creado con {len(self.turnos_asignados)} turnos asignados.")

    def cobertura_porcentaje(self):
        total = len(self.franjas)
        cubiertos = len(self.turnos_asignados)
        return round((cubiertos / total) * 100, 2) if total > 0 else 0

    def mostrar_plan(self):
        print("\n=== PLAN SEMANAL ===")
        for t in self.turnos_asignados:
            print(f"{t.franja.dia} {t.franja.hora_inicio}-{t.franja.hora_fin} "
                  f"=> {t.responsable.nombre} (Forzado: {t.marcado_forzado})")
        print(f"\nCobertura total: {self.cobertura_porcentaje()}%")

    def _registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })
