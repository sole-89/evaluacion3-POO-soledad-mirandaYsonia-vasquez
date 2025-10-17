from datetime import datetime, timedelta
from collections import defaultdict

class Suscriptor:
    def __init__(self, id_suscriptor: int, direccion: str):
        if not direccion:
            raise ValueError("La dirección no puede estar vacía.")
        self.__id_suscriptor = id_suscriptor
        self.__direccion = direccion
        self.__saldo_puntos = 0
        self.__estado = "habilitado"
        self.__historial_eventos = []

    # --- Getters de solo lectura ---
    @property
    def id_suscriptor(self): return self.__id_suscriptor

    @property
    def direccion(self): return self.__direccion

    @property
    def saldo_puntos(self): return self.__saldo_puntos

    @property
    def estado(self): return self.__estado

    @property
    def historial_eventos(self): return list(self.__historial_eventos)

    # --- Métodos de dominio ---
    def registrar_evento(self, tipo, detalle):
        self.__historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })

    def acreditar_puntos(self, puntos):
        if puntos < 0:
            raise ValueError("No se pueden acreditar puntos negativos.")
        self.__saldo_puntos += puntos
        self.registrar_evento("puntos_acreditados", f"+{puntos} puntos")

    def aplicar_bono_semanal(self):
        self.__saldo_puntos += 10
        self.registrar_evento("bono_aplicado", "Bonificación semanal de +10 puntos")

    def inhabilitar(self, motivo):
        self.__estado = "inhabilitado"
        self.registrar_evento("inhabilitado", motivo)

    def esta_habilitado(self):
        return self.__estado == "habilitado"
