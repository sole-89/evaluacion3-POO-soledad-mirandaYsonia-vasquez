from datetime import datetime, timedelta

class Retiro:
    def __init__(self, id_retiro: int, suscriptor, material, kg: float, fecha: datetime):
        if kg <= 0:
            raise ValueError("El peso debe ser mayor a 0 kg.")
        self.__id_retiro = id_retiro
        self.__suscriptor = suscriptor
        self.__material = material
        self.__kg = kg
        self.__fecha = fecha
        self.__estado = "registrado"
        self.__puntos_calculados = 0
        self.__historial_eventos = []
        self.registrar_evento("registrado", f"Retiro {id_retiro} registrado ({kg} kg).")

    # --- Getters ---
    @property
    def id_retiro(self): return self.__id_retiro

    @property
    def estado(self): return self.__estado

    @property
    def fecha(self): return self.__fecha

    @property
    def puntos_calculados(self): return self.__puntos_calculados

    @property
    def historial_eventos(self): return list(self.__historial_eventos)

    def registrar_evento(self, tipo, detalle):
        self.__historial_eventos.append({
            "timestamp": datetime.now(),
            "tipo": tipo,
            "detalle": detalle
        })

    # --- Operaciones del dominio ---
    def validar_retiro(self, estrategia_peso="rechazo"):
        if self.__estado != "registrado":
            raise Exception("Solo se pueden validar retiros en estado registrado.")
        if not self.__suscriptor.esta_habilitado():
            raise Exception("El suscriptor está inhabilitado.")
        max_kg = self.__material.max_kg_por_bolsa()
        if self.__kg > max_kg:
            if estrategia_peso == "rechazo":
                self.__estado = "rechazado"
                self.registrar_evento("rechazado", f"Excede el máximo de {max_kg} kg por bolsa.")
                return "rechazado"
            else:
                raise NotImplementedError("Estrategia de partición no implementada.")
        # calcular puntos
        puntos = self.__material.puntos(self.__kg)
        self.__puntos_calculados = puntos
        self.__suscriptor.acreditar_puntos(puntos)
        self.__estado = "validado"
        self.registrar_evento("validado", f"Retiro validado ({self.__kg} kg, {puntos} pts).")
        return "validado"

    def rechazar_retiro(self, motivo):
        if self.__estado != "registrado":
            raise Exception("Solo se puede rechazar un retiro registrado.")
        self.__estado = "rechazado"
        self.registrar_evento("rechazado", motivo)
