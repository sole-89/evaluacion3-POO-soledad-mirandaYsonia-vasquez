# politica_cancelacion.py
# =======================================
# Modelo 5 — PoliticaCancelacion (abstracta) y subtipos
# =======================================
from abc import ABC, abstractmethod

class PoliticaCancelacion(ABC):
    """Define cómo se calcula la penalización al cancelar."""
    @abstractmethod
    def penalizacion(self, horas_previas, importe):
        pass


class CancelacionFlexible(PoliticaCancelacion):
    """0% si >= 24h, 20% si menos."""
    def penalizacion(self, horas_previas, importe):
        if horas_previas >= 24:
            return {"monto_penalizacion": 0, "motivo": "Sin penalización por cancelación anticipada."}
        else:
            monto = round(importe * 0.2, 2)
            return {"monto_penalizacion": monto, "motivo": "Penalización 20% por cancelación tardía."}


class CancelacionEstricta(PoliticaCancelacion):
    """50% del importe siempre."""
    def penalizacion(self, horas_previas, importe):
        monto = round(importe * 0.5, 2)
        return {"monto_penalizacion": monto, "motivo": "Penalización fija del 50%."}
