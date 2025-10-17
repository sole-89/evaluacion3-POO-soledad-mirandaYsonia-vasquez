from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def puntos(self, kg: float) -> float:
        pass

    @abstractmethod
    def max_kg_por_bolsa(self) -> float:
        pass


class Plastico(Material):
    def puntos(self, kg: float) -> float:
        return round(kg * 5, 2)  # alto valor por kg

    def max_kg_por_bolsa(self) -> float:
        return 8.0


class Vidrio(Material):
    def puntos(self, kg: float) -> float:
        return round(kg * 2, 2)  # valor más bajo

    def max_kg_por_bolsa(self) -> float:
        return 5.0


class PapelCarton(Material):
    def puntos(self, kg: float) -> float:
        # valor intermedio, puede contemplar merma
        return round(kg * 3.5, 2)

    def max_kg_por_bolsa(self) -> float:
        return 10.0
