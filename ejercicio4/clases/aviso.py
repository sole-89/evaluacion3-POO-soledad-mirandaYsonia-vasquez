from abc import ABC, abstractmethod
from datetime import datetime

class Aviso(ABC):
    @abstractmethod
    def enviar(self, suscriptor, mensaje: str):
        pass


class AvisoApp(Aviso):
    def enviar(self, suscriptor, mensaje: str):
        suscriptor.registrar_evento("aviso_app", f"Mensaje en App: {mensaje}")
        print(f"[APP] Aviso enviado a {suscriptor.direccion}: {mensaje}")
        return True


class AvisoEmail(Aviso):
    def enviar(self, suscriptor, mensaje: str):
        suscriptor.registrar_evento("aviso_email", f"Correo: {mensaje}")
        print(f"[EMAIL] Aviso enviado a {suscriptor.direccion}: {mensaje}")
        return True
