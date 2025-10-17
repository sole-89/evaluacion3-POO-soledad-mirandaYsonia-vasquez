# servicio.py
# ==========================
# Modelo: Servicio (abstracto) y subtipos
# ==========================

from abc import ABC, abstractmethod

class Servicio(ABC):
    """Clase abstracta que define el contrato de duración mínima."""
    @abstractmethod
    def duracion_min(self):
        """Retorna la duración mínima del servicio en minutos (> 0)."""
        pass


class CorteCabello(Servicio):
    def duracion_min(self):
        return 30


class Coloracion(Servicio):
    def duracion_min(self):
        return 90
