from datetime import datetime

class BonoSemanal:
    @staticmethod
    def aplicar_bono(suscriptor, lista_retiros):
        """Aplica +10 puntos si hay 3 o más retiros validados en la misma semana calendario."""
        retiros_validados = [r for r in lista_retiros if r.estado == "validado"]
        # Agrupar retiros por semana
        semanas = {}
        for r in retiros_validados:
            semana = r.fecha.isocalendar()[1]  # número de semana del año
            semanas.setdefault(semana, []).append(r)
        for semana, lista in semanas.items():
            if len(lista) >= 3:
                suscriptor.aplicar_bono_semanal()
