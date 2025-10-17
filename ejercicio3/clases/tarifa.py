# tarifa.py
# =======================================
# Modelo 4 — Tarifa (abstracta) y subtipos
# =======================================
from abc import ABC, abstractmethod
from datetime import time, datetime

class Tarifa(ABC):
    """Clase abstracta para cálculo de tarifas."""
    @abstractmethod
    def calcular_importe(self, inicio, fin):
        pass


class TarifaDiurna(Tarifa):
    """Aplica entre 08:00 y 19:59"""
    def calcular_importe(self, inicio, fin):
        valor_hora = 5000
        duracion_horas = (fin - inicio).seconds / 3600
        return {"total": round(valor_hora * duracion_horas, 2),
                "detalle": [{"tipo": "Diurna", "horas": duracion_horas, "valor_hora": valor_hora}]}


class TarifaNocturna(Tarifa):
    """Aplica entre 20:00 y 07:59"""
    def calcular_importe(self, inicio, fin):
        valor_hora = 7000
        duracion_horas = (fin - inicio).seconds / 3600
        return {"total": round(valor_hora * duracion_horas, 2),
                "detalle": [{"tipo": "Nocturna", "horas": duracion_horas, "valor_hora": valor_hora}]}


class TarifaFinDeSemana(Tarifa):
    """Prioritaria los sábados y domingos."""
    def calcular_importe(self, inicio, fin):
        valor_hora = 8000
        duracion_horas = (fin - inicio).seconds / 3600
        return {"total": round(valor_hora * duracion_horas, 2),
                "detalle": [{"tipo": "FinDeSemana", "horas": duracion_horas, "valor_hora": valor_hora}]}
