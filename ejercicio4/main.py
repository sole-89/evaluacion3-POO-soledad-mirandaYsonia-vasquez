from datetime import datetime
from clases.material import Plastico, Vidrio, PapelCarton
from clases.suscriptor import Suscriptor
from clases.retiro import Retiro
from clases.bono import BonoSemanal
from clases.aviso import AvisoApp, AvisoEmail

if __name__ == "__main__":
    # Crear materiales
    plastico = Plastico()
    vidrio = Vidrio()
    carton = PapelCarton()

    # Crear suscriptor
    s1 = Suscriptor(1, "Av. Las Torres 456, Puente Alto")

    # Registrar retiros
    r1 = Retiro(101, s1, plastico, 4, datetime(2025, 10, 14))
    r2 = Retiro(102, s1, vidrio, 3, datetime(2025, 10, 15))
    r3 = Retiro(103, s1, carton, 2, datetime(2025, 10, 16))

    # Validar retiros (estrategia rechazo)
    for r in [r1, r2, r3]:
        r.validar_retiro()

    # Aplicar bono semanal si corresponde
    BonoSemanal.aplicar_bono(s1, [r1, r2, r3])

    # Enviar aviso
    app = AvisoApp()
    email = AvisoEmail()
    app.enviar(s1, "Gracias por reciclar esta semana ")
    email.enviar(s1, "Has recibido tu bono semanal de 10 puntos.")

    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    print(f"Saldo total de puntos: {s1.saldo_puntos}")
    print("Eventos del suscriptor:")
    for e in s1.historial_eventos:
        print(f" - {e['timestamp']:%Y-%m-%d %H:%M:%S}: {e['tipo']} → {e['detalle']}")
